from pandas import *
import requests

test = requests.get('https://api.github.com/repos/apache/hive/pulls/3472/commits')

# test.json()[0]["commit"]["author"]