package com.mobinets.digitaltwinlab;

import com.mobinets.digitaltwinlab.util.MailClient;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringRunner;
import org.thymeleaf.TemplateEngine;
import org.thymeleaf.context.Context;

@RunWith(SpringRunner.class)
@SpringBootTest
@ContextConfiguration(classes = DigitalTwinLabApplication.class)
@MapperScan({"com.mobinets.digitaltwinlab.dao"})
public class MailTests {
    @Autowired
    private MailClient mailClient;

    @Autowired
    private TemplateEngine templateEngine;

    @Test
    public void testTextMail() {
        mailClient.sendMail("2097733073@qq.com", "TEST_FROM_LIUJIANGSHU", "你好");
    }

    @Test
    public void testHtmlMail() {
        Context context = new Context();
        context.setVariable("username", "Teacher Wang");

        String content = templateEngine.process("/mail/demo", context);
        System.out.println(content);

        mailClient.sendMail("jiangshu@mobinets.org", "HTML_TEST_FROM_LIUJIANGSHU", content);
    }
}
