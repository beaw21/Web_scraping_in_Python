import pandas as pd

from file_test_functions import loop_items
from file_test_func import cell_api

data_test = pd.read_csv('git_csv/git_hive.csv')

data = data_test['url'].head(5)
x = pd.DataFrame.from_dict(data)
# loop_items(data)
cell_api(x['url'])
