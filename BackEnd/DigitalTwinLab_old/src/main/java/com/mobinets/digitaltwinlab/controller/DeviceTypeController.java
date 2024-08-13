package com.mobinets.digitaltwinlab.controller;

import com.mobinets.digitaltwinlab.service.DeviceTypeService;
import com.mobinets.digitaltwinlab.util.response.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@Controller
@RestController
@RequestMapping("/deviceTypeManager")
public class DeviceTypeController {

    @Autowired
    private DeviceTypeService deviceTypeService;
    /**
     * 获得所有设备类别
     */
    @RequestMapping(path = "/getAllType", method = RequestMethod.GET)
    public Response getAllClass(HttpServletRequest request, HttpServletResponse httpResponse){
        return deviceTypeService.selectAllDeviceType();
    }
}
