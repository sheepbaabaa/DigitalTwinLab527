from AIDetector_pytorch import Detector
import imutils
from threading import Thread
import cv2
import numpy as np
import transfrom
import ToJson
import math
import keyboard


def plot_bboxes(image, bboxes, positions, line_thickness=None):
    # Plots one bounding box on image img
    tl = line_thickness or round(
        0.001 * (image.shape[0] + image.shape[1]) / 2) + 1  # line/font thickness
    index = 0
    for (x1, y1, x2, y2, cls_id, pos_id) in bboxes:
        if cls_id in ['person']:
            color = (0, 0, 255)
        else:
            color = (0, 255, 0)
        c1, c2 = (x1, y1), (x2, y2)
        cv2.rectangle(image, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
        tf = max(tl - 1, 1)  # font thickness
        cv2.putText(image, '{} ID-{}'.format(cls_id, pos_id), (c1[0], c1[1] - 2), 0, tl / 3,
                    [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)
        cv2.putText(image, 'position: {}'.format(positions[index]), (c1[0], c1[1] - 20), 0, tl / 3,
                    [0, 0, 225], thickness=tf, lineType=cv2.LINE_AA)
        index = index + 1

    return image


class tracker(object):
    def __init__(self, path, det, wsize):
        self.videoList = []
        self.path = path
        self.det = det
        self.window = wsize
        self.fps = 20

    def video_cap(self):
        cap = cv2.VideoCapture(self.path)
        self.fps = cap.get(cv2.CAP_PROP_FPS)  # 帧数
        while True:
            _, im = cap.read()
            if im is None:
                break
            self.videoList.append(im)
            if keyboard.is_pressed('q'):  # 如果用户按下了 'q' 键
                break  # 退出循环
        print("video_cap Finish")

    def track(self):
        name = 'demo'
        t = int(1)
        print("track start")
        # 创建视频编码器
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用H.264编码器
        index = 1
        while not self.videoList:
            continue
        while True:
            if not self.videoList:
                continue
            im = self.videoList[0]
            if im is None:
                break
            for i in range(len(self.videoList)-self.window):
                self.videoList.pop(0)
            if not self.videoList:
                break
            self.videoList.pop(0)
            timer = cv2.getTickCount()
            personList = []
            positionList = []
            result = self.det.feedCap(im)
            bboxs = result['bboxes']
            result = result['frame']
            print(result.shape)
            for (x1, y1, x2, y2, cls_id, pos_id) in bboxs:
                personList.append(str(pos_id))
                point = np.array([result.shape[1]/2 - x1 - x2/2, y1 + y2 - result.shape[0] / 2])
                position = transfrom.to3d(np.array([result.shape[1], result.shape[0]]), point,
                                          np.array([0.60, 2.00, 1.90]), 0,  math.pi * 2 / 3, 0,
                                          [math.pi*110/180, math.pi*75/180])
                positionList.append(position)
                print(point)
                print(position)
            result = plot_bboxes(result, bboxs, positionList)
            if index == 1:
                output_video = cv2.VideoWriter('output_video.mp4', fourcc, self.fps,
                                               (result.shape[1], result.shape[0]))
            json_data = ToJson.Tojson(personList, positionList)
            print(json_data)
            result = imutils.resize(result, height=500)
            # 将json格式的数据写入文件
            # file_handle = open("json_data.txt", mode="w")
            # file_handle.write(json_data + "\n")
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
            print("fps: " + str(fps))
            cv2.putText(result, "FPS : " + str(int(fps)), (result.shape[1] - 150, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
            output_video.write(result)
            cv2.imshow(name, result)
            cv2.waitKey(t)
            index = index + 1
            if keyboard.is_pressed('q'):  # 如果用户按下了 'q' 键
                break  # 退出循环
        output_video.release()
        cv2.destroyAllWindows()
        cv2.destroyAllWindows()
        print("track end")


if __name__ == '__main__':
    path = 'http://192.168.3.108:8081/?action=stream'
    # path = 'D:/desk/数字孪生系统/data/test1.mp4'
    det = Detector()
    tracker1 = tracker(path, det, 50)

    t1 = Thread(target=tracker1.video_cap)
    t2 = Thread(target=tracker1.track)

    t1.start()
    t2.start()

