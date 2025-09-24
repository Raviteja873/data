import pandas as pd
import numpy as np

df = pd.read_csv("titanic_train.csv")
print(df.head())


print(df.isnull().sum())


df['Age'] = df['Age'].fillna(df['Age'].mean())


print(df.isnull().sum())

