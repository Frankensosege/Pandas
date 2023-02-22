import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print()

print(df["수학"]) # == df.수학 열이름이 문자열일 경우 가능
print(type(df["수학"]))
print(df["수학":'체육'])
print(df[1:3])

print(type(df[1:3]))

########################## 비추
english = df.영어
print(english)