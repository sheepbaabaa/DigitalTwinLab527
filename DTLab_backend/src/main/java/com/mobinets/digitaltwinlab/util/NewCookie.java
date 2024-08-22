package com.mobinets.digitaltwinlab.util;


import jakarta.servlet.http.Cookie;

public class NewCookie extends Cookie {
    private String sameSite;
    public final static String LAX = "Lax";
    public final static String NONE = "None";
    public final static String STRICT = "Strict";
    public final static String SET_COOKIE = "Set-Cookie";

    public NewCookie(String name, String value) {
        super(name, value);
    }

    public String getSameSite() {
        return sameSite;
    }

    public NewCookie setSameSite(String sameSite) {
        this.sameSite = sameSite;
        if (NONE.equals(sameSite)) {
            setSecure(true);
        }
        return this;
    }

    @Override
    public String toString() {
        // 参照Controller中的doSetCookie代码
        StringBuilder sb = new StringBuilder(getName()).append("=").append(getValue());
        sb.append(";Path=").append(getPath()==null?"/":getPath());
        if (getDomain() != null) {
            sb.append(";Domain=").append(getDomain());
        }
        if (isHttpOnly()) {
            sb.append(";HttpOnly");
        }
        sb.append(";Max-Age=").append(getMaxAge());
        // 默认Lax
        sb.append(";SameSite=").append(getSameSite()==null?"Lax":getSameSite());
        if (getSecure()) {
            sb.append(";Secure");
        }
        if (getComment() != null) {
            sb.append(";Comment=").append(getComment());
        }

        return sb.toString();
    }
}