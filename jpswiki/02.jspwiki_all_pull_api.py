import pandas as pd
import requests

cell_file = pd.read_csv('jpswiki_all_page.csv')

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