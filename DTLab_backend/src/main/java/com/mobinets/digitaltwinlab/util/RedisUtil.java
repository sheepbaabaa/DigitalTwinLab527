package com.mobinets.digitaltwinlab.util;
import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Component;



@Component
public  class RedisUtil {
    @Autowired
    private RedisTemplate redisTemplate;
    public static RedisTemplate redis;
    @PostConstruct
    public void getRedisTemplate(){
        redis=this.redisTemplate;
    }

}
