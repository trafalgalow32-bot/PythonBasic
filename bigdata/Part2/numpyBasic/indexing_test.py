# indexing_test.py

import numpy as np
import pandas as pd

# 1차원 배열 객체
print("===========1차원===========")
arr_1d = np.array([1,2,3,4,5])

print(arr_1d[0])
print(arr_1d[2])
print(arr_1d[4])
print(arr_1d[-1])
print("===========2차원===========")
# 2차원 배열 객체
arr_2d = np.array([[1,2,3],
                   [4,5,7],
                   [6,8,9],
                   [11,17,19]])
print(arr_2d[0,0])
print(arr_2d[-4,-3]) # -4번 행 인덱스와 -3번 열 인덱스로부터 값 하나 참조
print(arr_2d[2,1]) # 2번 행 인덱스와 1번 열 인덱스로부터 값 하나 참조
print(arr_2d[-2,-2]) # -2번 행/열 인덱스로부터 값 하나 참조