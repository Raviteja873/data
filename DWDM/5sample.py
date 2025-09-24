import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

items = [
    ['Milk','Bread','Butter'],
    ['Milk','Bread'],
    ['Milk','Eggs'],
    ['Bread','Butter'],
    ['Milk','Bread','Eggs']
]

df = pd.DataFrame(items)
table = pd.get_dummies(df.stack()).groupby(level=0).sum()
freq = apriori(table, min_support=0.4, use_colnames=True)
rules = association_rules(freq, metric="confidence", min_threshold=0.6)

print(rules[['antecedents','consequents','support','confidence']])
