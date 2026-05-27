# part4_practice2.py
print("연습 문제2.")
"""
본 풀이 과정 외 다양한 풀이가 나올 수 있으며 유의하고 최종 제출 코드의 실행 시간이 
1분 이내가 되어야 함을 반드시 고려해야 한다. 또한 본 풀이를 참고하여 여러 가지 방법을 
익히되 실제 시험에서 적용할 경우 다소 코딩에 많은 시간이 소요될 수 있으니 
일부만을 선택하여 사용하는 방법도 고려하자.
"""

import pandas as pd
X_train = pd.read_csv('data/연습문제/College_X_train.csv', encoding='cp949')
X_test = pd.read_csv('data/연습문제/College_X_test.csv', encoding='cp949')
y_train = pd.read_csv('data/연습문제/College_y_train.csv', encoding='cp949')

# 데이터 확인 (라인 바이 라인)
# print(X_train.head())
# print(X_test.head())
# print(y_train.head())

# 데이터셋 요약 정보 확인 (라인 바이 라인)
# print(X_train.info())
# print(X_test.info())
# print(y_train.info())

# 수치형 컬럼들의 기초 통계 확인 (라인 바이 라인)
# print(X_train.describe())
# print(X_test.describe())

#### 데이터셋 전처리
##### 불필요한 컬럼 삭제
# ID 컬럼은 학교에 대한 고유 정보로 key 역할로 모델에는 불필요함
# Name 컬럼도 학교명에 대한 고유 정보로 key 역할로 모델에는 불필요함
# 결과 제출 시에는 X_test의 ID 컬럼이 필요하기 때문에 별도 저장
ID = X_test['ID'].copy()

# 데이터들에서 ID 컬럼 삭제
X_train = X_train.drop(columns = ['ID', 'Name'])
X_test = X_test.drop(columns = ['ID', 'Name'])
y_train = y_train.drop(columns = 'ID')

# 결측치 확인
X_train.isna().sum()
# print(X_train.isna().sum()) 
X_test.isna().sum()
# print(X_test.isna().sum())

##### 수치형 컬럼 전처리
# Top10perc,Top25perc, PhD, Terminal, S.F.Ratio, Grad.Rate, perc.alumni
# 위 7개 컬럼은 비율에 관한 컬럼으로 단위는 백분율임
# 이를 소수점으로 변환
col_per = ['Top10perc','Top25perc', 'PhD', 'Terminal', 'S.F.Ratio', 'Grad.Rate', 'perc.alumni']
X_train[col_per] = X_train[col_per]/100
X_test[col_per] = X_test[col_per]/100

####### 수치형 컬럼 간 상관관계 확인
# print(X_train.corr()) # ??? 
col_del = ['Apps','Accept','F.Undergrad','Top25perc','Terminal']
X_train = X_train.drop(col_del, axis = 1)
X_test = X_test.drop(col_del, axis = 1)

# 345p 부터(114015.jpg)