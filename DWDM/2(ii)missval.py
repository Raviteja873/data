import pandas as pd

df = pd.read_csv("titanic_train.csv")
print("Before:\n", df.isnull().sum())

df = df.fillna(df.mean(numeric_only=True))
df = df.fillna(df.mode().iloc[0])

print("After:\n", df.isnull().sum())
