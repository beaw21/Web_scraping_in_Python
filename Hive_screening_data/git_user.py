import pandas as pd
import requests
from requests.adapters import HTTPAdapter, Retry

# import or

df = pd.read_csv('git_hive.csv')

# get df of columns
col = pd.DataFrame(df.columns)
print(list(df.columns))
new_df = pd.DataFrame({
    # key
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

d = []
for i in Dict['user_url']:
    x = requests.get(i)
    d += x.json()
    print(d)
    if i == 'https://api.github.com/users/guydou':
        break
        pass
    dn = pd.json_normalize(d)
    dn.to_csv('git_user.csv')
