import pandas as pd
import requests
from requests.adapters import HTTPAdapter, Retry

# import or

df = pd.read_csv('git_csv/git_hive.csv')

# get df of columns
col = pd.DataFrame(df.columns)
print(list(df.columns))
new_df = pd.DataFrame({
    # key
    'index': range(1, len(df) + 1),
    'ID': df['id'].values,
    #
    # 'url_pull': df['url'].values,
    'created_at': df['created_at'],
    'closed_at': df['closed_at'],
    'commit_sha': df['merge_commit_sha'],
    'commits_url': df['commits_url'],
    'user_name': df['user.login'],
    'user_id': df['user.id'],
    'user_url': df['user.url'],
    # complexity
    'user_node': df['user.node_id'],
    'repo_size': df['head.repo.size']
})

# Creates DataFrame object from dictionary by columns or by index allowing type specification
Dict = pd.DataFrame.from_dict(new_df)

# Creates a Value for call in each Url
get_url = Dict.apply(lambda x: x["ID"], 1)

# get obj json in each URL
# get_obj = get_url.apply(lambda x: requests.get(x).json())

# d = []
# for i in Dict['commits_url']:
#     x = requests.get(i)
#     d += x.json()
#     print(d)
#     # if i == ['https://api.github.com/repos/apache/hive/pulls/1/commits']:
#     #     break
#     if d == {'message', 'documentation_url'} :
#         break

# dn = pd.json_normalize(d)
# dn.to_csv('git_hive_commit_list.csv')

Dict.to_csv('git_hive_set_dict.csv')
