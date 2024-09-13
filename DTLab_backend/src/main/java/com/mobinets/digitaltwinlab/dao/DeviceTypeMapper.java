package com.mobinets.digitaltwinlab.dao;

import com.mobinets.digitaltwinlab.entity.DeviceType;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Mapper
public interface DeviceTypeMapper {
    List<DeviceType> selectAll();
}
