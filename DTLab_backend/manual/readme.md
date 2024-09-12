# DTLab

- 通信方式：前端与服务器通过应用层协议**WebSocket**全双工实时通信
- 基本功能：
  - 注册与登录
  - 登录后前端可通过网页实时查看物理世界的设备状态等信息
  - 通过网页交互按钮，控制真实设备
- 服务器地址(需连接612局域网): 192.168.0.191:8080/dtlab

---



## 1. 注册与登录

### 1. 1 注册

> 地址:  /register
>
> 方法：**post**
>
> 参数:  (String **username**, String **password**, Long **campusNum**, String **email**) 
>
> 备注：campusNum是学号，页面填写表单时进行**数据校验**（格式）



### 1.2 登录

> 地址：**/login**
>
> 方法：**post**
>
> 参数: (String **username**, String **password**, Boolean **rememberMe**)
>
> 备注：
>
> - rememberMe 勾选框
> - 登录成功跳转孪生页面，不成功跳转本页面



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
> > socket.send()
>
> sendInstruction

- **心跳检测**

  ```json
  // 由客户端每两分钟发一次，服务器连续3次心跳检测未收到则关闭连接
  {
      "heartBeat":"heartBeat",
      "clientType":"gatewayClient",
      "clientID":"ID"
  }
  ```

- **前端请求与数据格式：**

> Webscoket连接建立地址：**"/ws/{clientType}/{userId}"**
>
> > **clientType**:  网页端请求webClient
> >
> > **userId**: 与用户名相同
>
> **发送消息**数据格式：
>
> ```json
> {
>     "deviceType":"1",
>     "deviceId":"123",
>     "instruction":"1", // 这三个具体后面和王工交流后写一个device表和指令表
>     "instructionID":"UserId.deviceId.timestamp",
>     "toClientType":"gatewayClient"
> }
> ```
>
> **接收消息**数据格式：
>
> ```json
> // 在连接建立时接收结果,1:成功, 0:失败
> // {"connectionStatusCode":"1"}   
> ```
>
> ```json
> // 用户在网页进行操作后接收操作结果，仅发送本次指令的用户会收到，其他用户不会收到此消息
> {
>     "fromUserID":"gatewayID",
>     "instructionID":"用户操作时前端发送的指令ID(UserId + deviceId + timestamp)",
>     "xResult":"1", //1:成功, 0:失败
>     "message":"可选"
> }
> ```
>
> ```json
> //服务器发送实时的物理设备信息
> {
>     "isInit":true, // 是否初次建立，true: 初次建立，全局初始化，false: 局部更新
>     "fromUerID":"gatewayID", // isInit为false的时候会有此项，为发送该信息的网关序号
>     "device":[
>         {
>             "deviceType":"1",
>             "deviceID":"123",
>             "deviceStatus":"1"
>         },
>         {
>             "deviceType":"2",
>             "deviceId":"3232",
>             "deviceStatus":"3"
>         }
>     ]
> }
> ```



- **网关通信的数据格式**

>Webscoket连接建立地址：**"/ws/{clientType}/{userId}"**
>
>> **clientType**:  网关命名gatewayClient
>>
>> **userId**: gateway1
>
>**接收消息**数据格式：
>
>```json
>{
>    "fromUserID":"UserID",
>    "deviceType":"1",
>    "deviceId":"123",
>    "instruction":"1", 
>    "instructionID":"UserId.deviceId.timestamp",
>    "toClientType":"gatewayClietn"
>}
>```
>
>**发送消息**数据格式（有用户指令后返回两段）
>
>```json
>// 仅在有用户指令时发送
>{
>    "instructionID":"用户操作时前端发送的指令ID(UserId + deviceId + timestamp)",
>    "xResult":"1", //1:成功, 0:失败
>    "message":"可选"
>}
>```
>
>```json
>// 物理设备状态信息更新时发送
>{
>"device":[
>        {
>            "deviceType":"1",
>            "deviceID":"123",
>            "deviceStatus":"1"
>        }
>]
>}
>```

