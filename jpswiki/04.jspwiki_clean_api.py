import pandas as pd
from natsort import natsorted
df = pd.read_csv("02.Get_pull_url.csv")

# Select Columns by labels
label = df[['url' , 'id', 'node_id', 'number',
            'state', 'created_at', 'updated_at',
            'closed_at', 'merged_at', 'merge_commit_sha',
            'commits', 'additions', 'deletions',
            'changed_files', 'user.login', 'user.id',
            'user.type', 'head.sha', 'head.user.login',
            'head.user.id', 'head.user.type', 'head.repo.id',
            'base.label', 'base.sha', 'base.repo.created_at',
            'base.repo.updated_at', 'base.repo.pushed_at']]


label_time = df[['created_at', 'updated_at', 'closed_at', 'merged_at',
                 'base.repo.created_at', 'base.repo.updated_at', 'base.repo.pushed_at']]

label_time.apply(pd.to_datetime)
df['url']  = natsorted(df['url'])

# base is open commits
# check git branches each of commits
base_sha =  df.drop_duplicates(subset=['base.sha'])
# base_sha['base.ref'].to_csv('jspwiki_branches.text', index=False, header=None, sep="\n")
# base_sha['base.sha'].to_csv('jspwiki_base.text', index=False, header=None, sep="\n")

# merge is close commits
merge_draft_false = df.loc[df['merged'] == False]
merge_draft_true = df.loc[df['merged'] == True]

merge = merge_draft_true['merge_commit_sha'].drop_duplicates()
# merge.to_csv('jspwiki_merge.text', index=False, header=None, sep="\n")
