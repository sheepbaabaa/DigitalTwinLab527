package com.mobinets.digitaltwinlab.entity;

import com.alibaba.fastjson.annotation.JSONField;

import java.util.Date;

public class PermissionApplication {
    private int id;
    private int applicantId;
    private int permissionApplyFor;
    @JSONField(format="yyyy-MM-dd HH:mm:ss")
    private Date date;

    private int ifProcessed;
    @JSONField(format="yyyy-MM-dd HH:mm:ss")
    private Date processedDate;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getApplicantId() {
        return applicantId;
    }

    public void setApplicantId(int applicantId) {
        this.applicantId = applicantId;
    }

    public int getPermissionApplyFor() {
        return permissionApplyFor;
    }

    public void setPermissionApplyFor(int permissionApplyFor) {
        this.permissionApplyFor = permissionApplyFor;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }

    public int getIfProcessed() {
        return ifProcessed;
    }

    public void setIfProcessed(int ifProcessed) {
        this.ifProcessed = ifProcessed;
    }

    public Date getProcessedDate() {
        return processedDate;
    }

    public void setProcessedDate(Date processedDate) {
        this.processedDate = processedDate;
    }

    @Override
    public String toString() {
        return "permissionApplication{" +
                "id=" + id +
                ", applicantId=" + applicantId +
                ", permissionApplyFor=" + permissionApplyFor +
                ", date=" + date +
                ", ifProcessed=" + ifProcessed +
                ", processedDate=" + processedDate +
                '}';
    }
}
