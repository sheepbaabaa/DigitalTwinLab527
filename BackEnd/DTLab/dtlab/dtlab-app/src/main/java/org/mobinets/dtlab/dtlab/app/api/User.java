package org.mobinets.dtlab.dtlab.app.api;

import org.mobinets.dtlab.common.Response;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
public class User {

    /**
     * 注册页面，POST4个参数
     * @param username username
     * @param password password
     * @param campusNum campusNum
     * @param email email
     * @return return
     */
    @RequestMapping(path="/register", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
    public Response register(@RequestParam("username") String username, @RequestParam("password") String password,
                             @RequestParam("campusNum") String campusNum, @RequestParam("email") String email) {

    }
    /**
     * 激活账号
     * @param userId UserId
     * @param code 激活码
     * @return return
     */
    @RequestMapping(path="/activation/{userId}/{code}", method = RequestMethod.GET, produces = "application/json;charset=UTF-8")
    public String activation(@PathVariable("userId") int userId, @PathVariable("code") String code) {

    }

    /**
     * 登录
     * ·登录log
     * @param username username
     * @param password password
     * @param rememberMe rememberme 过期时间
     * @param httpResponse httpResponse
     * @return return
     */
    @RequestMapping(path = "/login", method = RequestMethod.POST, produces = "application/json;charset=UTF-8")
    public Response login(@RequestParam("username") String username, @RequestParam("password") String password,
                          @RequestParam("rememberMe") boolean rememberMe, HttpServletRequest request, HttpServletResponse httpResponse) {
    }

    @RequestMapping(path = "/logout",method = RequestMethod.GET)
    public String logout(@CookieValue("ticket") String ticket) {

    }

}
