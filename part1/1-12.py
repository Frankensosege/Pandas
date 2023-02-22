import pandas as pd

exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)
print()

df.set_index('이름', inplace=True) # 열명이 Data에 포함되어 열명을 설정할 경우
print(df)
print()

a = df.loc['서준', '음악']
print(a)
print(type(a))
print()

b = df.iloc[0, 2]
print(b)
print(type(b))
print()

c = df.loc['서준', ['음악', '체육']] # == c = df.iloc[0, [2, 3]]
print(c)
print(type(c))
print()

e = df.loc['서준', '영어':'체육'] # == e = df.iloc[0, 1:]
print(c)
print(type(c))
print()

g = df.loc[['서준', '우현'], ['영어', '체육']] # == g = df.iloc[[0, 1], [2,3]]
print(g)
print(type(g))
print()

h = df.loc['서준':'우현', '영어':'체육'] # == h = df.iloc[0:1, 2:]
print(h)
print(type(h))
print()