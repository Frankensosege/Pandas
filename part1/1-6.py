import pandas as pd

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

df2 = df[:]

df2.drop('우현', inplace=True) # == df2 = df2.drop('우현') axis = 0 이 default 열삭제시 필수 axis = 1
print(df2)

df3 = df2.drop(['서준', '인아'])
print(df3)