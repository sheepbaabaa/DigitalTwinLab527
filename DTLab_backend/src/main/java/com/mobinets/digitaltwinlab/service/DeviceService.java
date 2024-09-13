package com.mobinets.digitaltwinlab.service;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.mobinets.digitaltwinlab.dao.DeviceMapper;
import com.mobinets.digitaltwinlab.entity.Device;
import com.mobinets.digitaltwinlab.entity.DeviceType;
import com.mobinets.digitaltwinlab.util.response.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.ValueOperations;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class DeviceService {
    @Autowired
    RedisTemplate<String, Object> redisTemplate;

    @Autowired
    private DeviceMapper deviceMapper;

    public Response selectAllDevice(){
        List<Device> deviceList=deviceMapper.selectAll();
        Map<String,List<Device>> deviceMapItem = new HashMap<String,List<Device>>();
        deviceMapItem.put("devices",deviceList);
        return Response.success(JSON.parseObject(JSON.toJSONString(deviceMapItem),Map.class));
    }

    public Response selectDeviceInfo(int id){
        Map<String,Object> resultData=new HashMap<String,Object>();
        resultData.put("info",redisTemplate.opsForValue().get("device"+id));
        return Response.success(resultData);
    }

    public boolean changeLightsState(JSONArray result) {
        try {
            ValueOperations ops = redisTemplate.opsForValue();
            for (int i = 0; i < result.size(); i++) {
                JSONObject jsonObject = result.getJSONObject(i);
                JSONObject device = (JSONObject) ops.get("device"+jsonObject.get("device_id"));
                device.put("switch",jsonObject.get("value"));
                System.out.println(device);
                ops.set("device"+jsonObject.get("device_id"),device);
            }
            return true;
        }
        catch (Exception e){
            return false;
        }

    }
    public boolean changeMonitorState(JSONArray result){
        try{
            ValueOperations ops = redisTemplate.opsForValue();
            for (int i = 0; i < result.size(); i++) {
                JSONObject jsonObject = result.getJSONObject(i);
                JSONObject device = (JSONObject) ops.get("device"+jsonObject.get("device_id"));
                device.put("switch",jsonObject.get("value"));
                System.out.println(device);
                ops.set("device"+jsonObject.get("device_id"),device);
            }
            return true;
        }
        catch (Exception e){
            return false;
        }
    }
    public boolean changeAircoditionState(JSONArray result) {
        try {
            ValueOperations ops = redisTemplate.opsForValue();
            for (int i = 0; i < result.size(); i++) {
                JSONObject jsonObject = result.getJSONObject(i);
                JSONObject device = (JSONObject) ops.get("device"+jsonObject.get("device_id"));
                device.put("power",jsonObject.get("power"));
                device.put("mode",jsonObject.get("mode"));
                device.put("basic_fan",jsonObject.get("basic_fan"));
                device.put("temp",jsonObject.get("temp"));
                device.put("turbo",jsonObject.get("turbo"));
                device.put("light",jsonObject.get("light"));
                device.put("xfan",jsonObject.get("xfan"));
                device.put("swing_v",jsonObject.get("swing_v"));
                device.put("swing_h",jsonObject.get("swing_h"));
                ops.set("device"+jsonObject.get("device_id"),device);
            }
            return true;
        }
        catch (Exception e){
            return false;
        }

    }

}
