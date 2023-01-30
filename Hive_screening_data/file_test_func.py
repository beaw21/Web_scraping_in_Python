import pandas as pd
import requests
import time
import pickle
from datetime import datetime
import json


def cell_api(api_name):
    list_api_name = []
    for api in api_name:
        data = requests.get(api)
        print(data)
        list_api_name += data.json()
        statu_api = data.status_code
        print(statu_api)
    while statu_api == 403:
        print("sleep for 30 minutes ", str(datetime.now()))
        time.sleep(31 * 60)
        print("start query again at", str(datetime.now()))
        time.sleep(5)

    data_loads_json = json.loads(data.content.decode('utf8'))
    data_loads_json_nol = pd.json_normalize(data_loads_json)
    print(data_loads_json)
    print(data_loads_json_nol.to_markdown())
    return data_loads_json_nol
