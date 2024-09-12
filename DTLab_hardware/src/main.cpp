/*
    Esp32 Websockets Client

    This sketch:
        1. Connects to a WiFi network
        2. Connects to a Websockets server
        3. Sends the websockets server a message ("Hello Server")
        4. Prints all incoming messages while the connection is open

    Hardware:
        For this sketch you only need an ESP32 board.

    Created 15/02/2019
    By Gil Maimon
    https://github.com/gilmaimon/ArduinoWebsockets

*/

#include <Arduino.h>
#include <ArduinoJson.h>

#include <WiFi.h>
#include <WiFiClientSecure.h>

#include <WebSocketsClient.h>

#include <time.h>

#include <IRremoteESP8266.h>
#include <IRsend.h>
#include <ir_Kelvinator.h>

#include <definitions.h>

#include <SPI.h>
#include "printf.h"
#include "RF24.h"

#define GATEWAY_ID 1

#define TEST_LED_PIN 33
#define TEST_BUTTON_PIN 0

#define USE_SERIAL Serial

/// Constants
// Wifi
const char *ssid = "612";                             // Enter SSID
const char *password = "wififor612";                  // Enter Password
                                                      // Websockets
const char *websockets_server_host = "192.168.3.80"; // Enter server adress
// const char *websockets_server_host = "192.168.0.191";                   // Enter server adress
uint16_t websockets_server_port = 808;                                 // Enter server port
const char *websockets_server_url = "/dtlab/ws/gatewayClient/gateway1"; // Enter server url
// IR
const uint16_t kIrLed_1 = 27;
const uint16_t kIrLed_2 = 32;
// NTP
const char *ntpServer = "ntp.ntsc.ac.cn";
const long gmtOffset_sec = 0;
const int daylightOffset_sec = 0;

/// Variables
// Websockets
unsigned long interval = 5000;
bool connected = false;
// Status
uint8_t led = 0;
// Time
uint32_t epochTime;

/// Objects
WebSocketsClient webSocket;
IRKelvinatorAC ac1(kIrLed_1);
IRKelvinatorAC ac2(kIrLed_2);
IRKelvinatorAC *pac;
StaticJsonDocument<200> doc;

/// Lights & Monitor
RF24 radio(16, 17);  // using pin 16 for the CE pin, and pin 17 for the CSN pin

// Let these addresses be used for the pair
uint8_t address[][6] = { "1Node", "2Node" };
bool radioNumber = 1;  // 0 uses address[0] to transmit, 1 uses address[1] to transmit

bool role = false;  // true = TX role, false = RX role
bool light_control = false;//是否需要发送命令给电灯和屏幕

bool flag1 = false;  // false = 开关1是关上的，开关2是打开的
bool flag2 = false;
bool flag3 = false;

// 通过2.4G通信发送的命令（给灯/测电流）
int light_command = 0;

//接受的报文
int payload = 0;
// 电流的大小
float ele_value = 0;

void recv_handle(char *data)
{
    bool valid = true;
    DynamicJsonDocument doc(1024);
    String input = String(data);
    deserializeJson(doc, input);
    JsonObject obj = doc.as<JsonObject>();
    String _echo = obj["echo"];
    String _action = obj["action"];
    uint16_t _device_id = obj["params"]["device_id"];

    if (_action == API_SET_POWER_SWITCH)
    {
        if (!obj["params"]["switch"].isNull() && !obj["params"]["device_id"].isNull())
        {
            bool _switch = obj["params"]["switch"];
            if (_device_id == 1){
                if (_switch == 0)
                {
                    flag1 = false;
                    light_command = 10;
                    light_control = true;
                }
                else if (_switch == 1)
                {
                    flag1 = true;
                    light_command = 11;
                    light_control = true;
                }

            }
            else if (_device_id ==2){
                if (_switch == 0)
                {
                    flag2 = false;
                    light_command = 20;
                    light_control = true;
                }
                else if (_switch == 1)
                {
                    flag2 = true;
                    light_command = 21;
                    light_control = true;
                }
            }
            else if (_device_id == 3){
                if (_switch == 0)
                {
                    flag3 = false;
                    light_command = 30;
                    light_control = true;
                }
                else if (_switch == 1)
                {
                    flag3 = true;
                    light_command = 31;
                    light_control = true;
                }
            }
            else{
                valid = false;
            }

            if (connected)
            {
                String resp = "{\"status\": \"" + String(API_STATUS_OK) + "\", \"retcode\": " + String(API_STATUS_OK_CODE) + ", \"data\": {\"device_id\": " + String(_device_id) + ", \"switch\": " + String(_switch) + "}";
                if (_echo != "null")
                {
                    resp += ", \"echo\": \"" + String(_echo) + "\"}";
                }
                else
                {
                    resp += "}";
                }
                USE_SERIAL.print("[Pkg] [Send] ");
                USE_SERIAL.println(resp);
                webSocket.sendTXT(resp);
            }
        }
        else
        {
            if (connected)
            {
                String resp = "{\"status\": \"" + String(API_STATUS_FAILED) + "\", \"retcode\": " + String(API_STATUS_INVALID_DATA_CODE) + ", \"msg\": \"Invalid params.\"";
                if (_echo != "null")
                {
                    resp += ", \"echo\": \"" + String(_echo) + "\"}";
                }
                else
                {
                    resp += "}";
                }
                USE_SERIAL.print("[Pkg] [Send] ");
                USE_SERIAL.println(resp);
                webSocket.sendTXT(resp);
            }
        }
    }
    else if (_action == API_SET_AIR_CONDITIONER)    //设置空调
    {
        if (obj["params"]["mode"].isNull() ||
            obj ["params"]["power"].isNull() ||
            obj["params"]["basic_fan"].isNull() ||
            obj["params"]["temp"].isNull())
        {
            valid = false;
        }
        else
        {   
            bool _power = obj["params"]["power"];
            uint8_t _basic_fan = obj["params"]["basic_fan"];
            uint8_t _temp = obj["params"]["temp"];
            uint8_t _mode = obj["params"]["mode"];

            if (_device_id == 1)
            {
                pac = &ac1;
            }
            else if (_device_id == 2)
            {
                pac = &ac2;
            }
            else
            {
                valid = false;
            }

            (*pac).setMode(_mode);

            if (_power)
            {
                (*pac).on();
            }
            else
            {
                (*pac).off();
            }

            (*pac).setFan(_basic_fan);
            (*pac).setTemp(_temp);

            if (!obj["params"]["turbo"].isNull())
            {
                bool _turbo = obj["params"]["turbo"];
                (*pac).setTurbo(_turbo);
            }

            if (!obj["params"]["light"].isNull())
            {
                bool _light = obj["params"]["light"];
                (*pac).setLight(_light);
            }

            if (!obj["params"]["xfan"].isNull())
            {
                bool _xfan = obj["params"]["xfan"];
                (*pac).setXFan(_xfan);
            }

            if (!obj["params"]["swing_v"].isNull())
            {
                bool _swing_v = obj["params"]["swing_v"];
                (*pac).setSwingVertical(_swing_v, kKelvinatorSwingVOff);
            }

            if (!obj["params"]["swing_h"].isNull())
            {
                bool _swing_h = obj["params"]["swing_h"];
                (*pac).setSwingHorizontal(_swing_h);
            }

            if (!obj["params"]["quiet"].isNull())
            {
                bool _quiet = obj["params"]["quiet"];
                (*pac).setQuiet(_quiet);
            }

            Serial.println("[Brd] Sending IR command to A/C ...");
            (*pac).send();

            if (connected)
            {
                if (valid)
                {
                    String resp = "{\"status\": \"" + String(API_STATUS_OK) + "\", \"retcode\": " + String(API_STATUS_OK_CODE) + ", \"data\": {\"device_id\": " + String(_device_id) + ", \"mode\": " + String(_mode) + ", \"power\": " + String(_power) + "}";
                    if (_echo != "null")
                    {
                        resp += ", \"echo\": \"" + String(_echo) + "\"}";
                    }
                    else
                    {
                        resp += "}";
                    }
                    USE_SERIAL.print("[Pkg] [Send] ");
                    USE_SERIAL.println(resp);
                    webSocket.sendTXT(resp);
                }
                else
                {
                    String resp = "{\"status\": \"" + String(API_STATUS_FAILED) + "\", \"retcode\": " + String(API_STATUS_DEVICE_NOT_FOUND_CODE) + ", \"msg\": \"Device not found.\"";
                    if (_echo != "null")
                    {
                        resp += ", \"echo\": \"" + String(_echo) + "\"}";
                    }
                    else
                    {
                        resp += "}";
                    }
                    USE_SERIAL.print("[Pkg] [Send] ");
                    USE_SERIAL.println(resp);
                    webSocket.sendTXT(resp);
                }
            }
        }
    }
    else if (_action == API_SET_MONITOR_ELECTRICITY)
    {
        if (!obj["params"]["switch"].isNull())
        {
            bool _switch = obj["params"]["switch"];
            if (_switch == 1)
            {
                light_command = 99;
                light_control = true;
                USE_SERIAL.println("okkkkkk");
            }

            if (connected)
            {
                String resp = "{\"status\": \"" + String(API_STATUS_OK) + "\", \"retcode\": " + String(API_STATUS_OK_CODE) + ", \"data\": {\"device_id\": " + String(_device_id) + ", \"switch\": " + String(_switch) + "}";
                if (_echo != "null")
                {
                    resp += ", \"echo\": \"" + String(_echo) + "\"}";
                }
                else
                {
                    resp += "}";
                }
                USE_SERIAL.print("[Pkg] [Send] ");
                USE_SERIAL.println(resp);
                webSocket.sendTXT(resp);
            }
        }
        else
        {
            if (connected)
            {
                String resp = "{\"status\": \"" + String(API_STATUS_FAILED) + "\", \"retcode\": " + String(API_STATUS_INVALID_DATA_CODE) + ", \"msg\": \"Invalid params.\"";
                if (_echo != "null")
                {
                    resp += ", \"echo\": \"" + String(_echo) + "\"}";
                }
                else
                {
                    resp += "}";
                }
                USE_SERIAL.print("[Pkg] [Send] ");
                USE_SERIAL.println(resp);
                webSocket.sendTXT(resp);
            }
        }
    }
    else
    {
        if (connected)
        {
            String resp = "{\"status\": \"" + String(API_STATUS_FAILED) + "\", \"retcode\": " + String(API_STATUS_INVALID_API_CODE) + ", \"msg\": \"Invalid API.\"";
            if (_echo != "null")
            {
                resp += ", \"echo\": \"" + String(_echo) + "\"}";
            }
            else
            {
                resp += "}";
            }
            USE_SERIAL.print("[Pkg] [Send] ");
            USE_SERIAL.println(resp);
            webSocket.sendTXT(resp);
        }
    }
}

void hexdump(const void *mem, uint32_t len, uint8_t cols = 16)
{
    const uint8_t *src = (const uint8_t *)mem;
    USE_SERIAL.printf("\n[HEXDUMP] Address: 0x%08X len: 0x%X (%d)", (ptrdiff_t)src, len, len);
    for (uint32_t i = 0; i < len; i++)
    {
        if (i % cols == 0)
        {
            USE_SERIAL.printf("\n[0x%08X] 0x%08X: ", (ptrdiff_t)src, i);
        }
        USE_SERIAL.printf("%02X ", *src);
        src++;
    }
    USE_SERIAL.printf("\n");
}

unsigned long getTime()
{
    time_t now;
    struct tm timeinfo;

    if (!getLocalTime(&timeinfo))
    {
        // Serial.println("Failed to obtain time");
        return (0);
    }

    time(&now);

    return now;
}

void webSocketEvent(WStype_t type, uint8_t *payload, size_t length)
{

    switch (type)
    {
    case WStype_DISCONNECTED:
        USE_SERIAL.printf("[WSc] Disconnected!\n");
        connected = false;
        break;
    case WStype_CONNECTED:
        USE_SERIAL.printf("[WSc] Connected to url: %s\n", payload);

        // send message to server when Connected
        // webSocket.sendTXT("Connected");
        connected = true;
        break;
    case WStype_TEXT:
        USE_SERIAL.printf("[Pkg] [Recv] %s\n", payload);
        recv_handle((char *)payload);
        // send message to server
        // webSocket.sendTXT("message here");
        break;
    case WStype_BIN:
        USE_SERIAL.printf("[Pkg] [Recv] [BIN] %u\n", length);
        hexdump(payload, length);

        // send data to server
        // webSocket.sendBIN(payload, length);
        break;
    case WStype_ERROR:
    case WStype_FRAGMENT_TEXT_START:
    case WStype_FRAGMENT_BIN_START:
    case WStype_FRAGMENT:
    case WStype_FRAGMENT_FIN:
        break;
    }
}

void setup()
{
    // USE_SERIAL.begin(921600);
    USE_SERIAL.begin(115200);

    // Serial.setDebugOutput(true);
    USE_SERIAL.setDebugOutput(true);

    for (uint8_t t = 4; t > 0; t--)
    {
        USE_SERIAL.printf("[SETUP] BOOT WAIT %d...\n", t);
        USE_SERIAL.flush();
        delay(1000);
    }

    WiFi.begin(ssid, password);

    // WiFi.disconnect();
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(100);
    }

    configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);

    // server address, port and URL
    webSocket.begin(websockets_server_host, websockets_server_port, websockets_server_url);

    // event handler
    webSocket.onEvent(webSocketEvent);

    // use HTTP Basic Authorization this is optional remove if not needed
    // webSocket.setAuthorization("admin", "022c74f");

    // try ever 5000 again if connection has failed
    webSocket.setReconnectInterval(5000);

    pinMode(TEST_LED_PIN, OUTPUT);
    pinMode(TEST_BUTTON_PIN, INPUT_PULLUP);

    // IR
    ac1.begin();
    ac2.begin();

    Serial.begin(115200);
    while (!Serial) {}

    if (!radio.begin()) {
        Serial.println(F("radio hardware is not responding!!"));
        while (1) {}  // hold in infinite loop
    }

    Serial.println(F("RF24/examples/GettingStarted"));

    radioNumber = 1;
    Serial.print(F("radioNumber = "));
    Serial.println((int)radioNumber);

    // Serial.println(F("*** PRESS 'T' to begin to control light"));


    radio.setPALevel(RF24_PA_LOW);  // RF24_PA_MAX is default.

    radio.setPayloadSize(sizeof(light_command));  // float datatype occupies 4 bytes

    radio.openWritingPipe(address[radioNumber]);  // always uses pipe 0

    radio.openReadingPipe(1, address[!radioNumber]);  // using pipe 1

    if (role) {
        radio.stopListening();  // put radio in TX mode
    } else {
        radio.startListening();  // put radio in RX mode
    }

}

unsigned long lastUpdate = millis();

void loop()
{
    webSocket.loop();
    if (connected && lastUpdate + interval < millis())
    {
        epochTime = getTime();

        String str = "{\"time\": " + String(epochTime) + ", \"gateway_id\": " + String(GATEWAY_ID) + ", \"event_type\": \"" + String(EVENT_TYPE_META) + "\", \"meta_type\": \"" + String(META_EVENT_TYPE_HEARTBEAT) + "\", \"interval\": " + String(interval) + "}";
        USE_SERIAL.print("[Pkg] [Send] ");
        USE_SERIAL.println(str);
        webSocket.sendTXT(str);
        lastUpdate = millis();
    }
    if (!digitalRead(TEST_BUTTON_PIN))
    {
        delay(10);
        if (!digitalRead(TEST_BUTTON_PIN))
        {
            epochTime = getTime();

            USE_SERIAL.println("[Brd] button pressed");
            led = !digitalRead(TEST_LED_PIN);
            digitalWrite(TEST_LED_PIN, led);
            if (connected)
            {
                String str = "{\"time\": " + String(epochTime) + ", \"gateway_id\": " + String(GATEWAY_ID) + ", \"event_type\": \"" + String(EVENT_TYPE_NOTICE) + "\", \"notice_type\": \"" + String(NOTICE_EVENT_TYPE_POWER_SWITCH_EVENT) + ", \"data\": {\"device_id\": " + String(1) + ", \"switch\": " + String(led) + "}}";
                USE_SERIAL.print("[Pkg] [Send] ");
                USE_SERIAL.println(str);
                webSocket.sendTXT(str);
            }
            while (!digitalRead(TEST_BUTTON_PIN))
            {
                delay(10);
            }
        }
    }



    if (role) {// This device is a TX node

      unsigned long start_timer = micros();                // start the timer

      bool report = radio.write(&light_command, sizeof(int)); // transmit 

      unsigned long end_timer = micros();                  // end the timer

        if (report) {
            Serial.print(F("Transmission successful! "));  // payload was delivered
            Serial.print(F("Time to transmit = "));
            Serial.print(end_timer - start_timer);  // print the timer result
            Serial.print(F(" us. Sent: "));
            Serial.println(light_command);  // print payload sent
            // payload += 0.01;          // increment float payload、
            //每次发送完，control_light置为负，目的是让控制台（网关）处于接受消息的状态，即接收电灯控制器的消息
            light_control = false;
            //light_command = light_command + 1;
            delay(1000);  // slow transmissions down by 1 second
        } 
        else {
            Serial.println(F("Transmission failed or timed out"));  // payload was not delivered
        }
    }else // This device is a RX node
    {

      uint8_t pipe;
      if (radio.available(&pipe)) {              // is there a payload? get the pipe number that recieved it
        uint8_t bytes = radio.getPayloadSize();  // get the size of the payload
        radio.read(&payload, bytes);             // fetch payload from FIFO
        Serial.print(F("Received "));
        Serial.print(bytes);  // print the size of the payload
        Serial.print(F(" bytes on pipe "));
        Serial.print(pipe);  // print the pipe number
        Serial.print(F(": "));
        Serial.println(payload);  // print the payload's value


        switch(int(payload/10)){
          case 1:
            if (int(payload)%10 == 0){
              Serial.print("report :");
              Serial.println("device 1 turn off ");
              flag1 = false;
            }
            else if(int(payload)%10 == 1){
              Serial.print("report :");
              Serial.println("device 1 turn on ");
              flag1 = true;
            }else{
              Serial.println("report error");
              break;
            }
            if (connected)
            {
                String resp = "{\"status\": \"" + String(API_STATUS_OK) + "\", \"retcode\": " + String(API_STATUS_OK_CODE) + ", \"data\": {\"device_id\": " + String(1) + ", \"switch\": " + String(flag1) + "}";
                USE_SERIAL.print("[Pkg] [Send] ");
                USE_SERIAL.println(resp);
                webSocket.sendTXT(resp);
            }
            break;
          case 2:
            if (int(payload)%10 == 0){
              Serial.print("report :");
              Serial.println("device 1 turn off ");       
              flag2 = false;                
            }
            else if(int(payload)%10 == 1){
              Serial.print("report :");
              Serial.println("device 1 turn on ");
              flag2 = true;
            }else{
              Serial.println("report error");
              break;
            }
            // if (connected)
            // {
            //     String resp = "{\"status\": \"" + String(API_STATUS_OK) + "\", \"retcode\": " + String(API_STATUS_OK_CODE) + ", \"data\": {\"device_id\": " + String(2) + ", \"switch\": " + String(flag2) + "}";
            //     USE_SERIAL.print("[Pkg] [Send] ");
            //     USE_SERIAL.println(resp);
            //     webSocket.sendTXT(resp);
            // }
            break;
          case 3:
            if (int(payload)%10 == 0){
              Serial.print("report :");
              Serial.println("device 1 turn off ");       
              flag3 = false;                 
            }
            else if(int(payload)%10 == 1){
              Serial.print("report :");
              Serial.println("device 1 turn on ");
              flag3 = true;
            }else{
              Serial.println("report error");
              break;
            }
            // if (connected)
            // {
            //     String resp = "{\"status\": \"" + String(API_STATUS_OK) + "\", \"retcode\": " + String(API_STATUS_OK_CODE) + ", \"data\": {\"device_id\": " + String(3) + ", \"switch\": " + String(flag3) + "}";
            //     USE_SERIAL.print("[Pkg] [Send] ");
            //     USE_SERIAL.println(resp);
            //     webSocket.sendTXT(resp);
            // }
            break;
          default: 
            // Serial.println("report error");
            // Serial.println(light_command);
            //计算出此时的电压
            payload = payload - 100;
            float v = float(payload)*3.3/1024;
            Serial.println("Analogh：");
            Serial.println(payload);
            Serial.println("V：");
            Serial.println(v);
            //再计算出电流值的大小
            Serial.println("A:");
            ele_value = (2.5/0.185)-(1/0.185)*v;
            Serial.println(ele_value);
            // if (connected)
            // {
            //     String resp = "{\"status\": \"" + String(API_STATUS_OK) + "\", \"retcode\": " + String(API_STATUS_OK_CODE) + ", \"data\": {\"device_id\": " + String(999) + ", \"switch\": " + String(ele_value) + "}";
            //     USE_SERIAL.print("[Pkg] [Send] ");
            //     USE_SERIAL.println(resp);
            //     webSocket.sendTXT(resp);
            // }
            break;
        }

      }
    }  // role

    delay(10000);
}
