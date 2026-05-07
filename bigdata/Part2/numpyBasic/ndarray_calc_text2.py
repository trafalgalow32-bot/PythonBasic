#ndarray_calc_text2.py

"""
두 배열 객체가 서로 다른 길이, 차원, shape를 가질 경우!
"""

import numpy as np
import pandas as pd

# Case1. 길이가 다른 경우
# 길이가 3인 1d-array 생성
print("길이가 다른 경우. 길이 3인 1d-array")
arr_1d_3 = np.array([1,2,3])
print(arr_1d_3)

print(arr_1d_3.shape)

print("길이가 1인 1d-array")
arr_1d_1 = np.array([5])
print(arr_1d_1)

print(arr_1d_1.shape)

# 두 배열 객체의 합은 길이가 3인 1d-array가 됨
print("두 배열 객체의 합")
arr_add = arr_1d_3 + arr_1d_1
print(arr_add)

print(arr_add.shape)

#Case2. 차원이 다른 경우
#행길이 3, 열길이 3인 2d-array 생성
print("차원이 다른 경우. 행길이 3, 열길이 3인 2d-array")
arr_2d_3x3 = np.array([[1,4,7],
                       [2,5,8],
                       [3,6,9]])
print(arr_2d_3x3)

print(arr_2d_3x3.shape)

# 길이가 3인 1d-array 생성
print("길이가 3인 1d-array")
arr_1d_3 = np.array([1,0,-1])

print(arr_1d_3)

print(arr_1d_3.shape)

#두 배열 객체의 합은 행길이 3, 열길이 3인 2d-array가 됨
print("두 배열 객체의 합")
arr_add = arr_2d_3x3 + arr_1d_3

print(arr_add)

print(arr_add.shape)

# Case3. shape가 다른 경우
# 행길이 1, 열길이 3인 2d-array 생성
print("shape가 다른 경우. 행길이 1, 열길이 3인 2d-array")
arr_2d_1x3 = np.array([[1,2,3]])
print(arr_2d_1x3)

print(arr_2d_1x3.shape)

print(arr_2d_1x3.ndim)

# 행길이 3, 열길이 1인 2d-array 생성
print("행길이 3, 열길이 1인 2d-array")
arr_2d_3x1 = np.array([[1],
                       [0],
                       [-1]])
print(arr_2d_3x1)

print(arr_2d_3x1.shape)

print(arr_2d_3x1.ndim)

# 두 배열 객체의 합은 행길이 3, 열길이 3인 2d-array가 됨
print("두 배열 객체의 합. 행길이 3, 열길이 3인 2d-array")
arr_add = arr_2d_1x3 + arr_2d_3x1
print(arr_add)

print(arr_add.shape)