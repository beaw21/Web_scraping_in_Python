import json

import pandas as pd
import requests

# get_file_pull = pd.read_json('datapull.json')
#
# # mew data Frame for pull state closed
# new_df = pd.DataFrame({'ID': get_file_pull['id'].values,
#                        'url_pull': get_file_pull['url'].values})

api_get = 'https://api.github.com/repos/apache/hive/pulls?state=closed'


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

json_odject = json.dumps(result)
with open("pull_colsed.json", "w") as outfile:
    outfile.write(json_odject)


