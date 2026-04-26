# slicing_test.py
"""
인덱싱과 달리 슬라이싱은 음수일 경우에도 정방향!!
"""

import numpy as np
import pandas as pd

# 1차원 배열 객체
print("===========1차원===========")
arr_1d = np.array([1,2,3,4,5])

print(arr_1d[0:2])
print(arr_1d[:2])
print(arr_1d[1:4])
print(arr_1d[-4:-1])
print(arr_1d[1:-1])
print(arr_1d[3:5])
print(arr_1d[3:])
print(arr_1d[-2:])
print("===========2차원===========")
# 2차원 배열 객체
arr_2d = np.array([[1,2,3,5],
                   [1,3,5,7],
                   [2,4,6,9],
                   [7,11,13,17]])
print(arr_2d[0:4,0]) # r1:42
print(arr_2d[:4,0]) # r1=0이므로 생략 가능
print(arr_2d[:,0]) # r1=0이고 r2=행길이 이므로 생략 가능
#행/열 : 처음(인덱스 0번)부터 인덱스 3번(-1번) 사이의 구간
print(arr_2d[0:3, 0:3])
print(arr_2d[:3, :3]) # r1=c1=0으로 생략 가능
print(arr_2d[:-1, :-1]) # r1=c1=0으로 생략 가능
#행/열 : 처음 바로 뒤(1번 또는 -3번)부터 마지막 바로 앞(-1번 또는 3번) 사이의 구간
print(arr_2d[1:3, 1:3])
print(arr_2d[-3:-1, -3:-1])
print(arr_2d[1:-1, 1:-1])
#행: 처음 바로 뒤(1번 또는 -3번)부터 마지막 바로 앞(-1번 또는 3번) 사이의 구간
#열: 전체
print(arr_2d[1:3, 0:4])
print(arr_2d[1:3, :])
print(arr_2d[1:-1, :])
#행: 마지막 행, 열: 열 전체
print(arr_2d[3, 0:4])
print(arr_2d[3, :]) # c1=0이고 c2=열길이이므로 생략 가능
print(arr_2d[-1, :]) # c1=0이고 c2=열길이이므로 생략 가능
#행/열 : 2번(또는 -2번)부터 마지막 인덱스 사이의 구간
print(arr_2d[2:4, 2:4])
print(arr_2d[2:, 2:]) # c2=열길이이므로 생략 가능
print(arr_2d[-2:, -2:]) # c2=열길이이므로 생략 가능