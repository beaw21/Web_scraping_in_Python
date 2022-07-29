import json

import pandas as pd
import requests

test = requests.get('https://api.github.com/repos/apache/hive/pulls/3472/commits')

# test.json()[0]["commit"]["author"]

pull_closed = requests.get('https://api.github.com/repos/apache/hive/pulls?state=closed')
data_json_pull_closed = pull_closed.json()


# print(data_json_pull_closed)

def pull():
    for i in data_json_pull_closed:
        print('Id', i['id'])
        print("State", i['state'])
        print("Created_at", i['created_at'])
        print('Closed_at', i['closed_at'])
        user_id = list(data_json_pull_closed[0]['user'].values())[1]
        print('User_Id', user_id)

pd.DataFrame(pull())
