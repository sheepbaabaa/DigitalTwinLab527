package com.mobinets.digitaltwinlab.controller;

import com.mobinets.digitaltwinlab.dao.DeviceMapper;
import com.mobinets.digitaltwinlab.entity.Device;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import java.util.Arrays;
import java.util.List;

/**
 * 开启时自动运行
 */
@Component
@Order(1)
public class InitController implements CommandLineRunner {
    public static List<Device> deviceList;
    @Autowired
    private DeviceMapper deviceMapper;

    @Override
    public void run(String... args) throws Exception {
        System.out.println("Server started..." + Arrays.toString(args));
//        deviceService.getDeviceStatus(2);
    }
}
