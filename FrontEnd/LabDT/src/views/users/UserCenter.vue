<template>
	 <el-tabs v-model="activeName" class="tabs">
        <el-tab-pane label="账户编辑" name="userInfo">
			<el-card shadow="hover">
					<el-form label-width="90px">
						<el-form-item label="用户名：">{{ userData.username }}</el-form-item>
						<el-form-item label="用户类型：">{{ userTypeName.get(userData.type) }}</el-form-item>
						<el-form-item label="邮箱">
							<el-input v-model="userData.email"></el-input>
						</el-form-item>
						<el-form-item label="新密码：">
							<el-input type="password" v-model="userData.password"></el-input>
						</el-form-item>
						<el-form-item label="确认密码：">
							<el-input type="password" v-model="userData.confirmPassword"></el-input>
						</el-form-item>
						<el-form-item>
							<el-button type="primary" @click="onSubmit">保存</el-button>
							<el-button type="primary" @click="applyForPermission">申请普通权限</el-button>
						</el-form-item>
					</el-form>
				</el-card>
        </el-tab-pane>
        <el-tab-pane label="操作日志" name="OpLogs">
			<el-card shadow="hover">
					
					<div class="info">
						<el-scrollbar>
							<el-table class="deviceLogTable" border :header-cell-style="{ background: '#FAFAFA' }"
								:data="deviceLogs" stripe>
								<el-table-column prop="deviceId" label="设备ID" width="140" />
								<!-- 这里后续要不要做个映射呢 -->
								<el-table-column prop="deviceName" label="设备名称" width="140" />
								<el-table-column prop="operation" label="改动字段" width="140" />
								<el-table-column prop="oldValue" label="原值" width="140" />
								<el-table-column prop="newValue" label="新值" width="140" />
								<el-table-column prop="changeDate" sortable label="更改时间" />
							</el-table>
						</el-scrollbar>
					</div>
				</el-card>
        </el-tab-pane>
		<el-tab-pane label="进出日志" name="AccessLogs">
			<el-card shadow="hover">
					<div class="info">
						<el-scrollbar>
							<el-table class="AccessLogTable" border :header-cell-style="{ background: '#FAFAFA' }"
								:data="AccessLogs" stripe>
								<el-table-column prop="direction" label="进/出" width="140" />
								<el-table-column prop="time" sortable label="时间" />
							</el-table>
						</el-scrollbar>
					</div>
				</el-card>
				<ActivityCalendar :data="AccessData" :width="40" :height="7" :cellLength="20" :cellInterval="10"
					:cellBorderRadius="4" :fontSize="12" :showLevelFlag="false" :levelMapper="levelMapper" />
        </el-tab-pane>
    </el-tabs>
	
</template>

<script>

import { ref, reactive } from 'vue'
import http from '@/utils/request/http.js'

export default {
	components: {

	},
	data() {
		return {
			activeName:'userInfo',
			AccessData: [
				
			],
			userData: {
				username: null,
				email: null,
				type: null,
				password: null,
			},
			userTypeName: new Map([
				[1, '普通用户'],
				[2, '管理员'],
				[3, '初级用户']]),
			deviceLogs: [],
			AccessLogs: [],

		}
	},
	mounted() {
		http.get("user/userInfo", {}).then(res => {
			this.userData.username = res.data.userInfo.username;
			this.userData.email = res.data.userInfo.email;
			this.userData.type = res.data.userInfo.type;
		}).catch(err => {
			console.log(err)
		})
		http.get("deviceLog/getMyLog", {}).then(res => {
			this.deviceLogs = res.data.deviceLogs
		}).catch(err => {
			console.log(err)
		})
		http.get("person/userAccessInfo", {}).then(res => {
			this.AccessLogs = res.data.logs
			var timeCount={}
			var data=res.data.logs
			data.forEach(item => {
				if(item.direction==0){
					var date=item.time.split(" ")[0]
					if(timeCount.hasOwnProperty(date)){
						timeCount[date]=timeCount[date]+1
					}
					else
					{
						timeCount[date]=1
					}
				}
			});
			for(var key in timeCount){
				this.AccessData.push({date:key,count:timeCount[key]})
			}
		}).catch(err => {
			console.log(err)
		})
	},
	methods: {
		onSubmit() {
			if (this.userData.password == this.userData.confirmPassword) {
				http.post("user/changeUserInfo", { password: this.userData.password, email: this.userData.email }).then(res => {
				}).catch(err => {
					console.log(err)
				})
			} else {
				alert("两次密码输入不一致")
			}
		},
		levelMapper(count) {
			if (count == 0) {
				return 0;
			} else if (count <= 2) {
				return 3;
			} else if (count <= 6) {
				return 4;
			} else {
				return 5;
			}
		},
		applyForPermission() {
			http.post("permissionApplication/apply", { permissionApplyFor: 1 }).then(res => {
				console.log(res)
			}).catch(err => {
				console.log(err)
			})
		}
	},
	computed: {
	}
}

</script>

<style scoped>
.info {
	text-align: center;
	padding: 35px 0;
}
.tabs{
    padding-left: 10px;
}
</style>
