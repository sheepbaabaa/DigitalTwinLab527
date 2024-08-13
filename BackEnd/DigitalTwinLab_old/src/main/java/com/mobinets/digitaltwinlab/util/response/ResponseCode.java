package com.mobinets.digitaltwinlab.util.response;
import lombok.AllArgsConstructor;
import lombok.Getter;

/**
 * @author mahaotian
 * @date 2022/11/05
 */
@Getter
@AllArgsConstructor
public enum ResponseCode {

    //成功提示码
    SUCCESS(200, "success"),

    //错误提示码
    FAILURE(500, "failed"),

    //越权访问
    PERMISSION_ERROR(403,"Illegal access deny"),

    //未登录
    NOT_LOGGED_IN(405,"Haven't logged in yet");

    private final Integer code;
    private final String message;
}