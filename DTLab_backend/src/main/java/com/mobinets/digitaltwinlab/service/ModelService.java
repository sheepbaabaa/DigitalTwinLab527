package com.mobinets.digitaltwinlab.service;

import com.alibaba.fastjson.JSON;
import com.mobinets.digitaltwinlab.annotation.AdminRequired;
import com.mobinets.digitaltwinlab.annotation.LoginRequired;
import com.mobinets.digitaltwinlab.dao.ModelMapper;
import com.mobinets.digitaltwinlab.entity.Model;
import com.mobinets.digitaltwinlab.entity.User;
import com.mobinets.digitaltwinlab.util.CommunityConstant;
import com.mobinets.digitaltwinlab.util.CommunityUtil;
import com.mobinets.digitaltwinlab.util.HostHolder;
import com.mobinets.digitaltwinlab.util.response.Response;
import org.apache.catalina.mapper.Mapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


@Service
public class ModelService implements CommunityConstant {
    @Value("${digitaltwinlab.path.upload}")
    private String uploadFilePath;

    @Autowired
    private ModelMapper modelMapper;

    @Autowired
    private HostHolder hostHolder;

    public Response getLatestModel(){
       Model model=modelMapper.selectLatestModel();
       Map<String, Object> map = new HashMap<>();
       map.put("modelInfo",model);
       return Response.success(map);
    }

    public Response getAllModel(){

        List<Model> models=modelMapper.selectAll();
        Map<String,List<Model>> modelList = new HashMap<String,List<Model>>();
        modelList.put("modelList",models);
        return Response.success(JSON.parseObject(JSON.toJSONString(modelList), Map.class));
    }

    public Response uploadModel(MultipartFile modelFile) throws IOException {
        //获取文件名称
        String filename = CommunityUtil.generateUUID();
        String destFilePath = String.format(uploadFilePath+"/model/%s", filename);
        File destPath = new File(destFilePath);
        //调用transferTo将上传的文件保存到指定的地址
        try{
            modelFile.transferTo(destPath);
        }catch (IOException e){
            return Response.failure("failed to save file");
        }
        Model model=new Model();
        model.setUploadDate(new Date());
        model.setFileName(filename);
        model.setUploaderId(hostHolder.getUser().getId());
        Map<String, Object> map = new HashMap<>();
        modelMapper.insertModel(model);
        map.put("modelInfo",model);
        return Response.success(map);
    }

}
