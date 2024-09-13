import json
import datetime
import string
import time


def Tojson(person_list, position_list):
    now = datetime.datetime.now()
    dict_data = {"response": "response_tracking", "time": now.strftime('%Y-%m-%d %H:%M:%S.%f'), "position": []}
    positions = []
    dict_position = {"name": "", "position": ""}
    for i in range(len(person_list)):
        dict_position["name"] = person_list[i]
        dict_position["position"] = position_list[i]
        positions.append(dict_position)
    dict_data["position"] = positions
    json_data = json.dumps(dict_data)
    return json_data


if __name__ == '__main__':
    json_list = []
    file_handle = open("json_data.txt", mode="w")
    for i in range(100):
        person = []
        position = []
        person.append("Zhang Tianyi")
        position.append([str(100), str(100+i), str(0)])
        json_data = Tojson(person, position)
        json_list.append(json_data)
        time.sleep(0.1)
        file_handle.write(json_data+"\n")
    print(json_list)
