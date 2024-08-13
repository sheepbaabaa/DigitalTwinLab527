package com.mobinets.digitaltwinlab.controller;

import com.alibaba.fastjson.JSON;
import com.mobinets.digitaltwinlab.annotation.AdminRequired;
import com.mobinets.digitaltwinlab.annotation.LoginRequired;
import com.mobinets.digitaltwinlab.dao.DeviceMapper;
import com.mobinets.digitaltwinlab.entity.Device;
import com.mobinets.digitaltwinlab.entity.User;
import com.mobinets.digitaltwinlab.service.UserService;
import com.mobinets.digitaltwinlab.util.CookieUtil;
import com.mobinets.digitaltwinlab.util.HostHolder;
import com.mobinets.digitaltwinlab.util.response.Response;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.*;

@Controller
@RestController
@RequestMapping("/user")
public class UserController {

    private static final Logger logger = LoggerFactory.getLogger(UserController.class);

    @Value("${digitaltwinlab.path.upload}")
    private String uploadPath;

    @Value("${digitaltwinlab.path.domain}")
    private String domain;

    @Value("${server.servlet.context-path}")
    private String contextPath;

    @Autowired
    private UserService userService;

    @Autowired
    private HostHolder hostHolder;

    @Autowired
    private DeviceMapper deviceMapper;


    @RequestMapping(path = "/header/{filename}", method = RequestMethod.GET)
    public void getHeader(@PathVariable("filename") String filename, HttpServletResponse response) {
        // 服务器存放路径
        filename = uploadPath + "/" + filename;
        // 文件后缀
        String suffix = filename.substring(filename.lastIndexOf(".") + 1);
        response.setContentType("image/" + suffix);
        try(
                FileInputStream fis = new FileInputStream(filename);
                OutputStream os = response.getOutputStream();
                ) {
            byte[] buffer  = new byte[1024];
            int b = 0;
            while ((b = fis.read(buffer)) != -1){
                os.write(buffer,0,b);
            }
        } catch (IOException e) {
            logger.error("读取图像失败！" + e.getMessage());
        }
    }

    @GetMapping("/deviceStatus")
    @ResponseBody
    public List<Device> getDeviceGroup() {
        return deviceMapper.selectAll();
    }

//    @GetMapping("/change1")
//    public String changeID() {
//        deviceMapper.updateStatus(1,1);
//        deviceMapper.updateChangeTime(1,new Date());
//        return "redirect:/user/deviceStatus";
//    }
    /**
     * 删除用户
     * @return
     */
    @LoginRequired
    @AdminRequired
    @RequestMapping(path = "/deleteUser", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
    public Response deleteUser(@RequestParam("id") int id, HttpServletRequest request, HttpServletResponse httpResponse) {
        return userService.deleteUser(id);
    }
    /**
     * 更改用户Type
     * @return
     */
    @LoginRequired
    @AdminRequired
    @RequestMapping(path = "/changeUserType", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
    public Response changeUserType(@RequestParam("id") int id, @RequestParam("type") int type, HttpServletRequest request, HttpServletResponse httpResponse) {
        return userService.changeUserType(id,type);
    }
    /**
     * 更改用户信息
     * @return
     */
    @LoginRequired
    @RequestMapping(path = "/changeUserInfo", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
    public Response changeUserInfo(@RequestParam("password") String password, @RequestParam("email") String email, HttpServletRequest request, HttpServletResponse httpResponse) {
        Map<String, Object> map = new HashMap<>();
        User user=userService.changeUserInfo(password,email);
        map.put("newUserInfo",user);
        return Response.success(map);
    }
    /**
     * 获得所有用户信息
     * @return
     */
    @LoginRequired
    @AdminRequired
    @RequestMapping(path = "/getAllUser", method = RequestMethod.GET)
    public Response getAllUser(HttpServletRequest request, HttpServletResponse httpResponse) {
        return userService.selectAllUser();
    }
    /**
     * 获得用户信息
     */
    @LoginRequired
    @RequestMapping(path = "/userInfo", method = RequestMethod.GET)
    public Response getUserInfo(HttpServletRequest request, HttpServletResponse httpResponse) {
        Map<String, Object> map = new HashMap<>();
        String ticket = CookieUtil.getValue(request,"ticket");
        User user=userService.getUserInfo();
        map.put("ticket",ticket);
        map.put("userInfo",user);
        return Response.success(map);
    }
}
