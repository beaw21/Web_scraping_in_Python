import pandas as pd
import pdb

df = pd.read_json('rule_smells.json')

rules = df.rules


for i in range(1, rules.shape[0]):
    print('col :', i)
    so_r = rules.iloc[i]
    print(so_r)
    # so_r.to_csv('sonar_rules_smell.csv')
