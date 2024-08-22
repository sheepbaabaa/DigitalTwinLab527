package com.mobinets.digitaltwinlab.service;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.mobinets.digitaltwinlab.dao.PermissionApplicationMapper;
import com.mobinets.digitaltwinlab.dao.UserMapper;
import com.mobinets.digitaltwinlab.entity.PermissionApplication;
import com.mobinets.digitaltwinlab.entity.User;
import com.mobinets.digitaltwinlab.util.HostHolder;
import com.mobinets.digitaltwinlab.util.response.Response;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class PermissionApplicationService {
    @Autowired
    private HostHolder hostHolder;

    @Autowired
    private UserMapper userMapper;
    @Autowired
    private PermissionApplicationMapper permissionApplicationMapper;

    public Response permissionApply(int permissionApplyFor){
        User user=hostHolder.getUser();
        PermissionApplication permissionApplication=new PermissionApplication();
        permissionApplication.setDate(new Date());
        permissionApplication.setPermissionApplyFor(permissionApplyFor);
        permissionApplication.setApplicantId(user.getId());
        permissionApplicationMapper.insertApplication(permissionApplication);
        return Response.success();
    }

    public Response getApplications(){
        List<PermissionApplication> permissionApplications=permissionApplicationMapper.selectAllApplication();
        List<JSONObject> result=new ArrayList<>();
        permissionApplications.forEach((application)->{
            JSONObject jsonObject= (JSONObject) JSONObject.toJSON(application);
            User user= userMapper.selectById(application.getApplicantId());
            jsonObject.put("username",user.getUsername());
            jsonObject.put("email",user.getEmail());
            result.add(jsonObject);
        });
        Map<String,List<JSONObject>> item = new HashMap<String,List<JSONObject>>();
        item.put("applications",result);
        return Response.success(JSON.parseObject(JSON.toJSONString(item),Map.class));
    }

    public Response approvalApplication(int id,int result){
        if(result==1){
            permissionApplicationMapper.updateProcessedResult(id,1,new Date()); //更新处理结果
            PermissionApplication permissionInfo=permissionApplicationMapper.selectById(id);
            userMapper.updateType(permissionInfo.getApplicantId(),permissionInfo.getPermissionApplyFor());
        }else if(result==2) {
            permissionApplicationMapper.updateProcessedResult(id,1,new Date());
        }
        return Response.success();
    }


}
