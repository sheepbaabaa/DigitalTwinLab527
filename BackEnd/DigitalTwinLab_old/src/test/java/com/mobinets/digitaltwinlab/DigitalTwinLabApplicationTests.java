package com.mobinets.digitaltwinlab;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONArray;
import com.alibaba.fastjson.JSONObject;
import com.mobinets.digitaltwinlab.dao.StaffMapper;
import com.mobinets.digitaltwinlab.dao.UserMapper;
import com.mobinets.digitaltwinlab.entity.Staff;
import com.mobinets.digitaltwinlab.entity.User;
import com.mobinets.digitaltwinlab.util.CommunityUtil;
import org.apache.hc.client5.http.classic.methods.HttpGet;
import org.apache.hc.client5.http.impl.classic.CloseableHttpClient;
import org.apache.hc.client5.http.impl.classic.CloseableHttpResponse;
import org.apache.hc.client5.http.impl.classic.HttpClients;
import org.apache.hc.core5.http.HttpEntity;
import org.apache.hc.core5.http.ParseException;
import org.apache.hc.core5.http.io.entity.EntityUtils;
import org.junit.jupiter.api.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringRunner;

import java.io.IOException;
import java.util.Date;

@RunWith(SpringRunner.class)

@SpringBootTest(classes=DigitalTwinLabApplication.class,webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@ContextConfiguration(classes = DigitalTwinLabApplication.class)
class DigitalTwinLabApplicationTests {

    @Autowired
    private UserMapper userMapper;

    @Autowired
    private StaffMapper staffMapper;

    @Test
    public void testSelectStaff() {
        Staff staff = staffMapper.selectByCampusNum("202121080731");
        System.out.println(staff);

        staff = staffMapper.selectByName("刘江澍");
        System.out.println(staff);


    }

    @Test
    public void testInsertUser() {
        User user = new User();
        user.setCampusNum("202121080730");
        user.setPassword("zhuoliu");
        user.setEmail("zhuoliu@mobinets.org");
        user.setSalt("abc");
        user.setType(1);
        user.setStatus(1);
        user.setCreateTime(new Date());

        int rows = userMapper.insertUser(user);
        System.out.println(rows);
        System.out.println(user.getId());

    }

    @Test
    public void testsalt(){
        String name = "system";
        String salt = "abc";
        String res = new String();
        res = CommunityUtil.md5(name+salt);
        System.out.println(res);
    }

}
