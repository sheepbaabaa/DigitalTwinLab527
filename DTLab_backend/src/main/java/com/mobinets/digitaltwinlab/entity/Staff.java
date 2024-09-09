package com.mobinets.digitaltwinlab.entity;

public class Staff {

    private int memberId;
    private String nameZh;
    private long campusNum;
    private String nameEn;
    private int type;
    private String personState;

    public long getCampusNum() {
        return campusNum;
    }

    public void setCampusNum(long campusNum) {
        this.campusNum = campusNum;
    }

    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }

    public int getMemberId() {
        return memberId;
    }

    public void setMemberId(int memberId) {
        this.memberId = memberId;
    }

    public String getNameZh() {
        return nameZh;
    }

    public void setNameZh(String nameZh) {
        this.nameZh = nameZh;
    }

    public String getNameEn() {
        return nameEn;
    }

    public void setNameEn(String nameEn) {
        this.nameEn = nameEn;
    }

    public String getPersonState() {
        return personState;
    }

    public void setPersonState(String personState) {
        this.personState = personState;
    }

    @Override
    public String toString() {
        return "Staff{" +
                "memberId=" + memberId +
                ", nameZh='" + nameZh + '\'' +
                ", campusNum=" + campusNum +
                ", nameEn='" + nameEn + '\'' +
                ", type=" + type +
                ", personState=" + personState +
                '}';
    }
}
