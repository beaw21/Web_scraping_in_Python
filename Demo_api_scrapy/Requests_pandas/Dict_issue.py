import pandas as pd
import requests

pull_number = requests.get('https://api.github.com/repos/apache/hive/pulls/{{$randomInt}}')

