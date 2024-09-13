import os
import pickle

import face_recognition

data_file_path = "./data.pkl"


def save_data():
    faces = []
    names = []
    peoples = os.listdir("./dataSet")
    for people in peoples:
        if os.path.isdir("./dataSet/" + people):
            files = os.listdir("./dataSet/" + people)
            for file in files:
                images = face_recognition.load_image_file("./dataSet/" + people + "/" + file)
                face_encodings = face_recognition.face_encodings(images)
                if len(face_encodings) != 0:
                    faces.append(face_encodings[0])
                    names.append(people)
    data = {
        "faces": faces,
        "names": names
    }
    with open(data_file_path, "wb") as f:
        pickle.dump(data, f)


def load_data():
    data = None
    if not os.path.exists(data_file_path):
        save_data()
    with open(data_file_path, 'rb') as f:
        data = pickle.load(f)

    return data
