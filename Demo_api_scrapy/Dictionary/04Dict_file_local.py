import json

import pandas as pd
import requests
import ast

# get_file_pull = pd.read_json('datapull.json')
#
# # mew data Frame for pull state closed
# new_df = pd.DataFrame({'ID': get_file_pull['id'].values,
#                        'url_pull': get_file_pull['url'].values})

api_get = 'https://api.github.com/repos/apache/hive/pulls?state=closed'


# pull_closed = requests.get('https://api.github.com/repos/apache/hive/pulls?state=closed')

# api_get = pull_closed.json()

# api_get_users = 'https://api.github.com/users'
#
#
# def call_api(apicall, **kwargs):
#     data = kwargs.get('page', [])
#     resp = requests.get(apicall)
#     data += resp.json()
#
#     # failsafe
#     if len(data) > 500:
#         return (data)
#
#     if 'next' in resp.links.keys():
#         return (call_api(resp.links['next']['url'], page=data))
#
#     return (data)
#
#
# data = call_api(api_get_users)
# print(data)


def check_page_api(api, **page):
    x = page.get('page', [])
    call = requests.get(api)
    x += call.json()

    if len(x) > 3000:
        return (x)
    if 'next' in call.links.keys():
        return (check_page_api(call.links['next']['url'], page=x))
    return (x)


result = check_page_api(api_get)
df = pd.DataFrame(result)

for num in range(1, 10):
    with open("pull_closed" + str(num) + ".json", 'w') as f:
        f.write(df.to_json(orient='values'))
        f.close()
    print(f)