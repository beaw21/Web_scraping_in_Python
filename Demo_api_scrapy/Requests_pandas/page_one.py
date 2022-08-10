import json

from datetime import timedelta
import pandas as pd
import numpy as np
import requests
import io

pull_closed = requests.get('https://api.github.com/repos/apache/hive/pulls?state=closed')

data_json_pull_closed = pull_closed.json()

length = list(data_json_pull_closed)

df = pd.DataFrame(length)

new_data = []

new_df = pd.DataFrame(new_data)
new_df['ID'] = df['id'].values
new_df['url_pull'] = df['url'].values
new_df['url_issues'] = df['issue_url'].values
new_df['url_commits'] = df['commits_url'].values
new_df['Stats'] = df['state'].values
new_df['Created_at'] = df['created_at'].values
new_df['Closed_at'] = df['closed_at'].values
new_df['User_id'] = df['user'].apply(lambda x: x['id']).values
