package com.mobinets.digitaltwinlab.dao;

import com.mobinets.digitaltwinlab.entity.User;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface UserMapper {

    User selectById(int id);

    User selectByCampusNum(long campusNum);

    User selectByUsername(String username);

    User selectByEmail(String email);

    int insertUser(User user);

    int updateStatus(int id, int status);

    int updateHeader(int id, String headerUrl);

    int updatePassword(int id, String password,String salt);

    int updateEmail(int id,String email);

    int updateType(int id,int type);

    int deleteUser(int id);

    List<User> selectAll();
}
