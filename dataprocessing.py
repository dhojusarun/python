import pandas as pd

df = pd.read_csv("first.csv", delimiter=",")

print(df.head(10))

print(df.tail(10))

# how may null values
print(df.isnull().sum())

# how many duplicate values
print(df.duplicated().sum())


# remove null values
df.dropna()
print(df)
df.dropna(inplace=True)
print(df)

# remove duplicates
df.drop_duplicates(inplace=True)

# remove columns
df.drop("name", axis=1, inplace=True)

# remove rows
df.drop(0, axis=0, inplace=True)


# transform data
def convert_to_numeric(location):
    if location == "ktm":
        return 1
    elif location == "bkt":
        return 2
    else:
        return 3


df["address"] = df["address"].apply(convert_to_numeric)
print(df)
