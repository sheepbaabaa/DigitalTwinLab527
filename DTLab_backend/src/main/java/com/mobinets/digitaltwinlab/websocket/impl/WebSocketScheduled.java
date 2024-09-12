package com.mobinets.digitaltwinlab.websocket.impl;

import com.mobinets.digitaltwinlab.websocket.WebSocketService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@EnableScheduling
@Component
public class WebSocketScheduled {
    @Autowired
    WebSocketService webSocketService;

    /**
     * 定时消息，可用于发送心跳包
     */
    @Scheduled(fixedRate = 1000 * 60 * 60 * 10)
//    @Scheduled(fixedRate = 1000)
    public void heartBeatSchedule() {
        webSocketService.setUserId("Server");
        webSocketService.heartBeat();
    }

    public void sendInfoAll(String data)
    {
        webSocketService.sendInfoAll(data);
    }
}
