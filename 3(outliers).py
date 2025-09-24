import pandas as pd

df = pd.read_csv("churn_prediction.csv")

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

df_clean = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

print("Before:", df.shape)
print("After:", df_clean.shape)
