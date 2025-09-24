import pandas as pd

df = pd.read_csv("big_mart_data.csv")

df['Item_Weight_bin'] = pd.cut(df['Item_Weight'], bins=3, labels=['Low','Medium','High'])
print(df[['Item_Weight','Item_Weight_bin']].head())
