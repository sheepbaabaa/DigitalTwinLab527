package com.mobinets.digitaltwinlab.controller;

import com.mobinets.digitaltwinlab.annotation.AdminRequired;
import com.mobinets.digitaltwinlab.annotation.LoginRequired;
import com.mobinets.digitaltwinlab.service.PermissionApplicationService;
import com.mobinets.digitaltwinlab.util.response.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;


import java.io.IOException;

@Controller
@RestController
@RequestMapping("/permissionApplication")
public class PermissionApplicationController {

    @Autowired
    private PermissionApplicationService permissionApplicationService;
    /**
     * 申请权限接口
     * @param permissionApplyFor
     * @param request
     * @param httpResponse
     * @return
     */
    @LoginRequired
    @RequestMapping(path ="/apply", method = RequestMethod.POST)
    public Response apply(@RequestParam("permissionApplyFor") int permissionApplyFor, HttpServletRequest request, HttpServletResponse httpResponse){
        return permissionApplicationService.permissionApply(permissionApplyFor);
    }


    /**
     * 审批接口
     * @param id
     * @param result
     * @param request
     * @param httpResponse
     * @return
     */
    @LoginRequired
    @AdminRequired
    @RequestMapping(path ="/approval", method = RequestMethod.POST)
    public Response approval(@RequestParam("id") int id,@RequestParam("result") int result, HttpServletRequest request, HttpServletResponse httpResponse) {
        return permissionApplicationService.approvalApplication(id,result);
    }

    /**
     * 获得申请列表
     * @param request
     * @param httpResponse
     * @return
     */
    @LoginRequired
    @AdminRequired
    @RequestMapping(path ="/getApplications", method = RequestMethod.GET)
    public Response getApplications(HttpServletRequest request, HttpServletResponse httpResponse){
        return permissionApplicationService.getApplications();
    }
}
