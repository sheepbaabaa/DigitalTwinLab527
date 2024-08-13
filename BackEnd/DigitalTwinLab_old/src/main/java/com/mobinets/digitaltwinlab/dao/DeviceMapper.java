package com.mobinets.digitaltwinlab.dao;

import com.mobinets.digitaltwinlab.entity.Device;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.Date;
import java.util.List;

@Mapper
@Repository
public interface DeviceMapper {


    List<Device> selectAll();

    int insertDevice(Device device);

    void updateChangeTime(int id, Date changeTime);

}
