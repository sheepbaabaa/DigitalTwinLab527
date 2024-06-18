<template>
    <div>
        <div class="container">
            <div>
                <el-scrollbar>
                    <el-table class="userInfoTable" border :header-cell-style="{ background: '#FAFAFA' }"
                        :data="filterPersonData.slice((currentPage - 1) * pageSize, currentPage * pageSize)"
                        :row-class-name="tableRowClassName" @row-dblclick="handleTableRow">
                        <el-table-column fixed property="seatId" label="座位号" width="100" />
                        <el-table-column property="nameZh" label="姓名（中）" width="120" />
                        <el-table-column property="nameEn" label="姓名（英）" width="120" />
                        <el-table-column property="personState" label="状态" />
                        <el-table-column label="操作" width="220" align="center">
                            <template #header>
                                <el-input v-model="search" placeholder="根据姓名查询" />
                            </template>
                            <template #default="scope">
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
            <!-- 后续能不能做成导入excel之后自动转换的 -->
            <el-button type="primary" plain @click="AddPVisible = true">新增人员</el-button>
        </div>

        <div>
            <el-dialog v-model="PInfoDialogVisible" title="人员详细信息" width="30%" :before-close="handlePInfoDialogClose">
                <el-form :model="form" label-width="120px">
                    <!-- <el-form-item label="姓名（中）">
                        {{ PInfoDialog.nameZh }}
                    </el-form-item>
                    <el-form-item label="姓名（英）">
                        {{ PInfoDialog.nameEn }}
                    </el-form-item> -->
                    <el-form-item label="姓名">
                        {{ PInfoDialog.nameZh }}
                    </el-form-item>
                    <el-form-item label="状态">
                        {{ PInfoDialog.personState }}
                    </el-form-item>
                    <el-form-item label="备注">
                        {{ PInfoDialog.note }}
                    </el-form-item>
                </el-form>
            </el-dialog>
        </div>
        <!-- 新增人员弹出框 -->
        <div>
            <el-dialog v-model="AddPVisible" title="新增人员信息" width="30%" :before-close="handleAddPDialogClose">
                <el-form ref="AddPFormRef" :model="AddPForm" label-width="80px">
                    <el-form-item label="学号" prop="campusNum" :rules="{
                        required: true,
                        message: '学号不可为空',
                        trigger: 'blur',
                    }">
                        <el-input v-model="AddPForm.campusNum" />
                    </el-form-item>
                    <el-form-item label="英文名" prop="nameEn" :rules="{
                        required: true,
                        message: '英文名不可为空',
                        trigger: 'blur',
                    }">
                        <el-input v-model="AddPForm.nameEn" />
                    </el-form-item>
                    <el-form-item label="中文名" prop="nameZh" :rules="{
                        required: true,
                        message: '中文名不可为空',
                        trigger: 'blur',
                    }">
                        <el-input v-model="AddPForm.nameZh" />
                    </el-form-item>
                    <el-form-item label="座位号" prop="seatId" :rules="[
                        { required: true, message: '座位号不可为空' },
                        { type: 'number', message: '座位号必须是数字' },
                    ]">
                        <el-input v-model.number="AddPForm.seatId" />
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="submitAddPForm(AddPFormRef)">提交</el-button>
                        <el-button @click="resetAddPForm(AddPFormRef)">重置</el-button>
                    </el-form-item>
                </el-form>
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
const filterPersonData = computed(() =>
    tableData.value.filter(
        (data) =>
            !search.value ||
            data.nameZh.toLowerCase().includes(search.value.toLowerCase()) ||
            data.nameEn.toLowerCase().includes(search.value.toLowerCase())
    )
)

const currentPage = ref(1)
const small = ref(false)
const background = ref(true)
const pageSize = ref(10)
const disabled = ref(false)
const pageNum = ref(filterPersonData.value.length)

const AddPVisible = ref(false)
const PInfoDialogVisible = ref(false)
const PInfoDialog = reactive({
    nameZh: '',
    nameEn: '',
    personState: '',
    note: '',
})

const AddPForm = reactive({
    campusNum: '',
    nameEn: '',
    nameZh: '',
    seatId: null,
})

const AddPFormRef = null;

const rules = reactive({
    campusNum: [{ required: true, message: '学号不能为空', trigger: 'change' },],
    nameEn: [{
        required: true, message: '姓名（英）不能为空', trigger: 'change'
    }],
    nameZh: [{
        required: true, message: '姓名（中）不能为空', trigger: 'change'
    }],
    seatId: [
        { required: true, message: '座位号不能为空' },
        { type: 'number', message: '座位号必须为数字' },
    ]
})

const handlePInfoDialogClose = (done) => {
    PInfoDialogVisible.value = false
    done()
}

const handleAddPDialogClose = (done) => {
    AddPVisible.value = false
    done()
}

const filterType = (value, row) => {
    console.log(typeof value)
    console.log(typeof row.type)
    return row.type === value
}

// 这里要传进去的是 {row, rowIndex} 而不是 row, index！
const tableRowClassName = ({ row, rowIndex }) => {
    console.log(row)
    console.log('rowIndex: ' + rowIndex)
    console.log('row.nameZh: ' + row.nameZh)
    if (row.personState === "In_Meeting_Room") {
        return 'warning-row';
    } else if (row.personState === "In_Lab") {
        return 'success-row';
    }
    return '';
}

onMounted(() => {
    http.get("person/getAllStaff").then(res => {
        console.log("onMounted!")
        console.log(res)
        // composition api 的用法，要加 value 
        tableData.value = res.data.staffs
        pageNum.value = tableData.value.length
    }).catch(err => {
        console.log(err)
    })
})

// 双击表格某一行
const handleTableRow = (row, column, event) => {
    PInfoDialog.nameZh = row.nameZh
    PInfoDialog.nameEn = row.nameEn
    PInfoDialog.personState = row.personState
    // PInfoDialog.note = 
    PInfoDialogVisible.value = true
}

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

            http.post("person/deleteStaff", { "memberId": tableData.value[index].memberId }).then(res => {
                console.log("after post");
                // console.log(res)
                if (res.code == 200) {
                    // ElMessage.success('删除成功');
                    tableData.value.splice(index, 1);
                    // 这里需不需要再更新下页数呢？下面的 saveEdit 同理
                    // pageNum.value = tableData.value.length;
                    ElMessage({
                        showClose: true,
                        duration: 0,
                        message: '删除人员成功！',
                        type: 'success',
                    })
                }
                else {
                    ElMessage({
                        showClose: true,
                        duration: 0,
                        // message: res.message,
                        message: '删除人员失败',
                        type: 'error',
                    })
                }
            }).catch(err => {
                console.log(err)
            })
        })
        .catch((err) => { console.log(err) });
};

// const inputChange = (e) => {
//     //强制刷新
//     this.$forceUpdate()
// }

// 表格编辑时弹窗和保存
const editVisible = ref(false);
let form = reactive({
    type: '',
});
let idx = -1;


// const handleSizeChange = (val) => {
//   console.log(`${val} items per page`)
// }
const handleCurrentChange = (val) => {
    console.log(`current page: ${val}`)
};

const submitAddPForm = async (formEl) => {
    if (!formEl) return
    await formEl.validate((valid, fields) => {
        if (valid) {
            http.post("person/addStaff", {
                "campusNum": AddPForm.campusNum, "nameEn": AddPForm.nameEn,
                "nameZh": AddPForm.nameZh, "seatId": AddPForm.seatId
            }).then((res) => {
                console.log(res)
                if (res.code == 200) {
                    AddPVisible.value = false
                    ElMessage({
                        showClose: true,
                        duration: 0,
                        message: '新增人员成功！',
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
            }).catch((err) => {
                console.log(err)
            })
            console.log('提交成功！')
        } else {
            console.log('提交失败！', fields)
        }
    })
};

const resetAddPForm = (formEl) => {
    if (!formEl) return;
    formEl.resetFields();
};

// 使用 <script setup> 的组件是默认关闭的，即通过模板引用或者 $parent 链
// 获取到的组件的公开实例，不会暴露任何在 <script setup> 中声明的绑定。
defineExpose({
    tableData,
    search,
    filterPersonData,
    currentPage,
    small,
    background,
    pageSize,
    disabled,
    pageNum,
    AddPVisible,
    PInfoDialogVisible,
    PInfoDialog,
    AddPForm,
    AddPFormRef,
    rules,
    handlePInfoDialogClose,
    handleAddPDialogClose,
    filterType,
    tableRowClassName,
    handleTableRow,
    handleDelete,
    // inputChange,
    editVisible,
    form,
    handleCurrentChange,
    submitAddPForm,
    resetAddPForm,
})

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

.el-table .warning-row {
    --el-table-tr-bg-color: var(--el-color-warning-light-9);
}

.el-table .success-row {
    --el-table-tr-bg-color: var(--el-color-success-light-9);
}
</style>
  