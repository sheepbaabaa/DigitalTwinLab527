package com.mobinets.digitaltwinlab.controller;

import com.alibaba.fastjson.JSONObject;
import com.mobinets.digitaltwinlab.service.DeviceService;
import com.mobinets.digitaltwinlab.util.response.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.data.redis.core.ValueOperations;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Controller
@RestController
@RequestMapping("/deviceManager")
public class DeviceController {


    @Autowired
    private DeviceService deviceService;
    /**
     * 获得所有设备
     */
    @RequestMapping(path = "/getAllDevice", method = RequestMethod.GET)
    public Response getAllDevice(HttpServletRequest request, HttpServletResponse httpResponse){
        return deviceService.selectAllDevice();
    }

    /**
     * 获得指定id设备信息
     */
    @RequestMapping(path = "/getDeviceInfo", method = RequestMethod.POST)
    public Response getDeviceInfo(@RequestParam("id") int id, HttpServletRequest request, HttpServletResponse httpResponse){
        return deviceService.selectDeviceInfo(id);
    }

}
