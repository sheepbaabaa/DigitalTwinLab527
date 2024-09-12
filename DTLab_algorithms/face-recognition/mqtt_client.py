import json

import paho.mqtt.client as mqtt


class MqttClient:

    def __init__(self, client_id, broker, port, username, password):
        self.client_id = client_id
        self.broker = broker
        self.port = port
        self.username = username
        self.password = password
        self.client = self.connect()
        self.client.loop_start()

    def connect(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt.Client(client_id=self.client_id)
        client.username_pw_set(self.username, self.password)
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client

    def publish(self, topic, data):
        result = self.client.publish(topic, json.dumps(data))
        status = result[0]
        if status == 0:
            print(f"Send `{data}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def on_message(self, on_message):
        self.client.on_message = on_message

    def disconnect(self):
        self.client.disconnect()
