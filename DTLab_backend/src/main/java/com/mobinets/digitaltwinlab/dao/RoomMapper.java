package com.mobinets.digitaltwinlab.dao;

import com.mobinets.digitaltwinlab.entity.Room;
import org.apache.ibatis.annotations.Mapper;

import java.util.Date;

@Mapper
public interface RoomMapper {

    Room selectById(int id);

    int insertRoom(Room room);

    int updateStatus(int id, int status);

    int updateChangeTime(int id, Date changeTime);

}
