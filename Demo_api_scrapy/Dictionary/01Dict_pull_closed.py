import json
import importlib

from datetime import timedelta
import pandas as pd
import numpy as np
import requests
import io

import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

pull_closed = requests.get('https://api.github.com/repos/apache/hive/pulls?state=closed')
data_json_pull_closed = pull_closed.json()

length = list(data_json_pull_closed)

df = pd.DataFrame(length)

new_data = []

new_df = pd.DataFrame(new_data)
new_df['ID'] = df['id'].values
new_df['url_pull'] = df['url'].values

myDict = {}
myDict["ID_pulls"] = new_df['ID']
myDict["pulls"] = new_df['url_pull']

Dict = pd.DataFrame.from_dict(new_df)
print(Dict)

get_requests_url = requests.get(Dict['url_pull']).json()
print(get_requests_url)

set_index = Dict.set_index("ID").to_dict()["url_pull"]

Dict.apply(lambda x: x["url_pull"], 1)
