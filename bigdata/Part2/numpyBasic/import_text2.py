# import_test2.py 교재 67p

import numpy as np
import pandas as pd

# 2행 5열
arr1 = np.array([[1,3,5,7,9], [2,4,6,8,10]])
print(arr1)

# 3행 3열
arr2 = np.array([[1,2,3], [4,5,6,], [7,8,9]])
print(arr2)

# 모든 값이 1(정수)이고 행의 수가 2, 열의 수가 5개인 2차원 배열 생성
arr3 = np.ones((2,5), dtype= 'int') # dtype 생략할 경우 실수로 자동 생성
print(arr3)

# 모든 값이 0(정수)이고 행의 수가 2, 열의 수가 5개인 2차원 배열 생성
arr4 = np.zeros((2,5), dtype= 'int') 
print(arr4)

# 모든 값이 5(정수)이고 행의 수가 2, 열의 수가 5개인 2차원 배열 생성
arr5 = np.full((2,5), 5)
print(arr5)

# 주 대각성분이 1인 행과 열의 수가 5개인 정사각 2차원 배열 생성(항등행렬과 유사)
arr6 = np.identity(5)
print(arr6)