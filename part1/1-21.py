import pandas as pd
import numpy as np

sudent1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
sudent2 = pd.Series({'수학':80, '국어':90})
print(sudent1)
print(sudent2)
print()

add_st = sudent1 + sudent2
sub_st = sudent1 - sudent2
multi_st = sudent1 * sudent2
dive_st = sudent1 / sudent2
result = pd.DataFrame([add_st, sub_st, multi_st, dive_st], index=['덧셈', '뺄셈', '곰셈', '나눗셈'])
print(result)
print()

add_st1 = sudent1.add(sudent2, fill_value=0)
sub_st1 = sudent1.sub(sudent2, fill_value=0)
multi_st1 = sudent1.mul(sudent2, fill_value=0)
dive_st1 = sudent1.div(sudent2, fill_value=0)
result = pd.DataFrame([add_st1, sub_st1, multi_st1, dive_st1], index=['덧셈', '뺄셈', '곰셈', '나눗셈'])
print(result)
print()