import json

import pandas as pd
import requests

for num in range(1, 10):
    with open("commit_" + str(num) +".csv", 'w') as f:
        f.write(str(num) + "\n" + str(10 - num))
        f.close()
        # f.write("name_api".format(json))
    print(f)
