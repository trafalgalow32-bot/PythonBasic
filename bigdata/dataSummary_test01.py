# dataSummary_test01.py

import pandas as pd

"""
4장. 데이터 결합 및 요약
1절. 데이터 결합
1. 데이터 붙이기: 판다스에서 제공하는 concat() 함수는 데이터프레임을 봍이는 역할을 수행한다. 
단순히 행이나 열을 물리적으로 잇는 함수이다.
pandas.concat(objs, axis = 0, ...)
"""
print("데이터 결합")
# 데이터 프레임 생성
print("데이터프레임1")
obj1 = {'student_id' : ['s1', 's2', 's3', 's4', 's5', 's6'],
        'score': [55, 90, 85, 71, 63, 99]}
df1 = pd.DataFrame(obj1)
print(df1)

# 데이터 프레임2 생성
print("\n 데이터프레임2")
obj2 = {'student_id' : ['t1', 't2', 't3', 't4', 't5', 't6'],
        'score' : [65, 99, 87, 75, 57, 88]}
df2 = pd.DataFrame(obj2)
print(df2)

# 두 데이터프레임을 행을 기준으로 붙임
print("\n pandas.concat() - 행기준")
print(pd.concat([df1, df2]))

# 두 데이터프레임을 열을 기준으로 붙임
print("\n pandas.concat() - 열기준")
print(pd.concat([df1, df2], axis = 1))

"""
2. 데이터 병합 : 두 데이터프레임의 고유한 키를 기준으로 병합.
데이터프레임 객체의 merge() 메소드가 이 역할을 수행
데이터프레임객체.merge(right, how = 'inner', on = None, ...)
"""

print("\n 데이터 병합")
print("데이터프레임1")
obj1 = {'student_id' : ['s3', 's4', 's5', 's6'],
        'stat_core' : [85, 71, 63, 99]}
df1 = pd.DataFrame(obj1)
print(df1)

print("\n 데이터프레임2")
obj2 = {'student_id' : ['s1', 's2', 's3', 's4'],
        'stat_core' : [65, 99, 87, 75]}
df2 = pd.DataFrame(obj2)
print(df2)

# 두 데이터 프레임 병합
print("데이터프레임객체.merge()")
print("Case1. 병합유형(how): inner(default)")
# 두 데이터프레임의 공통 학생들의 점수만이 합쳐짐
print(df1.merge(df2, on = 'student_id'))
print("Case2. 병합유형(how): outer")
# 두 데이터프레임의 모든 학생들의 점수가 합쳐짐
# 점수가 없는 과목은 NaN을 반환
# 학생 순서는 왼쪽 데이터프레임(df1)에 있는 student_id 먼저 나옴
print(df1.merge(df2, on = 'student_id'))
print("Case3. 병합유형(how): left")
# 왼쪽 데이터프레임(df1)에 있는 학생들의 점수들만 반환
# 점수가 없는 과목은 NaN을 반환
print(df1.merge(df2, how = 'left', on = 'student_id'))
print("Case4. 병합유형(how): right")
# 오른쪽 데이터프레임(df2)에 있는 학생들의 점수들만 반환
# 점수가 없는 과목은 NaN을 반환
print(df1.merge(df2, how = 'right', on = 'student_id'))
