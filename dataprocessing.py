import pandas as pd

# delimeter is used to identify how data is separated
df = pd.read_csv("first.csv", delimiter=",")

print(df.head())