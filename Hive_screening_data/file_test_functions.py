import pandas as pd
import requests
import time
import pickle
from datetime import datetime
import json


def call_api(api_name):
    data_odj =[]
    data = requests.get(api_name)
    print(data)
    statu_api = data.status_code
    print(statu_api)
    data_odj += data.json()
    while data.status_code == 403:
        print("sleep for 30 minutes ", str(datetime.now()))
        time.sleep(31 * 60)
        print("start query again at", str(datetime.now()))
        time.sleep(5)
        data = requests.get(api_name)

    data_loads_json = json.loads(data.content.decode('utf8'))
    data_loads_json_nol = pd.json_normalize(data_loads_json)
    return data_loads_json_nol


def write_file(prefix: object, suffix: object, type_file: object, content: object):
    # create the file which name is prefix_suffix.csv
    # with open(str() + int() + str(), 'w') as f:
    #     f.write(content)
    #     f.close()
    # print(f)
    print("functions file")


def countdown(t):
    while t:
        print(t)
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('countdown complete!!')


def loop_items(api_list):
    counter = 1
    data_list = []
    for api_name in api_list:
        return_obj = call_api(api_name)
        print(return_obj)
        df = pd.DataFrame.from_dict(return_obj)
        # data_list.append(df)
        # time.sleep(4)

    # df_con = pd.concat(data_list, ignore_index=True)
    # print(df_con.to_markdown())

    # data_concat = pd.concat([df])
    # print(data_concat)
    # x = pd.DataFrame.to_csv(data_concat)
    # write out return obj
    # with open("commit" + str(counter) + ".csv", 'w') as file:
    #     file.write(str(df))
    # counter += 1
