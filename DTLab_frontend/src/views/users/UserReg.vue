<template>
  <div id='building'>
    <div class="UserReg" style="text-align: -webkit-center">
      <el-card class="box-card">
        <template #header>
          <div class="card-header">
            <span>用户注册</span>
          </div>
        </template>

        <el-form :model="reginfo" label-width="80px" :rules="rules" ref="reginfoRef" status-icon>
          <el-form-item label="学号" prop="campusNum">
            <el-input v-model="reginfo.campusNum" placeholder="请输入学号"></el-input>
          </el-form-item>
          <el-form-item label="用户名" prop="username">
            <el-input v-model="reginfo.username" placeholder="请输入用户名"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="pass">
            <el-input v-model="reginfo.password" placeholder="请输入密码" type="password" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="确认密码" prop="checkPass">
            <el-input v-model="reginfo.checkPass" type="password" autocomplete="off" />
          </el-form-item>
          <el-form-item label="邮箱" prop="email">
            <el-input v-model="reginfo.email" placeholder="请输入邮箱"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" style="width: 30%" @click="submitForm($refs.reginfoRef)">注册</el-button>
            <el-button style="width: 30%" @click="resetForm($refs.reginfoRef)">重置</el-button>
          </el-form-item>
        </el-form>

      </el-card>

    </div>
  </div>
</template>

<script>
import { ElMessageBox } from 'element-plus';
import { ElMessage } from 'element-plus';
import axios from 'axios';
import Long from 'long';
import http from '@/utils/request/http.js'
export default {
  name: "UserReg",
  data() {

    // var checkemail = (rule, value, callback) => {
    //   const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/
    //   if (/^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((.[a-zA-Z0-9_-]{2,3}){1,2})$/.test(value)) {
    //     callback()
    //   } else {
    //     callback(new Error('请输入正确的邮箱格式'))
    //   }
    // }

    return {
      reginfo: {
        campusNum: '',
        username: '',
        password: '',
        email: '',
        checkPass: '',
      },
      rules: {
        password: [{ validator: this.validatePass, trigger: 'blur' }],
        checkPass: [{ validator: this.validatePass2, trigger: 'blur' }],
      },
      // reginfoRef: '',
      // rules:{
      // 	email: [{required: true, message: '邮箱不能为空', trigger: 'blur'},{validator: checkemail, trigger: 'blur'}]

      // },
    }
  },

  methods: {
    register() {
      var data = {
        username: this.reginfo.username,
        password: this.reginfo.password,
        campusNum: this.reginfo.campusNum,
        email: this.reginfo.email
      }
      //初始化人物模型
      http.post("register", data).then(res => {
        console.log(res)
        if(res.code==200)
        {
          ElMessage({
            showClose: true,
            duration: 0,
            message: '注册成功，请前往邮箱进行账号激活！',
            type: 'success',
          })
        }
        else{
          ElMessage({
            showClose: true,
            duration: 0,
            message: res.message,
            type: 'error',
          })
        }
        
      }).catch(err => {
        console.log(err)
      })
    },

    validatePass(rule, value, callback) {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.reginfo.checkPass !== '') {
          console.log(this.$refs)
          if (!this.$refs.reginfoRef) return
          this.$refs.reginfoRef.validateField('checkPass', () => null)
        }
        callback()
      }
    },
    validatePass2(rule, value, callback) {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.reginfo.password) {
        callback(new Error("两次输入的密码不同！"))
      } else {
        callback()
      }
    },
    submitForm(formEl) {
      if (!formEl) return
      formEl.validate((valid) => {
        if (valid) {
          this.msgbox()
          // console.log('提交成功！')
        } else {
          console.log('提交错误！')
          return false
        }
      })
    },
    resetForm(formEl) {
      console.log('before reset')
      console.log(formEl)
      if (!formEl) return
      console.log('reset!')
      formEl.resetFields()
    },

  },
}
</script>

<style>
#building {
  background: url("../../assets/background2.jpg");
  width: 100%;
  height: 100%;
  position: fixed;
  background-size: 100% 100%;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.box-card {
  width: 360px;
  padding: 10px;
  margin-top: 10%;
  opacity: 0.9;
}
</style>
  