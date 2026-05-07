# dataSummary_test02.py

import pandas as pd

"""
Part2. epdlxj gosemffld
4장. 데이터 결합 및 요약
2절. 데이터 요약
1. 그룹별 통계 요약: 특정 컬럼(카테고리형)에 따라 숫자형 값을 하나로 묶어 통계 또는 집계 결과를 얻는 것.
데이터프레임객체.groupby(by, as_index = True, ...)
특정 데이터프레임을 특정 기준으로 그룹화한 데이터프레임객체
"""

print("\n 그룹별 통계 요약")
# 데이터프레임 생성
obj = {'student_id' : ['s1','s2','s3','s4','s5','s6'],
       'stat_score' : [55, 90, 85, 71, 63, 99],
       'math_score' : [65, 99 ,87, 75, 57, 88],
       'sex' : ['Female', 'Male', 'Female', 'Female', 'Male', 'Male'],
       'pre_level' : ['B', 'A', 'B', 'B', 'C', 'A']
       }
df = pd.DataFrame(obj)
print(df)

# 그룹화한 후 데이터프레임 메소드 mean()을 통해 그룹화 평균 계산 가능
print("\n--- 성별 평균 (as_index=True) ---")
sex_stats = df.groupby('sex').mean(numeric_only=True)
print(sex_stats)

# 옵션 as_index = False
# 행 인덱스로 행 위치 인덱스 번호를 사용함
print("\n--- 성별 평균 (as_index=False) ---")
sex_stats_index = df.groupby('sex', as_index=False).mean(numeric_only=True)
print(sex_stats_index)

# 여러 열을 기준으로 그룹화하는 방법은 컬렴명을 담은 리스트를 사용
print("\n--- 성별 및 등급별 평균 ---")
prelevel_stats = df.groupby(['sex', 'pre_level'], as_index=False).mean(numeric_only=True)
print(prelevel_stats)

print("\n--- 성별 상세 요약 통계 ---")
sex_describe = df.groupby('sex', as_index=False).describe()
print(sex_describe)

print("\n 데이터프레임객체.agg(func)")
# 동시에 원하는 여러 통계량만을 구하거나, 컬럼별로 상이한 통계량들만을 사용하고 싶을 경우!

# agg : 동시에 원하는 여러 통계량 도출
# import numpy as np
print(df.groupby('sex')[['stat_score', 'math_score']].agg(['mean', 'sum'])) # np.mean 안쓴다!

print("컬럼별로 상이한 통계량")
print(df.groupby('sex', as_index = False).agg({'stat_score':'mean', 'math_score': 'sum'}))
print("\n")
print(df.groupby('sex', as_index = False).agg({'stat_score' :['mean', 'median'],
                                               'math_score' : ['sum', 'max']
                                               }))

"""
2. 데이터에 함수 적용하기 : 전체 데이터에 대해서 행 혹은 열별로 한 번에 함수를 적용할 수 있는 판다스의 함수.
시리즈의 요소, 데이터프레임의 행, 열 요소마다 연산을 수행할 수 있으므로 빠르고 쉽게 데이터 요약을 수행하여 원하는 정보 확인 가능
"""
print("\n 시리즈에 함수 적용하기")
"""
시리즈에 각 요소에 동일한 함수를 적용하고 싶을 경우, 앞서 언급된 시리즈 객체의 메소드인 map()을 이용한다. 
map()은 원래 라벨 인코딩에만 사용하는 것이 아니라 다음과 같은 방법처럼 딕셔너리로 정의한 내용을 통해 시리즈 객체의 요소를 변경하는
것이 주요 기능이다.
"""

# 데이터프레임 생성
obj = {'student_id' : ['s1', 's2', 's3', 's4', 's5', 's6'],
       'stat_score' : [55 ,90, 85, 71, 63, 99],
       'math_score' : [65, 99, 87, 75, 57, 88],
       'sex' : ['Female', 'Male', 'Female', 'Female', 'Male', 'Male'],
       'pre_level' : ['B', 'A', 'B', 'B', 'C', 'A']
       }
df = pd.DataFrame(obj)
print(df)

print("\n pre_level 컬럼 라벨 인코딩")
print(df['pre_level'].map({'A' : 0, 'B' : 1, 'C' : 2}))

print("\n sex 컬럼의 요소를 한글로 변경")
print(df['sex'].map({'Female' : '여자', 'Male' : '남자'}))

"""
또한 map()은 사용자 정의 함수를 통해 아래와 같은 방법으로 메소드로 지원하지 않는 함수에 대해서 각 요소에 동일한 함수를 적용할 수 있다. 
map()은 시리즈만을 위한 메서드로 데이터프레임에는 사용되지 않는다.
"""
print("\n 시리즈에 사용자 정의 함수 적용")
def f(x) :
    return x ** 2 + 2*x - 5000 # 각 요소에 적용할 함수
print(df['stat_score'].map(f))

"""
데이터프레임에 함수 적용하기 : 데이터프레임에 각 열 또는 행에 함수 일괄 적용하기 위해서는 데이터프레임 객체의 메소드인 apply()
를 사용하면 된다. 
데이터프레임객체.apply(func, axis = 0,)
"""
print("\n apply")
print(df[['stat_score', 'math_score']].apply('sum'))

print("")
print(df[['stat_score', 'math_score']].apply('sum', axis = 1))

print("\n apply 메소드 없이")
print(df[['stat_score', 'math_score']].sum())