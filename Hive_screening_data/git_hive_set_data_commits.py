import pandas as pd

com1 = pd.read_csv("git_csv/git_hive_commits_dict_1_140.csv")
com2 = pd.read_csv("git_csv/git_hive_commits_dict_141.csv")
com3 = pd.read_csv("git_csv/git_hive_commits_dict_306.csv")
com4 = pd.read_csv("git_csv/git_hive_commits_dict_536.csv")
com5 = pd.read_csv("git_csv/git_hive_commits_dict_717.csv")

get_all = pd.concat([com1, com2, com3, com4, com5])

new_commits = pd.DataFrame({
    'commit_sha': get_all['sha'],
    'commit_node_id': get_all['node_id'],
    'commit_parents': get_all['parents'],
    'commit_name': get_all['commit.committer.name'],
    'commit_email': get_all['commit.committer.email'],
    'commit_date': get_all['commit.committer.date'],
    'commit_name_author': get_all['commit.author.name'],
    'commit_email_author': get_all['commit.author.email'],
    'commit_date_author': get_all['commit.author.date']
})

# new_commits.to_csv("git_commits_test_data_986.csv")
