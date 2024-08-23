import { ElMessage } from 'element-plus'


export default class websockConnect {

    websock;
    url;
    LightChangeFun;
    LightChangeFun = function () { console.log("函数指针success") };
    constructor(url = "ws://127.0.0.1:8080/dtlab/ws/webClient/") {
        this.url = url
    }
    setUrl(url) {
        this.url = url;
    }
    getwebsocket() {
        return this.websock;
    }
    start() {
        //检查浏览器是否支持websocket
        if (typeof (WebSocket) === 'undefined') {
            ElMessage.error('您的浏览器不支持WebSocket，无法获取数据')
            return false
        }
        this.websock = new WebSocket(this.url)
        //默认处理方法
        this.websock.onmessage = this.webSocketOnMessage
        this.websock.onopen = this.webSocketOnOpen
        this.websock.onerror = this.webSocketOnError
        this.websock.onclose = this.webSocketOnClose
    }
    // 关闭ws连接
    webSocketOnClose(e) {
        console.log("websocket关闭连接")
        console.log(e)
    }
    // 建立ws连接
    webSocketOnOpen(e) {

    }

    // 连接出错
    webSocketOnError(e) {
        ElMessage({
            message: "websocket连接出错",
            type: 'error',
            duration: 3 * 1000
        })
        console.log(e)
    }

    //收到消息
    webSocketOnMessage(e) {
        console.log("收到消息:", e)
        var data = JSON.parse(e.data);
        if (data.response == "response_light_state") {
            var event = new CustomEvent('light_change', { "detail": data });
            this.dispatchEvent(event);
        }
        else if (data.response == "response_aircodition_state") {
            var event = new CustomEvent('AirCondition_change', { "detail": data });
            this.dispatchEvent(event);
        }
        else if (data.response == "response_monitor_state") {
            var event = new CustomEvent('monitor_change', { "detail": data });
            this.dispatchEvent(event);
        }
    }

    webSocketSend(msg) {
        if (this.websock.readyState === this.websock.OPEN) {
            this.websock.send(JSON.stringify(msg))
        } else if (this.websock.readyState === this.websock.CONNECTING) {
            // 若是 正在开启状态，则等待1s后重新调用
            setTimeout(() => {
                this.webSocketSend(msg);
            }, 1000);
        } else {
            // 若未开启 ，则等待1s后重新调用
            setTimeout(() => {
                this.webSocketSend(msg);
            }, 1000);
        }
    }

    webSocketClose() {
        this.websock.close()
    }

}

