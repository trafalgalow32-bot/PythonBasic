# import_test.py 교재65-66p

import numpy as np
import pandas as pd

# # 간단한 테스트 코드
# arr = np.array([1, 2, 3])
# print(f"NumPy 배열 생성 성공: {arr}")
# print(f"Pandas 버전 확인: {pd.__version__}")

arr1 = np.array([1,3,5,7,9])
print(arr1)

arr2 = np.array('dataedu')
print(arr2)

arr3 = np.arange(7)
print(arr3)

arr4 = np.arange(1, 6, 0.5)
print(arr4)

arr5 = np.ones(5)
print(arr5)

arr6 = np.zeros(5)
print(arr6)

arr7 = np.full(5, 4.)
print(arr7)