package com.mobinets.digitaltwinlab.dao;

import com.mobinets.digitaltwinlab.entity.PermissionApplication;
import org.apache.ibatis.annotations.Mapper;

import java.util.Date;
import java.util.List;

@Mapper
public interface PermissionApplicationMapper {
    int insertApplication(PermissionApplication permissionApplication);
    List<PermissionApplication> selectAllApplication();

    int updateProcessedResult(int id, int result, Date date);

    PermissionApplication selectById(int id);
}
