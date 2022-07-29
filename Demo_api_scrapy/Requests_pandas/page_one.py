from sklearn.datasets import load_wine
from datetime import timedelta
import pandas as pd
import numpy as np
import requests

pull_closed = requests.get('https://api.github.com/repos/apache/hive/pulls?state=closed')
data_json_pull_closed = pull_closed.json()

length = list(data_json_pull_closed)


def closed_pull():
    for i in length:
        print("Id", i['id'])
        print("State", i['state'])
        print("Created_at", i['created_at'])
        print('Closed_at', i['closed_at'])
        # x = list(dic[0]['user'].values())[1]
        print('User_id', i['user']['id'])
        print('User_type', i['user']['type'])
        #
        # print(i['id'])
        # print(i['state'])
        # print(i['created_at'])
        # print(i['closed_at'])
        # print(i['user']['id'])
        # print(i['user']['type'])
