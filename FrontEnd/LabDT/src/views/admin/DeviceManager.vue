<template>
    <!-- 这个页面专做设备类型管理吧 -->
    <!-- 想法：导航栏的 “设备管理” 下面做三个子导航：设备类型管理、设备控制记录（按设备）和设备控制记录（按人员） -->
    <el-tabs v-model="activeName" class="tabs">
        <el-tab-pane label="设备类型管理" name="deviceTypeManage">
            <DeviceTypeComponents></DeviceTypeComponents>
        </el-tab-pane>
        <el-tab-pane label="设备日志" name="DeviceLogs">
            <DeviceLogComponents></DeviceLogComponents>
        </el-tab-pane>
        <!-- <el-tab-pane label="操作日志" name="OperationLogs">
            <OperationLogComponents></OperationLogComponents>
        </el-tab-pane> -->
    </el-tabs>
    
</template>
  
<script>
import DeviceLogComponents from '@/components/DeviceLogComponents.vue';
import DeviceTypeComponents from '@/components/DeviceTypeComponents.vue';
import OperationLogComponents  from '@/components/OperationLogComponents.vue'
export default {
    data() {
        return {
            activeName:"deviceTypeManage",
            routes: null,
            collapseIcon: "icon-shouqi",
            showNav: (this.$route.path != "/"),
            isCollapse: false,
            headerUrl: this.$cookies.get("headerUrl"),
            userName: null,
        };
    },
    methods: {},
    components: { DeviceTypeComponents, DeviceLogComponents,OperationLogComponents }
}
</script>

<style scoped>
.tabs{
    padding-left: 10px;
}
</style>