import pandas as pd

file_path = "./남북한발전전력량.xlsx"
df = pd.read_excel(file_path, engine='openpyxl') # 예전버전 엑셀 engine='?????'

print(df)

df1 = pd.read_excel(file_path, engine='openpyxl', header=None)
print(df1)
print()