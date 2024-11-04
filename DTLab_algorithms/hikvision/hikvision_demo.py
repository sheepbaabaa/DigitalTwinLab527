import cv2
import requests




camera_ip = "192.168.3.122"
username = "admin"
password = "wififor612"

cap = cv2.VideoCapture(f'rtsp://{username}:{password}@{camera_ip}/Streaming/Channels/101?tcp')
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
cv2.namedWindow('camera',cv2.WINDOW_NORMAL)

while True:
    img = cap.read()[1]
    cv2.imshow('camera',img)
    cv2.waitKey(1)
