# pandas_test01.py

import numpy as np
import pandas as pd

"""
2장 Pandas를 활용한 데이터 다루기
1절. Series와 DataFrame
1. Series(시리즈)
 - 시리즈는 일차원 배열 데이터인 값(value)과 데이터의 레이블(label) 배열인 인덱스로 이루어진 구조원 1차원 객체
 - 1d-array객체와의 가장 큰 차이점은 시리즈 객체는 원소의 데이터 타입이 서로 달라도 된다는 점!

가. 시리즈의 생성: Series 함수를 통해 객체(시퀀스, 딕셔너리)를 시리즈 객체로 반환하여 생성
 pandas.Series(object, index) 
 object: 객체, 주로 리스트 등과 같은 시퀀스형 객체와 딕셔너리형 객체를 사용
 index: 원하는 인덱스(레이블 배열)를 지정할 때 사용. 별도 지정하지 않을 경우 위치 인덱스 번호로 자동 지정 
"""

# Series객체 생성: pd.Series(object, index)
# 1. object에 리스트(시퀀스) 객체 이용
print("1. object에 리스트(시퀀스) 객체 이용")
obj = ['이유리', '최민준', '김민지'] # 값 리스트
series_1 = pd.Series(obj) # 시리즈 생성
print(series_1)

# 원하는 인덱스 지정
print("\n 원하는 인덱스 지정")
idx = ['A', 'B', 'C'] # 인덱스 리스트
series_2 = pd.Series(obj, index = idx) # 시리즈 생성
print(series_2)

# 2. object에 딕셔너리객체 이용
print("\n 2. object에 딕셔너리객체 이용")
obj = {'A':'이유리', 'B':'최민준', 'C':'김민지'} # 딕셔너리
series_3 = pd.Series(obj) # 시리즈 생성
print(series_3)

"""
나. 시리즈의 정보 확인(시리즈객체)
.values : 시리즈객체 내 값을 배열 형태로 반환
.index : 시리즈객체 내 인덱스를 레이블 배열 형태로 반환
.dtypes : 시리즈객체의 데이터 타입 확인. 데이터 타입은 object(일반 문자), float(실수), int(정수), category(카테고리) 등이 있음
.size : 시리즈객체의 총 객체 수
"""
print("========================================================")
# 시리즈 정보 확인 메소드
print("시리즈 정보 확인 메소드: .values")
# .values
# 시리즈객체 내 값을 배열 형태로 반환
print(series_1.values)

print("\n 시리즈 정보 확인 메소드: .index")
# .index
# 시리즈객체 내 인덱스를 레이블 배열 형태로 반환
print(series_1.index)

print("\n 시리즈 정보 확인 메소드: .dtypes")
# .dtypes
# 시리즈객체의 데이터 타입 확인
print(series_1.dtypes)

print("\n 시리즈 정보 확인 메소드: .size")
# .size
# 시리즈객체의 총 객체 수
print(series_1.size)

print("\n 시리즈객체의 인덱스 변경")
# 시리즈객체의 인덱스 변경
print("\n 인덱스 변경 전")
print(series_1.index) # 변경 전
series_1.index = ['A', 'B', 'C'] # 변경
print("\n 인덱스 변경 후")
print(series_1.index)

print("========================================================")
"""
다. 시리즈의 인덱싱과 슬라이싱
 - 시리즈는 대괄호([])와 위치 인덱스 번호를 통한 인덱싱과 슬라이싱이 가능
 - 위치 기반 인덱스 번호 뿐만 아니라 레이블 기반 인덱스들로도 인덱싱 및 슬라이싱 가능
 - 시리즈명[위치인덱스] 또는 시리즈명[레이블인덱스]
"""
print("시리즈의 인덱싱과 슬라이싱 \n")
#시리즈 생성
obj = [22, 32, 27, 18, 38, 19] # 값 리스트
idx = list('abcdef') # 레이블 인덱스 리스트
sr = pd.Series(obj, index = idx)
print(sr)

print("")
# 인덱싱
print("sr[4] 또는 sr['e']로 인덱싱")
print(sr[4])
print(sr['e'])
print("")

# 슬라이싱
print("sr[1:5] 또는 sr['b':'e']로 슬라이싱")
print(sr[1:5])
print(sr['b':'e'])

print("")
# 연속하지 않은 위치
print("연속하지 않은 위치")
idx = [0,3,4] # 위치 번호를 담은 리스트
print(sr[idx])

print("")
# 연속하지 않은 레이블
print("연속하지 않은 레이블")
lbl = ['a','d','e'] # 레이블을 담은 리스트
print(sr[lbl])

print("")
print("========================================================")
"""
라. 시리즈의 통계 메소드 : 메서드가 너무 많으니... 일일이 타이핑은 안 하고 실습을 통한 확인만 ^^;;
"""
print("라. 시리즈의 통계 메소드 \n")
sr_1 = pd.Series(range(100))

# describe()
# 시리즈객체의 요약 통계량에 대한 정보
# 총 객체 수, 평균, 표준편차, 최솟값, 제1사분위수, 중앙값, 제3사분위수, 최댓값, 데이터타입
print(".describe() \n")
sr_1.describe()

#count() : 시리즈객체의 총 객체 수
print(".count() \n")
print(sr_1.count())


#mean() : 시리즈객체의 평균
print(".mean() \n")
print(sr_1.mean())

#var() : 시리즈객체의 분산
print(".var() \n")
print(sr_1.var())

#std() : 시리즈객체의 표준편차
print(".std() \n")
print(sr_1.std())

#min() : 시리즈객체의 최솟값
print(".min() \n")
print(sr_1.min())

#max() : 시리즈객체의 최댓값
print(".max() \n")
print(sr_1.max())

#median() : 시리즈객체의 중앙값
print(".median() \n")
print(sr_1.median())

#quantile() : 시리즈객체의 사분위수
print(".quantile(q = 0.25), 제1사분위수 \n")
print(sr_1.quantile(q = 0.25))

print(".quantile(), 중앙값 default 5 \n")
print(sr_1.quantile())

print(".quantile(q = 0.75), 제3사분위수 \n")
print(sr_1.quantile(q = 0.75))

#새 시리즈 생성(유일값, 최빈값, 최빈값의 빈도, unique 등)
print("\n 새 시리즈 생성")
sr_2 = pd.Series(['a','b','b','b','c','c','d'])
print(sr_2.describe())

#unique() : 시리즈객체의 유일값을 1d-array로 반환
print("\n sr_2.unique() 시리즈객체의 유일값")
print(sr_2.unique())

#value_counts() : 시리즈객체의 유일값별 빈도수를 시리즈로 반환
print("\n sr_2.value_counts() 시리즈객체의 유일값별 빈도수")
print(sr_2.value_counts())

#mode() : 시리즈객체의 최빈값을 시리즈로 반환
print("\n sr_2.mode() 시리즈객체의 최빈값")
print(sr_2.mode())