import asyncio

from websockets import server
from websockets.exceptions import ConnectionClosed, InvalidState

websocket_users = set()

flag = False

test_str1 = """
{
    "action": "set_power_switch",
    "params": {
        "device_id": 5,
        "switch": 0
    }
}
"""

test_str2 = """
{
    "action": "set_power_switch",
    "params": {
        "device_id": 1,
        "switch": 1
    },
    "echo": "114.514"
}
"""

test_str3 = """
{
    "action": "set_air_conditioner",
    "params": {
        "device_id": 1,
        "mode": 1,
        "power": 1,
        "basic_fan": 1,
        "temp": 26,
        "light": 1
    },
    "echo": "1919.810"
}
"""

test_str4 = """
{
    "action": "set_air_conditioner",
    "params": {
        "device_id": 1,
        "mode": 1,
        "power": 0,
        "basic_fan": 1,
        "temp": 26
    },
    "echo": "1919.810"
}
"""

test_str5 = """
{
    "action": "set_monitor_electricity",
    "params": {
        "switch": 1
    }
}
"""

test_str6 = """
{
    "action": "get_power_light",
    "params": {
        "device_id": 0
    }
}
"""



# 检测客户端权限，用户名密码通过才能退出循环
async def check_user_permit(websocket):
    print("new websocket_users:", websocket)
    websocket_users.add(websocket)
    print("websocket_users list:", websocket_users)
    while True:
        recv_str = await websocket.recv()
        cred_dict = recv_str.split(":")
        print(cred_dict[0])
        print(cred_dict[1])
        if cred_dict[0] == "admin" and cred_dict[1] == "022c74f":
            response_str = "Congratulation, you have connect with server..."
            await websocket.send(response_str)
            print("Password is ok...")
            return True
        else:
            response_str = "Sorry, please input the username or password..."
            print("Password is wrong...")
            await websocket.send(response_str)


# 接收客户端消息并处理
async def recv_user_msg(websocket):
    global flag
    while True:
        recv_text = await websocket.recv()
        # print("[WS] recv_text: ", websocket.pong, recv_text)
        print("[WS] recv_text: ", recv_text)
        if "heartbeat" in recv_text:
            if flag:
                response_text = test_str1
            else:
                response_text = test_str1
            flag = ~flag
            # print("[WS] response_text: ", response_text)
            await websocket.send(response_text)


# 服务器端主逻辑
async def run(websocket, path):
    while True:
        try:
            # await check_user_permit(websocket)
            await recv_user_msg(websocket)
        except ConnectionClosed:
            print("ConnectionClosed...", path)  # 链接断开
            print("websocket_users old:", websocket_users)
            websocket_users.remove(websocket)
            #print("websocket_users new:", websocket_users)
            break
        except InvalidState:
            print("InvalidState...")  # 无效状态
            break
        except Exception as e:
            print("Exception:", e)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(server.serve(run, "192.168.3.80", 8080))
    asyncio.get_event_loop().run_forever()
