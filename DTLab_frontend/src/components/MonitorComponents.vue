<template>

</template>
  
<script>
import * as THREE from 'three';
export default {
    name: 'MonitorComponents',
    props: ['MonitorVisible','MonitorName'],
    data() {
        return {
            formLabelWidth: '80px',
            MonitorData: {
                device_id: null,
                power: null, //1:开 0：关
            },
        }
    },
    mounted() {
        setTimeout(()=>{ 
            var monitorList = this.$store.state['monitorList']
            monitorList.forEach(item => {
                this.setMonitor(item, this.$store.state[item].switch)
            });
         }, 5000);
        this.$websocket.getwebsocket().addEventListener('response_monitor_state', this.onmonitorChangeMessage, true);
        //初始化赋值该屏幕MonitorData
    },
    methods: {
        getScene(){
            return this.$parent.getScene();
        },
        onmonitorChangeMessage(e){
            var updateInfo = e.detail.data;
            updateInfo.forEach(item => {
                var name = this.$store.state.deviceMap.get(item.device_id)
                this.$store.dispatch(name + "/set_power_switch", item.value)
                this.setMonitor(name, item.value);
            });
        },
        setMonitor(MonitorName, power) {
            var screen = this.getScene().getObjectByName("ComputerScreen" + MonitorName.substr(7, 3) + "_2");//scren mesh
            try {
                if (power == "1")
                    screen.material = new THREE.MeshBasicMaterial({ color: 0xffffff });
                else if (power == "0")
                    screen.material = new THREE.MeshBasicMaterial({ color: 0x000000 });
            } catch (error) {
                //console.log(error)
            }
        },
        changePower() {
            this.setMonitor(this.MonitorData.power);
        }
    }
}
</script>