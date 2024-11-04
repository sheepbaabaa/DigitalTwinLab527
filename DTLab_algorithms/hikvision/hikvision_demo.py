import cv2

from hikvision.camera_controller import CameraController

controller = CameraController()

while True:
    img = controller.get_frame()
    cv2.imshow('camera',img)
    cv2.waitKey(1)
