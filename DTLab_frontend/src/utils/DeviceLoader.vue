<template>
</template>
<script>
import Person from "@/store/modules/Person.js"
import http from '@/utils/request/http.js'
import Light from "@/store/modules/Light"
import AirCondition from "@/store/modules/AirCondition"
import Monitor from '@/store/modules/Monitor'
export default {
    name: 'DeviceLoader',
    data() {
        
    },
    mounted() {
        //person
        http.get("person/getAllStaff").then(res => {
            res.data.staffs.forEach(staff => {
                this.$store.registerModule(staff.nameEn, Person);
                this.$store.commit(staff.nameEn + "/init", staff);
            });
        }).catch(err => {
            console.log(err)
        })
        http.get("deviceManager/getAllDevice").then(res=>{
            this.$store.commit("initDeviceMap",res.data.devices)
            res.data.devices.forEach((device)=>{
            if(device.type==1){
                this.initAircodition(device);
            }
            //Light类型设备
            else if(device.type==2){
                this.initLight(device);
            } 

            else if(device.type==3){
                this.initMonitor(device);
            }
        })
        }).catch((err)=>{
            console.log(err);
        }).finally(()=>{
            console.log(this.$store.state)
        })
    },
    methods: {
        //         var name = "Monitor"+monitor.device_name; //device_name是模型序号
        //         this.$store.registerModule(name, monitor);
        //         this.$store.dispatch(name + "/init", monitor);
        initLight(device){
            http.post("deviceManager/getDeviceInfo", { "id": device.deviceID }).then(res=>{
                this.$store.registerModule(device.deviceName, Light);
                this.$store.dispatch(device.deviceName + "/init", res.data.info);
            })
        },
        // 初始化空调
        initAircodition(device){
            http.post("deviceManager/getDeviceInfo", { "id": device.deviceID }).then(res => {
                this.$store.registerModule(device.deviceName, AirCondition)
                this.$store.commit(device.deviceName + "/init", res.data.info)
            })
        },
        initMonitor(device){
            http.post("deviceManager/getDeviceInfo", { "id": device.deviceID }).then(res => {
                this.$store.registerModule(device.deviceName, Monitor)
                this.$store.dispatch(device.deviceName + "/init", res.data.info)
            })
        }
    }
}
</script>
