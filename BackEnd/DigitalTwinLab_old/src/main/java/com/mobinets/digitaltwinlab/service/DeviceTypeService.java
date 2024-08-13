package com.mobinets.digitaltwinlab.service;

import com.alibaba.fastjson.JSON;
import com.mobinets.digitaltwinlab.dao.DeviceTypeMapper;
import com.mobinets.digitaltwinlab.entity.DeviceType;
import com.mobinets.digitaltwinlab.entity.Model;
import com.mobinets.digitaltwinlab.util.response.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class DeviceTypeService {

    @Autowired
    private DeviceTypeMapper deviceTypeMapper;

    public Response selectAllDeviceType(){
        List<DeviceType> deviceTypeList=deviceTypeMapper.selectAll();
        Map<String,List<DeviceType>> deviceTypeMapItem = new HashMap<String,List<DeviceType>>();
        deviceTypeMapItem.put("deviceTypes",deviceTypeList);
        return Response.success(JSON.parseObject(JSON.toJSONString(deviceTypeMapItem),Map.class));
    }
}
