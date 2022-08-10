import pandas as pd
import numpy as np
import requests

pull_closed = requests.get('https://api.github.com/repos/apache/hive/pulls?state=closed')
data_json_pull_closed = pull_closed.json()

df = pd.DataFrame(data_json_pull_closed)

# mew data Frame
new_data = []

new_df = pd.DataFrame(new_data)
new_df['ID'] = df['id'].values
new_df['url_pull'] = df['url'].values

# Creates DataFrame object from dictionary by columns or by index allowing dtype specification
Dict = pd.DataFrame.from_dict(new_df)

# Creates a Value for call in each Url
get_url = Dict.apply(lambda x: x["url_pull"], 1)

# get obj json in each URL
# for i in get_url:
#     requests.get(i).json()
#     print(requests.get(i).json())
#     if i == 29:
#         break;

get_url.apply(lambda x: requests.get(x).json())
# get_obj = requests.get(get_url[0]).json()


# create an empty pandas to dictionary
# dct = pd.DataFrame.to_dict(new_df)

# set index by ID in Dict
# set_index = Dict.set_index("ID").to_dict()["url_pull"]

# Creates a Value for call in each Url
# dict_values = set_index.values()


# getUrl = Dict.apply(lambda x: x["url_pull"], 1)
# triedGetUrl = requests.get(Dict['url_pull'][0]).json()

#
# data_json = requests.get(getUrl[0]).json()
