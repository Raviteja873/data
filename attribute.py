import pandas as pd

df = pd.read_csv("titanic_train.csv")

df = df.fillna(df.mean(numeric_only=True))
df = df.fillna(df.mode().iloc[0])

df = df.drop(['Name','Ticket','Cabin'], axis=1)

df['Sex'] = df['Sex'].map({'male':0,'female':1})
df['Embarked'] = df['Embarked'].map({'S':0,'C':1,'Q':2})

print(df.corr()['Survived'])
