# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import json

class TestScrapyItem(scrapy.Spider):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = 'quotes'
    allowed_domains = ['https://github.com/apache/hive/pulls']
    start_url = ['https://api.github.com/repos/apache/hive/pulls']

    # test function response
    def parse(self, response):
        resp = json(response.boby)
        quotes = resp.get('quotes')
        print(quotes)
