package com.mobinets.digitaltwinlab.controller;

import com.alibaba.fastjson.JSONObject;
import com.mobinets.digitaltwinlab.annotation.AdminRequired;
import com.mobinets.digitaltwinlab.annotation.LoginRequired;
import com.mobinets.digitaltwinlab.dao.StaffMapper;
import com.mobinets.digitaltwinlab.entity.Staff;
import com.mobinets.digitaltwinlab.service.ModelService;
import com.mobinets.digitaltwinlab.service.UserService;
import com.mobinets.digitaltwinlab.util.response.Response;
import com.mobinets.digitaltwinlab.websocket.impl.WebSocketScheduled;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.File;
import java.io.IOException;
import java.util.List;

@RestController
@RequestMapping("/model")
public class ModelController {

    @Value("${digitaltwinlab.path.upload}")
    private String uploadFilePath;

    @Autowired
    private ModelService modelService;

    @LoginRequired
    @AdminRequired
    @RequestMapping("/uploadModelFile")
    public Response upload(@RequestParam("modelFile") MultipartFile modelFile, HttpServletRequest request, HttpServletResponse httpResponse) throws IOException {
        return modelService.uploadModel(modelFile);
    }

    @RequestMapping(path = "/getLatestModel", method = RequestMethod.GET)
    public Response getLatestModel(HttpServletRequest request, HttpServletResponse httpResponse){
        return modelService.getLatestModel();
    }

    @LoginRequired
    @AdminRequired
    @RequestMapping(path = "/getAllModels", method = RequestMethod.GET)
    public Response getAllModels(HttpServletRequest request, HttpServletResponse httpResponse){
        return modelService.getAllModel();
    }
}
