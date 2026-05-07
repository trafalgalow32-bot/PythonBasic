#ndarray_calc_text.py

"""
ndarray 배열객체에 대한 산술연산자 또는 범용 함수(univcersal functions; nddary 안의 원소별 연산을 수행하는 함수)
범용 함수 - 단일 배열객체 // 서로 다른 배열
"""

import numpy as np
import pandas as pd

 # 단일 배열객체에 대한 범용 함수 (arr_1)
 # 1d-array 객체 생성
print("1d-array 객체: arr_1")
arr_1 = np.array([0, 1, -4 ,9 ,-16, 25])
print(arr_1)

# abs: 원소별 절대값을 반환(abs는 파이썬 기본 내장함수로도 가능!)
print("원소별 절대값")
arr_1_abs = np.abs(arr_1)
print(arr_1_abs)

# fabs: 원소별 절대값을 반환(abs보다 빠름) : 복소수가 아닌 경우 빠르게 연산 가능! floating
print("원소별 절대값:fabs")
arr_1_fabs = np.fabs(arr_1)
print(arr_1_fabs)

# sqrt : 원소별 제곱근 값 반환
print("원소별 제곱근")
arr_1_sqrt = np.sqrt(arr_1)
print(arr_1_sqrt)

# square : 원소별 제곱 값을 반환
print("원소별 제곱")
arr_1_square = np.square(arr_1)
print(arr_1_square)


# arr_1 = np.array([0, 1, -4 ,9 ,-16, 25])

# exp : 원소별 밑이 e인 지수 함수 값을 반환
print("원소별 e")
arr_1_exp = np.exp(arr_1)
print(arr_1_exp)

# log : 원소별 자연로그 값을 반환, 음수는 nan, 0은 -inf 반환됨. 밑이 e인 자연로그!!!
print("원소별 log")
arr_1_log = np.log(arr_1)
print(arr_1_log)

# log10 : 원소별 상용로그 값을 반환. 음수는 nan, 0은 -inf 반환
print("원소별 log10")
arr_1_log10 = np.log10(arr_1)
print(arr_1_log10)

# sign : 원소별 부호 값을 반환
print("원소별 sign")
arr_1_sign = np.sign(arr_1)
print(arr_1_sign)

"""
단일 배열 객체의 소숨저을 처리하는 범용 함수
"""

#1d-array 객체 생성
print("1d-array 객체: arr_2")
arr_2 = np.array([1.15, -2.33, 3.457, -4.095])
print(arr_2)

#round : 원소별 소수점을 원하는 자릿수까지 반올림한 값을 반환
print("원소별 소수점")
arr_2_round = np.round(arr_2)
print(arr_2_round)

arr_2_round_decimals_1 = np.round(arr_2,1)
print(arr_2_round_decimals_1)

#ceil : 원소별 소수점을 올림한 값을 반환
print("원소별 올림값")
arr_2_ceil = np.ceil(arr_2)
print(arr_2_ceil)


# arr_2 = np.array([1.15, -2.33, 3.457, -4.095])

#floor : 원소별 소수점을 내림한 값을 반환
print("원소별 내림값")
arr_2_floor = np.floor(arr_2)
print(arr_2_floor)

#trunc : 원소별 소수점을 잘라버린 값을 반환
print("원소별 자른값")
arr_2_trunc = np.trunc(arr_2)
print(arr_2_trunc)

"""
서로 다른 배열객체의 범용 함수: 산술 연산과 관련되어 있으며, 함수가 아닌 연산자로 대신 사용 가능
"""

#1d-array 객체 생성
print("1d-array 객체: arr_3")
arr_3 = np.arange(5) # 0 1 2 3 4
print(arr_3)

print("1d-array 객체: arr_4")
arr_4 = np.arange(1, 10 , step=2) # 1 3 5 7 9
print(arr_4)

# add : 두 배열객체의 원소 별 덧셈
print("두 배열 객체의 합: arr_3 + arr_4")
arr_add_1 = np.add(arr_3, arr_4)
print(arr_add_1)

# 연산자 +로 대체
print("+로 대체한 합")
arr_add_2 = arr_3 + arr_4
print(arr_add_2)

#subtract : 두 배열객체의 원소별 뺄셈
print("두 배열 객체의 차: arr_3 - arr_4") # 0 1 2 3 4 // # 1 3 5 7 9
arr_subtract_1 = np.subtract(arr_3, arr_4)
print(arr_subtract_1)

# 연산자 -로 대체
print("-로 대체한 합")
arr_subtract_2 = arr_3 - arr_4
print(arr_subtract_2)

# multiply : 두 배열객체의 원소 별 곱셈
print("두 배열 객체의 곱")
arr_mulitply_1 = np.multiply(arr_3, arr_4)
print(arr_mulitply_1)

# 연산자 *로 대체
print("*으로 대체한")
arr_mulitply_2 = arr_3 * arr_4
print(arr_mulitply_2)

# devide : 두 배열 객체의 원소별 나눗셈
print("두 배열 객체의 나눗셈")
arr_divide_1 = np.divide(arr_3, arr_4)
print(arr_divide_1)

# 연산자 /로 대체
print("/으로 대체한")
arr_divide_2 = arr_3 / arr_4
print(arr_divide_2)

# mod : 두 배열객체의 원소별 나눈 후 나머지
print("두 배열 객체의 나눗셈 후 나머지")
arr_mod_1 = np.mod(arr_3, arr_4)
print(arr_mod_1)

# 연산자 %로 대체
print("%으로 대체한")
arr_mod_2 = arr_3 % arr_4
print(arr_mod_2)
