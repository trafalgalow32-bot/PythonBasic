# pandas_test03.py

import numpy as np
import pandas as pd

"""
2장 Pandas를 활용한 데이터 다루기
2절. 데이터 입출력
1. 데이터 불러오기 : pandas.read_csv(filepath, sep = ',', ...)
2. 데이터 저장하기 : 데이터프레임객체.to_csv(path, index=True, ...)

3절. 데이터 정렬 및 순위
1. 데이터 정렬 : 데이터프레임객체.sort_values(by, axis = 0, ascending = True, inplace = False, ...)
"""

print(".sort_values")
print("\n 데이터 프레임 생성")
obj = {'Name' : ['Olivia', 'Lucas', 'Sophia', 'Zoe', 'Ava', 'Elliot'],       
       'Age' : [22, 22, 27, 18, 18, 19],
       'Score' : [100, 95, 60, 77, 83, 84]
       }
df = pd.DataFrame(obj)

print("\n Score 열에 대하여 데이터프레임 오름차순 정렬")
print(df.sort_values('Score'))

print("\n Age와 Score 열에 대하여 데이터프레임 정렬")
# Age에 대해 오름차순으로 정렬하고, 동일한 Age에 대해 Score가 내림차순 정렬
print(df.sort_values(['Age','Score'], ascending = [True, False]))

print("\n .sort_index")
# 행/열 인덱스를 기준으로 정렬
print("\n 데이터프레임 생성")
rownm = ['Olivia', 'Lucas', 'Sophia', 'Zoe', 'Ava', 'Elliot']
obj = {'Score' : [100, 95, 60, 77, 83, 84],
       'Age' : [22, 22, 27, 18, 18, 19]
       }
df = pd.DataFrame(obj, index = rownm)

print("\n 행 인덱스에 대해 오름차순으로 정렬됨")
print(df.sort_index())

print("\n 열 인덱스에 대해 오름차순으로 정렬됨")
print(df.sort_index(axis = 1))

"""
2. 데이터 순위 : 데이터프레임객체.rank(axis=0, method='average', ascending=True, ...)
"""
print("\n 2. 데이터 순위 : 데이터프레임객체.rank(axis=0, method='average', ascending=True, ...)")
print(".rank")
# 데이터프레임 생성
obj = {'Score' : [100,95,60,77,83,85,90,90,88,75,90,54,48,84,73],
       'Age' : [22,22,27,18,18,19,24,26,30,27,25,21,20,17,20]    
}
df = pd.DataFrame(obj)

# Score에 대해 순위 생성 : 결과 비교가 용이하도록 정렬을 먼저 수행, inplace = True로 원본 데이터프레임을 바로 변경
print("Score에 대해 순위 생성")
df.sort_values('Score', ascending=False, inplace = True)
print(df.head())

# case1. 동점자 평균 순위
print("\n case1. 동점자 평균 순위")
df['rank_avg1'] = df['Score'].rank()
print(df['rank_avg1'])

# case2. 동점자 평균 순위(가장 큰 값이 1위)
print("\n case2. 동점자 평균 순위(가장 큰 값이 1위)")
# Score가 90점인 경우가 3개로, 3~5위의 평균인 4위
df['rank_avg2'] = df['Score'].rank(ascending=False)
print(df['rank_avg2'])

# case3. 동점자 가장 낮은 순위(가장 큰 값이 1위)
# Score가 90인 경우가 3개로, 3~5위 중 가장 낮은 3위
print("\n case3. 동점자 가장 낮은 순위(가장 큰 값이 1위)")
df['rank_min'] = df['Score'].rank(method = 'min', ascending = False)
print(df['rank_min'])

# case4. 동점자 가장 높은 순위(가장 큰 값이 1위)
# Score가 90인 경우가 3개로, 3~5위 중 가장 높은 5위
print("\n case4. 동점자 가장 높은 순위(가장 큰 값이 1위)")
df['rank_max'] = df['Score'].rank(method= 'max', ascending= False)
print(df)