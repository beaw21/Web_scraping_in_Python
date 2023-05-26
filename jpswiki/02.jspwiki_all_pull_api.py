import pandas as pd
import requests

cell_file = pd.read_csv('jpswiki_all_page.csv')

token_ozone = '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'
url = "https://api.github.com/rate_limit"
header = {'Authorization': 'Bearer ' + token_ozone}
response = requests.get(url, headers=header)
print(response.json())

data_odj = []
list_all_pd = []
for i in cell_file['commits_url']:
    print(i)
    response_url = requests.get(i, headers=header)
    data_odj += response_url.json()
    data_loads_json = pd.json_normalize(data_odj)
    print("data_loads_json:", data_loads_json)

    data_loads_json['index'] = i
    data_loads_json.set_index(['index', 'sha', 'node_id', 'commit.tree.sha'])
    append_obj = list_all_pd.append(data_loads_json)
    all_pd = pd.concat(list_all_pd)
    drop_all_pd = all_pd.drop_duplicates(subset=['sha', 'node_id'])
    set_pull = drop_all_pd.set_index(['index', 'sha'])
    set_pull.to_csv('02.get_pull_commits_all.csv')

    if i == 'https://api.github.com/repos/apache/ozone/pulls/1':
        print("ok!!")
        break
    if response_url.status_code != 200:
        break
