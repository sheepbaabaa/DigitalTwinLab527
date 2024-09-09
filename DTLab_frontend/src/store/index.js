import { createStore } from 'vuex'

const store = createStore({
    modules: {
    },
    state: {
        personList: [],
        lightList: [],
        monitorList: [],
        deviceMap: null,
        userInfo: {
            id: null,
            username: null,
            campusNum: null,
            email: null,
            type: 0,
            ticket: null,
        }
    },
    getters: {
        allPerson: (state) => () => {
            var result = []
            state.personList.forEach(item => {
                result.push(state[item])
            });
            return result;
        },
        allLight(state) {
            var result = []
            state.lightList.forEach(item => {
                result.push(state[item])
            });
            return result;
        },
        allMonitor(state) {
            var result = []
            state.monitorList.forEach(item => {
                result.push(state[item])
            });
            return result;
        }
    },
    mutations: {
        initDeviceMap(state, info) {
            state.deviceMap = new Map();
            info.forEach(item => {
                state.deviceMap.set(item.deviceID, item.deviceName);
            })
        },
        addPerson(state, member_id) {
            state.personList.push(member_id);
        },
        addLight(state, device_name) {
            state.lightList.push(device_name);
        },
        addMonitor(state, device_name) {
            state.monitorList.push(device_name);
        },
        initUserInfo(state, userInfo, ticket) {
            state.userInfo.id = userInfo.id
            state.userInfo.username = userInfo.username
            state.userInfo.campusNum = userInfo.campusNum
            state.userInfo.email = userInfo.email
            state.userInfo.type = userInfo.type
            state.userInfo.ticket = ticket
        },
    }
});

export default store;