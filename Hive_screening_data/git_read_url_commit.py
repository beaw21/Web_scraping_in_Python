import pandas as pd

commit_file = pd.read_csv('git_hive_commit1_1')
commit_file_x = pd.read_csv('git_hive_commit1')
x = commit_file_x.dropna(thresh=2)
