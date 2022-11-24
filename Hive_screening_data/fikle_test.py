import pandas as pd
import time
import requests

commit = ['item_1', 'item_2', 'item_3', 'item_4', 'item_5', 'break', 'item_6', 'break', 'item_7', 'item_8', 'break',
          'item_9', 'break', 'item_10', 'item_11', 'item_12', 'item_13', 'break', 'item_14', 'item_15']
df = pd.DataFrame(commit, columns=['items'])

timeout = time.time() + 60*2

for i in df['items']:
    data_count = i
    print("data i :" + i)
    if i == 'break':
        break
    if timeout == 2 or time.time() > timeout:
        continue

