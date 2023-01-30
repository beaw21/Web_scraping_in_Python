import pandas as pd
from fikle_test import call_api

git_commits = pd.read_csv("git_csv/git_hive.csv")
git_pull = pd.read_csv("git_csv/git_hive_pull.csv")

git_pull_drop = git_pull.drop(columns=['url_pull', 'commits_url', 'user_url'])

# result = pd.concat([git_commits, git_pull_drop], ignore_index=True, sort=False)

sonar_issues = pd.read_csv("sonar/Sonar_hive_issues_16ec655.csv")

git_all = pd.concat([git_commits , git_pull_drop], axis=1)

new_df = pd.merge(git_commits , git_pull_drop , on='commit_sha')

