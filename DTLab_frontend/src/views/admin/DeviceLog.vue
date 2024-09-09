<template>
	<div>
		<el-row :gutter="20" style="margin-left:2%;margin-top:2%">
			<el-col :span="3">
				<el-input v-model="searchDeviceName" placeholder="根据设备名称查询" />
			</el-col>
			<el-col :span="3">
				<el-input v-model="searchOperator" placeholder="根据操作者查询" />
			</el-col>
			<el-col :span="1">
				<el-button text :icon="Delete" class="red" @click="handleDelete">
					删除设备日志
				</el-button>
			</el-col>

			<el-col>
				<div class="block">
					<span class="demonstration">查询以下时间段内的操作日志:</span>
					<el-date-picker v-model="timeValueCheck" type="datetimerange" start-placeholder="Start Date"
						end-placeholder="End Date" :default-time="defaultTime" @change="handleDateChange"
						format="YYYY/MM/DD hh:mm:ss" />
				</div>
			</el-col>

		</el-row>

		<el-scrollbar>
			<el-table class="deviceLogTable" border :header-cell-style="{ background: '#FAFAFA' }"
				:data="filterTableData.slice((currentPage - 1) * pageSize, currentPage * pageSize)" stripe>
				<el-table-column prop="deviceId" label="设备ID" width="140" />
				<!-- 这里后续要不要做个映射呢 -->
				<el-table-column prop="deviceName" label="设备名称" width="140" />
				<el-table-column prop="operation" label="改动字段" width="140" />
				<el-table-column prop="oldValue" label="原值" width="140" />
				<el-table-column prop="newValue" label="新值" width="140" />
				<el-table-column prop="operatorId" label="操作者ID" width="120" />
				<el-table-column prop="changeDate" sortable label="更改时间" />
			</el-table>
		</el-scrollbar>
	</div>
	<div class="demo-pagination-block">
		<el-pagination v-model:current-page="currentPage" v-model:page-size="pageSize" :small="small" :disabled="disabled"
			:background="background" layout="prev, pager, next, jumper" :total=pageNum
			@current-change="handleCurrentChange" />
	</div>
	<div>
		<!-- 删除弹出框：选择时间（value 指定时间戳格式） -->
		<el-dialog title="选择时间" v-model="editVisible" width="30%">
			<div class="block">
				<!-- <span class="demonstration">Timestamp</span>
				<div class="demonstration">Value：{{ timeValue }}</div> -->
				<span class="demonstration">删除该时间前的设备日志：</span>
				<el-date-picker v-model="timeValue" type="datetime" placeholder="Pick a Date" format="YYYY/MM/DD hh:mm:ss"
					value-format="x" />
			</div>
			<template #footer>
				<span class="dialog-footer">
					<el-button @click="editVisible = false">取 消</el-button>
					<el-button type="primary" @click="saveEdit">确 定</el-button>
				</span>
			</template>
		</el-dialog>
	</div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus';
import { Delete, Edit, Search, Plus } from '@element-plus/icons-vue';
import { onMounted } from 'vue'
import http from '@/utils/request/http.js'
import moment from 'moment';

const devices = ref([]);
const tableData = ref([]);
const deviceLogsAll = ref([]);
const timeValue = ref()
const timeValueCheck = ref([]) // 存储选择的日期范围

const defaultTime = new Date(2000, 1, 1, 12, 0, 0) // '12:00:00'
// const moment = require('moment');
const format = "YYYY-MM-DD HH:mm:ss";

const searchDeviceName = ref('')
const searchOperator = ref('')


// const search = ref('')

const filterTableData = computed(() => {
	if (!searchDeviceName.value && !searchOperator.value && timeValueCheck.value.length === 0) {
		console.log('searchDeviceName.value: ' + searchDeviceName.value)
		console.log('searchOperator.value: ' + searchOperator.value)
		console.log('timeValueCheck.value.length: ' + timeValueCheck.value.length)
		return deviceLogsAll.value
	}
	else {
		let filteredData = deviceLogsAll.value.filter((item) => {
			// console.log('timeValueCheck.value: '+timeValueCheck.value)
			// 判断是否在日期范围内
			// 先把 string 类型的 item.changeDate 转换为 Date 类型
			let changeDateToBeCmp = new Date(item.changeDate)

			// let dateMatch = item.changeDate >= timeValueCheck.value[0] &&
			// 	item.changeDate <= timeValueCheck.value[1]

			// let dateMatch = changeDateToBeCmp >= timeValueCheck.value[0] &&
			// 	changeDateToBeCmp <= timeValueCheck.value[1]

			let dateMatch = timeValueCheck.value.length === 0 ? true : (changeDateToBeCmp >= timeValueCheck.value[0] && changeDateToBeCmp <= timeValueCheck.value[1])

			console.log('item.changeDate: ' + item.changeDate)
			// 发现 changeDate 是 string 类型，格式如：'2022-12-29 15:55:02'，无法与 timeValueCheck.value[0] 的 Date 类型作比较
			// 且 timeValueCheck.value[0] 的格式如: 'Tue Mar 01 2022 12:00:00 GMT+0800 (中国标准时间) '
			// 所以在比较之前要做一个类型转换
			console.log('typeof item.changeDate: ' + typeof (item.changeDate))
			console.log('timeValueCheck.value[0]: ' + timeValueCheck.value[0])
			console.log('typeof timeValueCheck.value[0]: ' + typeof (timeValueCheck.value[0]))

			console.log('dateMatch: ' + dateMatch)
			// 判断是否包含搜索关键字

			let searchDeviceNameMatch = item.deviceName.toLowerCase().includes(searchDeviceName.value.toLowerCase())
			let searchOperatorMatch = item.operatorId.toString().toLowerCase().includes(searchOperator.value.toLowerCase())

			console.log('searchDeviceNameMatch: ' + searchDeviceNameMatch)
			console.log('searchOperatorMatch: ' + searchOperatorMatch)
			console.log('dateMatch && searchDeviceNameMatch && searchOperatorMatch: ' + (dateMatch && searchDeviceNameMatch && searchOperatorMatch))

			// let searchMatch = item.deviceName.toLowerCase().includes(search.value.toLowerCase()) ||
			// 	item.operatorId.toString().toLowerCase().includes(search.value.toLowerCase())
			// console.log('searchMatch: ' + searchMatch)

			// console.log("dateMatch && searchMatch: " + (dateMatch && searchMatch))
			// return dateMatch && searchMatch
			return dateMatch && searchDeviceNameMatch && searchOperatorMatch
		})
		console.log("filteredData: ", filteredData); // 打印过滤后的数据
		return filteredData; // 返回过滤后的数据
	}
}
)

const currentPage = ref(1)
const small = ref(false)
const background = ref(true)
const pageSize = ref(10)
const disabled = ref(false)
const pageNum = ref(filterTableData.value.length)
console.log('pageNum')
console.log(pageNum.value)

onMounted(() => {
	http.get("deviceManager/getAllDevice").then(res => {
		console.log("getAllDevice onMounted!")
		console.log(res)
		// composition api 的用法，要加 value
		devices.value = res.data.devices
		console.log(devices.value.length)
		console.log(devices.value)
		// tableData.value = res.data.userList
	}).catch(err => {
		console.log(err)
	})


	http.get("deviceLog/getAllLogs").then(res => {
		console.log("getAllLogs onMounted!")
		console.log(res)
		// composition api 的用法，要加 value
		deviceLogsAll.value = res.data.deviceLogs
		// tableData.value = res.data.userList
	}).catch(err => {
		console.log(err)
	})
})

const editVisible = ref(false);
// 删除操作
const handleDelete = () => {
	editVisible.value = true;
};

const saveEdit = () => {
	// 二次确认删除
	ElMessageBox.confirm('确定要删除吗？', '提示', {
		type: 'warning'
	})
		.then(() => {

			// console.log("before post");
			// console.log(index)
			// console.log(deviceLogsAll.value[index])
			// deviceLogsAll.value.splice(index, 1);
			// 缺一个 post 操作
			console.log(timeValue.value / 1000)
			// 但这种删除不能实现页面实时显示删除，必须刷新之后才能看到数据被删掉
			http.post("deviceLog/clearLog", { "timeNode": Math.floor(timeValue.value / 1000) }).then(res => {
				// console.log(res)
				if (res.code == 200) {
					ElMessage({
						showClose: true,
						duration: 0,
						message: '删除日志成功！',
						type: 'success',
					})
				}
				else {
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
			editVisible.value = false;
		})
		.catch((err) => { console.log(err) });
}

const handleCurrentChange = (val) => {
	console.log(`current page: ${val}`)
}

// change事件处理函数，打印选择的日期范围
const handleDateChange = (value) => {
	console.log("value: " + value);
};

const handleDeviceNameClear = () => {
	this.$refs.table.clearFilter("deviceName");
	this.$refs.table.clearFilter("operatorId");
}

// const handleDeviceNameFilter = (value, row) => {
//       return row.name.includes(value);
//     }

</script>

<style scoped>
.deviceLogTable {
	width: 80%;
	margin-left: 2%;
}

/* 这个红色好像没生效，为什么呢？ */
/* 因为有优先级更高的 style 覆盖了，查看控制台发现是 el-button-text-color 默认为深灰色的原因 */
/* 解决方法：在分号前加 !important */
.red {
	color: #ff0000 !important;
}

.demo-pagination-block {
	margin-left: 1.5%;
	margin-top: 2%;
}

.block {
	/* padding: 30px 0; */
	text-align: center;
	border-right: solid 1px var(--el-border-color);
	flex: 1;
}

.block:last-child {
	border-right: none;
}

.block .demonstration {
	display: block;
	color: var(--el-text-color-secondary);
	font-size: 16px;
	margin-bottom: 20px;
}
</style>