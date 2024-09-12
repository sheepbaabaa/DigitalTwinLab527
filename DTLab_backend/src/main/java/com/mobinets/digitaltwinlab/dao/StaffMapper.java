package com.mobinets.digitaltwinlab.dao;

import com.mobinets.digitaltwinlab.entity.Staff;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface StaffMapper {

    Staff selectByCampusNum(String campusNum);

    Staff selectByName(String name);

    Staff selectByEnglishName(String name_en);

    List<Staff> selectAllStaff();

    int insertStaff(Staff staff);

    int updateType(String campusNum,int type);
    int updatePersonState(int member_id,String state);

}
