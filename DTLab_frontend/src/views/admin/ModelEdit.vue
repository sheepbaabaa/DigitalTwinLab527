<template>
    <div style="position:absolute;top: 0px;left:0px;z-index:-1" id="WebGL-output">

    </div>

    <el-card class="box-card2" modal="false" :close-on-click-modal="false">

        <el-row>
            <el-col :span="12">
                <el-button type="primary" @click="handleSave()" class="pointerAble" style="width: 90%">保存模型</el-button>
            </el-col>

            <el-col :span="12">
                <el-button @click="handleClose()" class="pointerAble" style="width: 90%">撤销</el-button>
            </el-col>
        </el-row>

        <el-row>
            <el-col :span="12">{{chooseObjName}}</el-col>
            <el-col :span="12">
                <el-button @click="eraseDrag" class="pointerAble" style="width: 90%">切换</el-button>
            </el-col>
        </el-row>

        <el-row>
            <el-col :span="12">
                <el-button @click="move" class="pointerAble" style="width: 90%">移动</el-button>
            </el-col>
            <el-col :span="12">
                <el-button @click="rotate" class="pointerAble" style="width: 90%">旋转</el-button>
            </el-col>
        </el-row>

        <el-row>
            <el-col :span="12">
                <el-button @click="clone" class="pointerAble" style="width: 90%">复制</el-button>
            </el-col>
            <el-col :span="12">
                <el-button @click="delete" class="pointerAble" style="width: 90%">删除</el-button>
            </el-col>
        </el-row>

    </el-card>



</template>

<script>
// load gltf , edit model
import { ElMessage } from 'element-plus';
import * as THREE from 'three';
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import { GLTFExporter } from "three/examples/jsm/exporters/GLTFExporter.js";
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'
import { TransformControls } from 'three/examples/jsm/controls/TransformControls.js';
import axios from 'axios'
import { RectAreaLightHelper } from 'three/examples/jsm/helpers/RectAreaLightHelper.js';
import { RectAreaLightUniformsLib } from 'three/examples/jsm/lights/RectAreaLightUniformsLib.js';
var scene;
var root;
var root_copy;
var transformControl;
var beIntersectObjects = [];//用来存放需要射线检测的物体数组
var controls; //轨道控制器
export default {
    name: 'EditModel',
    data() {
        return {
            EditBasicVisible: false,
            moduleFile: "/static/Lab.glb",
            camera: null, //相机实例
            renderer: null, //渲染器实例
            renderEnabled: true,
            //点击
            raycaster: new THREE.Raycaster(),
            mouse: new THREE.Vector2(),
            container: "",
            chooseObjName: null,
            box:{//orbit范围
                min: {
                x: -30,
                y: 0,
                z: -5,
                },
                max: {
                x: 20,
                z: 20,
                },
            },
        }
    },
    mounted() {
        //init
        this.runThree()
        this.animate()
        this.initEnv()
        window.addEventListener('resize', this.onWindowResize);
        //add model
        this.loadGltf()
        console.log("whole scene", scene);
        this.initDrag();
        //this.initTransformControls();
    },
    methods: {
        runThree() {
            this.container = document.getElementById('WebGL-output');
            scene = new THREE.Scene();
            this.camera = new THREE.PerspectiveCamera(63, window.innerWidth / window.innerHeight, 0.1, 1000);/////////////
            // position and point the camera to the center of the scene
            this.camera.position.set(-15, 6, 10); //设置相机位置
            this.camera.lookAt(scene.position);
            this.renderer = new THREE.WebGLRenderer({ antialias: true });
            this.renderer.outputEncoding = THREE.sRGBEncoding;//rgb颜色
            this.renderer.setClearColor(new THREE.Color(0xeeeeee));//设置背景颜色
            this.renderer.setPixelRatio(window.devicePixelRatio);//清晰度
            this.renderer.setSize(window.innerWidth, window.innerHeight);
            this.renderer.shadowMapEnabled = true;//有阴影
            this.renderer.shadowMap.enabled = true;
            // add the output of the renderer to the html element
            this.container.appendChild(this.renderer.domElement);//body元素中插入canvas对象
            this.container.addEventListener('click', this.onMouseClick, false); //鼠标点击事件监听器
            //奇怪，关掉这个轨道控制器，反而是对的了
            //轨道控制器
            controls = new OrbitControls(this.camera, this.renderer.domElement);
            controls.enableDamping = true;
            //this.controls.addEventListener( 'change', this.render() );
            controls.maxPolarAngle = Math.PI / 2;
        },
        animate() {
            controls.update()
            this.renderer.render(scene, this.camera)
            requestAnimationFrame(this.animate)
            
            if (this.camera.position.x > this.box.max.x||this.camera.position.x < this.box.min.x) {
                controls.reset();
            } else if (this.camera.position.z > this.box.max.z||this.camera.position.z < this.box.min.z) {
                controls.reset();
            } else if (this.camera.position.y < this.box.min.y) {
                controls.reset();
            } else {
                controls.saveState();
            }
        },
        initEnv() {
            //根据昼夜光线调整点光源
            //环境光线,强度随时间改变
            const envLight = new THREE.AmbientLight( 0x404040,1 ); //
            scene.add( envLight );
            //实验室光线，强度随灯光开关改变
            var labLight = new THREE.DirectionalLight( 0xffffff, 0.5 );
            labLight.position.set(-10, 50, 10);
            //labLight.castShadow = true;
            scene.add(labLight);
            // var lightpos = [
            //     [-8.7, 3.7, -4],
            //     [-5.7, 3.7, -4],
            //     [-2.7, 3.7, -4],
            //     [1.7, 3.7, -4],
            //     [4.7, 3.7, -4],
            //     [7.7, 3.7, -4],
            //     [-8.7, 3.7, 0],
            //     [-5.7, 3.7, 0],
            //     [-2.7, 3.7, 0],
            //     [1.7, 3.7, 0],
            //     [4.7, 3.7, 0],
            //     [7.7, 3.7, 0],
            //     [-8.7, 3.7, 4],
            //     [-5.7, 3.7, 4],
            //     [-2.7, 3.7, 4],
            //     [1.7, 3.7, 4],
            //     [4.7, 3.7, 4],
            //     [7.7, 3.7, 4]
            // ];
            // var group = new THREE.Group();//声明组容器
            // group.name = "Set_ThreejsLight";
            // scene.add(group);
            // const rectLight = [];
            // var BoxGeometry = new THREE.BoxGeometry(1, 0.01, 1);
            // var planeMaterial = new THREE.MeshBasicMaterial( { color: 0xffffff, wireframe: true });
            // rectLight.push(new THREE.Mesh(BoxGeometry, planeMaterial))
            // rectLight[0].position.set(lightpos[0][0], lightpos[0][1], lightpos[0][2]);
            // rectLight[0].name = "Light000"
            // group.add(rectLight[0]);
            // //plane.visible  = false;
            // for (let i = 1; i < 18; i++) {
            //     rectLight.push(rectLight[0].clone())
            //     rectLight[i].position.set(lightpos[i][0], lightpos[i][1]-0.1, lightpos[i][2]);
            //     rectLight[i].name = "Light" + i.toString().padStart(3, '0');
            //     group.add(rectLight[i]);
            // }
            //根据天气调整天空盒
            //skybox changed with weather
            var urls1 = [
                "/static/skybox/morning/posx.jpg",
                "/static/skybox/morning/negx.jpg",
                "/static/skybox/morning/posy.jpg",
                "/static/skybox/morning/negy.jpg",
                "/static/skybox/morning/posz.jpg",
                "/static/skybox/morning/negz.jpg"
            ];
            var urls2 = [
                "/static/skybox/afternoon/posx.jpg",
                "/static/skybox/afternoon/negx.jpg",
                "/static/skybox/afternoon/posy.jpg",
                "/static/skybox/afternoon/negy.jpg",
                "/static/skybox/afternoon/posz.jpg",
                "/static/skybox/afternoon/negz.jpg"
            ];
            var urls3 = [
                "/static/skybox/sunset/posx.jpg",
                "/static/skybox/sunset/negx.jpg",
                "/static/skybox/sunset/posy.jpg",
                "/static/skybox/sunset/negy.jpg",
                "/static/skybox/sunset/posz.jpg",
                "/static/skybox/sunset/negz.jpg"
            ];
            var urls4 = [
                "/static/skybox/night/posx.jpg",
                "/static/skybox/night/negx.jpg",
                "/static/skybox/night/posy.jpg",
                "/static/skybox/night/negy.jpg",
                "/static/skybox/night/posz.jpg",
                "/static/skybox/night/negz.jpg"
            ];
            var urls5 = [
                "/static/skybox/fog/posx.jpg",
                "/static/skybox/fog/negx.jpg",
                "/static/skybox/fog/posy.jpg",
                "/static/skybox/fog/negy.jpg",
                "/static/skybox/fog/posz.jpg",
                "/static/skybox/fog/negz.jpg"
            ];
            var cubeLoader = new THREE.CubeTextureLoader();
            scene.background = cubeLoader.load(urls5);
        },
        onWindowResize() {
            this.camera.aspect = window.innerWidth / window.innerHeight;
            this.camera.updateProjectionMatrix();
            this.renderer.setSize(window.innerWidth, window.innerHeight);
        },
        loadGltf() {
            const gltfLoader = new GLTFLoader()
            gltfLoader.load(this.moduleFile, (gltf) => {
                root = gltf.scene.children[0];//注意！！！为了保持层级不变，gltf最外空一层
                console.log(root)
                gltf.scene.name = "LabScene";
                root.scale.set(1,1,1);
                root.position.set(0,0,0);
                root.castShadow = true;
                root.traverse(function (child) {
                    if (child.isMesh) {
                        child.frustumCulled = false;
                        //模型阴影
                        child.castShadow = true;
                        //材质
                        child.material.side = THREE.FrontSide;
                        if (child.name.substr(0, 5) == "floor") {
                            child.receiveShadow = true; 
                        }
                        if (child.name.substr(0, 4) == "hole"||child.name == "ceiling" || child.name.substr(0, 4) =="door") { //只在游览视图中显示
                            child.visible = false;
                        }
                    }
                    if(child.name == "Person")
                    {
                      child.visible = false;
                    }
                    //set下的子对象为可点击物体
                    if (child.parent && child.parent.name.substr(0, 3) == "Set"){
                            beIntersectObjects.push(child);
                        }
                })
                scene.add(root) //scene: soptlight + root
            })
            console.log("beIntersectObjects",beIntersectObjects)
        },
        onMouseClick(event) {
            // 将鼠标位置归一化为设备坐标。x 和 y 方向的取值范围是 (-1 to +1)
            this.mouse.x = (event.clientX / this.container.clientWidth) * 2 - 1;
            this.mouse.y = -(event.clientY / this.container.clientHeight) * 2 + 1;
            this.raycaster.setFromCamera(this.mouse, this.camera);
            // 计算物体和射线的焦点
            let intersects = this.raycaster.intersectObjects(beIntersectObjects, true);
            //let intersects = this.raycaster.intersectObjects(scene.children, true);
            // 获取选中最近的 Mesh 对象
            // if (intersects.length !== 0 && intersects[0].object instanceof THREE.Mesh) {
            //   console.log(intersects[0].object.name)
            //   this.attachDrag(intersects[0].object);
            // }
            if (intersects.length !== 0) {
                console.log(intersects[0].object.name)
                this.attachDrag(intersects[0].object);
            }
        },
        //transformControl 控制模型移动旋转,
        //初始化
        initDrag() {
            transformControl = new TransformControls(this.camera, this.renderer.domElement);
            //transformControl.setMode('rotate')//旋转
            //transformControl.addEventListener( 'change', this.render() );
            transformControl.addEventListener('dragging-changed', function (event) {
                console.log("dragging-changed", controls)
                controls.enabled = false;
            });
            scene.add(transformControl);//控件对象添加到场景对象
        },
        //由onMouseClick函数选择attach对象
        attachDrag(obj) {
            //为多个mesh对象的，指向group
            if(obj.parent.name.substr(0, 3) != "Set")
                obj = obj.parent;
            transformControl.attach(obj);
            console.log("attach", scene, obj);
            this.container.removeEventListener('click', this.onMouseClick, false);
            this.chooseObjName = obj.name;
        },
        //由按钮控制
        eraseDrag() {
            console.log("detach", transformControl.object);
            transformControl.detach(transformControl.object);
            controls.enabled = true;
            this.container.addEventListener('click', this.onMouseClick, false);
            this.chooseObjName = "";
        },
        move() {
            transformControl.setMode('translate')
        },
        rotate() {
            transformControl.setMode('rotate')//旋转
        },
        clone() {
            var item = transformControl.object.clone();
            transformControl.object.parent.add(item);
            transformControl.object.parent.add(item);
            this.attachDrag(item)
        },
        delete() {
            var item = transformControl.object;
            console.log("deleteObj name", item.name)
            this.eraseDrag(item)
            item.parent.remove(item);
        },
        //可用
        saveGlbModel(filename) {//eg filename = 'Lab_add.glb';
            this.igltfexporter = new GLTFExporter();
            const options = {
                //true导出位置、缩放、旋转变换，false导出节点的矩阵变换
                trs: false,
                //是否只导出可见的
                onlyVisible: false,
                truncateDrawRange: true,
                //是否二进制，true导出glb模型，false导出gltf模型
                binary: true,
                //最大贴图尺寸
                maxTextureSize: Infinity,
            };
            this.igltfexporter.parse(
                root,
                function (result) {
                    if (result instanceof ArrayBuffer) {
                        console.log('scene.glb');
                        var blob = new Blob([result], { type: 'application/octet-stream' });
                        var formData = new FormData()
                        formData.append('modelFile', blob);
                        var url = null
                        if (process.env.VUE_APP_HOST == "dtlab.qylh.xyz:9003") {
                            url = "https://dtlab.qylh.xyz/dtlab/model/uploadModelFile"
                        }
                        else {
                            url = 'http://' + process.env.VUE_APP_HOST  + '/dtlab/model/uploadModelFile'
                        }
                        axios({
                            method: 'post',
                            url: url,
                            data: formData,
                            headers: {
                                'Content-Type': 'multipart/form-data'
                            },
                            withCredentials: true
                        }).then(res => {
                            console.log(res.data)
                        })
                            .catch(e => {
                                console.log(e)
                            })
                        // var link = document.createElement( 'a' );
                        // link.style.display = 'none';
                        // document.body.appendChild( link ); 
                        // link.href = URL.createObjectURL( blob );
                        // link.download = filename;
                        // console.log(link)
                        //link.click();
                    } else {
                    }
                },
                function (error) {
                    console.log('An error happened during parsing', error);
                },
                options
            );
        },
        //可用
        cloneObj(EditData) {
            console.log("cloneObj.objPath", EditData.objPath);
            var aimItem = scene, addItem;
            for (let i = 0; i < EditData.objPath.length; i++) {
                aimItem = aimItem.children[EditData.objPath[i]];
            }
            addItem = aimItem.clone();
            var NameLength = aimItem.name.length - 3;
            var NameIndex = aimItem.parent.children.length;
            addItem.name = aimItem.name.substring(0, NameLength) + NameIndex.toString().padStart(3, '0')
            console.log("cloneObj.addItem.name", addItem.name);
            //addItem.position.set(EditData.tx,EditData.ty,EditData.tz);
            addItem.position.set(aimItem.position.x + 2, aimItem.position.y, aimItem.position.z);
            aimItem.parent.add(addItem);
            console.log("cloneObj After", scene);
        },
        render() {
            this.renderer.render(scene, this.camera);
        },
        handleSave() {
            this.igltfexporter = new GLTFExporter();
            const options = {
                //true导出位置、缩放、旋转变换，false导出节点的矩阵变换
                trs: false,
                //是否只导出可见的
                onlyVisible: false,
                truncateDrawRange: true,
                //是否二进制，true导出glb模型，false导出gltf模型
                binary: true,
                //最大贴图尺寸
                maxTextureSize: Infinity,
            };
            this.igltfexporter.parse(
                root,
                function (result) {
                    if (result instanceof ArrayBuffer) {
                        console.log('scene.glb');
                        var blob = new Blob([result], { type: 'application/octet-stream' });
                        var formData = new FormData()
                        formData.append('modelFile', blob);
                        var url = null
                        if (process.env.VUE_APP_HOST == "dtlab.qylh.xyz:9003") {
                            url = "https://dtlab.qylh.xyz/dtlab/model/uploadModelFile"
                        }
                        else {
                            url = 'http://' + process.env.VUE_APP_HOST + '/dtlab/model/uploadModelFile'
                        }
                        axios({
                            method: 'post',
                            url: url,
                            data: formData,
                            headers: {
                                'Content-Type': 'multipart/form-data'
                            },
                            withCredentials: true
                        }).then(res => {
                            console.log("uploaded", res.data)
                        })
                            .catch(e => {
                                console.log("error", e)
                            })
                        // var link = document.createElement( 'a' );
                        // link.style.display = 'none';
                        // document.body.appendChild( link ); 
                        // link.href = URL.createObjectURL( blob );
                        // link.download = filename;
                        // console.log(link)
                        //link.click();
                    } else {
                    }
                },
                function (error) {
                    console.log('An error happened during parsing', error);
                },
                options
            );
        },
        handleClose() {
        },
    }
}
</script>

<style>
.demo-tabs>.el-tabs__content {
    color: #6b778c;
    font-size: 32px;
    font-weight: 600;
}
.dialog {
    opacity: 0.5;
    pointer-events: none;
    margin: 0;
}
.box-card2 {
    opacity: 0.6;
    pointer-events: none;
    width: 260px;
}
.pointerAble {
    pointer-events: auto;
}
.el-row {
    margin-bottom: 20px;
}
.el-row:last-child {
    margin-bottom: 0;
}
.el-col {
    border-radius: 4px;
}
</style>


<!--  </script>
 <style>
   #three {
     width: 100%;
     height: 100%;
     position: center;
     left: 0;
     top: 0;
   }
 </style> -->
