import pandas as pd

tup_data = ('영인', '2010-05-01', '여', True)

sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr)
print()
print(sr['이름'])
print()
print(sr[0])
print()
print(sr[[1, 2]])
print()
print(sr[["이름", "성별"]])
print(sr["이름":"성별"])
print()
print(sr[0:3])