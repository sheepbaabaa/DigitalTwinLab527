<!-- markdownlint-disable MD036 -->

# API Reference

## API

### 基础传输

#### 请求说明

WebSocket JSON 格如下

```json
{
    "action": "终结点名称, 例如 'set_power_switch'",
    "params": {
        "参数名": "参数值",
        "参数名2": "参数值"
    },
    "echo": "'回声', 如果指定了 echo 字段, 那么响应包也会同时包含一个 echo 字段, 它们会有相同的值"
}
```

#### 响应说明

调用 API 时, 返回信息格式如

```json
{
    "status": "状态, 表示 API 是否调用成功, 如果成功, 则是 ok, 其他的在下面会说明",
    "retcode": 0,
    "msg": "错误消息, 仅在 API 调用失败式有该字段",
    "data": {
        "响应数据名": "数据值",
        "响应数据名2": "数据值"
    },
    "echo": "'回声', 如果请求时指定了 echo, 那么响应也会包含 echo"
}
```

其中, `status` 字段：

| 值 | 说明 |
| -- | -- |
| ok | API 调用成功 |
| async | API 调用已经提交异步处理 |
| failed | API 调用失败 |

`retcode` 字段：

| 值 | 说明 |
| -- | -- |
| 0 | 调用成功 |
| 1 | 已提交异步处理 |
| 其他 | 调用失败 |

### 参数及响应数据

下面是请求所需 `params` 和响应包含的 `data` 格式。

#### 设置开关

终结点：`set_power_switch`

**参数**

| 字段名 | 数据类型 | 默认值 | 说明 |
| -- | -- | -- | -- |
| device_id | uint16 | - | 对象 ID |
| switch | boolean | - | 0 表示关, 1 表示开 |

*该 API 无响应数据*

#### 设置空调状态

终结点：`set_air_conditioner`

**参数**

| 字段名 | 数据类型 | 默认值 | 说明 |
| -- | -- | -- | -- |
| device_id | uint16 | - | 对象 ID |
| mode | uint8 | - | 模式, 0 表示自动, 1~4 分别表示制冷, 除湿, 送风, 制热 |
| power | boolean | - | 0 表示关, 1 表示开 |
| basic_fan | uint8 | - | 风速, 0 表示自动, 1~3 分别表示三级风速 |
| temp | uint8 | - | 摄氏度表示的空调温度 (16~30) |
| turbo | boolean | false | 强劲模式 |
| light | boolean | false | 空调灯光 |
| xfan | boolean | false | 干燥模式, 在制冷, 除湿模式下可用 |
| swing_v | boolean | false | 上下扫风 |
| swing_h | boolean | false | 左右扫风 |
| quiet | boolean | false | 静音模式 |

*该 API 无响应数据*

## Event

### 通用数据

#### 所有上报

所有上报都将包含下面的有效通用数据：

| 字段名 | 数据类型 | 可能的值 | 说明 |
| -- | -- | -- | -- |
| time | uint32 | - | 事件发生的时间戳 |
| gateway_id | uint16 | - | 事件发生的网关 ID |
| event_type | string | notice, meta | 上报类型 (通知, 元事件) |

#### 通知上报

`event_type` 为 `notice` 的上报将会有以下有效通用数据

| 字段名 | 数据类型 | 可能的值 | 说明 |
| -- | -- | -- | -- |
| notice_type | string | 见 Notice_Type | 通知类型 |
| data | message | - | 详细参数 |

#### 元事件上报

`event_type` 为 `meta` 的上报将会有以下有效通用数据

| 字段名 | 数据类型 | 可能的值 | 说明 |
| -- | -- | -- | -- |
| meta_type | string | 见 Meta_Type | 元事件类型 |

## 数据结构

### Notice_Type

一个枚举, 传输使用字符串, 表示通知类型。

| 值 | 说明 |
| -- | -- |
| power_switch | 开关状态变化 |

#### power_switch

`data` 中将会有以下字段

| 字段名 | 数据类型 | 默认值 | 说明 |
| -- | -- | -- | -- |
| device_id | uint16 | - | 对象 ID |
| switch | boolean | - | 0 表示关, 1 表示开 |

### Meta_Type

一个枚举, 传输使用字符串, 表示元事件类型。

| 值 | 说明 |
| -- | -- |
| gateway_update | 网关状态更新 |
| device_update | 设备状态更新 |
| heartbeat | 心跳包 |

#### gateway_update

#### device_update

#### heartbeat

数据包中中将会有以下额外字段

| 字段名 | 数据类型 | 可能的值 | 说明 |
| -- | -- | -- | -- |
| interval | uint32 | - | 下次心跳包时间间隔 (毫秒) |
