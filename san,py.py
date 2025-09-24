import pandas as pd

df = pd.read_csv("churn_prediction.csv")

numeric_df = df.select_dtypes(include=['float64','int64'])

Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)
IQR = Q3 - Q1

df_clean = df[~((numeric_df < (Q1 - 1.5 * IQR)) | (numeric_df > (Q3 + 1.5 * IQR))).any(axis=1)]

print("Before:", df.shape)
print("After:", df_clean.shape)
