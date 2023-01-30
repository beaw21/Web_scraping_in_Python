import pandas as pd
import json
commit_file = pd.read_csv('git_hive_commit_all')
x = commit_file.dropna(thresh=2)

data_commit = x['parents']

# series convert to frame
series_to_frame = pd.Series.to_frame(data_commit)

# frame -> json
result = series_to_frame.to_json(orient="split")
parsed = json.loads(result)
# ValueError: All arrays must be of the same length
# คิดว่าแต่ละ commit มีการแก้ไข้ commit ไม่เท่ากัน ???
data = pd.DataFrame.from_dict(parsed, orient='index')
# data.to_csv("/home/ec2-user/output/pull_commits")
# data.to_csv("pull_commits")

# get_commits = data.apply(lambda x: x[1], 1)
# jsonobj = json.dumps(parsed)

# json obj convert to frame
# df_nested_list = pd.json_normalize(jsonobj)


# data_loads_json = json.loads(jsonobj)
# df = pd.DataFrame.from_dict(data_loads_json, orient='index')
