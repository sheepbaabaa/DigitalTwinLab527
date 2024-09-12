package com.mobinets.digitaltwinlab.util;

import com.alibaba.fastjson.JSONObject;

import java.util.ArrayList;

public class MessageUtil {
    public String setPowerSwitch (String instructionID, ArrayList<String> params) {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("action","set_power_switch");
        jsonObject.put("echo", instructionID);
        jsonObject.put("params", params);
        return jsonObject.toJSONString();
    }
    public String setAirConditioner (String instructionID, ArrayList<String> params) {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("action","set_power_switch");
        jsonObject.put("echo", instructionID);
        jsonObject.put("params", params);
        return jsonObject.toJSONString();
    }
}
