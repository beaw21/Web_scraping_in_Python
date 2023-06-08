import pandas as pd
import requests

cell_file = pd.read_csv('01.ozone_all_pll.csv')

token_ozone = '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'
url = "https://api.github.com/rate_limit"
header = {'Authorization': 'Bearer ' + token_ozone}
response = requests.get(url, headers=header)
print(response.json())

# Empty list to store the API response data
data_list = []

for i in cell_file['url']:
    data = requests.get(i, header)
    data_list.append(data.json())
    print("========= :", data_list)
    obj = pd.json_normalize(data_list)
    print(obj)

df = pd.DataFrame(obj)
print(df)
df.to_csv('02.ozone_all.csv', index=False, sep="\n")
