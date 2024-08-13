package com.mobinets.digitaltwinlab.controller.interceptor;

import com.alibaba.fastjson.JSONObject;
import com.mobinets.digitaltwinlab.annotation.AdminRequired;
import com.mobinets.digitaltwinlab.entity.LoginTicket;
import com.mobinets.digitaltwinlab.entity.User;
import com.mobinets.digitaltwinlab.service.UserService;
import com.mobinets.digitaltwinlab.util.CookieUtil;
import com.mobinets.digitaltwinlab.util.HostHolder;
import com.mobinets.digitaltwinlab.util.response.Response;
import com.mobinets.digitaltwinlab.util.response.ResponseCode;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.method.HandlerMethod;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.PrintWriter;
import java.lang.reflect.Method;
import java.util.Date;

@Component
public class LoginTicketInterceptor implements HandlerInterceptor {

    @Autowired
    private UserService userService;

    @Autowired
    private HostHolder hostHolder;

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        //从cookie中获取凭证
        String ticket = CookieUtil.getValue(request,"ticket");
        System.out.println(ticket);
        if(ticket != null) {
            // 查询凭证
            LoginTicket loginTicket = userService.findLoginTicket(ticket);
            // 检查凭证是否有效
            if(loginTicket != null && loginTicket.getStatus()==0 && loginTicket.getExpired().after(new Date())) {
                // 根据凭证查询用户
                User user = userService.findUserById(loginTicket.getUserId());
                // 在本次请求中持有用户
                hostHolder.setUser(user);
                if(handler instanceof HandlerMethod){
                    HandlerMethod handlerMethod =(HandlerMethod) handler;
                    Method method=handlerMethod.getMethod();
                    AdminRequired adminRequired=method.getAnnotation(AdminRequired.class);
                    //需要管理权限且非管理员
                    if(adminRequired!=null && user.getType()!=2){
                        Response r =Response.failure(ResponseCode.PERMISSION_ERROR);
                        response.setStatus(200);
                        response.setCharacterEncoding("UTF-8");
                        response.setContentType("application/json");
                        PrintWriter writer = response.getWriter();
                        writer.write(JSONObject.toJSONString(r));
                        writer.close();
                        return false;
                    }
                }
            }
            else
            {
                Response r =Response.failure(ResponseCode.NOT_LOGGED_IN);
                response.setStatus(200);
                response.setCharacterEncoding("UTF-8");
                response.setContentType("application/json");
                PrintWriter writer = response.getWriter();
                writer.write(JSONObject.toJSONString(r));
                writer.close();
                return false;
            }
        }
        return true;
    }

    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
        User user = hostHolder.getUser();
        if(user != null && modelAndView != null){
            modelAndView.addObject("loginUser",user);
        }
    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        hostHolder.clear();
    }
}
