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


class ErrbackSpider(scrapy.Spider):
    name = "Pang pulls"
    start_urls_pulls = Dict['url_pull']

    def start_requests(self):
        for u in self.start_urls_pulls:
            yield scrapy.Request(u, callback=self.parse_httpbin, errback=self.errback_httpbin, dont_filter=True)

    def parse_httpbin(self, response):
        self.logger.info('Got successful response from {}'.format(response.url))
        print(response)
