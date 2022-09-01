import json

from datetime import timedelta
import pandas as pd
import numpy as np
import requests
import io

response = requests.get('https://api.github.com/repos/apache/hive/pulls?state=closed', stream=True,
                        headers={'Authorization': 'Bearer '})
# data_json_pull_closed = pull_closed.json()
#
# length = list(data_json_pull_closed)
#
# df = pd.DataFrame(length)
#
# new_data = []
#
# new_df = pd.DataFrame(new_data)
# new_df = pd.DataFrame({'ID': df['id'].values,
#                        'url_issues': df['issue_url'].values})
#
# Dict = pd.DataFrame.from_dict(new_df)
# print(Dict)
