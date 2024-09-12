import http from '@/utils/request/http.js'
const AirCondition = {
    namespaced: true,
    //函数来声明模块状态,解决模块重用问题
    state: () => ({
        device_id: null, //设备id
        mode: null, //模式 1~4 对应制冷，除湿，送风，制热
        power: null, //1:开 0：关
        basic_fan: null, //风速 0：自动 1-3表示三级风速
        temp: null,//温度 （16-30度）
        turbo: false,//强劲模式
        light: false,//灯光
        xfan: false,//干燥模式，仅在制冷和除湿模式下可用
        swing_v: false,//上下扫风
        swing_h: false,//静音模式
    }),
    mutations: {
        set_power_switch(state, power) {
            state.power = power
        },
        set_air_conditioner(state, changedState) {
            Object.keys(changedState).forEach(function (key) {
                state[key] = changedState[key]
            });
        },
        init(state, initState) {
            Object.keys(state).forEach(function (key) {
                state[key] = initState[key]
            });
        }
    },
    //带有异步请求的必须要使用action套一层
    actions: {
        //设置开关
        set_power_switch(context, power) {
            context.commit('set_power_switch', power)
        },
        //设置空调状态
        set_air_conditioner(context, changedState) {
            //先改前端状态还是先发请求？ 待沟通
            Object.keys(changedState).forEach(function (key) {
                //对象合并 把device_id加上去
                var data = Object.assign({ device_id: context.state.device_id }, changedState)
                context.commit('set_air_conditioner', changedState)

            });
        }
    }
};

export default AirCondition;