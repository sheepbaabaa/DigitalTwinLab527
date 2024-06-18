<template>
    <el-container>
      <el-aside style="width:auto">
        <Menu></Menu>
      </el-aside>
      <el-main style="z-index:1;padding:0px">
        <router-view></router-view>
      </el-main>
    </el-container>
</template>
<script>
import Menu from './components/Menu.vue'
import http from './utils/request/http.js'

export default {
  components: {
    Menu,
    
  },
  data() {
    return {
      
    }
  },
  methods:{
  },
  async created(){
    //首先获得用户信息
    var res= await http.get('user/userInfo')
    this.$store.commit("initUserInfo", res.data.userInfo, res.data.ticket);

    //判断是否存在cookie
    if (this.$cookies.isKey('userId')){
      //获得userId
      var userId = this.$cookies.get("userId")
      //设置websocket链接地址
      if (this.$host == "dtlab.qylh.xyz:9003") {
        this.$websocket.setUrl("wss://dtlab.qylh.xyz/dtlab/ws/webClient/" + userId)
      }
      else {
        this.$websocket.setUrl("ws://" + this.$host + "/dtlab/ws/webClient/" + userId)
      }
      this.$websocket.start()
    }
    //不存在的话需要以游客的身份进行websocket链接 （待完善）
    else{
        //pass
    }
  },
  mounted() {
    
  },
  beforeDestroy() {
    //应用销毁前关闭连接
    this.$websocket.webSocketClose()
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}

a {
  text-decoration: none;
}

body {
  margin: 0;
  padding: 0;
  border: 0;
}


.flex-grow {
  flex-grow: 1;
}

</style>