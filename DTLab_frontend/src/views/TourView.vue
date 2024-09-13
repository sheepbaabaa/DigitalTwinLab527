<template>
    <PersonComponents :PersonInfoVisible="PersonInfoVisible" :PersonData="PersonData"></PersonComponents>
    <MonitorComponents :MonitorVisible="MonitorVisible" :MonitorName="MonitorName"></MonitorComponents>
    <LightComponents :LightVisible="LightVisible" :LightName="LightName"></LightComponents>
    <AirConditionComponents :AirConditionVisible="AirConditionVisible" :AirConditionName="AirConditionName">
    </AirConditionComponents>
    <div style="position:absolute;top: 0px;left:0px;z-index:-1" id="WebGL-output">
    </div>

</template>
<style>
.peopleLabel {
    background-color: rgb(87, 96, 111, 0.5);
    border-radius: 2px;
    padding: 3px;
    font-size: 3px;
    color: #a3bbdb
}
</style>
<script>
import http from '@/utils/request/http.js'
import PersonComponents from '@/components/PersonComponents.vue'
import MonitorComponents from '@/components/MonitorComponents.vue'
import LightComponents from '@/components/LightComponents.vue'
import AirConditionComponents from '@/components/AirConditionComponents.vue'
import { searchObject } from '@/utils/SearchObject.js';
import * as THREE from 'three';
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import { GLTFExporter } from "three/examples/jsm/exporters/GLTFExporter.js";
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls'
import { TransformControls } from 'three/examples/jsm/controls/TransformControls.js';
import { DragControls } from 'three/examples/jsm/controls/DragControls.js';
import { FirstPersonControls } from 'three/examples/jsm/controls/FirstPersonControls.js'
import { CSS2DObject, CSS2DRenderer } from "three/examples/jsm/renderers/CSS2DRenderer"
import { ElMessage, linkProps } from 'element-plus';
import { RectAreaLightHelper } from 'three/examples/jsm/helpers/RectAreaLightHelper.js';
import { RectAreaLightUniformsLib } from 'three/examples/jsm/lights/RectAreaLightUniformsLib.js';
var beIntersectObjects = [];//用来存放需要射线检测的物体数组
var MemberList = [];//存放人物模型
var scene;//场景对象实例
var root;
var root_copy;
var labelGroup = new THREE.Group();
var peopleLabelRenderer; //人物label渲染器
var peopleLabelControls;
export default {
    name: 'TourView',
    components: {
        PersonComponents,
        MonitorComponents,
        LightComponents,
        AirConditionComponents,
    },
    data() {
        return {
            moduleFile: "/static/Lab.glb",
            camera: null, //相机实例
            renderer: null, //渲染器实例
            renderEnabled: true,

            mixer: null,//混合器实例
            clock: new THREE.Clock(),//时钟对象
            controls: "", //轨道控制器
            //点击
            raycaster: new THREE.Raycaster(),
            mouse: new THREE.Vector2(),
            container: "",
            timer: null,//定时器
            objectModal: null, //模型实例
            loading: true,
            personData: null,
            activeName: "first",//视图选择
            PersonInfoVisible: false,

            chooseComponent: null,
            MonitorVisible: false,
            MonitorName: null,
            LightVisible: false,
            LightName: null,
            AirConditionVisible: false,
            AirConditionName: null,
        };
    },
    created(){
        peopleLabelRenderer = new CSS2DRenderer()
        peopleLabelRenderer.domElement.style.pointerEvents = 'none';//重要！避免鼠标冲突
        this.runThree()
        this.animate()
        this.loadGltf()
        this.initEnv()
        window.addEventListener('resize', this.onWindowResize);
        console.log("whole scene", scene);
        console.log("beIntersectObjects", beIntersectObjects);
    },
    mounted() {
        // add the output of the renderer to the html element
        this.container = document.getElementById('WebGL-output');
        this.container.appendChild(this.renderer.domElement);//body元素中插入canvas对象
        // this.container.addEventListener('click', this.onMouseClick, false); //鼠标点击事件监听器
    },
    methods: {
        LightTest(){
            this.LightVisible =!this.LightVisible;
            this.LightName="Light001"
        },
        //增加人物Label
        addPeopleLabel(people, model) {
            var name_id = "Member" + people['member_id'].toString().padStart(3, '0')
            var peopleLabelDiv = document.createElement('div');
            peopleLabelDiv.className = 'peopleLabel';
            //peopleLabelDiv.style.color ='#139bf0';
            peopleLabelDiv.textContent = people['name'];
            var peopleLabel = new CSS2DObject(peopleLabelDiv);
            peopleLabel.name = name_id + "_label";//设置name
            peopleLabel.visible = people['visible'];
            peopleLabel.position.set(0, 5, 0);
            model.add(peopleLabel);
            peopleLabel.layers.set(0);
        },
        //人物Label渲染器初始化
        peopleLabelRendererInit() {
                peopleLabelRenderer.setSize(window.innerWidth, window.innerHeight);
                peopleLabelRenderer.domElement.style.position = "absolute";
                peopleLabelRenderer.domElement.style.top = 0;
                peopleLabelRenderer.domElement.id = "peopleLabels";
                console.log(peopleLabelRenderer.domElement)
                document.getElementById("WebGL-output").appendChild(peopleLabelRenderer.domElement);
                peopleLabelRenderer.render(scene, this.camera);
                peopleLabelControls = new OrbitControls(this.camera, peopleLabelRenderer.domElement);
            
        },
        //更改人物模型及其label可见性
        setMemberVisible(merberName, visible) {

            var temp = searchObject(root, merberName)
            temp.visible = visible;
            var tempLabel = searchObject(temp, (merberName + "_label"))
            tempLabel.visible = visible;
        },
        runThree() {
           
            scene = new THREE.Scene();
            this.camera = new THREE.PerspectiveCamera(63, window.innerWidth / window.innerHeight, 0.1, 1000);/////////////
            // position and point the camera to the center of the scene
            this.camera.position.set(-9, 1.7, 6); //设置相机位置
            this.camera.lookAt(0,1.7,0);
            this.renderer = new THREE.WebGLRenderer({ antialias: true });
            this.renderer.outputEncoding = THREE.sRGBEncoding;//rgb颜色
            this.renderer.setClearColor(new THREE.Color(0xeeeeee));//设置背景颜色
            this.renderer.setPixelRatio(window.devicePixelRatio);//清晰度
            this.renderer.setSize(window.innerWidth, window.innerHeight);
            this.renderer.shadowMapEnabled = true;//有阴影
            this.renderer.shadowMap.enabled = true;

            //奇怪，关掉这个轨道控制器，反而是对的了
            // //轨道控制器
            // this.controls = new OrbitControls(this.camera, this.renderer.domElement);
            // this.controls.enableDamping = true;
  
            this.controls = new FirstPersonControls( this.camera);
            this.controls.enabled = true;
            this.controls.lookSpeed = 0.02; //鼠标移动查看的速度
            this.controls.movementSpeed = 1; //相机移动速度
             this.controls.lookVertical= false;
            //  this.controls.constrainVertical = true; //约束垂直
            // this.controls.verticalMin = 1.0;
            // this.controls.verticalMax = 2.0;
            // this.controls.heightMax = 3;
            // this.controls.heightMin = 1;
            // this.controls.heightCoef = 0;
            // this.controls.heightSpeed = true;
            this.controls.lon = 0; //进入初始视角x轴的角度
            this.controls.lat = 0; //初始视角进入后y轴的角度

        },
        animate() {
            //this.controls.update()
            
            this.renderer.render(scene, this.camera)
            peopleLabelRenderer.render(scene, this.camera)
            requestAnimationFrame(this.animate)
            var time = this.clock.getDelta();
            this.controls.update(time);
            // if (this.mixer) {
            //     this.mixer.update(time);
            // }
        },
        loadGltf() {

            const gltfLoader = new GLTFLoader()
            gltfLoader.load(this.moduleFile, (gltf) => {
                root = gltf.scene.children[0];//注意！！！为了保持层级不变，gltf最外空一层
                console.log(root)
                //root = gltf.scene;
                gltf.scene.name = "LabScene";
                console.log("gltf.scene.children", gltf.scene.children)
                //beIntersectObjects.push(gltf.scene.children);
                root.scale.set(1, 1, 1);
                root.position.set(0, 0, 0);
                root.castShadow = true;
                root.traverse(function (child) {
                    if (child.isMesh) {
                        child.frustumCulled = false;
                        //模型阴影
                        child.castShadow = true;
                        //材质
                        child.material.side = THREE.FrontSide;
                        if (child.name.substr(0, 4) == "hole") {
                            child.visible = false;
                        }
                        if (child.name.substr(0, 5) == "floor") {
                            child.receiveShadow = true;
                        }
                        // if (child.name == "ceiling") { //只在游览视图中显示
                        //     child.visible = false;
                        // }
                    }
                    if (child.name == "Person") {
                        MemberList.push(child.children);
                    }

                })
                
                scene.add(root) //scene: soptlight + root
                // 调用动画
                this.mixer = new THREE.AnimationMixer(root);
                // var action = this.mixer.clipAction(gltf.animations[0]);
                // action.setLoop(THREE.LoopOnce);
                // action
                // .stop()
                // .setDuration(4)
                // .play();
                http.get("person/getAllStaff").then(res => {
                    res.forEach(staff => {
                        var name = "Member" + this.$store.state[staff.nameEn].member_id.toString().padStart(3, '0')
                        this.setMemberVisible(name, this.$store.state[staff.nameEn].visible);
                        //为人物增加标签
                        this.addPeopleLabel(this.$store.state[staff.nameEn], searchObject(root, name));
                    });
                    this.peopleLabelRendererInit()
                    this.PersonData = this.$store.getters.allPerson;
                }).catch(err => {
                    console.log(err)
                })

            })
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

            var lightpos = [
                [-8.7, 3.7, -4],
                [-5.7, 3.7, -4],
                [-2.7, 3.7, -4],
                [1.7, 3.7, -4],
                [4.7, 3.7, -4],
                [7.7, 3.7, -4],
                [-8.7, 3.7, 0],
                [-5.7, 3.7, 0],
                [-2.7, 3.7, 0],
                [1.7, 3.7, 0],
                [4.7, 3.7, 0],
                [7.7, 3.7, 0],
                [-8.7, 3.7, 4],
                [-5.7, 3.7, 4],
                [-2.7, 3.7, 4],
                [1.7, 3.7, 4],
                [4.7, 3.7, 4],
                [7.7, 3.7, 4]
            ];

            var group = new THREE.Group();//声明组容器
            group.name = "Set_ThreejsLight";
            scene.add(group);

            const rectLight = [];
            var BoxGeometry = new THREE.BoxGeometry(1, 0.05, 1);
            var planeMaterial = new THREE.MeshBasicMaterial( { color: 0xffffff});

            rectLight.push(new THREE.Mesh(BoxGeometry, planeMaterial))
            rectLight[0].position.set(lightpos[0][0], lightpos[0][1]-0.1, lightpos[0][2]);
            rectLight[0].name = "Light000"
            group.add(rectLight[0]);
            //plane.visible  = false;

            for (let i = 1; i < 18; i++) {
                rectLight.push(rectLight[0].clone())
                rectLight[i].position.set(lightpos[i][0], lightpos[i][1]-0.1, lightpos[i][2]);
                rectLight[i].name = "Light" + i.toString().padStart(3, '0');
                group.add(rectLight[i]);
            }

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
        // onMouseClick(event) {
        //     // 将鼠标位置归一化为设备坐标。x 和 y 方向的取值范围是 (-1 to +1)
        //     this.mouse.x = (event.clientX / this.container.clientWidth) * 2 - 1;
        //     this.mouse.y = -(event.clientY / this.container.clientHeight) * 2 + 1;
        //     this.raycaster.setFromCamera(this.mouse, this.camera);
        //     // 计算物体和射线的焦点
        //     let intersects = this.raycaster.intersectObjects(beIntersectObjects, true);
        //     //let intersects = this.raycaster.intersectObjects(scene.children, true);
        //     // 获取选中最近的 Mesh 对象
        //     //if (intersects.length !== 0 && intersects[0].object instanceof THREE.Mesh) {
        //     if (intersects.length !== 0) {
        //         let selectObjectName = intersects[0].object.name;
        //         console.log("CLICK!", intersects[0].object);
        //         const object = { selectObjectName }
        //         if(selectObjectName.substr(0, 12)=='AirCondition'){
        //             this.clickAirCondition(intersects[0].object);
        //         }
        //         else if(selectObjectName.substr(0, 14)=='ComputerScreen'){
        //             this.clickMonitor(intersects[0].object);
        //         }
        //         else if(selectObjectName.substr(0, 5)=='Light'){
        //             this.clickLight(intersects[0].object);
        //         }
        //     }
        // },
        onWindowResize() {
            this.camera.aspect = window.innerWidth / window.innerHeight;
            this.camera.updateProjectionMatrix();
            this.renderer.setSize(window.innerWidth, window.innerHeight);
            peopleLabelRenderer.setSize(window.innerWidth, window.innerHeight);
            this.controls.handleResize();
        },
        // clickPersonComponents() {
        //     console.log("PersonInfoVisible", this.PersonInfoVisible);
        //     this.PersonInfoVisible = !this.PersonInfoVisible;
        //     console.log("PersonInfoVisible", this.PersonInfoVisible);
        // },
        //操作菜单部分
        // chooseComponentResponse() {
        //     console.log("chooseComponentResponse")
        //     switch (this.chooseComponent) { //想要判断的变量
        //         case '1':
        //             this.clickMonitorComponents();
        //             break
        //         case '2':
        //             this.clickLightComponents();
        //             break
        //         case '3':
        //             this.clickAirConditionComponents();
        //             break
        //     }
        // },
        // //屏幕
        // clickMonitorComponents() {
        //     beIntersectObjects = [];
        //     root.traverse(function (child) {
        //         if (child.isMesh && child.name.substr(0, 14) == "ComputerScreen") {
        //             beIntersectObjects.push(child);
        //         }
        //     })
        //     console.log("beIntersectObjects", beIntersectObjects);
        // },
        // clickMonitor(chooseMonitor) {
        //     console.log("clickMonitor");
        //     this.MonitorVisible = !this.MonitorVisible;
        //     this.MonitorName = "Monitor" + chooseMonitor.name.substr(14, 3);//"Monitor"+id,用作vuex注册
        // },
        // setMonitor(power) {
        //     console.log("setMonitor(power)");
        //     var screen = scene.getObjectByName("ComputerScreen" + this.MonitorName.substr(7, 3) + "_2");//scren mesh
        //     if (power == "1")
        //         screen.material = new THREE.MeshBasicMaterial({ color: 0xffffff });
        //     else if (power == "0")
        //         screen.material = new THREE.MeshBasicMaterial({ color: 0x000000 });
        // },
        // closeMonitor() {
        //     this.MonitorVisible = !this.MonitorVisible;
        //     this.MonitorName = "";
        // },
        // //灯光
        // clickLightComponents() {
        //     beIntersectObjects = [];
        //     var group = scene.getObjectByName("Set_ThreejsLight");
        //     group.traverse(function (child) {
        //         if (child.name.substr(0, 5) == "Light") {
        //             beIntersectObjects.push(child);
        //         }
        //     })
        //     console.log("beIntersectObjects", beIntersectObjects);
        // },
        // clickLight(chooseLight) {
        //     console.log("clickLight");
        //     this.LightVisible = !this.LightVisible;
        //     this.LightName = chooseLight.name;//"chooseLight"+id,用作vuex注册
        // },
        // setLight(power) {
        //     console.log("setchooseLight(power)");
        //     var light = scene.getObjectByName(this.LightName);
        //     if (power == "1")
        //         light.material = new THREE.MeshBasicMaterial({ color: 0xffffff , wireframe: true });
        //     else if (power == "0")
        //         light.material = new THREE.MeshBasicMaterial({ color: 0x000000 , wireframe: true });
        // },
        // closeLight() {
        //     this.LightVisible = !this.LightVisible;
        //     this.LightName = "";
        // },


        // //空调
        // clickAirConditionComponents() {
        //     beIntersectObjects = [];
        //     root.traverse(function (child) {
        //         if (child.name.substr(0, 12) == "AirCondition") {
        //             beIntersectObjects.push(child);
        //         }
        //     })
        //     console.log("beIntersectObjects", beIntersectObjects);
        // },
        // clickAirCondition(chooseAirCondition) {
        //     console.log("clickAirCondition");
        //     this.AirConditionVisible = !this.AirConditionVisible;
        //     this.AirConditionName = chooseAirCondition.name;
        // },
        // closeAirCondition() {
        //     this.AirConditionVisible = !this.AirConditionVisible;
        //     this.AirConditionName = "";
        // },
        getObject(name){
            return scene.getObjectByName(name)
        }
    }
}
</script>
<style>
.demo-tabs>.el-tabs__content {
    color: #6b778c;
    font-size: 32px;
    font-weight: 600;
}

.box-card3 {
    opacity: 0.8;
    pointer-events: none;
    margin-right: 10px;
    width: 120px;
}
</style>