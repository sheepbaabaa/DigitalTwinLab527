package com.mobinets.digitaltwinlab.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
@RequestMapping("/websocket")
public class WebSocketController {
//    public WebSocketController(SimpMessagingTemplate simpMessagingTemplate) {
//        this.simpMessagingTemplate = simpMessagingTemplate;
//    }

    @GetMapping("")
    public ModelAndView  webSocket() {
        return new ModelAndView("websocketIndex");
    }

//    private final SimpMessagingTemplate simpMessagingTemplate;

//    @GetMapping("/send")
//    public String send() {
//        return "send";
//    }
}
