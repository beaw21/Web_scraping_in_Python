import pandas as pd
import requests

cell_file = pd.read_csv('01.shiro_all_pll.csv')

token_ozone = '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'
url = "https://api.github.com/rate_limit"
header = {'Authorization': 'Bearer ' + token_ozone}
response = requests.get(url, headers=header)
print(response.json())

# Empty list to store the API response data
data_list = []

for i in cell_file['url']:
    data = requests.get(i, headers=header)
    data_list.append(data.json())
    print("========= :" , data_list)
    obj = pd.json_normalize(data_list)
    print(obj)

df = pd.DataFrame(obj)
print(df)