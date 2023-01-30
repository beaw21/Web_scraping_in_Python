import pandas as pd
import requests
import time
import tabulate
from datetime import datetime
from file_test_functions import countdown

df = pd.read_csv('git_csv/git_hive.csv')

# data_odj = []
# for i in df['commits_url']:
#     data = requests.get(i)
#     print(data)
#     print(str(datetime.now()))
#     data_odj += data.json()
#     print(data.status_code)
#     data_loads_json = pd.json_normalize(data_odj)
#     print(data_loads)
#     data_loads_json.to_csv("/home/ec2-user/output/git_hive_commit_test_1")
#     if data.status_code != 200:
#         print("sleep for 30 minutes ", str(datetime.now()))
#         time.sleep(31 * 60)
#         print("start query again at", str(datetime.now()))
#         time.sleep(5)
#         data = requests.get(i)
#
#     for x in df.columns[0]:
#         if x > '3484':
#             break
#         print(x)
