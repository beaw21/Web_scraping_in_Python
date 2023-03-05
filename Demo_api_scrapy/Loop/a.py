import pandas as pd
import requests

# df = pd.read_csv('git_all_hive.csv')

api_get = 'https://api.github.com/repos/apache/hive/pulls?state=closed&per_page=300&page='
print(type(api_get))

requests_data = requests.get(api_get)
print(type(requests_data))


def cell_api(api, fromPage=1, toPage=5, **page):
    data = page.get('page', [])
    for i in range(fromPage, toPage + 1, 1):
        cell = requests.get(api + str(i))
        data += cell.json()
        print('loading page' + str(i))
        data_obj = pd.json_normalize(data)
    if len(data_obj) > 10:
        return (data_obj)


data_list_api = cell_api(api_get, fromPage=1, toPage=300)
df = pd.json_normalize(data_list_api)
data_list_api.to_csv('cover_1.csv')
