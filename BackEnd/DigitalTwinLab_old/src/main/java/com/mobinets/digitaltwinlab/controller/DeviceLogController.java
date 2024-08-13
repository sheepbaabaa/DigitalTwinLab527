package com.mobinets.digitaltwinlab.controller;

import com.mobinets.digitaltwinlab.annotation.AdminRequired;
import com.mobinets.digitaltwinlab.annotation.LoginRequired;
import com.mobinets.digitaltwinlab.entity.User;
import com.mobinets.digitaltwinlab.service.DeviceLogService;
import com.mobinets.digitaltwinlab.util.response.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.Map;

@Controller
@RestController
@RequestMapping("/deviceLog")
public class DeviceLogController {
    @Autowired
    private DeviceLogService deviceLogService;
    /**
     * 获得指定设备日志
     */
    @RequestMapping(path = "/getLogs", method = RequestMethod.POST)
    public Response getLogs(@RequestParam("deviceId") int deviceId, HttpServletRequest request, HttpServletResponse httpResponse){
        return deviceLogService.selectLogsById(deviceId);
    }

    /**
     * 获得所有设备日志
     */
    @RequestMapping(path = "/getAllLogs", method = RequestMethod.GET)
    public Response getAllLog(HttpServletRequest request, HttpServletResponse httpResponse){
        return deviceLogService.selectAllLogs();
    }

    /**
     * 删除日志
     */
    @LoginRequired
    @AdminRequired
    @RequestMapping(path = "/clearLog", method = RequestMethod.POST)
    public Response clearLog(@RequestParam("timeNode") int timeNode,HttpServletRequest request, HttpServletResponse httpResponse){
        return deviceLogService.clearLog(timeNode);
    }

    /**
     * 获得登录用户的操作日志
     * @return
     */
    @LoginRequired
    @RequestMapping(path = "/getMyLog", method = RequestMethod.GET, produces = "application/json;charset=UTF-8")
    public Response getMyLog(HttpServletRequest request, HttpServletResponse httpResponse) {

        return deviceLogService.getMyLog();
    }

}
