package com.mobinets.digitaltwinlab.entity;

import java.util.Date;

public class Room {

    private int id;
    private int status;
    private Date changeTime;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public Date getChangeTime() {
        return changeTime;
    }

    public void setChangeTime(Date changeTime) {
        this.changeTime = changeTime;
    }

    @Override
    public String toString() {
        return "Room{" +
                "id=" + id +
                ", status=" + status +
                ", changeTime=" + changeTime +
                '}';
    }
}
