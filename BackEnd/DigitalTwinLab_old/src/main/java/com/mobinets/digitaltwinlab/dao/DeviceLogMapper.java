package com.mobinets.digitaltwinlab.dao;


import com.mobinets.digitaltwinlab.entity.Device;
import com.mobinets.digitaltwinlab.entity.DeviceLog;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.Date;
import java.util.List;

@Mapper
@Repository
public interface DeviceLogMapper {
    List<DeviceLog> selectAll();
    List<DeviceLog> selectById(int deviceId);
    int clearLog(String timeNode);
    int insertDeviceLog(DeviceLog deviceLog);

    List<DeviceLog> selectByUserId(int userId);
}
