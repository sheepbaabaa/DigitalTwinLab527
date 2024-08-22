package com.mobinets.digitaltwinlab.controller;

import com.alibaba.fastjson.JSONObject;
import com.mobinets.digitaltwinlab.dao.StaffMapper;
import com.mobinets.digitaltwinlab.entity.Staff;
import com.mobinets.digitaltwinlab.websocket.impl.WebSocketScheduled;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller
@RequestMapping("/person")
public class PersonController {
    @Autowired
    WebSocketScheduled webSocketScheduled;
    @Autowired
    private StaffMapper staffMapper;

    @GetMapping("/getAllStaff")
    @ResponseBody
    public String getAllStaff(){
        List<Staff> result = staffMapper.selectAllStaff();
        return JSONObject.toJSONString(result);
    }

    @GetMapping("/changeStaffState")
    @ResponseBody
    public JSONObject changeStaffState() {
        String data="{" +
                "    " +
                "    \"In Lab\": {" +
                "        \"time\" : \"2022-10-24 16_06_22\",\n" +
                "        \"name\": \"liuzhuoliu\"\n" +
                "    },\n" +
                "    \"Out Lab\": {\n" +
                "        \"time\": \"2022-10-24 16_06_22\",\n" +
                "        \"name\": \"zhanglinyuanqi\"\n" +
                "    }\n" +
                "}";
        String[] cameras={"In Lab","Out Lab","In Meeting Room","Out Meeting Room"};
        JSONObject jsonData=JSONObject.parseObject(data);
        JSONObject result = new JSONObject();
        result.put("type","peopleInout");
        for (String camera:cameras) {
            JSONObject temp= (JSONObject) jsonData.get(camera);
            if(temp==null){
                continue;
            }
            Staff persionInfo = staffMapper.selectByEnglishName((String) temp.get("name"));
            temp.put("name_zh",persionInfo.getNameZh());
            temp.put("member_id",persionInfo.getMemberId());
            result.put(camera,temp);
            //更新数据库状态
            updateDbState(persionInfo.getMemberId(),camera);

        }
        webSocketScheduled.sendInfoAll(JSONObject.toJSONString(result));
        JSONObject json = new JSONObject();
        json.put("code", 200);
        json.put("message", "success");
        return json;
    }

    public void updateDbState(int memberId ,String action){
        if (action == "In Lab") {
            staffMapper.updatePersonState(memberId,"In_Lab");
        }
        else if (action == "Out Lab") {
            staffMapper.updatePersonState(memberId,"Out_Lab");
        }
        else if (action == "In Meeting Room") {
            staffMapper.updatePersonState(memberId,"In_Meeting_Room");
        }
        else if (action == "Out Meeting Room") {
            staffMapper.updatePersonState(memberId,"In_Lab");
        }
    }
}
