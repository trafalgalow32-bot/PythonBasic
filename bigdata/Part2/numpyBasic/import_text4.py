# import_test3.py 교재 69-70p

import numpy as np
import pandas as pd

"""
ndarray 정보 확인 : 메서드
"""

#ndarray 생성
#1d-array
arr_1d = np.array([1,2,3,4])
print(arr_1d)

#2d-array
arr_2d = np.array([[1,2,3,4], [5,6,7,8,]])
print(arr_2d)

#3d-array
arr_3d = np.array([[1,2,3,4], [5,6,7,8],
                   [2,4,6,8], [10,12,14,16],
                   [1,3,5,7], [9,11,13,15]
                   ])
print(arr_3d)

#.shape : 배열객체의 형상 정보. 배열 객체의 [층,] 행, [열]의 수
print(arr_1d.shape) # 1d-array의 경우 (길이,)와 같은 형태로 반환

print(arr_2d.shape) # 2d-array의 경우 (행길이, 열길이)와 같은 형태로 반환

print(arr_3d.shape) # 3d-array의 경우 (층 수, 행길이, 열길이)와 같은 형태로 반환

#.size : 배열 객체의 총 원소의 수
print(arr_1d.size)

print(arr_2d.size)

print(arr_3d.size)

#.ndim : 배열 객체의 차원의 수
print(arr_1d.ndim)

print(arr_2d.ndim)

print(arr_3d.ndim)

print("==============리얼 3차원===============")
# 진짜 3차원 배열 예시: (3층, 2행, 4열)
arr_real_3d = np.array([
    [[1, 2, 3, 4], [5, 6, 7, 8]],      # 1층
    [[2, 4, 6, 8], [10, 12, 14, 16]],  # 2층
    [[1, 3, 5, 7], [9, 11, 13, 15]]    # 3층
])

print(arr_real_3d.ndim)   # 출력: 3
print(arr_real_3d.shape)  # 출력: (3, 2, 4)