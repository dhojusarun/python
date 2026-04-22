import pandas as pd

df = pd.read_csv("HAM10000_metadata.csv", delimiter=",")

print(df.head(10))

print(df.tail(10))

# how may null values
print(df.isnull().sum())

# how many duplicate values
print(df.duplicated().sum())


#remove null values
df.dropna()
print(df)
df.dropna(inplace=True)
print(df)

#remove duplicates
df.drop_duplicates(inplace=True)

#remove columns
df.drop("name", axis=1, inplace=True)

#remove rows
df.drop(0, axis=0, inplace=True)
