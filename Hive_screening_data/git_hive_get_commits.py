import pandas as pd
import requests

df = pd.read_csv('git_csv/git_hive_set_dict.csv')

data = []
for i in df['commits_url']:
    x = requests.get(i)
    data += x.json()
    y = range(1, len(data) + 1)
    print(x.status_code)
    print(y)
    if x.status_code == 403:
        break
    z = pd.json_normalize(data)
    z.to_csv("git_hive_commits_dict_981.csv")
