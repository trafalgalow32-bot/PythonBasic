#numpy_fun.py

import numpy as np
import pandas as pd

"""
NumPy의 주요 함수와 메소드
1. 형상 변환 메소드 : 배열객체. reshape(), ravel(), flatten(), transpose()
"""

# .reshape() : 배열 객체를 입력된 shape로 변환
# 길이가 8인 1d-array 객체 생성
print(".reshape()")
print("길이가 8인 1d-array 객체")
arr_1d = np.arange(8)
print(arr_1d)

# 행길이가 2이고 열길이가 4인 2d-array 객체로 변환
print("\n 행길이가 2이고 열길이가 4인 2d-array 객체")
arr_2d_2x4 = arr_1d.reshape(2,4)
print(arr_2d_2x4)

# 행길이가 4이고 열길이가 2인 2d-array 객체로 변환
print("\n 행길이가 4이고 열길이가 2인 2d-array 객체")
arr_2d_4x2 = arr_1d.reshape(4,2)
print(arr_2d_4x2)

# # 행길이가 3이고 열길이가 3인 2d-array 객체로 변환
# print("\n 행길이가 3이고 열길이가 3인 2d-array 객체")
# arr_2d_3x3 = arr_1d.reshape(3,3)
# print(arr_2d_3x3) ★ 오류나므로 주석 처리!!

"""
reshape 메소드 활용 :1차원 배열을 생성하여 2차원 배열로 변환
"""
print("===================================================")
# reshape 메소드 활용 예1 :(3,3)인 2차원 배열 변환
# 길이가 9인 1d-array 객체 생성
print("길이가 9인 1d-array 객체")
arr_1d = np.arange(9)
print(arr_1d)

# 행길이가 3이고 열길이가 3인 2d-array 객체로 변환
print("\n 행길이가 3이고 열길이가 3인 2d-array 객체")
arr_2d_3x3 = arr_1d.reshape(3,3)
print(arr_2d_3x3)

# -1 이용해 2d-array 객체로 변환. 행의 수를 3으로 지정하고 남은 차원(열) 알아서 정함
print("\n -1 이용해 2d-array 객체로 변환")
arr_2d_3xN = arr_1d.reshape(3,-1)
print(arr_2d_3xN)

# 열의 수를 3으로 지정하고 남은 차원(행)은 알아서 정함
print("\n 열의 수를 3으로 지정")
arr_2d_Nx3 = arr_1d.reshape(-1,3)
print(arr_2d_Nx3)

print("=====reshape 메소드 활용 2: (3,3)인 2차원 배열 생성=====")
"""
reshape 메소드 활용 2: (3,3)인 2차원 배열 생성
원소가 0~8이면서 (3,3)인 2d-array 객체 생성
"""
# 방법1. 
print("방법1.")
arr1 = np.array([[0,1,2,],
                 [3,4,5],
                 [6,7,8]])
print(arr1)

# 방법2.
print("\n 방법2.")
arr2 = np.arange(9).reshape(3,3)
print(arr2)

print("=====reshape 메소드 활용 3: (3,2,2)인 3차원 배열 생성=====")
"""
reshape 메소드 활용 3: (3,2,2)인 3차원 배열 생성
원소가 0~11이면서 층이 3층이고 행/열길이가 2인 3d-array 객체 생성
"""
# 방법1.
print("방법1.")
arr4 = np.arange(12).reshape(3,2,2)
print(arr4)

# 방법2.
print("\n 방법1.")
arr5 = np.arange(12).reshape(3,2,-1) # 층 수 3, 행 수 3으로 지정, 남은 차원(열) 자동
print(arr5)

# 방법3.
print("\n 방법3.")
arr6 = np.arange(12).reshape(-1,2,2) # 행/열의 수는 2로 지정, 남은 차원(층) 자동
print(arr6)

print("=====다차원 배열 객체를 1차원 배열로 변환(평탄화)=====")
"""
평탄화: 다차원 배열객체를 1차원 배열로 변환하는 과정. reshape 메소드로도 가능하지만, ravel과 flatten 메소드는 길이 일벽 없이 바로 수행 가능!
"""

# reshape 메소드 활용
print("\n reshape 메소드 활용. (3,3)인 2차원 배열을 길이가 9인 1차원 배열로 변환")
arr1_1d = arr1.reshape(9)
print(arr1_1d)

# (3,2,2)인 3차원 배열을 길이가 12인 1차원 배열로 변환
print("\n (3,2,2)인 3차원 배열을 길이가 12인 1차원 배열로 변환")
arr4_1d = arr4.reshape(12)
print(arr4_1d)

# ravel() : 다차원 배열객체를 1차원으로 평탄화함
print("\n ravel() : 다차원 배열객체를 1차원으로 평탄화함")
arr2_1d = arr2.ravel() # 길이 입력 불필요!
print(arr_1d)

arr5_1d = arr5.ravel() # 길이 입력 불필요!
print(arr_1d)

# flatten(): 다차원 배열객체를 1차원으로 평탄화함
print("\n flatten(): 다차원 배열객체를 1차원으로 평탄화함")
arr4_1d = arr4.flatten() # 길이 입력 불필요!
print(arr4_1d)

arr6_1d = arr6.flatten() # 길이 입력 불필요
print(arr6_1d)

print("\n =====transpose()=====")
# .transpose() : 배열의 축을 교환함
arr_2d = np.arange(8).reshape(4,2)
print(arr_2d)

arr_2d_T = arr_2d.transpose()
print(arr_2d_T)

print(arr_2d.T)