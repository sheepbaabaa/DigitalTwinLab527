<template>
    <div class="dialog" style="pointer-events: none;">
        <el-dialog v-model="AirConditionVisible"  :modal="false" :close-on-click-modal="false" :show-close="false" title="控制面板" width="25%"  @open="dialogOpened()">
            <el-form-item label="空调" :label-width="formLabelWidth">
                {{AirConditionName}}
            </el-form-item>
            <el-form-item class="pointerAuto" label="开关" :label-width="formLabelWidth">
                <el-select v-model="airConditionsData.power" placeholder="">
                    <el-option label="打开" value="1" @click="changePower()" />
                    <el-option label="关闭" value="0" @click="changePower()" />
                </el-select>
            </el-form-item>

            <el-form-item class="pointerAuto"  label="模式" :label-width="formLabelWidth">
                <el-select v-model="airConditionsData.mode" placeholder="">
                    <el-option label="制冷" value="1" />
                    <el-option label="除湿" value="2" />
                    <el-option label="送风" value="3" />
                    <el-option label="制热" value="4" />
                </el-select>
            </el-form-item>

            <el-form-item class="pointerAuto"  label="风速" :label-width="formLabelWidth">
                <el-select v-model="airConditionsData.basic_fan" placeholder="">
                    <el-option label="自动风速" value="0" />
                    <el-option label="一级风速" value="1" />
                    <el-option label="二级风速" value="2" />
                    <el-option label="三级风速" value="3" />
                </el-select>
            </el-form-item>

            <!-- 温度（限定为整数输入） -->
            <el-form-item class="pointerAuto"  label="温度" :label-width="formLabelWidth">
                <el-input-number v-model="airConditionsData.temp" :min="16" :max="30" @change="handleChange" />
            </el-form-item>
            <el-form-item class="pointerAuto"  label="强劲模式" :label-width="formLabelWidth">
                <el-switch v-model="airConditionsData.turbo" />
            </el-form-item>
            <el-form-item class="pointerAuto"  label="灯光" :label-width="formLabelWidth">
                <el-switch v-model="airConditionsData.light" />
            </el-form-item>
            <!-- 干燥模式要做判断 -->
            <el-form-item class="pointerAuto"  label="干燥模式" :label-width="formLabelWidth">
                <el-switch v-model="airConditionsData.xfan" :disabled="(airConditionsData.mode == 1 || airConditionsData.mode == 2) ? false : true" />
            </el-form-item>

            <el-form-item class="pointerAuto"  label="上下扫风" :label-width="formLabelWidth">
                <el-switch v-model="airConditionsData.swing_v" />
            </el-form-item>
            <el-form-item class="pointerAuto"  label="静音模式" :label-width="formLabelWidth">
                <el-switch v-model="airConditionsData.swing_h" />
            </el-form-item>
            <template #footer>
                <span class="dialog-footer pointerAuto" >
                    <el-button @click="handleClose()">取消</el-button>
                    <el-button type="primary" @click="changeState()">
                        确认
                    </el-button>
                </span>
            </template>
        </el-dialog>
    </div>
</template>
  
<script>
import SceneCanvas from '@/components/SceneCanvas.vue'
import { switchCase } from '@babel/types';
import { ElMessage, ElMessageBox } from 'element-plus'
import AirCondition from "@/store/modules/AirCondition.js"
import { Store } from "vuex"
export default {
    name: 'AirConditionComponents',
    props: ['AirConditionVisible','AirConditionName'],
    data() {
        return {
            // dialogFormVisible: this.dialogFormVisible,
            formLabelWidth: '80px',
            airConditionsData: {
                name:null,
                device_id: null,
                mode: null, //模式 1~4 对应制冷，除湿，送风，制热
                power: null, //1:开 0：关
                basic_fan: null, //风速 0：自动 1-3表示三级风速
                temp: null,//温度 （16-30度）
                turbo: false,//强劲模式
                light: false,//灯光
                xfan: false,//干燥模式，仅在制冷和除湿模式下可用
                // disabled_xfan: (this.mode == 1 || this.mode == 2) ? true : false,
                swing_v: false,//上下扫风
                swing_h: false,//静音模式
            },
            // disabled: (this.mode == 1 || this.mode == 2) ? true : false,
            disabled: ''
        }
    },
    mounted() {
        // var airConditionsData =
        // {
        //     "device_id": 1, //设备id
        //     "name": "aircondition1",
        //     "mode": 1, //模式 1~4 对应制冷，除湿，送风，制热
        //     "power": 1, //1:开 0：关
        //     "basic_fan": 0, //风速 0：自动 1-3表示三级风速
        //     "temp": 18,//温度 （16-30度）
        //     "turbo": false,//强劲模式
        //     "light": false,//灯光
        //     "xfan": true,//干燥模式，仅在制冷和除湿模式下可用
        //     "swing_v": false,//上下扫风
        //     "swing_h": true,//静音模式
        // }
        // this.$store.registerModule(airConditionsData['name'], AirCondition)
        // this.$store.commit(airConditionsData['name'] + "/init", airConditionsData)
        // console.log(this.$store.state['aircondition1'])
        this.$websocket.getwebsocket().addEventListener('AirCondition_change', this.onAirConditionChangeMessage, true);
    },
    methods: {
        onAirConditionChangeMessage(e){
            var updateInfo=e.detail.data;
            var name=this.$store.state.deviceMap.get(updateInfo.device_id)
            this.$store.dispatch(name + '/set_air_conditioner', updateInfo)
            this.airConditionsData=updateInfo;
        },
        dialogOpened() {
            var airConditionsData = this.$store.state[this.AirConditionName];
            Object.keys(this.airConditionsData).forEach((key)=>{
                this.airConditionsData[key] = airConditionsData[key]
            });
        },
        // changePower() {
        //     console.log(this.$websocket)
        //     // this.$store.dispatch('aircondition1/set_power_switch', this.$store.state['aircondition1'].power == 1 ? 0 : 1);
        //     this.$store.dispatch('aircondition1/set_power_switch', this.airConditionsData.power)
        //     console.log(this.$store.state['aircondition1'])
        //     this.$websocket.webSocketSend(
        //         {
        //             "action": "set_power_switch",
        //             "params": {
        //                 "device_id": this.$store.state['aircondition1']['device_id'],
        //                 "switch": this.$store.state['aircondition1'].power
        //             },
        //             "echo": "114.514"
        //         })
        // },
        changeState() {
            //this.$store.dispatch(this.AirConditionName+ '/set_air_conditioner',this.airConditionsData);
            this.$websocket.webSocketSend({
                "action": "set_air_conditioner",
                "params": this.airConditionsData,
                "echo": "1919.810"
            })
            this.handleClose();
        },
        handleClose() {
            this.$parent.closeAirCondition();
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