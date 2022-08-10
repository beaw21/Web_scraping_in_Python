import pandas as pd
import numpy as np
import requests

pull_closed = requests.get('https://api.github.com/repos/apache/hive/pulls?state=closed')
data_json_pull_closed = pull_closed.json()

df = pd.DataFrame(data_json_pull_closed)

# mew data Frame for pull state closed
new_data = []

new_df = pd.DataFrame(new_data)
new_df['ID'] = df['id'].values
new_df['url_pull'] = df['url'].values

# Creates DataFrame object from dictionary by columns or by index allowing dtype specification
Dict = pd.DataFrame.from_dict(new_df)

# create an empty pandas to dictionary
dct = pd.DataFrame.to_dict(new_df)

# Creates a Value for call in each Url
get_url = Dict.apply(lambda x: x["url_pull"], 1)

# get obj json in each URL
get_obj = get_url.apply(lambda x: requests.get(x).json())

# get data
id_p = get_obj.apply(lambda x: x['id'])
user_id = get_obj.apply(lambda x: x['user']['id'])
open_time = get_obj.apply(lambda x: x['created_at'])
closed_time = get_obj.apply(lambda x: x['closed_at'])
amount_commit =get_obj.apply(lambda x: x['commits'])
amount_review = get_obj.apply(lambda x: x['review_comments'])
amount_addition = get_obj.apply(lambda x: x['additions'])
a = get_obj.apply(lambda x: x['deletions'])
b = get_obj.apply(lambda x: x['changed_files'])
c = get_obj.apply(lambda x: x['user']['repos_url'])
d = get_obj.apply(lambda x: x['base']['sha'])
