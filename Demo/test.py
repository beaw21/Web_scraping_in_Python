import pandas as pd

# create a sample dataframe
df = pd.DataFrame({'ID': [1, 1, 2, 2, 3],
                   'Data': ['A', 'B', 'C', 'D', 'E'],
                   'Date': ['2023-01-01', '2023-02-01', '2023-01-15', '2023-02-15', '2023-03-01']})

# convert the 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# sort the dataframe by 'Date' in descending order
df = df.sort_values(by='Date', ascending=False)

# extract only the latest data for each ID
latest_data = df.groupby('ID').apply(lambda x: x.loc[x['Date'].idxmax()]).reset_index(drop=True)

print(latest_data)
