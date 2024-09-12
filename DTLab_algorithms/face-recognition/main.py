import time

import face_recognition
import cv2
import numpy as np

from data_utils import load_data
from mqtt_client import MqttClient

video_capture = cv2.VideoCapture(0)

tolerance = 0.6  # 识别阈值，越低越严格
data = load_data()
faces = data['faces']
names = data['names']
face_locations = []
face_encodings = []
face_names = []

mqtt_client = MqttClient("face_recognizer", "127.0.0.1", 1883, "dtlab", "527")
while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)
    new = rgb_small_frame.copy()
    face_encodings = face_recognition.face_encodings(new, face_locations)
    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(faces, face_encoding, )
        name = "Unknown"
        face_distances = face_recognition.face_distance(faces, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = names[best_match_index]
            mqtt_client.publish("face_recognize_result", {"name":name, "time":time.time(), "distance":face_distances[best_match_index]})
        face_names.append(name)
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(frame, (left-10, top-10), (right+10, bottom+10), (0, 0, 255), 1)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left, bottom), font, 1.0, (123, 237, 159), 1)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
