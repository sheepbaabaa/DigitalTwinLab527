package com.mobinets.digitaltwinlab;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan("com.mobinets")
public class DigitalTwinLabApplication {

    public static void main(String[] args) {
        SpringApplication.run(DigitalTwinLabApplication.class, args);
    }

}
