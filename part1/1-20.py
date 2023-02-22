import pandas as pd

sudent1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(sudent1)
print()

percetage = sudent1/200

print(percetage)
print(type(percetage))
print()

sudent2 = pd.Series({'수학':80, '국어':90, '영어':60 })
print(sudent1)
print(sudent2)
print()
add_st = sudent1 + sudent2
sub_st = sudent1 - sudent2
result = pd.DataFrame([add_st, sub_st], index=['덧셈', '뺄셈'])
print(result)
print()
