<template>
    <div>
        <div class="container">
            <div>
                <el-scrollbar>
                    <el-table class="deviceTypeTable" border :header-cell-style="{ background: '#FAFAFA' }"
                        :data="filterTableData.slice((currentPage - 1) * pageSize, currentPage * pageSize)" stripe
                        @expand-change="handleExpandChange">
                        <!-- 添加一个可展开的列 -->
                        <el-table-column type="expand">
                            <!-- 定义展开行的内容 -->
                            <!-- 使用 slot-scope 属性来定义一个对象，包含当前行的数据和索引 -->
                            <template v-slot:default="scope">
                                <!-- 使用一个子表格来显示属性数组 -->
                                <!-- 调用 getDeviceTypeInfo 函数，并传入 scope.row.typeName 参数 -->
                                <!-- 换一种方法 -->
                                <el-table :data="deviceAttributes[scope.row.typeName]" border
                                    :cell-style="{ textAlign: 'center' }" :header-cell-style="{ textAlign: 'center' }">
                                    <el-table-column prop="field_name" label="属性名" />
                                    <el-table-column prop="description" label="描述" />
                                    <el-table-column prop="type" label="字段值类型" />
                                    <!-- <el-table-column prop=controllableMap.get(controllable) label="是否可操纵" /> -->
                                    <!-- 可以使用 formatter 来格式化指定列的值,可以处理成自己想要的映射关系-->
                                    <el-table-column prop="controllable" label="是否可操纵" :formatter="controllableFormatter" />
                                </el-table>
                            </template>
                        </el-table-column>
                        <el-table-column prop="typeName" label="设备类型" />
                        <el-table-column prop="description" label="描述" />
                        <el-table-column label="操作" width="220" align="center">
                            <template #header>
                                <el-input v-model="search" placeholder="根据设备类型查询" />
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
            <el-button type="primary" plain @click="addTypeVisible = true">增加设备类型</el-button>
        </div>

        <div>
            <!-- 编辑设备类型弹出框 -->
            <el-dialog title="编辑设备类型" v-model="editTypeVisible" :before-close="handleClose">
                <el-form :model="deviceTypeEditForm" ref="deviceEditTypeFormRef" label-width="100px" class="demo-dynamic">
                    <el-row :gutter="20">
                        <el-col :span="6">
                            <el-form-item :label="'类型名称'" prop="typename" :rules="{
                                required: true,
                                message: '类型名称不可为空',
                                trigger: 'blur',
                            }">
                                <el-input v-model="deviceTypeEditForm.typename" />
                            </el-form-item>
                        </el-col>
                        <el-col :span="6">
                            <el-form-item :label="'描述'" prop="typedescription" :rules="{
                                required: true,
                                message: '描述不可为空',
                                trigger: 'blur',
                            }">
                                <el-input v-model="deviceTypeEditForm.typedescription" />
                            </el-form-item>
                        </el-col>
                        <el-col :span="6">
                            <!-- 需要加个 prop -->
                            <el-form-item label="操作权限" prop="permissionLevel" :rules="{
                                required: true,
                                message: '请选择操作权限',
                                trigger: 'blur',
                            }">
                                <el-select v-model="deviceTypeEditForm.permissionLevel" class="m-2" placeholder="请选择操作权限">
                                    <el-option v-for="item in permissionOptions" :key="item.value" :label="item.label"
                                        :value="item.value" />
                                </el-select>
                            </el-form-item>

                        </el-col>
                    </el-row>
                    <el-row :gutter="20" v-for="(domain, index) in deviceTypeEditForm.deviceFields" :key="domain.key">
                        <el-col :span="5">
                            <el-form-item :label="'属性名称'" :prop="'deviceFields.' + index + '.attributename'" :rules="{
                                required: true,
                                message: '属性名称不可为空',
                                trigger: 'blur',
                            }">
                                <el-input v-model="domain.attributename" />
                            </el-form-item>
                        </el-col>

                        <el-col :span="5">
                            <el-form-item label="字段值类型" :prop="'deviceFields.' + index + '.valuetype'" :rules="{
                                required: true,
                                message: '请选择字段值类型',
                                trigger: 'blur',
                            }">
                                <el-select v-model="domain.valuetype" class="m-2" placeholder="请选择"
                                    @change="handleEditValueChange(index, $event)">
                                    <el-option v-for="item in valuetypeOptions" :key="item.value" :label="item.label"
                                        :value="item.value" />
                                </el-select>
                            </el-form-item>
                        </el-col>

                        <!-- 输入最小值 -->
                        <el-col :span="5" v-show="deviceTypeEditForm.deviceFields[index].showMinMax">
                            <el-form-item label="最小值">
                                <el-input-number v-model.number="deviceTypeEditForm.deviceFields[index].minValue" />
                            </el-form-item>
                        </el-col>

                        <!-- 输入最大值 -->
                        <el-col :span="5" v-show="deviceTypeEditForm.deviceFields[index].showMinMax">
                            <el-form-item label="最大值">
                                <el-input-number v-model.number="deviceTypeEditForm.deviceFields[index].maxValue" />
                            </el-form-item>
                        </el-col>

                        <el-col :span="8" v-show="deviceTypeEditForm.deviceFields[index].showEnum">
                            <el-form-item label="取值集合">
                                <el-input v-model="deviceTypeEditForm.deviceFields[index].itemTxt" autosize type="textarea"
                                    placeholder="请以“value1:description1;value2:description2”的格式输入" />
                            </el-form-item>
                        </el-col>

                        <el-col :span="5">
                            <el-form-item label="是否可操纵" :prop="'deviceFields.' + index + '.controllable'" :rules="{
                                required: true,
                                message: '请确定是否可操作',
                                trigger: 'blur',
                            }">
                                <el-select v-model="domain.controllable" class="m-2" placeholder="请选择">
                                    <el-option label="不可人为操纵" value=0 />
                                    <el-option label="可人为操纵" value=1 />
                                </el-select>
                            </el-form-item>
                        </el-col>
                        <el-col :span="5">
                            <el-form-item :label="'描述'" :prop="'deviceFields.' + index + '.attrdescription'" :rules="{
                                required: true,
                                message: '描述不可为空',
                                trigger: 'blur',
                            }">
                                <el-input v-model="domain.attrdescription" />
                            </el-form-item>
                        </el-col>
                        <el-col :span="3">
                            <el-button class="mt-2" @click.prevent="removeEditDomain(domain)">删除</el-button>
                        </el-col>
                    </el-row>
                    <el-form-item>
                        <el-button @click="addEditDomain">增加属性</el-button>
                        <el-button @click="resetEditForm(this.$refs.deviceEditTypeFormRef)">重置</el-button>
                    </el-form-item>
                </el-form>

                <template #footer>
                    <span class="dialog-footer">
                        <el-button @click="handleCancle">取 消</el-button>
                        <el-button type="primary" @click="saveEdit">确 定</el-button>
                    </span>
                </template>
            </el-dialog>
        </div>

        <div>
            <!-- 增加设备类型弹出框 -->
            <el-dialog v-model="addTypeVisible" title="增加设备类型">
                <el-form :model="deviceTypeForm" ref="deviceTypeFormRef" label-width="100px" class="demo-dynamic">
                    <el-row :gutter="20">
                        <el-col :span="6">
                            <!-- 注意这里的 prop，vue组件的属性中，加冒号的，说明后面的是一个变量或者表达式；没加冒号的后面就是对应的字符串字面量！
                                这里 prop 前不能加冒号！下面 deviceFields 里的 prop 要形成一个表达式，所以才会加冒号！ -->
                            <el-form-item :label="'类型名称'" prop="typename" :rules="{
                                required: true,
                                message: '类型名称不可为空',
                                trigger: 'blur',
                            }">
                                <el-input v-model="deviceTypeForm.typename" />
                            </el-form-item>
                        </el-col>
                        <el-col :span="6">
                            <el-form-item :label="'描述'" prop="typedescription" :rules="{
                                required: true,
                                message: '描述不可为空',
                                trigger: 'blur',
                            }">
                                <el-input v-model="deviceTypeForm.typedescription" />
                            </el-form-item>
                        </el-col>
                        <el-col :span="6">
                            <!-- 需要加个 prop -->
                            <el-form-item label="操作权限" prop="permissionLevel" :rules="{
                                required: true,
                                message: '请选择操作权限',
                                trigger: 'blur',
                            }">
                                <el-select v-model="deviceTypeForm.permissionLevel" class="m-2" placeholder="请选择操作权限">
                                    <el-option v-for="item in permissionOptions" :key="item.value" :label="item.label"
                                        :value="item.value" />
                                </el-select>
                            </el-form-item>

                        </el-col>
                    </el-row>
                    <el-row :gutter="20" v-for="(domain, index) in deviceTypeForm.deviceFields" :key="domain.key">
                        <el-col :span="5">
                            <el-form-item :label="'属性名称'" :prop="'deviceFields.' + index + '.attributename'" :rules="{
                                required: true,
                                message: '属性名称不可为空',
                                trigger: 'blur',
                            }">
                                <el-input v-model="domain.attributename" />
                            </el-form-item>
                        </el-col>

                        <el-col :span="5">
                            <el-form-item label="字段值类型" :prop="'deviceFields.' + index + '.valuetype'" :rules="{
                                required: true,
                                message: '请选择字段值类型',
                                trigger: 'blur',
                            }">
                                <el-select v-model="domain.valuetype" class="m-2" placeholder="请选择"
                                    @change="handleValueChange(index, $event)">
                                    <el-option v-for="item in valuetypeOptions" :key="item.value" :label="item.label"
                                        :value="item.value" />
                                </el-select>
                            </el-form-item>
                        </el-col>

                        <!-- 输入最小值 -->
                        <el-col :span="5" v-show="deviceTypeForm.deviceFields[index].showMinMax">
                            <el-form-item label="最小值">
                                <el-input-number v-model.number="deviceTypeForm.deviceFields[index].minValue" />
                            </el-form-item>
                        </el-col>

                        <!-- 输入最大值 -->
                        <el-col :span="5" v-show="deviceTypeForm.deviceFields[index].showMinMax">
                            <el-form-item label="最大值">
                                <el-input-number v-model.number="deviceTypeForm.deviceFields[index].maxValue" />
                            </el-form-item>
                        </el-col>

                        <el-col :span="8" v-show="deviceTypeForm.deviceFields[index].showEnum">
                            <el-form-item label="取值集合">
                                <el-input v-model="deviceTypeForm.deviceFields[index].itemTxt" autosize type="textarea"
                                    placeholder="请以“value1:description1;value2:description2”的格式输入" />
                            </el-form-item>
                        </el-col>

                        <el-col :span="5">
                            <el-form-item label="是否可操纵" :prop="'deviceFields.' + index + '.controllable'" :rules="{
                                required: true,
                                message: '请确定是否可操作',
                                trigger: 'blur',
                            }">
                                <el-select v-model="domain.controllable" class="m-2" placeholder="请选择">
                                    <el-option label="不可人为操纵" value=0 />
                                    <el-option label="可人为操纵" value=1 />
                                </el-select>
                            </el-form-item>
                        </el-col>
                        <el-col :span="5">
                            <el-form-item :label="'描述'" :prop="'deviceFields.' + index + '.attrdescription'" :rules="{
                                required: true,
                                message: '描述不可为空',
                                trigger: 'blur',
                            }">
                                <el-input v-model="domain.attrdescription" />
                            </el-form-item>
                        </el-col>
                        <el-col :span="3">
                            <el-button class="mt-2" @click.prevent="removeDomain(domain)">删除</el-button>
                        </el-col>
                    </el-row>
                    <el-form-item>
                        <el-button type="primary" @click="submitForm(this.$refs.deviceTypeFormRef)">提交</el-button>
                        <el-button @click="addDomain">增加属性</el-button>
                        <el-button @click="resetForm(this.$refs.deviceTypeFormRef)">重置</el-button>
                    </el-form-item>
                </el-form>
            </el-dialog>
        </div>
    </div>
</template>
  
<script>

import { ref, reactive, computed, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus';
import { Delete, Edit, Search, Plus, Check, Close } from '@element-plus/icons-vue';
import http from '@/utils/request/http';
export default {
    name: 'DeviceTypeComponents',
    props: [],
    data() {
        return {
            tableData: [],
            search: "",
            currentPage: 1,
            small: false,
            background: true,
            pageSize: 10,
            disabled: false,
            addTypeVisible: false,
            formRef: null,
            editTypeVisible: false,
            idx: -1,
            deviceTypeEditForm: {
                typeId: null,
                typename: '',
                typedescription: '',
                permissionLevel: null,
                deviceFields: [
                    {
                        key: 1,
                        attributename: '',
                        valuetype: '',
                        attrdescription: '',
                        controllable: null,
                        minValue: null,
                        maxValue: null,
                        showMinMax: false,
                        showEnum: false,
                        item: [
                            {
                                value: null,
                                description: ''
                            }
                        ],
                        itemTxt: ''
                    },
                ],
            },
            // 深拷贝
            // deepCopy: JSON.parse(JSON.stringify(this.deviceTypeEditForm)),
            // deviceTypeEditFormBlank: {
            //     typeId: null,
            //     typename: '',
            //     typedescription: '',
            //     permissionLevel: null,
            //     deviceFields: [
            //         {
            //             key: 1,
            //             attributename: '',
            //             valuetype: '',
            //             attrdescription: '',
            //             controllable: null,
            //             minValue: null,
            //             maxValue: null,
            //             showMinMax: false,
            //             showEnum: false,
            //             item: [
            //                 {
            //                     value: null,
            //                     description: ''
            //                 }
            //             ],
            //             itemTxt: ''
            //         },
            //     ],
            // },

            permissionOptions: [
                {
                    value: 0,
                    label: '初级用户'
                },
                {
                    value: 1,
                    label: '普通用户'
                },
                {
                    value: 2,
                    label: '管理员'
                },
            ],
            valuetypeOptions: [
                {
                    value: 'int',
                    label: 'int（整型）'
                },
                {
                    value: 'float',
                    label: 'float（浮点类型）'
                },
                {
                    value: 'str',
                    label: 'str（字符串类型）'
                },
                {
                    value: 'enum',
                    label: 'enum（枚举型）'
                },
            ],
            deviceTypeForm: {
                typename: '',
                typedescription: '',
                permissionLevel: null,
                deviceFields: [
                    {
                        key: 1,
                        attributename: '',
                        valuetype: '',
                        attrdescription: '',
                        controllable: null,
                        minValue: null,
                        maxValue: null,
                        showMinMax: false,
                        showEnum: false,
                        item: [
                            {
                                value: null,
                                description: ''
                            }
                        ],
                        itemTxt: ''
                    },
                ],
            },
            deviceAttributes: [],
            deviceTypeFormRef: null,
            deviceEditTypeFormRef: null,
            controllableMap: new Map([
                [0, '否'],
                [1, '是'],
            ])
        }
    },
    mounted() {
        http.get("deviceTypeManager/getAllType").then((res) => {
            this.tableData = res.data.deviceTypes
            console.log("this.tableData: ", this.tableData)
            this.pageNum = this.tableData.length
        }).catch(err => {
            console.log(err)
        })

    },
    computed: {
        filterTableData() {
            return this.tableData.filter(
                (data) =>
                    !this.search || data.typeName.toLowerCase().includes(this.search.toLowerCase())
            )
        },
        pageNum() {
            return this.filterTableData.length
        }
    },
    methods: {
        removeDomain(item) {
            const index = this.deviceTypeForm.deviceFields.indexOf(item)
            if (index !== -1) {
                this.deviceTypeForm.deviceFields.splice(index, 1)
            }
        },
        removeEditDomain(item) {
            const index = this.deviceTypeEditForm.deviceFields.indexOf(item)
            if (index !== -1) {
                this.deviceTypeEditForm.deviceFields.splice(index, 1)
            }
        },
        addDomain() {
            this.deviceTypeForm.deviceFields.push({
                key: Date.now(),
                attributename: '',
                valuetype: '',
                attrdescription: ''
            })
        },
        addEditDomain() {
            this.deviceTypeEditForm.deviceFields.push({
                key: Date.now(),
                attributename: '',
                valuetype: '',
                attrdescription: ''
            })
        },
        handleValueChange(index, value) {
            if (value === "int" || value === "float") {
                this.deviceTypeForm.deviceFields[index].showMinMax = true;
                this.deviceTypeForm.deviceFields[index].showEnum = false;
            } else if (value === "enum") {
                this.deviceTypeForm.deviceFields[index].showMinMax = false;
                this.deviceTypeForm.deviceFields[index].showEnum = true;
            } else {
                this.deviceTypeForm.deviceFields[index].showMinMax = false;
                this.deviceTypeForm.deviceFields[index].showEnum = false;
            }
        },
        handleEditValueChange(index, value) {
            if (value === "int" || value === "float") {
                this.deviceTypeEditForm.deviceFields[index].showMinMax = true;
                this.deviceTypeEditForm.deviceFields[index].showEnum = false;
            } else if (value === "enum") {
                this.deviceTypeEditForm.deviceFields[index].showMinMax = false;
                this.deviceTypeEditForm.deviceFields[index].showEnum = true;
            } else {
                this.deviceTypeEditForm.deviceFields[index].showMinMax = false;
                this.deviceTypeEditForm.deviceFields[index].showEnum = false;
            }
        },
        submitForm(formEl) {
            console.log(formEl)
            if (!formEl) return
            formEl.validate((valid) => {

                console.log('valid!')
                let deviceTypeData = {}
                deviceTypeData['name'] = this.deviceTypeForm.typename
                deviceTypeData['description'] = this.deviceTypeForm.typedescription
                deviceTypeData['permissionLevel'] = this.deviceTypeForm.permissionLevel
                deviceTypeData['device_fields'] = []
                this.deviceTypeForm.deviceFields.forEach(item => {
                    var fieldData = {}
                    fieldData['type'] = item.valuetype
                    fieldData['controllable'] = item.controllable
                    fieldData['field_name'] = item.attributename
                    fieldData['description'] = item.attrdescription
                    if (item.valuetype == "int" || item.valuetype == "float") {
                        fieldData['min_value'] = item.minValue
                        fieldData['max_value'] = item.maxValue
                    }
                    else if (item.valuetype == "enum") {
                        fieldData['item'] = []
                        let enumItems = item.itemTxt.split(';')
                        enumItems.forEach(enumItem => {
                            var temp = enumItem.split(":")
                            fieldData['item'].push({ value: temp[0], description: temp[1] })
                        })
                    }
                    deviceTypeData.device_fields.push(fieldData)
                });
                console.log(deviceTypeData)
                // 无法传递带有数组的json对象，所以把这个json对象转换成string类型，再给他赋一个key 也就是{'data':字符串化的json对象}
                http.post("deviceTypeManager/addNewDeviceType", {
                    data: JSON.stringify(deviceTypeData)
                }).then((res) => {
                    if (res.code == 200) {
                        ElMessage({
                            showClose: true,
                            duration: 0,
                            message: '增加设备类型成功！',
                            type: 'success',
                        })
                    }
                    else {
                        ElMessage({
                            showClose: true,
                            duration: 0,
                            message: '增加设备类型失败',
                            type: 'error',
                        })
                    }
                    console.log(res)
                }).catch((err) => {
                    console.log(err)
                })
            })
        },
        resetForm(formEl) {
            console.log("formEl to be reset: ", formEl)
            if (formEl) {
                formEl.resetFields()
            }

        },
        resetEditForm(formEl) {
            console.log("formEl to be reset: ", formEl)
            if (formEl) {
                // formEl.resetFields()
                // 为什么这里用 resetFields 不起效啊？？
                this.deviceTypeEditForm = {
                    typeId: null,
                    typename: '',
                    typedescription: '',
                    permissionLevel: null,
                    deviceFields: [
                        {
                            key: 1,
                            attributename: '',
                            valuetype: '',
                            attrdescription: '',
                            controllable: null,
                            minValue: null,
                            maxValue: null,
                            showMinMax: false,
                            showEnum: false,
                            item: [
                                {
                                    value: null,
                                    description: ''
                                }
                            ],
                            itemTxt: ''
                        },
                    ],
                };
            }

        },
        // getDeviceTypeInfo(typeName) {
        //     console.log(typeName)
        //     http.post("deviceTypeManager/deviceTypeInfo", { "typeName": typeName }).then((res) => {
        //         console.log(res)
        //         // 需根据实际返回数据修改
        //         this.deviceAttributes = res.data.attributes;
        //     }).catch((err) => {
        //         console.log(err)
        //     })
        // }
        handleExpandChange(row, expandedRows) {
            // check if the device attributes are already fetched
            if (!this.deviceAttributes[row.typeName]) {
                // if not, send a request to get them
                http.post("deviceTypeManager/deviceTypeInfo", { "typeName": row.typeName }).then((res) => {
                    console.log(res);
                    console.log(this)
                    // this.$set(this.deviceAttributes, row.typeName, res.data.info.device_fields);
                    // Vue3中不需要使用this.$set方法了。因为Vue3使用了ES6的proxy来实现数据响应式，它可以自动检测到对象或数组中的新增或删除，并更新视图。
                    // 所以可以直接使用赋值的方式来修改数据，不用担心视图不更新的问题。
                    this.deviceAttributes[row.typeName] = res.data.info.device_fields;
                }).catch((err) => {
                    console.log(err);
                });
            }
        },
        controllableFormatter(row, column) {
            if (row.controllable == '0')
                return "否";
            else return "是"
        },

        handleClose(done) {
            this.deviceTypeEditForm = {
                typeId: null,
                typename: '',
                typedescription: '',
                permissionLevel: null,
                deviceFields: [
                    {
                        key: 1,
                        attributename: '',
                        valuetype: '',
                        attrdescription: '',
                        controllable: null,
                        minValue: null,
                        maxValue: null,
                        showMinMax: false,
                        showEnum: false,
                        item: [
                            {
                                value: null,
                                description: ''
                            }
                        ],
                        itemTxt: ''
                    },
                ],
            };
            // 这种为啥不行
            // this.deviceTypeEditForm  = this.deviceTypeEditFormBlank;
            done();
        },

        handleCancle() {
            this.editTypeVisible = false;
            this.deviceTypeEditForm = {
                typeId: null,
                typename: '',
                typedescription: '',
                permissionLevel: null,
                deviceFields: [
                    {
                        key: 1,
                        attributename: '',
                        valuetype: '',
                        attrdescription: '',
                        controllable: null,
                        minValue: null,
                        maxValue: null,
                        showMinMax: false,
                        showEnum: false,
                        item: [
                            {
                                value: null,
                                description: ''
                            }
                        ],
                        itemTxt: ''
                    },
                ],
            };
        },

        handleEdit(index, row) {
            console.log("Handle Edit!")
            console.log("row: ", row);
            this.idx = index;
            // 出问题的是这个部分
            // 应该利用前面得到的 this.deviceAttributes[row.typeName] 来给 deviceFields 赋值
            this.deviceTypeEditForm.typename = row.typeName;
            this.deviceTypeEditForm.typedescription = row.description;
            this.deviceTypeEditForm.typeId = row.id;
            // console.log("row.id: " + row.id)
            this.deviceTypeEditForm.permissionLevel = row.permissionLevel;
            // this.deviceTypeEditForm.deviceFields = row.deviceFields;
            console.log("this.deviceAttributes: ", this.deviceAttributes)
            console.log("this.deviceAttributes[row.typeName]: ", this.deviceAttributes[row.typeName])
            // 这个记得注释掉
            // this.deviceTypeEditForm.deviceFields = this.deviceAttributes[row.typeName];
            // let deviceEditTypeData = [];
            // 把 deviceAttributes[row.typeName] 每一项处理后 push 到 this.deviceTypeEditForm.deviceFields 中
            this.deviceAttributes[row.typeName].forEach(item => {
                var fieldData = {};
                fieldData['attributename'] = item.field_name;
                fieldData['valuetype'] = item.type;
                fieldData['attrdescription'] = item.description;
                fieldData['controllable'] = item.controllable;
                if (item.type == "int" || item.type == "float") {
                    fieldData['minValue'] = item.min_value;
                    fieldData['maxValue'] = item.max_value;
                    fieldData['showMinMax'] = true;
                    fieldData['showEnum'] = false;
                }
                // item 如何处理
                else if (item.type == "enum") {
                    fieldData['itemTxt'] = JSON.stringify(item.item);
                    fieldData['showEnum'] = true;
                    fieldData['showMinMax'] = false;
                }
                console.log("fieldData: ", fieldData);
                this.deviceTypeEditForm.deviceFields.push(fieldData);
                console.log("this.deviceTypeEditForm.deviceFields: ", this.deviceTypeEditForm.deviceFields);
            })
            this.deviceTypeEditForm.deviceFields.shift();
            console.log("this.deviceTypeEditForm.deviceFields after shift: ", this.deviceTypeEditForm.deviceFields);

            this.editTypeVisible = true;
            console.log(this.idx)
        },

        saveEdit() {
            this.editTypeVisible = false;
            ElMessage.success(`修改第 ${this.idx + 1} 行成功`);
            // this.tableData[this.idx].typename = this.deviceTypeEditForm.typename;
            // this.tableData[this.idx].typedescription = this.deviceTypeEditForm.typedescription;
            // this.tableData[this.idx].permissionLevel = this.deviceTypeEditForm.permissionLevel;
            // this.tableData[this.idx].deviceFields = this.deviceTypeEditForm.deviceFields;
            let deviceTypeData = {}
            deviceTypeData['type_id'] = this.deviceTypeEditForm.typeId
            deviceTypeData['name'] = this.deviceTypeEditForm.typename
            deviceTypeData['description'] = this.deviceTypeEditForm.typedescription
            deviceTypeData['permissionLevel'] = this.deviceTypeEditForm.permissionLevel
            deviceTypeData['device_fields'] = []
            this.deviceTypeEditForm.deviceFields.forEach(item => {
                var fieldData = {}
                fieldData['type'] = item.valuetype
                fieldData['controllable'] = item.controllable
                fieldData['field_name'] = item.attributename
                fieldData['description'] = item.attrdescription
                if (item.valuetype == "int" || item.valuetype == "float") {
                    fieldData['min_value'] = item.minValue
                    fieldData['max_value'] = item.maxValue
                }
                else if (item.valuetype == "enum") {
                    fieldData['item'] = []
                    let enumItems = item.itemTxt.split(';')
                    enumItems.forEach(enumItem => {
                        var temp = enumItem.split(":")
                        fieldData['item'].push({ value: temp[0], description: temp[1] })
                    })
                }
                deviceTypeData.device_fields.push(fieldData)
            });
            console.log(deviceTypeData)
            // 无法传递带有数组的json对象，所以把这个json对象转换成string类型，再给他赋一个key 也就是{'data':字符串化的json对象}
            http.post("deviceTypeManager/editDeviceType", {
                // "type_id": this.tableData[this.idx].id,
                "type_id": deviceTypeData['type_id'],
                data: JSON.stringify(deviceTypeData)
            }).then((res) => {
                console.log(res)
                this.deviceTypeEditForm = {
                    typeId: null,
                    typename: '',
                    typedescription: '',
                    permissionLevel: null,
                    deviceFields: [
                        {
                            key: 1,
                            attributename: '',
                            valuetype: '',
                            attrdescription: '',
                            controllable: null,
                            minValue: null,
                            maxValue: null,
                            showMinMax: false,
                            showEnum: false,
                            item: [
                                {
                                    value: null,
                                    description: ''
                                }
                            ],
                            itemTxt: ''
                        },
                    ],
                };
                console.log('编辑成功！')
            }).catch((err) => {
                console.log(err)
            })
        },

        handleDelete(index) {
            // 二次确认删除
            ElMessageBox.confirm('确定要删除吗？', '提示', {
                type: 'warning'
            })
                .then(() => {

                    console.log("before post");
                    console.log(index)
                    console.log(this.tableData[index])
                    // console.log(this.tableData[index].typeId)
                    console.log(this.tableData[index].id)

                    http.post("deviceTypeManager/deleteType", { "id": this.tableData[index].id }).then(res => {
                        console.log("after post");
                        // console.log(res)
                        if (res.code == 200) {
                            // ElMessage.success('删除成功');
                            this.tableData.splice(index, 1);
                            // 这里需不需要再更新下页数呢？下面的 saveEdit 同理
                            // pageNum.value = tableData.value.length;
                            ElMessage({
                                showClose: true,
                                duration: 0,
                                message: '删除设备类型成功！',
                                type: 'success',
                            })
                        }
                        else {
                            ElMessage({
                                showClose: true,
                                duration: 0,
                                // message: res.message,
                                message: '删除设备类型失败',
                                type: 'error',
                            })
                        }
                    }).catch(err => {
                        console.log(err)
                    })
                })
                .catch((err) => { console.log(err) });
        }
    }
}
</script>
  

<style scoped>
.deviceTypeTable {
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