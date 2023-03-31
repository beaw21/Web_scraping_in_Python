import pandas as pd
import requests
import requests_cache

df = pd.read_csv('git_all_pull_not_null.csv')

# token = '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'
token_bg = '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'
url = "https://api.github.com/rate_limit"
header = {'Authorization': 'Bearer ' + token_bg}
response = requests.get(url, headers=header)
print(response.json())

# Enable caching for all requests
requests_cache.install_cache('my_cache', expire_after=3600)  # cache for 1 hour

data_odj = []
list_all_pd = []
for i in df['commits_url']:
    print(i)
    response_url = requests.get(i, headers=header)
    data_odj += response_url.json()
    # print("OBJ:", data_odj)
    data_loads_json = pd.json_normalize(data_odj)
    print("data_loads_json:", data_loads_json)

    data_loads_json['index'] = i
    data_loads_json.set_index(['index', 'sha', 'node_id', 'commit.tree.sha'])
    append_obj = list_all_pd.append(data_loads_json)
    all_pd = pd.concat(list_all_pd)
    drop_all_pd = all_pd.drop_duplicates(subset=['sha', 'node_id'])
    set_pull = drop_all_pd.set_index(['index', 'sha'])
    set_pull.to_csv('get_pull_commits_all.csv')

    if i == 'https://api.github.com/repos/apache/hive/pulls/1/commits':
        break
    if response_url.status_code != 200:
        break
