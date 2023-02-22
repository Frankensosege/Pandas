import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                   index=['준서', '예은'],
                   columns=['나이', '성별', '학교'])

print(df)
print(df.columns)
print(df.index)
print(df.values)

df.index = ["학생1", "학생2"]
df.columns = ["연령", "남녀", "소속"]
print()
print(df)
print(df.columns)
print(df.index)
print(df.values)

df.rename(columns={"연령": '나이'}, inplace=True ) # 비파괴적 함수로 inplace = True 로 파괴적으로 바꾼다
df.rename(index={"학생1": '준서'}, inplace=True )
print("--------------------------------------------------")

print(df)
print(df.columns)
print(df.index)
print(df.values)