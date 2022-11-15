import json

from sklearn.datasets import load_wine
from datetime import timedelta
import pandas as pd
import numpy as np

hive_git = pd.read_csv('git_csv/git_hive.csv')
hive_sonar = pd.read_csv('Sonar_hive_issues_16ec655.csv')

# df_git = pd.DataFrame(read_file_hive_git)
# df_sonar = pd.DataFrame(read_file_hive_sonar)

re = pd.read_json('rule_smells.json')
