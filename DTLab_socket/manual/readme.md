# DTLab

- 通信方式：前端与服务器通过应用层协议**WebSocket**全双工实时通信
- 基本功能：
  - 注册与登录
  - 登录后前端可通过网页查看物理世界的设备状态等信息，并实时接收更新后的信息
  - 通过网页控制真实设备

---

## 1. 注册与登录

### 1. 1 注册

- [register](./com/mobinets/digitaltwinlab/controller/LoginController.html): POST方法，path="/register"

参数: ([String](https://docs.oracle.com/en/java/javase/18/docs/api/java.base/java/lang/String.html) **username**, [String](https://docs.oracle.com/en/java/javase/18/docs/api/java.base/java/lang/String.html) **password**, [Long](https://docs.oracle.com/en/java/javase/18/docs/api/java.base/java/lang/Long.html) **campusNum**, [String](https://docs.oracle.com/en/java/javase/18/docs/api/java.base/java/lang/String.html) **email**)

> - 注册页面

### 1.2 登录

- [login](./com/mobinets/digitaltwinlab/controller/LoginController.html): POST方法, path="/login"

参数:(String **username**, String **password**, Boolean **remember me**, HttpServletResponse response)

> - 登录页面
> - 跳转注册页面
> - 跳转数字孪生界面/个人管理界面

## 2. WebSocket 实时通信



html页面基本函数

> openWebSocket.onopen
>
> openWebSocket.onmessage -> send Message
>
> openWebSocket.onerror
>
> openWebSocket.onclose
>
> closeWebsocket
>
> **sendMessage**
>
> sendInstruction



