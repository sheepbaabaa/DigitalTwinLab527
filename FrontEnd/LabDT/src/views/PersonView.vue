<template>
    <el-tabs v-model="activeName" class="tabs">
        <el-tab-pane label="在读人员" name="StaffComponents">
            <StaffComponents></StaffComponents>
        </el-tab-pane>
        <el-tab-pane label="进出日志" name="AccessLogComponents">
            <AccessLogComponents></AccessLogComponents>
        </el-tab-pane>
    </el-tabs>
</template>

<!-- <template>
    <StaffComponents></StaffComponents>
</template> -->

<script setup>
import StaffComponents from '@/components/StaffComponents.vue';
import AccessLogComponents from '@/components/AccessLogComponents.vue';
import { ref } from 'vue'

const activeName = ref("StaffComponents");



</script>

<style scoped>
.tabs{
    padding-left: 10px;
}
</style>