package org.mobinets.dtlab.user;

import org.mobinets.dtlab.UserService;
import org.apache.dubbo.config.annotation.DubboService;

import java.util.Objects;

@DubboService
public class UserServiceImpl implements UserService {

    @Override
    public Boolean login(String username, String password) {
        return Objects.equals(username, "admin") && Objects.equals(password, "admin");
    }


}
