import socket
import time
import cv2
import sys


def checkimg(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)


def closeClient(client):
    flag = 'end server'
    client.send(flag.encode(encoding='utf-8'))


def recognition(client, img):
    client.send(bytes("calling server", encoding='utf-8'))
    ready = client.recv(1024)
    if ready.decode() != 'ready':
        print('服务器没有响应，稍后将重新请求')
        time.sleep(1)
    height = img.shape[0]
    if not height:
        print('高度不可为空！')
    print('要传输的图像高度为：', height)
    client.send(str(height).encode(encoding='utf-8'))
    ok_height = client.recv(1024)
    if ok_height.decode('utf-8') == 'wrong height':
        print('服务器没有接收到正确的图片高度信息！')
        time.sleep(1)
    client.send(img.tobytes())
    ok_img = client.recv(1024)
    if ok_img.decode() == 'wrong img data':
        print('服务器没有接收到图像数据！')
        time.sleep(1)
    result = client.recv(1024)
    if not result:
        print('未接受到服务器的返回结果！')
    person = result.decode()
    print('收到来自服务器的识别结果：', person)
    return person
