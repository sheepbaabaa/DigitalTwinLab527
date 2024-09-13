package com.mobinets.digitaltwinlab.controller;

import com.mobinets.digitaltwinlab.entity.User;
import com.mobinets.digitaltwinlab.service.WeatherServer;
import com.mobinets.digitaltwinlab.util.response.Response;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;


import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
@RestController
@RequestMapping("/weather")
public class WeatherController {


    @Autowired
    private WeatherServer weatherServer;

    @RequestMapping(path = "/getWeather", method = RequestMethod.GET)
    public Response getWeather(HttpServletRequest request, HttpServletResponse httpResponse){

        Object weatherInfo =weatherServer.weatherGet();
        Map<String,Object> data = new HashMap<String,Object>();
        data.put("weatherInfo",weatherInfo);
        return Response.success(data);
    }

}
