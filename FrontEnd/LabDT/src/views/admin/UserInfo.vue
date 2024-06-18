<template>
	<div>
		<div class="container">
			<div>
				<el-scrollbar>
					<el-table class="userInfoTable" border :header-cell-style="{ background: '#FAFAFA' }"
						:data="filterTableData.slice((currentPage - 1) * pageSize, currentPage * pageSize)" stripe>
						<el-table-column prop="campusNum" label="学号" width="140" />
						<el-table-column prop="username" label="用户名" width="120" />
						<el-table-column prop="email" label="邮箱" />
						<el-table-column prop="type" label="用户类型" :filters="[
							{ text: '普通用户', value: 1 },
							{ text: '管理员', value: 2 }
						]" :filter-method="filterType">
							<template #default="scope">
								<el-tag :type=tagType.get(scope.row.type) disable-transitions>{{
										userTypeName.get(scope.row.type)
								}}</el-tag>
							</template>
						</el-table-column>
						<el-table-column label="操作" width="220" align="center">
							<template #header>
								<el-input v-model="search" placeholder="根据学号查询" />
							</template>
							<template #default="scope">
								<el-button text :icon="Edit" @click="handleEdit(scope.$index, scope.row)">
									编辑
								</el-button>
								<el-button text :icon="Delete" class="red" @click="handleDelete(scope.$index)">
									删除
								</el-button>
							</template>
						</el-table-column>
					</el-table>
				</el-scrollbar>
			</div>
			<div class="demo-pagination-block">
				<el-pagination v-model:current-page="currentPage" v-model:page-size="pageSize" :small="small"
					:disabled="disabled" :background="background" layout="prev, pager, next, jumper" :total=pageNum
					@current-change="handleCurrentChange" />
			</div>
			<el-button type="primary" plain @click="dialogTableVisible = true">查看权限申请</el-button>
		</div>

		<div>
			<!-- 编辑弹出框 -->
			<el-dialog title="编辑" v-model="editVisible" width="30%">
				<el-form label-width="70px">
					<el-form-item label="用户类型">
						<el-input v-model="form.type"></el-input>
					</el-form-item>
				</el-form>
				<template #footer>
					<span class="dialog-footer">
						<el-button @click="editVisible = false">取 消</el-button>
						<el-button type="primary" @click="saveEdit">确 定</el-button>
					</span>
				</template>
			</el-dialog>
		</div>
		<div>
			<!-- 查看权限申请弹出框 -->
			<el-dialog v-model="dialogTableVisible" title="权限申请名单">
				<el-table :data="usersApplyForPermission" border :header-cell-style="{ background: '#FAFAFA' }" stripe>
					<el-table-column prop="username" label="用户名" width="120" />
					<el-table-column prop="email" label="邮箱" />
					<el-table-column label="操作" width="220" align="center">
						<!-- 无论通过或者拒绝，都需在后端请求成功后使用 splice 来删除这一行  -->
						<template #default="scope">
							<!-- 若通过，则对 user 数据库的 type 属性做更改（post） -->
							<el-button text type="success" :icon="Check" @click="handleApprove(scope.$index)">
								通过
							</el-button>
							<!-- 若拒绝，则不对原 user 数据库做更改，也需跟后端交互（post）【目的是为了让后端在权限申请列表里删掉这一行】-->
							<el-button text class="red" :icon="Close" @click="handleRefuse(scope.$index)">
								拒绝
							</el-button>
						</template>
					</el-table-column>
				</el-table>
			</el-dialog>
		</div>
	</div>

</template>
  
<script setup>
import { ref, reactive, computed } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus';
import { Delete, Edit, Search, Plus, Check, Close } from '@element-plus/icons-vue';
import { onMounted } from 'vue'
import http from '@/utils/request/http.js'

const tableData = ref([]);

const search = ref('')
const filterTableData = computed(() =>
	tableData.value.filter(
		(data) =>
			!search.value ||
			data.campusNum.toLowerCase().includes(search.value.toLowerCase())
	)
)

const currentPage = ref(1)
const small = ref(false)
const background = ref(true)
const pageSize = ref(10)
const disabled = ref(false)
const pageNum = ref(filterTableData.value.length)
console.log('pageNum')
console.log(pageNum.value)

// const tags = ref([
//   { name: 'Tag 1', value:'1', type: '' },
//   { name: 'Tag 2', value:'2', type: 'success' },
//   { name: 'Tag 3', value:'3', type: 'info' },
// ])

// 数据库存的用户类型 type 与 tag 类型的映射
// 注意数据库里的 type 是 INT 类型的，这里也应该对应整数，刚才一直出错就是因为写成了 ['1', ''] 这种
const tagType = new Map([
	[1, ''],
	[2, 'success'],
	[3, 'info']
])

// 数据库里存的用户类型 type 与用户类型名称的映射
// 初级用户就是和游客具有同样权限，但有账号可以登陆，并可以被升级为普通用户（具有一定修改权限）的用户
const userTypeName = new Map([
	[0, '初级用户'],
	[1, '普通用户'],
	[2, '管理员']
])

const dialogTableVisible = ref(false)

const filterType = (value, row) => {
	// console.log(value)
	// console.log(row.type)
	// console.log(tagType)
	// console.log(tagType.get(row.type))
	// // 注意这里数据类型的匹配问题
	// console.log(row.type === value)
	// console.log(row.type == value)
	console.log(typeof value)
	console.log(typeof row.type)
	return row.type === value
}

const usersApplyForPermission = ref([]);

onMounted(() => {
	http.get("/user/getAllUser").then(res => {
		console.log("onMounted!")
		console.log(res)
		// composition api 的用法，要加 value 
		tableData.value = res.data.userList
		pageNum.value = tableData.value.length
		console.log('pageNum.value')
		console.log(pageNum.value)
		// console.log("tableData: "+ tableData)
	}).catch(err => {
		console.log(err)
	})

	// 通过 http.get() 方法获取申请权限的用户信息 usersApplyForPermission
	// usersApplyForPermission.value = res.xxx
	// if 判断该在这里做吗？
	// if usersApplyForPermission != null
	// then 使用 ElNotification
	http.get("permissionApplication/getApplications").then(res => {
		// 此处做一下筛选，选出 ifProcessed == 0 的数据项赋给 usersApplyForPermission
		// usersApplyForPermission.value = res.data.applications;
		for(app in res.data.applications){
			if(app.ifProcessed == 0)
			usersApplyForPermission.value.push(app);
		}
	}).catch(err => {
		console.log(err);
	})
})

// 删除操作
const handleDelete = (index) => {
	// 二次确认删除
	ElMessageBox.confirm('确定要删除吗？', '提示', {
		type: 'warning'
	})
		.then(() => {

			console.log("before post");
			console.log(index)
			console.log(tableData.value[index])

			http.post("user/deleteUser", { "id": tableData.value[index].id }).then(res => {
				console.log("after post");
				// console.log(res)
				if (res.code == 200) {
					// ElMessage.success('删除成功');
					tableData.value.splice(index, 1);
					ElMessage({
						showClose: true,
						duration: 0,
						message: '删除用户成功！',
						type: 'success',
					})
				}
				else {
					ElMessage({
						showClose: true,
						duration: 0,
						// message: res.message,
						message: '删除用户失败',
						type: 'error',
					})
				}
			}).catch(err => {
				console.log(err)
			})
		})
		.catch((err) => { console.log(err) });
};

// 表格编辑时弹窗和保存
const editVisible = ref(false);
let form = reactive({
	type: '',
});
let idx = -1;
const handleEdit = (index, row) => {
	idx = index;
	form.type = row.type;
	editVisible.value = true;
};
const saveEdit = () => {
	editVisible.value = false;
	ElMessage.success(`修改第 ${idx + 1} 行成功`);
	tableData.value[idx].type = form.type;
	http.post("user/changeUserType", { "id": tableData.value[idx].id, "type": tableData.value[idx].type }).then(res => {
		// console.log(res)
		if (res.code == 200) {
			ElMessage({
				showClose: true,
				duration: 0,
				message: '修改用户类型成功！',
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
};

// const handleSizeChange = (val) => {
//   console.log(`${val} items per page`)
// }
const handleCurrentChange = (val) => {
	console.log(`current page: ${val}`)
};

const handleApprove = (index) => {
	http.post("permissionApplication/approval", {"id": usersApplyForPermission.value[index].id, "result": 1}).then(res => {
		if(res.code == 200){
			usersApplyForPermission.value.splice(index, 1);
		}
		else{
			ElMessage({
				showClose: true,
				duration: 0,
				message: res.message,
				type: 'error',
			})
		}
	})
};

const handleRefuse = (index) => {
	http.post("permissionApplication/approval", {"id": usersApplyForPermission.value[index].id, "result": 2}).then(res => {
		if(res.code == 200){
			usersApplyForPermission.value.splice(index, 1);
		}
		else{
			ElMessage({
				showClose: true,
				duration: 0,
				message: res.message,
				type: 'error',
			})
		}
	})
};

</script>
  
<style scoped>
.userInfoTable {
	width: 80%;
	margin-left: 2%;
	margin-top: 2%;
}

.demo-pagination-block {
	margin-left: 1.5%;
	margin-top: 2%;
}

/* 这个红色好像没生效，为什么呢？ */
/* 因为有优先级更高的 style 覆盖了，查看控制台发现是 el-button-text-color 默认为深灰色的原因 */
/* 解决方法：在分号前加 !important */
.red {
	color: #ff0000 !important;
}

.container {
	padding: 30px;
	background: #fff;
	border: 1px solid #ddd;
	border-radius: 5px;
}
</style>
  