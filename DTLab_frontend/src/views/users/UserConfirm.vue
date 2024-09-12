<template>
    <div class="UserConfirm" >
    <el-row>
      <el-col :span="8" ></el-col>
      <el-col :span="8" ><h3>激活成功！请重新登陆...</h3> </el-col>
      <el-col :span="8"></el-col>
    </el-row>
    <el-row>
      <el-col :span="8" ></el-col>
      <el-col :span="8" >
        <el-button @click="confirm">回到主页</el-button>
      </el-col>
      <el-col :span="8"></el-col>
    </el-row>
    </div>
</template>

<script>
    export default {
      name: "UserConfirm",
      data(){
        return {
        }
      },
      methods:{
        confirm(){
            this.$router.push({ name: 'UserLog'})
        }
      }
    }
</script>

<style>
    #building{
    background:url("../../assets/background.jpg");
    width:100%;
    height:100%;
    position:fixed;
    background-size:100% 100%;
  }
  
    .text {
      font-size: 14px;
    }


  </style>