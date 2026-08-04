import pandas as pd

df = pd.read_csv("logistics_regrassions.csv")
df.to_csv("logistics_regrassions.csv", index=False, lineterminator="\n")
print(df.head())
