<template>
    <DeviceLoader></DeviceLoader>
    <scene-canvas ref="scenecanvas" :moduleFile=moduleFile ></scene-canvas>
    </template>
<script>
import SceneCanvas from '@/components/SceneCanvas.vue'
import http from '@/utils/request/http.js'
import { switchCase } from '@babel/types';
import { ElMessage, ElMessageBox } from 'element-plus'
import DeviceLoader from "@/utils/DeviceLoader.vue"
export default {
    components: {
        SceneCanvas,
        DeviceLoader,
    },
    data() {
        return {
            moduleFile: "/static/Lab.glb",
        }
    },
    methods: {
    }
}
</script>

<style scoped>
.dialog {

    opacity: 0.9;
}
</style>