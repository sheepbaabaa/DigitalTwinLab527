package com.mobinets.digitaltwinlab.util.response;

import lombok.Data;

import java.util.Map;

/**
 * @author mahaotian
 * @date 2022/11/05
 */
@Data
public class Response{

    private Integer code;

    private String message;

    private Map<String,Object> data;

    /**
     * 成功
     */
    public static Response success() {
        Response result = new Response();
        result.setCode(ResponseCode.SUCCESS.getCode());
        result.setMessage(ResponseCode.SUCCESS.getMessage());
        return result;
    }

    /**
     * 成功，自定义成功信息
     */
    public static Response success(String message) {
        Response result = new Response();
        result.setCode(ResponseCode.SUCCESS.getCode());
        result.setMessage(message);
        return result;
    }
    /**
     * 成功，有返回数据
     */
    public static Response success(Map<String,Object> data) {
        Response result = new Response();
        result.setCode(ResponseCode.SUCCESS.getCode());
        result.setMessage(ResponseCode.SUCCESS.getMessage());
        result.setData(data);
        return result;
    }

    /**
     * 失败
     */
    public static Response failure() {
        Response result = new Response();
        result.setCode(ResponseCode.FAILURE.getCode());
        result.setMessage(ResponseCode.FAILURE.getMessage());
        return result;
    }

    /**
     * 失败，自定义失败信息
     */
    public static Response failure(String message) {
        Response result = new Response();
        result.setCode(ResponseCode.FAILURE.getCode());
        result.setMessage(message);
        return result;
    }

    /**
     * 失败，通过resultCode来传递
     */
    public static Response failure(ResponseCode resultCode) {
        Response result = new Response();
        result.setCode(resultCode.getCode());
        result.setMessage(resultCode.getMessage());
        return result;
    }
}