//显示器
const Monitor = {
    namespaced: true,
    //函数来声明模块状态,解决模块重用问题
    state: () => ({
        device_id: null, //设备id
        device_name: null,
        switch: null, //1:开 0：关
    }),
    mutations: {
        set_power_switch(state, power) {
            state.power = power
        },
        init(state, initState) {
            Object.keys(state).forEach(function (key) {
                state[key] = initState[key]
            });
        }
    },
    //带有异步请求的必须要使用action套一层
    actions: {
        init(context, initState) {
            context.commit("init", initState);
            context.commit("addMonitor", context.state.device_name, { root: true });
        },
        //设置开关
        set_power_switch(context, power) {
            context.commit('set_power_switch', power)
        },
    }
};

export default Monitor;