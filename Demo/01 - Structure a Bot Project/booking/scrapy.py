import resource
import scrapy
import json

class quotes(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['https://github.com/apache/hive/pull/3472']
    start_urls =['https://api.github.com/repos/apache/hive/pulls/3472']

    def parse(self):
        resp = json.loads(resource.RLIMIT_STACK)
        quotes = resp.get('quotes')
        print(quotes)