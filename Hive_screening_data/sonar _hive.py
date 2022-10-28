import pandas as pd
import requests

session = requests.Session()
session.auth = ('admin', 'admin21')

auth = session.post('http://localhost:9000')
response = session.get('http://localhost:9000/api/issues/search?project=Hive&ps=500&p=1')
data_json = response.json()

hive = 'http://localhost:9000/api/issues/search?projects=HIVE&types=CODE_SMELL&scopes=MAIN&ps=500&p='

# Can return only the first 10000 results. 10500th result asked
# all issues 43656 / 500 = 87.3 > 88 page
def cell_api(api, fromPage=1, toPage=2):
    data = []
    for i in range(fromPage, toPage + 1, 1):
        cell = session.get(api + str(i))
        data.append(cell.json())

        print('loading page' + str(i))
    return (data)


cell_page = cell_api(hive, fromPage=1, toPage=20)
df_test = pd.DataFrame(cell_page)

list_obj = df_test['issues'].to_list()

obj_issues = df_test.apply(lambda x: x['issues'], 1)
df_obj_issues = pd.DataFrame(obj_issues)


# for i in range(1, 5):
#     d = {}
#     for n in obj:
#         d["x{0}".format(i)] = pd.concat([pd.DataFrame(n)], ignore_index=True)
#     print(d)

# new_df = pd.DataFrame()

# new_df = pd.concat([new_df, df_obj], ignore_index = True)

