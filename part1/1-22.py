import pandas as pd
import seaborn as sns

tatinic = sns.load_dataset('titanic')
df = tatinic.loc[:, ['age', 'fare']]

print(df.head())
print()

addition = df + 10
print(addition.head())
print()


subtle = addition - 10
print(subtle.tail())
print()

remain = addition - subtle
print(remain.tail())
print()