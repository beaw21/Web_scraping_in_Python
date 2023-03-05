import pandas as pd
import requests

df = pd.read_csv('git_all_pull.csv')
df = df.dropna(thresh=2)

token = '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'
url = "https://api.qithub.com/rate_limit"
header = {'Authorization': 'Bearer' + token}
response = requests.get(url, headers=header)
print(response.json())
