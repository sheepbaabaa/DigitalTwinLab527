<!-- <template>
    <div>
        <el-row :gutter="20">
            <el-col :span="8">
                <el-card shadow="hover">
                    <template #header>
                        <div class="clearfix">
                            <span>进出日志</span>
                        </div>
                    </template>
                    <div class="AccessLog">
                        <el-scrollbar>
                            <el-table class="AccessLogTable" border :header-cell-style="{ background: '#FAFAFA' }"
                                :data="AccessLogs" stripe>
                                <el-table-column prop="time" label="时间" sortable />
                                <el-table-column prop="direction" label="进/出" />
                            </el-table>
                        </el-scrollbar>
                    </div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template> -->
<template>
    <div>
        <el-row :gutter="20" style="margin-left:2%;margin-top:2%;flex-wrap: nowrap;">
            <el-col :span="3">
                <el-input v-model="searchName" placeholder="根据姓名查询" />
            </el-col>
            <el-col :span="3">
                <el-input v-model="searchCampusNum" placeholder="根据学号查询" />
            </el-col>
            <el-col :span="1">
                <el-button text :icon="Delete" class="red" @click="handleDelete">
                    删除进出日志
                </el-button>
            </el-col>
            <el-col>
                <span class="demonstration" style="margin-right: 10px;">选择时间段: </span>
                <el-date-picker class="el-date-picker__editor-wrap" v-model="timeValueCheck" type="datetimerange"
                    start-placeholder="开始日期" end-placeholder="结束日期" :default-time="defaultTime" @change="handleDateChange"
                    format="YYYY/MM/DD hh:mm:ss" />
            </el-col>
        </el-row>

        <el-scrollbar>
            <el-table class="AccessLogTable" border :header-cell-style="{ background: '#FAFAFA' }"
                :data="filterTableData.slice((currentPage - 1) * pageSize, currentPage * pageSize)" stripe>
                <el-table-column prop="name" label="姓名" width="240"/>
                <el-table-column prop="campus_num" label="学号" width="240" />
                <el-table-column prop="direction" label="进/出" width="240" />
                <el-table-column prop="time" label="时间" sortable />
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
                <span class="demonstration">删除该时间前的进出日志：</span>
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
import { ref, reactive, onMounted, computed } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus';
import { Delete, Edit, Search, Plus } from '@element-plus/icons-vue';
import http from '@/utils/request/http.js'

const AccessLogs = ref([]);
const searchName = ref('');
const searchCampusNum = ref('');
const timeValueCheck = ref([]);
const timeValue = ref();
const defaultTime = new Date(2000, 1, 1, 12, 0, 0) // '12:00:00'

const filterTableData = computed(() => {
    if (!searchName.value && !searchCampusNum.value && timeValueCheck.value.length === 0) {
        console.log('searchName.value: ' + searchName.value)
        console.log('searchCampusNum.value: ' + searchCampusNum.value)
        console.log('timeValueCheck.value.length: ' + timeValueCheck.value.length)
        return AccessLogs.value
    }
    else {
        let filteredData = AccessLogs.value.filter((item) => {
            // console.log('timeValueCheck.value: '+timeValueCheck.value)
            // 判断是否在日期范围内
            // 先把 string 类型的 item.time 转换为 Date 类型
            let timeToBeCmp = new Date(item.time)

            // let dateMatch = item.time >= timeValueCheck.value[0] &&
            // 	item.time <= timeValueCheck.value[1]

            // let dateMatch = timeToBeCmp >= timeValueCheck.value[0] &&
            // 	timeToBeCmp <= timeValueCheck.value[1]

            let dateMatch = timeValueCheck.value.length === 0 ? true : (timeToBeCmp >= timeValueCheck.value[0] && timeToBeCmp <= timeValueCheck.value[1])

            console.log('item.time: ' + item.time)
            // 发现 time 是 string 类型，格式如：'2022-12-29 15:55:02'，无法与 timeValueCheck.value[0] 的 Date 类型作比较
            // 且 timeValueCheck.value[0] 的格式如: 'Tue Mar 01 2022 12:00:00 GMT+0800 (中国标准时间) '
            // 所以在比较之前要做一个类型转换
            console.log('typeof item.time: ' + typeof (item.time))
            console.log('timeValueCheck.value[0]: ' + timeValueCheck.value[0])
            console.log('typeof timeValueCheck.value[0]: ' + typeof (timeValueCheck.value[0]))

            console.log('dateMatch: ' + dateMatch)
            // 判断是否包含搜索关键字

            let searchNameMatch = item.name.toLowerCase().includes(searchName.value.toLowerCase())
            let searchCampusNumMatch = item.campus_num.toString().toLowerCase().includes(searchCampusNum.value.toLowerCase())

            console.log('searchNameMatch: ' + searchNameMatch)
            console.log('searchCampusNumMatch: ' + searchCampusNumMatch)
            console.log('dateMatch && searchNameMatch && searchCampusNumMatch: ' + (dateMatch && searchNameMatch && searchCampusNumMatch))

            // let searchMatch = item.name.toLowerCase().includes(search.value.toLowerCase()) ||
            // 	item.campus_num.toString().toLowerCase().includes(search.value.toLowerCase())
            // console.log('searchMatch: ' + searchMatch)

            // console.log("dateMatch && searchMatch: " + (dateMatch && searchMatch))
            // return dateMatch && searchMatch
            return dateMatch && searchNameMatch && searchCampusNumMatch
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
    http.get("person/getAccessLogs").then(res => {
        AccessLogs.value = res.data.logs
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
			// 但这种删除不能实现页面实时显示删除，必须刷新之后才能看到数据被删掉
			http.post("person/clearAccessLogs", { "timeNode": Math.floor(timeValue.value / 1000) }).then(res => {
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

defineExpose({
    AccessLogs,
    searchName,
    searchCampusNum,
    timeValueCheck,
    timeValue,
    defaultTime,
    filterTableData,
    currentPage,
    small,
    background,
    pageSize,
    disabled,
    pageNum,
    editVisible,
    handleDelete,
    saveEdit,
    handleCurrentChange,
    handleDateChange,
})

</script>

<style scoped>
/* .container {
    padding: 30px;
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
} */
.AccessLogTable {
    width: 80%;
	margin-left: 2%;
}

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

.el-date-picker__editor-wrap {
    display: inline-block;
}
</style>