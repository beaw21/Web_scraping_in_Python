import pandas as pd
import requests

pull_closed = requests.get('https://api.github.com/repos/apache/hive/pulls?state=closed')
data_json_pull_closed = pull_closed.json()

df = pd.DataFrame(data_json_pull_closed)

# mew data Frame for pull state closed
new_df = pd.DataFrame({'ID': df['id'].values,
                       'url_pull': df['url'].values})

# Creates DataFrame object from dictionary by columns or by index allowing dtype specification
Dict = pd.DataFrame.from_dict(new_df)

# create an empty pandas to dictionary
dct = pd.DataFrame.to_dict(new_df)

# Creates a Value for call in each Url
get_url = Dict.apply(lambda x: x["url_pull"], 1)

# get obj json in each URL
get_obj = get_url.apply(lambda x: requests.get(x).json())

# get data and Creates DataFrame
df_dict = pd.DataFrame({"id_pull": get_obj.apply(lambda x: x['id']),
                        "user_id": get_obj.apply(lambda x: x['user']['id']),
                        "open_time": get_obj.apply(lambda x: x['created_at']),
                        "closed_time": get_obj.apply(lambda x: x['closed_at']),
                        "amount_commit": get_obj.apply(lambda x: x['commits']),
                        "amount_review": get_obj.apply(lambda x: x['review_comments']),
                        "amount_addition": get_obj.apply(lambda x: x['additions']),
                        "amount_deletion": get_obj.apply(lambda x: x['deletions']),
                        "amount_changed_files": get_obj.apply(lambda x: x['changed_files']),
                        "number_sha": get_obj.apply(lambda x: x['base']['sha'])
                        })

# Check Map ID pull
list(map(lambda x, y: x == y, new_df['ID'], df_dict['id_pull']))
