import pandas as pd

from file_test_functions import loop_items


data_test = pd.read_csv('git_csv/git_hive.csv')
# call_api(commit)

loop_items(data_test['url'])
