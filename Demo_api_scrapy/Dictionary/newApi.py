import pandas as pd
import numpy as np
import requests
import io

pull_closed = requests.get('https://api.github.com/repos/apache/hive/pulls/3509')

data_json_pull_closed = pull_closed.json()
