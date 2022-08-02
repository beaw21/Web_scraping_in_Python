import json

from datetime import timedelta
import pandas as pd
import numpy as np
import requests
import io

pull_closed = requests.get('https://api.github.com/repos/apache/hive/pulls?state=closed').content
rawData = pd.read_csv(io.StringIO(pull_closed.decode('utf-8')))
print(rawData)

list_rawData = list(rawData)
