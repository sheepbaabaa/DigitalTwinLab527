package com.mobinets.digitaltwinlab.service;

import com.alibaba.fastjson.JSON;
import com.mobinets.digitaltwinlab.dao.LoginTicketMapper;
import com.mobinets.digitaltwinlab.dao.StaffMapper;
import com.mobinets.digitaltwinlab.dao.UserMapper;
import com.mobinets.digitaltwinlab.entity.LoginTicket;
import com.mobinets.digitaltwinlab.entity.Staff;
import com.mobinets.digitaltwinlab.entity.User;
import com.mobinets.digitaltwinlab.util.*;
import com.mobinets.digitaltwinlab.util.response.Response;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.thymeleaf.TemplateEngine;
import org.thymeleaf.context.Context;

import java.util.*;

@Service
public class UserService implements CommunityConstant {
    @Autowired
    private UserMapper userMapper;

    @Autowired
    private MailClient mailClient;

    @Autowired
    private TemplateEngine templateEngine;

    @Autowired
    private LoginTicketMapper loginTicketMapper;

    @Autowired
    private HostHolder hostHolder;

    @Autowired
    private StaffMapper staffMapper;

    @Value("${digitaltwinlab.path.domain}")
    private String domain;

    @Value("${server.servlet.context-path}")
    private String contextPath;

    public User findUserById(int id) {
        return userMapper.selectById(id);
    }

    public Response selectAllUser(){
        List<User> users=userMapper.selectAll();
        Map<String,List<User>> userList = new HashMap<String,List<User>>();
        userList.put("userList",users);
        return Response.success(JSON.parseObject(JSON.toJSONString(userList), Map.class));
    }
    public Response register(User user) {


        // 空值处理
        if(user == null) {
            throw new IllegalArgumentException("参数不能为空！");
        }
        if(StringUtils.isBlank(user.getUsername())) {
            return Response.failure("账号不能为空！")  ;
        }
        if(StringUtils.isBlank(user.getPassword())) {
            return Response.failure("密码不能为空！")  ;
        }
        if(StringUtils.isBlank(user.getEmail())) {
            return Response.failure("邮箱不能为空！")  ;
        }

        // 验证账号
        User u = userMapper.selectByUsername(user.getUsername());
        if(u != null) {
            return Response.failure("该用户名已存在！")  ;
        }

        // 验证邮箱
        u = userMapper.selectByEmail(user.getEmail());
        if(u != null) {
            return Response.failure("该邮箱已被注册！")  ;
        }



        // 查Staff表确定用户权限

        Staff staff = staffMapper.selectByCampusNum(user.getCampusNum());
        if(staff != null){
            user.setType(staff.getType());
        }else {
            return Response.failure("您暂无权限注册！");
        }
        // 注册用户
        user.setSalt(CommunityUtil.generateUUID().substring(0,5));//设置随机salt
        user.setPassword(CommunityUtil.md5(user.getPassword()+user.getSalt()));//密码加密
        // 激活状态
        user.setStatus(0);
        user.setActivationCode(CommunityUtil.generateUUID());
        user.setHeaderUrl(String.format("https://images.nowcoder.com/head/%dt.png", new Random().nextInt(100)));
        user.setCreateTime(new Date());
        userMapper.insertUser(user);

        // 激活邮件
        Context context = new Context();
        context.setVariable("email", user.getEmail());
        // http://localhost:8080/community/activation/101/code
        String url = domain + contextPath + "/activation/" + user.getId() + "/" +user.getActivationCode();
        context.setVariable("url", url);
        String content = templateEngine.process("/mail/activation", context);
        mailClient.sendMail(user.getEmail(), "激活账号", content);
        return Response.success("注册成功");
    }

    public int activation(int userId, String code) {
        User user = userMapper.selectById(userId);
        if(user.getStatus() == 1) {
            return ACTIVATION_REPEAT;
        } else if(user.getActivationCode().equals(code)) {
            userMapper.updateStatus(userId, 1);
            return ACTIVATION_SUCCESS;
        } else {
            return ACTIVATION_FAIL;
        }
    }

    public Response login(String username, String password, int expiredSeconds) {
        Map<String, Object> map = new HashMap<>();
        // 空值处理
        if(StringUtils.isBlank(username)) {
            return Response.failure("账号不能为空！");
        }
        if(StringUtils.isBlank(password)) {
            return Response.failure("密码不能为空！");
        }

        // 验证账号
        User user = userMapper.selectByUsername(username);
        if(user == null) {
            return Response.failure("该账号不存在！");
        }

        // 验证状态
        if(user.getStatus()==0){
            return Response.failure("该账号未激活！");
        }

        // 验证密码
        password = CommunityUtil.md5(password + user.getSalt());
        if(!user.getPassword().equals(password)){
            return Response.failure("密码错误！");
        }

        // 登录成功，生成登录凭证
        LoginTicket loginTicket = new LoginTicket();
        loginTicket.setUserId(user.getId());
        loginTicket.setTicket(CommunityUtil.generateUUID());
        loginTicket.setStatus(0);
        loginTicket.setExpired(new Date(System.currentTimeMillis() + expiredSeconds * 1000L));
        loginTicketMapper.insertLoginTicket(loginTicket);
        map.put("ticket",loginTicket.getTicket());
        map.put("userInfo",userMapper.selectById(user.getId()));
        return Response.success(map);
    }

    public void logout(String ticket) {
        loginTicketMapper.updateStatus(ticket,1);
    }

    public LoginTicket findLoginTicket(String ticket) {
        return loginTicketMapper.selectByTicket(ticket);
    }

    public int updateHeader(int userId, String headerUrl) {
        return userMapper.updateHeader(userId, headerUrl);
    }

    public User getUserInfo() {
        User user=hostHolder.getUser();
        return userMapper.selectById(user.getId());
    }

    public User changeUserInfo(String password,String email){

        User user=hostHolder.getUser();
        if(!password.equals("")){
            String newSalt = CommunityUtil.generateUUID().substring(0, 5);
            String newPassword=CommunityUtil.md5(password+newSalt);//密码加密
            userMapper.updatePassword(user.getId(),newPassword,newSalt);
        }
        userMapper.updateEmail(user.getId(),email);
        return userMapper.selectById(user.getId());
    }

    public Response changeUserType(int id,int type){
        User user=userMapper.selectById(id);
        if(user==null){
            return Response.failure("该用户ID不存在");
        }
        else
        {
            if(type!=1 && type!=2){
                return Response.failure("用户类别不合法");
            }
            else
            {
                userMapper.updateType(id,type);
                return Response.success("用户类型更新成功");
            }
        }
    }

    public Response deleteUser(int id){
        User user=userMapper.selectById(id);
        if(user==null){
            return Response.failure("该用户不存在");
        }
        else
        {
            userMapper.deleteUser(id);
            return Response.success("用户删除成功");
        }
    }

}
