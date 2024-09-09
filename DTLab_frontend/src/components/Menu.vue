<template >
    <el-menu  v-if="showNav" default-active="2" class="el-menu-vertical-demo" :collapse="isCollapse" @open="handleOpen"
        @close="handleClose">
        <div id="userHeader">
            <img :src="headerUrl"  @click="routerLinkTo('/UserCenter')" style="border-radius: 3px;"/>
            <p v-show="!this.isCollapse">{{ userName }}<span><i id="logoutIcon" :class="['icon', 'iconfont', 'icon-tuichu']" @click="logout"></i></span></p>
        </div>
        <template v-for="item in routes">
            <el-menu-item v-if="!item.meta.hasChildren & item.meta.show & complyWithPermissions(item.meta.accessLevel)" :index="item.meta.id" :key="item.meta.id"
                @click="routerLinkTo(item.path)">
                <i :class="['icon', 'iconfont', item.meta.icon]"></i><span>{{ item.name }}</span>
            </el-menu-item>
            <el-sub-menu v-if="item.meta.hasChildren & complyWithPermissions(item.meta.accessLevel)" :index="item.meta.id" :key="item.meta.id">
                <template #title>
                    <i :class="['icon', 'iconfont', item.meta.icon]"></i>
                    <span>{{ item.name }}</span>
                </template>
                <template v-for="children in item.children">
                    <el-menu-item v-if="children.meta.show & complyWithPermissions(item.meta.accessLevel)" :index="children.meta.id" :key="children.meta.id"
                        @click="routerLinkTo(children.path)">
                        <i :class="['icon', 'iconfont', children.meta.icon]"></i><span>{{
                                children.name
                        }}</span>
                    </el-menu-item>
                </template>
            </el-sub-menu>
        </template>
        <el-footer style="text-align:right;position:absolute;bottom:10px;width:100%" @click="changeCollapse()" >
            <i style="color:#3498db;font-size:20px;position: relative;" :class="['icon', 'iconfont', collapseIcon]"></i>
        </el-footer>
    </el-menu>
</template>
<script>
import http from '@/utils/request/http'
import { useRouter, useRoute } from 'vue-router'
export default {
    data() {
        return {
            routes: null,
            collapseIcon:'icon-shouqi',
            showNav: (this.$route.path != "/"),
            isCollapse: false,
            userName:null,

        }
    }, 
    computed: {
        headerUrl(){
            return this.$cookies.get("headerUrl");
        },
    },
    methods: {
        complyWithPermissions(accessLevel){
            if(accessLevel==0){
                return true;
            }
            return this.$cookies.isKey('userId') && this.$cookies.get("userType") >=accessLevel
        },
        routerLinkTo(path) {
            this.$router.push(path)
        },
        changeCollapse(){
            this.isCollapse = !this.isCollapse
            this.collapseIcon = this.isCollapse ? 'icon-zhankai' :'icon-shouqi'
        },
        logout(){
            http.get("logout").then((res)=>{
                console.log(res);
                //清除cookie
                this.$cookies.remove("headerUrl")
                this.$cookies.remove("userType")
                this.$cookies.remove("userId")
                this.$cookies.remove("username")
                this.routerLinkTo("/")
            })
            
        }
    },
    updated() {
        this.userName = this.$cookies.isKey("username") ? this.$cookies.get("username"):"游客"
        const router = useRouter()
        this.routes = router.options.routes
        //路由守卫
        this.$router.beforeEach((to, from) => {
            if(!this.complyWithPermissions(to.meta.accessLevel)){
                //无权限跳转到首页
               this.$router.push('/')
               return false;
            }
        })
    },
    watch: {
        $route(to, from) {
            this.showNav = (to.path != "/")
        }
    },
}
</script>
<style>
#userHeader{
    padding-top: 25px;
    margin-bottom: 10px;
    
}
#userHeader > img{
    border-style: solid;
    border-width:1px;
    border-radius: 0.5px;
    cursor: pointer;

}
.el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
    height: 100vh;
    z-index: 2;
}

.el-menu-vertical-demo {
    min-height: 400px;
    height: 100vh;
    z-index: 2;
}

.router-link-active {
    text-decoration: none;
}


.icon,
.iconfont {
    font-family: "iconfont" !important;
    padding-right: 5px;
    font-style: normal;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: 0.2px;
    -moz-osx-font-smoothing: grayscale;
}

#logoutIcon{
    padding-left: 5px;
    cursor: pointer;
    color: #ff7f50;
}
</style>