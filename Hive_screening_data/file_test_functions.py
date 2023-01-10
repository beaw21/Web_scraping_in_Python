import pandas as pd
import requests
import time
from datetime import datetime


def call_api(api_name):
    data = requests.get(api_name)
    # print(api_name)
    print(data)
    statu_api = data.status_code
    print(statu_api)
    while data.status_code == 403:
        print("sleep for 30 minutes ", str(datetime.now()))
        time.sleep(31*60)
        print ("start query again at", str(datetime.now()))
        # time.sleep(5)
        data = requests.get(api_name)

    json_obj = []
    json_obj += pd.json_normalize(data)
    return json_obj


def write_file(prefix: object, suffix: object, type_file: object, content: object) -> object:
    # create the file which name is prefix_suffix.csv
    with open(str() + int() + str(), 'w') as f:
        f.write(content)
        f.close()
    print(f)
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
    for api_name in api_list:
        return_obj = call_api(api_name)
        time.sleep(4)
        print(return_obj)
        # write out return obj
        write_file("/commit", counter, "/.csv", return_obj)
        counter += 1
        # if counter % 5 == 0:
        #     countdown(2)
        # if call_api(api_name) ==
