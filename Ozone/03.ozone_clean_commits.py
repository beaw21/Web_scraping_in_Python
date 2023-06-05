import pandas as pd
from natsort import natsorted

df = pd.read_csv('02.ozone_all.csv')

# Select Columns by labels

label_time = df[['created_at', 'updated_at', 'closed_at', 'merged_at',
                 'base.repo.created_at', 'base.repo.updated_at', 'base.repo.pushed_at']]

label_time.apply(pd.to_datetime)
df['url'] = natsorted(df['url'])

# base is open commits
# check git branches each of commits
base_sha = df.drop_duplicates(subset=['base.sha'], keep='last')
base_sha['base.ref'].to_csv('ozone_branches.text', index=False, header=None, sep="\n")
base_sha['base.sha'].to_csv('ozone_base.text', index=False, header=None, sep="\n")

# merge is close commits
merge_draft_false = df.loc[df['merged'] == False]
merge_draft_true = df.loc[df['merged'] == True]

merge = merge_draft_true['merge_commit_sha'].drop_duplicates()
merge.to_csv('ozone_merge.text', index=False, header=None, sep="\n")
