# practice01.py
# Part2(작업형2) 연습문제
"""
CHAPTER 08 | 회귀 연습문제 
SECTION 01 | 항공권 가격 예측
문제는 md 파일 참조!

1 베이스라인 기초
데이터를 불러오고, 간단한 탐색적 데이터 분석을 진행했다. train과 test의 object형의 카테고리를 비교했다. 
만약 시험에서 반복문 사용이 어려운 입문자라면 value_counts()를 활용해 비교하거나 다음과 같이 컬럼별로 비교하도록 한다. 
True가 출력되면 같은 카테고리고, False가 출력되면 다른 카테고리다. flight 컬럼은 train과 test의 카테고리가 다르고, 나머지 object형은 카테고리가 같다.

- set_train = set(train['컬럼명'])
- set_test = set(test['컬럼명'])
- print(set_train == set_test)

분류에서는 target의 카테고리를 확인하기 위해 value_counts()로 데이터를 살펴보았다. 회귀에서는 일반적으로 target의 데이터 분포를 히스토그램 등으로 시각화해 확인한다. 
하지만 빅데이터 분석기사 실기 시험은 시각화를 지원하지 않는 환경이라 target을 describe()로 출력했다.
"""

# 1. 문제 정의
# 평가: f1-macro
# target: Credit_Score
# 최종 파일: result.csv(컬럼 1개 pred)

# 2. 라이브러리 및 데이터 불러오기
import pandas as pd

train = pd.read_csv("bigdata2/part2/ch8/flight_train.csv")
test = pd.read_csv("bigdata2/part2/ch8/flight_test.csv")

# 3. 탐색적 데이터 분석(EDA)
print("===== 데이터 크기 =====")
print("Train Shape : ", train.shape)
print("Test Shape : ", test.shape)

print("\n ===== 데이터 정보(자료형) =====")
print(train.info())

print("\n ===== train 결측치 수 =====")
print(train.isnull().sum().sum())

print("\n ===== test 결측치 수 =====")
print(test.isnull().sum().sum())


print("\n ===== 카테고리 비교 =====")
cols = train.select_dtypes(include='object').columns
for col in cols:
    set_train = set(train[col])
    set_test = set(test[col])
    same = (set_train == set_test)
    if same:
        print(col, "\t카테고리 동일함")
    else:
        print(col, "\t카테고리 동일하지 않음")

print("\n ===== target 기술 통계 =====")
print(train['price'].describe())

"""
describe()에서 평균값이 중앙값(50%)보다 크므로 오른쪽 왜곡이 있다. 이 분포에서는 대부분의 값들이 왼쪽에 몰려 있고, 오른쪽으로 갈수록 값들이 희박해지는 것을 볼 수 있다. 
price(target)을 히스토그램으로 시각화해 학습하는 차원에서 확인해 보자. (시험 환경에서는 지원하지 않음)

(히스토그램: price가 0~10000 구간에 약 6,500건으로 집중되어 있고, 40000~60000 구간에 작은 봉우리가 있는 오른쪽 꼬리 분포)

베이스라인에서 flight 컬럼은 train과 test 데이터의 카테고리가 달라 삭제했다. 평가지표는 RMSE이며, 사이킷런에서 RMSE는 root_mean_squared_error 함수로 제공된다.
"""
# train['price'].hist() # 히스토그램 소환!

# 4. 데이터 전처리
target = train.pop('price')

# 컬럼 삭제
train = train.drop('flight', axis=1)
test = test.drop('flight', axis=1)

# 원-핫 인코딩
train = pd.get_dummies(train)
test = pd.get_dummies(test)

# 5. 검증 데이터 나누기
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

print("\n ===== 분할된 데이터 크기 =====")
print(X_tr.shape, X_val.shape, y_tr.shape, y_val.shape)

# 6. 머신러닝 학습 및 평가
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)

# RMSE(Root Mean Squared Error)
from sklearn.metrics import root_mean_squared_error
result = root_mean_squared_error(y_val, pred)
print('\n rmse : ', result)

# 7. 예측 및 결과 파일 생성
pred = rf.predict(test)
submit = pd.DataFrame({'pred' : pred})
submit.to_csv("result.csv", index=False)

# 제출 파일 확인
print("\n ===== 예측 결과 확인 (샘플 5개) =====")
print(pd.read_csv("bigdata2/part2/ch8/result.csv").head())

"""
2 성능 개선 심화
베이스라인에서는 flight 컬럼을 제외했다. 성능 개선에서는 flight 컬럼을 포함하되, 중복은 제외하고 일부만 포함하겠다.
flight 컬럼은 train과 test의 카테고리가 다르다. 이를 합쳐서 원-핫 인코딩이나 레이블 인코딩하는 방법은 있으나, 
1,000개가 넘는 카테고리로 인해 코랩에서는 메모리를 초과하므로 세션이 종료된다. 시험에서도 1분을 넘길 것으로 예상된다. 
따라서 그대로 사용할 수는 없다. 문자열을 나누는 split() 함수를 활용해 하이픈(-) 앞뒤로 나눈다. 예를 들어, UK-776에서 하이픈 앞뒤로 UK와 766을 나눈다. 
UK는 airline의 항공사 코드와 중복되므로 제외한다. 뒤의 숫자는 astype(int)를 활용해 int 자료형으로 변경해 사용한다.

① 데이터 전처리
레이블 인코딩: 효과가 없다.
스케일링: Standard Scaler가 가장 좋았다.
flight 컬럼: 앞의 영문은 airline의 약자므로 제외하고 뒤의 숫자만 활용한다.

② 하이퍼파라미터 튜닝
max_depth: 일반적으로 회귀는 분류보다 더 깊은 10~20 정도에서 튜닝한다.
n_estimators: 200, 500
"""

# 2. 라이브러리 및 데이터 불러오기
import pandas as pd
train = pd.read_csv("bigdata2/part2/ch7/flight_train.csv")
test = pd.read_csv("bigdata2/part2/ch7/flight_test.csv")

# 4. 데이터 전처리
target = train.pop('price')

# flight 컬럼 일부 사용
train['f2'] = train['flight'].str.split('-').str[1].astype(int)
test['f2'] = test['flight'].str.split('-').str[1].astype(int)

# 컬럼 삭제
train = train.drop('flight', axis=1)
test = test.drop('flight', axis=1)

# 스케일링
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
cols = ['duration', 'days_left']
train[cols] = scaler.fit_transform(train[cols])
test[cols] = scaler.fit_transform(test[cols])

# 원-핫 인코딩
train = pd.get_dummies(train)
test = pd.get_dummies(test)

# # 레이블 인코딩
# from sklearn.preprocessing import LabelEncoder
# cols = train.select_dtypes(include='object').columns
# for col in cols:
#     le = LabelEncoder()
#     train[col] = le.fit_transform(train[col])
#     test[col] = le.fit_transform(test[col])

# 5. 검증 데이터 나누기
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# 6. 머신러닝 학습 및 평가
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(max_depth=20, n_estimators=200, random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)

# RMSE(Root Mean Squared Error)
from sklearn.metrics import root_mean_squared_error
result = root_mean_squared_error(y_val, pred)
print('rmse : ', result)

from sklearn.metrics import f1_score
f1 = f1_score(y_val, pred, average='macro')
print('\n f1-macro: ', f1)

# 7. 예측 및 결과 파일 생성
pred = rf.predict(test)
submit = pd.DataFrame({'pred':pred})
submit.to_csv("result.csv", index=False)