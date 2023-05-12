import requests
import pandas as pd

token_bg = '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'
url = "https://api.github.com/rate_limit"
header = {'Authorization': 'Bearer ' + token_bg}
response = requests.get(url, headers=header)
print(response.json())


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
    if len(data) > 10:
        return (data)


data_list_api = cell_api(api_get, fromPage=1, toPage=2)
df = pd.json_normalize(data_list_api)
