import pandas as pd
import requests

git_pull = pd.read_csv('git_hive.csv')
# git_commits = pd.read_csv('git_commit.csv')

sonar_rule = pd.read_json('rule_smells.json')
