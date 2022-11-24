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
get_url_commit = Dict.apply(lambda x: x["commits_url"], 1)

# get obj json in each URL
# get_obj = get_url_commit.apply(lambda x: requests.get(x).json())

# Dict.to_csv('git_hive_set_dict.csv')

def loop_api(commit):
    data_count = []
    for i in commit:
        get = requests.get(i)
        data_count += get.json()
        count_data_commit = range(len(data_count))
        print(get.status_code)
        print(count_data_commit)
        if get.status_code == 403:
            break
