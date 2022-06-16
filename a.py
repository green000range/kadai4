import pandas as pd
df = pd.read_csv("e.py\FEH_00200521_220610143730.csv",index_col=0)

#kodo = df[(df['コード'] == 0.1)]

print(df.describe())
