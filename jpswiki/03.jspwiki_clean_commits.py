import pandas as pd
from natsort import natsorted

df_all = pd.read_csv('get_pull_commits_all.csv')
gb_df = df_all.groupby(by='index')['commit.committer.date'].agg(['max', 'min'])

df = pd.DataFrame(df_all)

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

# create empty dataframes to hold the results
data_set_count = pd.DataFrame(df_drop_col)
# convert the 'Date' column to datetime type
data_set_count['commit.author.date'] = pd.to_datetime(data_set_count['commit.author.date'])

# sort the dataframe by 'Date' in descending order
df_set_date = data_set_count.sort_values(by='commit.author.date', ascending=False)

# extract only the latest data for each INDEX
latest_data = df_set_date.groupby('index').apply(lambda x: x.loc[x['commit.author.date'].idxmax()]).reset_index(drop=True)
# sort the data using natsort
latest_data['index'] = natsorted(latest_data['index'])

# x = latest_data[['sha']]
# x.to_csv("sha_1.csv" , sep='\n' ,  index=False)
# x.to_csv('sha.txt', header=None, index=False, sep=' ', mode='a')
