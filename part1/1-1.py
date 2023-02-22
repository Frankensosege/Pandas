import pandas as pd

list_a = ['2019-01-02', 3.14, 'ABC', 100, True]

sr = pd.Series(list_a)

print(sr)

idx = sr.index
print(idx)
print(type(idx))
val = sr.values
print(val)
