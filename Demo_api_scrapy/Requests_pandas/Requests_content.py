import json
import importlib
import page_one

from datetime import timedelta
import pandas as pd
import numpy as np
import requests
import io


pull_closed = requests.get('https://api.github.com/repos/apache/hive/pulls?state=closed')
content = pull_closed.content
