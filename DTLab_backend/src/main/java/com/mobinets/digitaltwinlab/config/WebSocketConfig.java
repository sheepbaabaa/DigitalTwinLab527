package com.mobinets.digitaltwinlab.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.socket.config.annotation.WebSocketMessageBrokerConfigurer;
import org.springframework.web.socket.server.standard.ServerEndpointExporter;

/**
 * 定义WebSocket服务器的端点，客户端可请求服务器的端点
 */
//@EnableWebSocketMessageBroker // 启动STOMP协议
@Configuration
//@ConditionalOnProperty(name = "spring.profiles.active", havingValue = "dev")
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    /**
     * 可通过这个Bean使用@ServerEndPoint定义一个端点服务类，在其中定义打开关闭和消息发送等方法
     * @return
     */
    @Bean
    public ServerEndpointExporter serverEndpointExporter() {
        return new ServerEndpointExporter();
    }
//    // 注册服务器端点
//    @Override
//    public void registerStompEndpoints(StompEndpointRegistry registry) {
//        // 增加聊天服务端点
//        registry.addEndpoint("/socket").withSockJS();
//        // 增加用户服务端点
//        registry.addEndpoint("/wsuser").withSockJS();
//    }
//    // 定义服务器端点请求和订阅前缀
//    @Override
//    public void configureMessageBroker(MessageBrokerRegistry registry) {
//        // 客户端订阅路径前缀
//        registry.enableSimpleBroker("/sub", "/queue");
//        // 服务端点请求前缀
//        registry.setApplicationDestinationPrefixes("/request");
//    }
}
