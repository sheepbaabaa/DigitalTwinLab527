package com.mobinets.digitaltwinlab.dao;

import com.mobinets.digitaltwinlab.entity.Model;
import com.mobinets.digitaltwinlab.entity.User;
import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

import java.util.List;

@Mapper
public interface ModelMapper {

    int insertModel(Model model);
    Model selectLatestModel();
    List<Model> selectAll();
}
