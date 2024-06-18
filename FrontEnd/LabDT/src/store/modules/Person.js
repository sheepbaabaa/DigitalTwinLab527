const Person = {
    namespaced: true,
    //函数来声明模块状态,解决模块重用问题
    state: () => ({
        member_id: null, //id
        seat_id:null,
        name: null, //中文姓名
        name_en: null,
        person_state: null,//三种状态 In_Lab Out_Lab In_Meeting_Room
        position: [0, 0, 0],
        rotation: [0, 0, 0],
        visible: false,
    }),
    mutations: {
        change_people_state(state, person_action) {
            if (person_action == "In Lab") {
                state.person_state = "In_Lab";
                state.visible = true;
            }
            else if (person_action == "Out Lab") {
                state.person_state = "Out_Lab";
                state.visible = false;
            }
            else if (person_action == "In Meeting Room") {
                state.person_state = "In_Meeting_Room";
                state.visible = false;
            }
            else if (person_action == "Out Meeting Room") {
                state.person_state = "In_Lab";
                state.visible = true;
            }

        },
        init(state, initState) {
            this.commit("addPerson", state.name_en, { root: true });
            state.member_id = initState.memberId
            state.seat_id = initState.seatId
            state.name = initState.nameZh
            state.person_state = initState.personState
            state.name_en = initState.nameEn
            if (state.person_state == "In_Lab") {
                state.visible = true;
            }
            else {
                state.visible = false;
            }
        },

    },
    //带有异步请求的必须要使用action套一层
    actions: {
    }
};

export default Person;