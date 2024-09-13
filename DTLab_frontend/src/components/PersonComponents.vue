<template>
    <div v-show="PersonInfoVisible" class="PersonComponents">
        <el-drawer
            v-model="PersonInfoVisible"
            title="实验室成员"
            direction="rtl"
            size="30%"
            :before-close="handleClose"
            >
            
            <el-table 
            :data="PersonData"
            :row-class-name="tableRowClassName"
            max-height="900"
            @row-dblclick="handleTableRow"
            > <!-- data = this.$store.state -->
            <el-table-column fixed property="member_id" label="座位号" width="100" />
            <el-table-column property="name" label="姓名" width="120" />
            <el-table-column property="person_state" label="状态" />
            </el-table>
        </el-drawer>

        <el-dialog
            v-model="dialogVisible"
            title="人员详细信息"
            width="30%"
            :before-close="handleDialogClose"
        >
            <el-form :model="form" label-width="60px">
                <el-form-item label="姓名">
                    {{this.dialogInfo.name}}
                </el-form-item>
                <el-form-item label="状态">
                    {{this.dialogInfo.person_state}}
                </el-form-item>
                <el-form-item label="备注">
                    {{this.dialogInfo.note}}
                </el-form-item>
            </el-form>
        </el-dialog>

    </div>
</template>

<script>
import { ElDrawer,ElMessageBox} from 'element-plus'
import { toRaw } from '@vue/reactivity'

export default {
    name: "PersonComponents",
    props: ['PersonInfoVisible','PersonData'],//父组件SceneCanvas传值
    data() {
        return {
            dialogVisible:false,
            dialogInfo:{
                member_id: null,
                name: "佚名",
                person_state: "??",
                note:"啦啦啦"
            },
        }
    },
    mounted() {
        // for (let person of list) {
        //    PersonData.push(person);
        // }

        //初始化人物模型
       
    },
    methods: {
        tableRowClassName({row,rowIndex}){
            console.log(rowIndex,row.name)
            if (row.person_state === "In_Meeting_Room") {
                return 'warning-row';
            } else if(row.person_state === "In_Lab"){
                return 'success-row';
            }
            return '';
        },
        
        handleClose(done){
            this.$parent.clickPersonComponents()
            done()
        },

        handleDialogClose(done){
            this.dialogVisible = false
            done()
        },


        handleTableRow(row, column, event){
            this.dialogInfo.name = row.name
            this.dialogInfo.person_state = row.person_state
            //this.dialogInfo.note = this.$store.state[row.name].
            this.dialogVisible = true
        }

    }

    
}
</script>

<style>
.PersonComponents {
  
  opacity: 1;
}

.el-table .warning-row {
  --el-table-tr-bg-color: var(--el-color-warning-light-9);
}
.el-table .success-row {
  --el-table-tr-bg-color: var(--el-color-success-light-9);
}

</style>