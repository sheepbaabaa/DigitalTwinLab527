package com.mobinets.digitaltwinlab.websocket.impl;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.mobinets.digitaltwinlab.dao.DeviceMapper;
import com.mobinets.digitaltwinlab.entity.Device;
import com.mobinets.digitaltwinlab.service.DeviceLogService;
import com.mobinets.digitaltwinlab.service.DeviceService;
import com.mobinets.digitaltwinlab.websocket.WebSocketService;
import org.apache.ibatis.annotations.Mapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.validation.constraints.NotNull;
import javax.websocket.*;
import javax.websocket.server.PathParam;
import javax.websocket.server.ServerEndpoint;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.CopyOnWriteArraySet;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * clientType: webClient, gatewayClient
 */
//@ConditionalOnClass(value = WebSocketConfig.class)
@ServerEndpoint("/ws/{clientType}/{userId}") // 创建WebSocket服务端点，请求地址是"/ws"
@Service
public class WebSocketServiceImpl implements WebSocketService {

    private static DeviceService deviceService;
    private static DeviceLogService deviceLogService;
    @Autowired
    public void setDeviceService(DeviceService deviceService) {
        WebSocketServiceImpl.deviceService = deviceService;
    }

    @Autowired
    public void setDeviceLogService(DeviceLogService deviceLogService) {WebSocketServiceImpl.deviceLogService = deviceLogService;}

    /**
     * 线程安全的计数器
     * webClientCount.getAndIncrement() ++, webClientCount.get(), webClientCount.getAndDecrement() --
     */
    private static final AtomicInteger webClientCount = new AtomicInteger();
    private static final AtomicInteger gatewayClientCount = new AtomicInteger();
    /**
     * 线程安全的集合，存放Websocket用户对象
     */
    private static final CopyOnWriteArraySet<WebSocketService> webSocketClientSet = new CopyOnWriteArraySet<>();
    /**
     * 与某个客户端的连接会话，通过session来给客户端发送数据
     */
    private Session session;
    private static final Logger log = LoggerFactory.getLogger(WebSocketService.class);

    private static DeviceMapper deviceMapper;

    @Autowired
    public void setDeviceMapper(DeviceMapper deviceMapper1) {
        WebSocketServiceImpl.deviceMapper = deviceMapper1;
    }

    //    private final DeviceService deviceService = new DeviceServiceImpl();
    private String userId = "";
    private String clientType = "";
    private int heartBeatCount = 0;

    @OnOpen
    public void onOpen(Session session,
                       @PathParam("clientType") String clientType,
                       @PathParam("userId") String userId) {
        this.session = session;
        this.setClientType(clientType);
        this.setUserId(userId);
        webSocketClientSet.add(this);
        // 网页客户端
        if (this.getClientType().equals("webClient")) {
            webClientCount.getAndIncrement(); // 在线数加一
            log.info("New webclient connected, UserID: " + this.userId + ", onLine number: " + webClientCount.get());
            try {
                // 网页客户端初始化时发送所有设备信息
                List<Device> devices = new ArrayList<>(deviceMapper.selectAll());
                JSONObject jsonObject = new JSONObject();
                jsonObject.put("isInit", true);
                jsonObject.put("device", devices);
                sendMessage(jsonObject.toJSONString());
            } catch (IOException e) {
                log.error("IO error");
            }
            // 网关客户端
        } else if (this.getClientType().equals("gatewayClient")) {
            gatewayClientCount.getAndIncrement();
            log.info("New gatewayClient connected, UserID: " + this.userId + "onLine number: " + gatewayClientCount.get());
            try {
                sendMessage("gateway connected!");
            } catch (IOException e) {
                log.error("IO error");
            }
        } else {
            log.error("Wrong Client type connecting, rejected");
            try {
                sendMessage("Wrong Client type");
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

    }

    @OnClose
    public void onClose() {
        webSocketClientSet.remove(this);
        if (this.clientType.equals("webClient")) {
            webClientCount.getAndDecrement();
            log.info("Webclient disconnected, onLine number: " + webClientCount.get());
        } else if (this.clientType.equals("gatewayClient")) {
            gatewayClientCount.getAndDecrement();
            log.info("GatewayClient disconnected, gateway number: " + gatewayClientCount.get());
        }
    }

    @Override
    public void closeSession() {
        Session session = this.session;
        if (!session.isOpen()) {
            log.error("session is not open!");
        }
        try {
            session.close();
        } catch (IOException e) {
            log.error("session close error");
        }
    }

    @Override
    public void heartBeat() {
        for (WebSocketService client : webSocketClientSet) {
            if (client.getHeartBeatCount() >= 3) {
                log.info("Client disconnected");
                client.closeSession();
            }else {
                client.HeartBeatCountAdder();
            }
        }

    }


    @OnMessage
    public void onMessage(String message, Session session) {
        if (message.contains("heartBeat")) {
            this.heartBeatCount = 0;
            return;
        }
        log.info("Message from client: " + this.userId + ", message: " + message);
        // 若是来自网关的消息，则转发给所有在线用户
        if (this.getClientType().equals("gatewayClient")) {
            JSONObject msg = JSON.parseObject(message);
            if(msg.get("response")==null){
                return;
            }
            if( msg.get("response").equals("response_light_state")){
                JSONArray data= msg.getJSONArray("data");
                if(!deviceService.changeLightsState(data)){
                    return;
                }
            }
            else if(msg.get("response").equals("response_aircodition_state")){
                JSONArray data= msg.getJSONArray("data");
                if(!deviceService.changeAircoditionState(data)){
                    return;
                }
            }
            else if(msg.get("response").equals("response_monitor_state")){
                JSONArray data= msg.getJSONArray("data");
                if(!deviceService.changeMonitorState(data)){
                    return;
                }
            }
            sendInfoAll(message);

            // 来自用户的消息
        } else {
            String action = JSON.parseObject(message).getString("action"); // 私发给用户的消息
            JSONObject deviceInfo = JSON.parseObject(message).getJSONObject("params");
            if(action.substring(0,3).equals("set")){
                deviceLogService.insertDeviceLogs(deviceInfo, Integer.parseInt(this.userId));
            }
            sendToGateway(message);
        }
    }

    @OnError
    public void onError(Session session, @NotNull Throwable error) {
        log.error("Error");
        error.printStackTrace();
    }

    public void sendInfoAll(String message) {
        for (WebSocketService user : webSocketClientSet) {
            try {
                if (user.getClientType().equals("webClient")) {
                    user.sendMessage((message));
                }
            } catch (IOException e) {
                e.printStackTrace();
            }

        }
    }

    public void sendToId(String toUserId, String message) {
        boolean isFound = false;
        for (WebSocketService user : webSocketClientSet) {
            String userId = user.getUserId();
            if (userId.equals(toUserId)) {
                try {
                    user.sendMessage(parseJSON(message));
                    isFound = true;
                    break;
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
        }
        if (!isFound) {
            log.info("toUser not online!");
            try {
                sendMessage("目标用户不在线！");
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    }

    public void sendToGateway(String message) {
        if (gatewayClientCount.get() != 0) {
            for (WebSocketService gateway : webSocketClientSet) {
                if (gateway.getClientType().equals("gatewayClient")) {
                    try {
                        gateway.sendMessage(parseJSON(message));
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                }
            }
        } else {
            try {
                log.error("No gateway online");
                Map<String,Object> res = new HashMap<>();
                res.put("msg","无网关设备在线");
                sendMessage(JSON.toJSONString(res));
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }
    }

    public void sendMessage(String message) throws IOException {
        this.session.getBasicRemote().sendText(message);
    }

    /**
     * 解析消息文本，并加入fromUserId信息
     *
     * @param message 消息内容，字符串
     * @return JSON格式字符串
     */
    private String parseJSON(String message) {
        JSONObject jsonObject = JSON.parseObject(message);
        jsonObject.put("fromUserID", this.userId);
        return jsonObject.toJSONString();
    }

    /**
     * 将设备信息变化写入数据库
     *
     * @param message 网关发送的消息文本
     */
    private void logSQL(String message) {
//        JSONObject jsonObject = JSONObject.parseObject(message);
////        JSONArray jsonArray = (JSONArray) jsonObject.get("device");
////        for (Object object : jsonArray) {
////            JSONObject jsonObject1 = (JSONObject) object;
//        JSONObject jsonObject1 = jsonObject;
//        int deviceID = Integer.parseInt((String)jsonObject1.get("deviceID"));
//        int deviceStatus = Integer.parseInt((String) jsonObject1.get("status"));
//        Date changeTime = new Date((Long) jsonObject1.get("changeTime"));
//        deviceMapper.updateStatus(deviceID, deviceStatus);
//        deviceMapper.updateChangeTime(deviceID, changeTime);
//        log.info("deviceID: " + deviceID + ", update Status: " + deviceStatus);
        }
//    }

    public String getClientType() {
        return clientType;
    }

    private void setClientType(String clientType) {
        this.clientType = clientType;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public int getHeartBeatCount() {
        return heartBeatCount;
    }

    public void setHeartBeatCount(int heartBeatCount) {
        this.heartBeatCount = heartBeatCount;
    }

    public void HeartBeatCountAdder(){
        this.heartBeatCount++;
    }

    public void test(){
        log.info("success");
    }
}