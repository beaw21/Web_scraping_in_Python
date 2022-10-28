import json

from sklearn.datasets import load_wine
from datetime import timedelta
import pandas as pd
import numpy as np

read_file_hive_git = pd.read_csv('git_hive.csv')
read_file_hive_sonar = pd.read_csv('Sonar_hive_issues.csv')

df_git = pd.DataFrame(read_file_hive_git)
df_sonar = pd.DataFrame(read_file_hive_sonar)

re = pd.read_json('rule_smells.json')
