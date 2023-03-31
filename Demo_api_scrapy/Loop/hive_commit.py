import pandas as pd

df_all = pd.read_csv('commit_of_all_pull_hive.csv')
gb_df = df_all.groupby(by='index')['commit.committer.date'].agg(['max', 'min'])

df = pd.DataFrame(df_all)
# counts_all = df_all['index'].value_counts()
# counts_commit_all = counts_all.reset_index()

df_drop_col = df.drop(columns=['url', 'html_url', 'comments_url',
                               'commit.tree.url', 'commit.url',
                               'commit.comment_count', 'commit.verification.verified',
                               'commit.verification.reason', 'commit.verification.signature',
                               'commit.verification.payload', 'author.avatar_url',
                               'author.gravatar_id', 'author.html_url', 'author.followers_url', 'author.following_url',
                               'author.following_url', 'committer.starred_url', 'author.events_url',
                               'author.received_events_url',
                               'author.type', 'author.site_admin', 'committer.avatar_url', 'committer.gravatar_id',
                               'committer.html_url', 'committer.followers_url', 'committer.following_url',
                               'committer.repos_url',
                               'committer.events_url', 'committer.received_events_url', 'committer.type',
                               'committer.site_admin', 'committer', 'author'
                               ])

for i, row in df_drop_col.iterrows():
    count = df_drop_col.loc[df_drop_col['index'] == row['index']].shape[0]
    df_drop_col.loc[i, 'count'] = count
    # print(count)
print(df_drop_col)

counts_pull_greater_than_one = []
counts_pull_equal_one = []

# create empty dataframes to hold the results
equal = pd.DataFrame(df_drop_col)

# # loop through dataframe
for index, row in df_drop_col.iterrows():
    if row['count'] > 1:
        greater_than_ones = counts_pull_greater_than_one.append(row)
    else:
        equal_ones = counts_pull_equal_one.append(row)

print("Values equal one :")
print(counts_pull_equal_one)
print("Values greater than one:")
print(counts_pull_greater_than_one)


# series_greater_one = pd.Series(counts_pull_greater_than_one)
# series_equal_one = pd.Series(counts_pull_equal_one)
# df_greater_one = pd.DataFrame(series_greater_one)
# df_equal_one = pd.DataFrame(series_equal_one)
