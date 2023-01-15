import pandas as pd

from file_test_functions import loop_items
from file_test_functions import call_api

data_test = pd.read_csv('git_csv/git_hive.csv')

data = data_test['url'].head(5)
loop_items(data)
