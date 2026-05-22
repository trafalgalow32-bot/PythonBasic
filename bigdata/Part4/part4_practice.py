# part4_practice.py
"""
(참고) 본 풀이 과정 외 다양한 풀이가 나올 수 있음에 유념하고 최종 제출 코드의 실행 시간이 1분 이내가 되어야 함을 반드시 고려해야 한다. 
또한 본 풀이를 참고하여 여러 가지 방법을 익히되 실제 시험에서 적용할 경우 다소 코딩에 많은 시간이 소요될 수 있으니 일부만을 선택하여
사용하는 방법도 고려하자.
"""
print("연습 문제1.")
import pandas as pd
X_train = pd.read_csv('data/연습문제/FIFA_X_train.csv', encoding = 'cp949')
X_test = pd.read_csv('data/연습문제/FIFA_X_test.csv', encoding = 'cp949')
y_train = pd.read_csv('data/연습문제/FIFA_y_train.csv', encoding = 'cp949')

# 데이터셋 일부 확인
# print(X_train.head())
# print(X_test.head())
# print(y_train.head())

# 데이터셋 요약 정보 확인
# print(X_train.info())
# print(X_test.info())
# print(y_train.info())

# 기초통계량 확인(수치형 컬럼들의 기초통계 확인)
print(X_train.describe())
print(X_test.describe())
print(y_train.describe())

### STEP3. 데이터셋 전처리

#### 3-1. 불필요한 컬럼 삭제
"""- ID 컬럼은 선수에 대한 고유 정보로 유일하게 구별하는 Key 역할을 하며 레코드마다 모두 다른 값을 가진다. 
이는 모형 학습에는 불필요하다. 그러나 결과 제출 시 문제의 요구 사항에서 ID 컬럼이 필요하기 때문에 별도 저장이 필요하다.
"""
id = X_test['ID'].copy()

# 데이터들에서 ID 컬럼 삭제
X_train = X_train.drop(columns = 'ID')
X_test = X_test.drop(columns = 'ID')
y_train = y_train.drop(columns = 'ID')

# 결측치 처리 : 컬럼별 결측치를 확인한 결과, 결측치가 있는 컬럼은 Position_CLass, Height_cm, Weight_lb
X_train.isna().sum()
X_test.isna().sum()