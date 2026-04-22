import pandas as pd

df = pd.read_csv("HAM10000_metadata.csv", delimiter=",")

print(df.head(10))

print(df.tail(10))

# how may null values
print(df.isnull().sum())

# how many duplicate values
print(df.duplicated().sum())


