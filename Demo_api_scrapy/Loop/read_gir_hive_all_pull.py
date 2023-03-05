import pandas as pd
import requests

df = pd.read_csv('git_all_pull_not_null.csv')

token = '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'
url = "https://api.qithub.com/rate_limit"
headers = {'Authorization': 'Bearer ' + token}
# response = requests.get(url, headers=headers)
# print(response.json())

data_odj = []
list_all_pd = []
for i in df['commits_url'].head(3):
    print(i)
    data = requests.get(i, headers=headers)
    data_odj += data.json()
    print("OBJ:", data_odj)
    data_loads_json = pd.json_normalize(data_odj)
    print("data_loads_json:", data_loads_json)
    data_loads_json['index'] = i
    data_loads_json.set_index(['index', 'sha', 'node_id'])
    list_all_pd.append(data_loads_json)

all_pd = pd.concat(list_all_pd)
drop_all_pd = all_pd.drop_duplicates(subset=['sha', 'node_id'])
set_pull = drop_all_pd.set_index(['index', 'sha'])
