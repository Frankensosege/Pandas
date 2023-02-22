import pandas as pd

exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)
print()

print("=========== 데이터 프레임 전치 = 메소드 활용=============")
df = df.transpose()
print(df)
print("=========== 데이터 프레임 전치 = 클래스 속섣 활용=============")
print(df.T)
print(type(df.T))