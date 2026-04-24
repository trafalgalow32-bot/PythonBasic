# import_test3.py 교재 68p

import numpy as np
import pandas as pd

#3d-array 생성, 리스트 객체를 3차원 배열로
arr1 = np.array([[1,2,3,4], [5,6,7,8],
                 [2,4,6,8], [10,12,14,16],
                 [1,3,5,7], [9,11,13,15]])
print(arr1)

# 모든 값이 1이고 3층 2행 4열인 3차원 배열 생성
arr2 = np.ones((3,2,4), dtype = 'int')
print(arr2)

# 모든 값이 0이고 3층 2행 4열인 3차원 배열 생성
arr3 = np.zeros((3,2,4), dtype= 'int')
print(arr3)

# 모든 값이 5이고 3층 2행 4열인 3차원 배열 생성
arr4 = np.full((3,2,4), 5)
print(arr4)