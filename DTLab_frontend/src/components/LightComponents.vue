<template>
    <div class="dialog" style="pointer-events: none;">
        <el-dialog v-model="LightVisible" :modal="false" :close-on-click-modal="false" :show-close="false" title="灯光控制面板" width="15%" @open="dialogOpened()" >
            <el-form-item label="灯光" :label-width="formLabelWidth">
                {{LightName}}
            </el-form-item>

            <el-form-item label="电源" :label-width="formLabelWidth">
                <el-switch class="pointerAuto" v-model="LightData.switch" @change="changePower()" active-text="开" inactive-text="关" />
            </el-form-item>
            <template #footer>
                <span class="dialog-footer pointerAuto" >
                    <el-button @click="handleClose()">返回</el-button>
                </span>
            </template>
        </el-dialog>
    </div>
</template>
  

    
<script>
import SceneCanvas from '@/components/SceneCanvas.vue'
import { switchCase } from '@babel/types';
import { ElMessage, ElMessageBox } from 'element-plus'
import { Store } from "vuex"
import * as THREE from 'three';
export default {
    name: 'LightComponents',
    props: ['LightVisible','LightName'],
    data() {
        return {
            formLabelWidth: '80px',
            LightData: {
                device_id: null,
                switch: true, //1:开 0：关
            },
        }
    },
    mounted() {
        //添加事件监听器
        this.$websocket.getwebsocket().addEventListener('light_change', this.onlightChangeMessage, true);
        setTimeout(() => {
            var LightList = this.$store.getters.allLight;
            LightList.forEach(item => {
                console.log(this.$store.state[item.device_name])
                this.setLight(item.device_name, item.switch)
            })
        }, 100);
    },

    methods: {
        setLight(LightName, power) {
            var light =this.$parent.getScene().getObjectByName(LightName);
            light.visible = true;
            if (power == "1") {
                light.children.forEach((item) => {
                    item.material = new THREE.MeshBasicMaterial({ color: 0xffffff, wireframe: true });
                })
            } else {
                light.children.forEach((item) => {
                    item.material = new THREE.MeshBasicMaterial({ color: 0x000000, wireframe: true });
                })
            }
        },
        updateLightState(){
            var lightData = {
                "action": "get_power_light",
                "params": {
                    "device_id": this.LightData.device_id,
                },
                "echo": "123"
            }
            this.$websocket.webSocketSend(lightData);
        },
        onlightChangeMessage(e){
            var updateInfo=e.detail.data;
            updateInfo.forEach(item => {
                var name = this.$store.state.deviceMap.get(item.device_id)
                this.$store.dispatch(name + "/set_power_switch", item.value)
                this.setLight(name, item.value);
                if(this.LightData.device_id==item.device_id){
                    this.LightData.switch=(item.value==1)
                }
            });
        },
        dialogOpened(){
            this.LightData.device_id = this.$store.state[this.LightName].device_id;
            this.LightData.switch = (this.$store.state[this.LightName].switch==1);
        },
        changePower() {
            var data={
                "action":"set_power_switch",
                "params":{
                    "device_id": this.LightData.device_id,
                    "switch": this.LightData.switch?1:0
                }
            }
            //change model
            this.setLight(this.LightName,this.LightData.switch);
            this.$websocket.webSocketSend(data)
        },
        handleClose() {
            this.$parent.closeLight();
        }
    }
}
</script>
  
<style scoped>
.dialog {
    opacity: 0.9;
}

.dialog-footer button[data-v-472cff63]:first-child {
    margin-right: 10px;
}   
.pointerAuto{
    pointer-events: auto
}
</style>