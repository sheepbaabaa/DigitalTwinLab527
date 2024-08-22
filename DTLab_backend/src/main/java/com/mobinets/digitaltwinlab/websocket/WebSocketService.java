package com.mobinets.digitaltwinlab.websocket;

import jakarta.websocket.*;
import jakarta.websocket.server.PathParam;


import java.io.IOException;
//@Service
public interface WebSocketService {
    /**
     * 连接建立时调用的方法
     * @param session session
     * @param clientType 客户端类型(webClient/gatewayClient)
     * @param userId 创建的用户Id
     */
    @OnOpen
    public void onOpen(Session session,
                       @PathParam("clientType") String clientType, @PathParam("userId") String userId);
    /**
     * 连接关闭时调用的方法
     */
    @OnClose
    public void onClose();

    /**
     * 服务器主动关闭连接
     *
     */
    public void closeSession();
    public void heartBeat();
    /**
     * 有消息到达时调用的方法
     * @param message message
     * @param session session
     */
    @OnMessage
    public void onMessage(String message, Session session);
    /**
     * 发生错误时调用的方法
     * @param session session
     * @param error error
     */
    @OnError
    public void onError(Session session, Throwable error);
    /**
     * 发送消息
     * @param message message
     * @throws IOException IOException
     */
    public void sendMessage(String message) throws IOException;
    /**
     * 向所有浏览器用户发送Info(真实世界控制器所更新的物理信息)
     * @param message 消息内容
     */
    public void sendInfoAll(String message);

    /**
     * 向Id为toUserId的用户发送消息
     * @param toUserId 目标用户Id
     * @param message 消息内容
     */
    public void sendToId(String toUserId, String message);

    public void HeartBeatCountAdder();
    /**
     * 向网关发送信息
     * @param message message
     */
    public void sendToGateway(String message);
    public void setUserId(String userId);
    public int getHeartBeatCount();
    public String getClientType();
    public String getUserId();

    public void test();

}
