import pandas as pd

file_path = "./read_csv_sample.csv"

df = pd.read_csv(file_path)
print(df)
print()


df1 = pd.read_csv(file_path, header=None)
print(df1)
print()


df2 = pd.read_csv(file_path, index_col=None) # index_col=None default
print(df2)
print()


df3 = pd.read_csv(file_path, index_col='c0')
print(df3)
print()