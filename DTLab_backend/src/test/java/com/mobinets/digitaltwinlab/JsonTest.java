package com.mobinets.digitaltwinlab;

import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.mobinets.digitaltwinlab.util.RedisUtil;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.StringRedisTemplate;


public class JsonTest {


    @Test
    public void JSONTest() {
        JSONObject object = JSONObject
                .parseObject("{\"device\": [{\"deviceType\": \"1\", \"deviceID\": \"666888\", \"deviceStatus\": \"1\"}]}");
        JSONArray jsonArray = (JSONArray) object.get("device");
//        System.out.println(object.get("device"));
        for (Object jsonObject : jsonArray) {
            JSONObject jsonObject2 = (JSONObject) jsonObject;
            int deviceID = Integer.parseInt((String) jsonObject2.get("deviceID"));

            System.out.println((jsonObject2.get("deviceID")));
            System.out.println(deviceID);
        }
        System.out.println(jsonArray);

    }
}
