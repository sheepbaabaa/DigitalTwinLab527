const Light = {
    namespaced: true,
    //函数来声明模块状态,解决模块重用问题
    state: () => ({
        device_id: null, //设备id
        device_name: null,
        switch: null, //1:开 0：关
    }),
    mutations: {
        set_power_switch(state, power) {
            state.switch = power
        },
        init(state, initState) {
            Object.keys(state).forEach(function (key) {
                state[key] = initState[key]
            });
        }
    },
    actions: {
        init(context, initState) {
            context.commit("init", initState);
            context.commit("addLight", context.state.device_name, { root: true });
        },
        //设置开关
        set_power_switch(context, power) {
            context.commit('set_power_switch', power)
        },

    }
};

export default Light;