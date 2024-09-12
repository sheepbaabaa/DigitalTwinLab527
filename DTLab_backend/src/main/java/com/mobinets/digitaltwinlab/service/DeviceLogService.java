package com.mobinets.digitaltwinlab.service;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.mobinets.digitaltwinlab.dao.DeviceLogMapper;
import com.mobinets.digitaltwinlab.dao.DeviceMapper;
import com.mobinets.digitaltwinlab.entity.Device;
import com.mobinets.digitaltwinlab.entity.DeviceLog;
import com.mobinets.digitaltwinlab.entity.User;
import com.mobinets.digitaltwinlab.util.HostHolder;
import com.mobinets.digitaltwinlab.util.response.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

import java.security.Timestamp;
import java.text.SimpleDateFormat;
import java.util.*;

@Service
public class DeviceLogService {

    @Autowired
    private HostHolder hostHolder;
    @Autowired
    private DeviceLogMapper deviceLogMapper;
    @Autowired
    RedisTemplate<String, Object> redisTemplate;

    public void insertDeviceLogs(JSONObject deviceInfo,int userId){
        Set<String> keySet=deviceInfo.keySet();
        JSONObject oldData= (JSONObject) redisTemplate.opsForValue().get("device"+deviceInfo.getString("device_id"));
        for(String key:keySet){
            //发生改变
            if(!deviceInfo.getString(key).equals(oldData.getString(key))){
                DeviceLog deviceLog=new DeviceLog();
                deviceLog.setDeviceId(Integer.parseInt(deviceInfo.getString("device_id")));
                deviceLog.setDeviceName(oldData.getString("device_name"));
                deviceLog.setOperatorId(userId);
                deviceLog.setOperation(key);
                deviceLog.setChangeDate(new Date());
                deviceLog.setNewValue(deviceInfo.getString(key));
                deviceLog.setOldValue(oldData.getString(key));
                deviceLogMapper.insertDeviceLog(deviceLog);
            }
        }
    }

    public Response selectAllLogs(){
        List<DeviceLog> deviceLogs=deviceLogMapper.selectAll();
        Map<String,List<DeviceLog>> deviceLogItem = new HashMap<String,List<DeviceLog>>();
        deviceLogItem.put("deviceLogs",deviceLogs);
        return Response.success(JSON.parseObject(JSON.toJSONString(deviceLogItem),Map.class));
    }

    public Response selectLogsById(int deviceId){
        List<DeviceLog> deviceList=deviceLogMapper.selectAll();
        Map<String,List<DeviceLog>> deviceMapItem = new HashMap<String,List<DeviceLog>>();
        deviceMapItem.put("deviceLogs",deviceList);
        return Response.success(JSON.parseObject(JSON.toJSONString(deviceMapItem),Map.class));
    }

    public Response getMyLog(){
        User user=hostHolder.getUser();
        int userId=user.getId();
        List<DeviceLog> deviceList=deviceLogMapper.selectByUserId(userId);
        Map<String,List<DeviceLog>> deviceMapItem = new HashMap<String,List<DeviceLog>>();
        deviceMapItem.put("deviceLogs",deviceList);
        return Response.success(JSON.parseObject(JSON.toJSONString(deviceMapItem),Map.class));
    }

    public Response clearLog(int timeNode){
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        Date date= new Date(timeNode * 1000L);
        String time_Date = sdf.format(date);
        System.out.println(time_Date);
        deviceLogMapper.clearLog(time_Date);
        return Response.success();
    }
}
