# MissingValue.py

"""
Part2. 데이터 핸들링
5장. 결측치와 이상치
1절. 결측치
1. 결측치 인식 : 판다스는 시리즈와 데이터프레임 객체에서 메소드 isnull()과 isna()를 제공한다. 이는 데이터 내의 결측값(NaN)의 여부를
판단하는 함수로 이를 통해 결측치(Missing Value)를 인식할 수 있다. 
결과는 데이터에서 결측인 값은 True, 아닌 요소는 False로 반환하고, 이를 메소드 sum()을 통해 단순히 합하면 숫자 1과 0으로 인식해 결측
치의 개수를 쉽게 파악할 수 있다. 
"""
import pandas as pd

print("\n 결측치가 포함된 데이터프레임 생성")
obj = {'student_id' : ['s1', 's2', 's3', 's4', 's5', 's6'],
       'stat_score' : [None ,90, 85, 71, 63, None],
       'math_score' : [65, None, 87, 75, 57, 88],
       'sex' : ['Female', 'Male', 'Female', None, 'Male', 'Male'],
       'pre_level' : ['B', 'A', 'B', 'B', 'C', None]
       }
df = pd.DataFrame(obj)
print(df)

print("\n isnull() : 결측치 여부 확인")
print(df.isnull())

print("\n isna() : 결측치 여부 확인")
print(df.isna())

print("\n 컬럼별 결측치 개수")
print(df.isnull().sum())

print("\n 행별 결측치 개수")
print(df.isnull().sum(axis = 1))

"""
2. 결측치 처리 : 데이터에 결측치가 존재할 때 이 결측치를 처리하기 위한 방법 중 하나는 단순 대치법(Single Imputation)이다.

Complete analysis : 결측값이 존재하는 행을 삭제
평균 대치법 : 관측 또는 실험을 통해 얻어진 데이터의 평균으로 결측치를 대치. 
비조건부 평균 대치법 : 관측 데이터의 평균값으로 대치
조건부 평균 대치법 : 회귀분석을 활용한 대치법(본 수험서에서는 안 다룸!)
단순확률 대치법 : 평균 대치법에서 추정량 표준 오차의 과소 추정 문제를 보완하고자 고안된 방법으로 Hot-deck 방법, 
nearest neighbor 방법 등이 있음(본 수험서에서는 안 다룸!)

가. 결측치 제거
 - 데이터에서 특정 행의 모든 컬럼 중 결측치가 하나라도 존재하는 경우, 해당 행을 제거한 후 데이터 분석을 진행하고자 할 때 결측치 제거
 를 수행한다.
 - 이는 데이터프레임의 dropna() 메소드를 통해 간단히 제거가 가능하다.
"""

print("\n dropna() : 결측치가 있는 행을 모두 제거")
print(df.dropna())
print("열도 가능")
print(df.dropna(axis = 1))

print("\n 'stat_score' 컬럼(시리즈)에서 결측인 요소 제거")
print(df['stat_score'].dropna())
print("'stat_score'과 'math_score' 컬럼 중 결측치가 있는 모든 행을 제거")
print(df[['stat_score', 'math_score']].dropna())

"""
나. 평균 대치법
 - 결측치가 존재할 경우, 해당 변수 값들의 평균으로 빈값을 대치할 수 있다. 이는 데이터프레임의 fillna() 메소드를 통해 쉽게 적용할 수 있다.
 - fillna() 메소드는 본래 fillna(value)의 형태로 value에 원하는 숫자, 시리즈, 데이터프레임 등을 입력하여 결측값을 대치할 수 있다. 
 따라서 value에 통계 메소드 mean()의 결과인 시리즈를 통해 행/열별로 결측값을 대치할 수 있다.
"""

print("\n 숫자형 컬럼만 추출")
df1 = df[['stat_score', 'math_score']].copy() # copy() 원본 소실 방지
print(df1)
print(".fillna() :  결측치를 모두 0으로 대치")
print(df1.fillna(0))
print("평균대치 : 컬럼별 평균으로 대치")
print(df1.fillna(df1.mean()))