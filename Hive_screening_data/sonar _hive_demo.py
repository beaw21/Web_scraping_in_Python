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

x1 = pd.DataFrame(df_obj_issues[0][0])
x2 = pd.DataFrame(df_obj_issues[0][1])
x3 = pd.DataFrame(df_obj_issues[0][2])
x4 = pd.DataFrame(df_obj_issues[0][3])
x5 = pd.DataFrame(df_obj_issues[0][4])
x6 = pd.DataFrame(df_obj_issues[0][5])
x7 = pd.DataFrame(df_obj_issues[0][6])
x8 = pd.DataFrame(df_obj_issues[0][7])
x9 = pd.DataFrame(df_obj_issues[0][8])
x10 = pd.DataFrame(df_obj_issues[0][9])
x11 = pd.DataFrame(df_obj_issues[0][10])
x12 = pd.DataFrame(df_obj_issues[0][11])
x13 = pd.DataFrame(df_obj_issues[0][12])
x14 = pd.DataFrame(df_obj_issues[0][13])
x15 = pd.DataFrame(df_obj_issues[0][14])
x16 = pd.DataFrame(df_obj_issues[0][15])
x17 = pd.DataFrame(df_obj_issues[0][16])
x18 = pd.DataFrame(df_obj_issues[0][17])
x19 = pd.DataFrame(df_obj_issues[0][18])
x20 = pd.DataFrame(df_obj_issues[0][19])

con_data = pd.concat([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10,
                      x11, x12, x13, x14, x15, x16, x17, x18, x19, x20])

# con_data.to_csv('Hive_issues.csv')
