# practice01.py
# Part2(작업형2) 연습문제
"""
CHAPTER 08 | 회귀 연습문제 
SECTION 03 | 중고차 가격 예측
문제는 md 파일 참조!

1 베이스라인 기초
데이터를 불러오고, 간단한 탐색적 데이터 분석을 진행했다. 학습용 데이터가 91개인 매우 작은 데이터 크기다. 
train과 test 데이터에 결측치가 있고, object 컬럼의 경우 카테고리가 모두 동일하지 않다.
"""

# 1. 문제 정의
# 평가: R²
# target: Price
# 최종 파일: result.csv(컬럼 1개 pred, 1 확률값)

# 2. 라이브러리 및 데이터 불러오기
import pandas as pd
train = pd.read_csv("bigdata2/part2/ch8/car_train.csv")
test = pd.read_csv("bigdata2/part2/ch8/car_test.csv")

# 3. 탐색적 데이터 분석(EDA)
print("===== 데이터 크기 =====")
print(train.shape, test.shape)

print("\n ===== train 데이터 샘플 =====")
print(train.head(1))

print("\n ===== test 데이터 샘플 =====")
print(test.head(1))

print("\n ===== 데이터 정보(자료형) =====")
print(train.info())

print("\n ===== train 결측치 수 =====") # 왜 어떤 데는 sum().sum() 이고 여긴 sum() 이지?
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
print(train['Price'].describe())

"""
베이스라인에서 train과 test 데이터를 합친 후 레이블 인코딩을 적용했다. 원-핫 인코딩 적용 시 7,500개가 넘는 컬럼이 생성되어 코랩 환경으로 1분 내에 학습하기 어렵다. 
RMSLE(Root Mean Squared Log Error) 평가지표로 대략 1.1의 결과가 나왔다.
"""

# 4. 데이터 전처리
target = train.pop('Price')

# 레이블 인코딩
from sklearn.preprocessing import LabelEncoder
combined = pd.concat([train, test])
cols = train.select_dtypes(include='object').columns

for col in cols:
    le = LabelEncoder()
    combined[col] = le.fit_transform(combined[col])

n_train = len(train)
train = combined[:n_train]
test = combined[n_train:]

# 5. 검증 데이터 나누기
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# 6. 머신러닝 학습 및 평가
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(random_state=0) # 유의:  n_estimators=200 여부 체크! 오타로 보임...
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)

# RMSLE
from sklearn.metrics import root_mean_squared_log_error
result = root_mean_squared_log_error(y_val, pred)
print('\n rmsle : ', result)

# 7. 예측 및 결과 파일 생성
pred = rf.predict(test)
submit = pd.DataFrame({'pred' : pred})
submit.to_csv("result.csv", index=False)

# # 제출 파일 확인
# print("\n ===== 예측 결과 확인 (샘플 5개) =====")
# print(pd.read_csv("bigdata2/part2/ch8/result.csv").head())

"""
2 성능 개선 심화
이번 성능 개선에서는 Engine volume 컬럼과 Mileage 컬럼이 데이터 샘플에서는 숫자지만, 자료형은 object인 컬럼을 다루어 본다. 
전처리를 위해 추가적인 탐색적 데이터 분석(EDA)이 필요하다.

(1) Engine volume 컬럼 EDA
Engine volume 컬럼에서 value_counts()를 활용해 카테고리를 확인해 보자. 91개의 카테고리와 Turbo가 붙어 있는 값도 있음을 확인할 수 있다.
Turbo 외에도 추가적으로 확인하고 싶다면 판다스 설정을 pd.options.display.max_rows = 100으로 해서 출력될 최대 행의 개수를 변경해 91개의 카테고리를 모두 확인하는 것도 방법이다. 
최종적으로 Turbo만 있음을 확인했다.

(2) Mileage 컬럼 EDA
Mileage 컬럼은 숫자 뒤에 km이 붙어 있다. 
다른 단위가 있는 데이터는 없는지 확인하기 위해 숫자와 단위를 split()으로 분리하고, 이 중에서 단위 값(str[1])의 카테고리(value_counts())만 출력했다. 
km이 6732로 모든 데이터가 km 단위를 사용하고 있다.

① 데이터 전처리
Engine volume 컬럼: 자료형 int로 변경 및 Turbo 컬럼 생성
Mileage 컬럼: 단위 km 제거

② 하이퍼파라미터 튜닝
max_depth: 15, 20
n_estimators: 200
"""

# # Engine volume 컬럼 EDA
# train = pd.read_csv("bigdata2/part2/ch8/car_train.csv")
# train['Engine volume'].value_counts()

# # Mileage 컬럼 EDA
# train['Mileage'].str.split().str[1].value_counts()

# 2. 라이브러리 및 데이터 불러오기
import pandas as pd
train = pd.read_csv("bigdata2/part2/ch8/car_train.csv")
test = pd.read_csv("bigdata2/part2/ch8/car_test.csv")

# 4. 데이터 전처리
target = train.pop('Price')

# Engine volume 자료형 변경 및 Turbo 컬럼 생성
train['Turbo'] = train['Engine volume'].str.contatins('Turbo').astype(int)
train['Engine volume'] = train['Engine volume'].str.replace('Turbo','').astype(float)

test['Turbo'] = test['Engine volume'].str.contatins('Turbo').astype(int)
test['Engine volume'] = test['Engine volume'].str.replace('Turbo','').astype(float)

# Mileage 자료형 변경(km 제거)
train['Mileage'] = train['Mileage'].str.split().str[0].astype(int)
test['Mileage'] = test['Mileage'].str.split().str[0].astype(int)

# 레이블 인코딩
from sklearn.preprocessing import LabelEncoder
combined = pd.concat([train, test])
cols = train.select_dtypes(include='object').columns

for col in cols:
    le = LabelEncoder()
    combined[col] = le.fit_transform(combined[col])

n_train = len(train)
train = combined[:n_train]
test = combined[n_train:]

# 5. 검증 데이터 나누기
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# 6. 머신러닝 학습 및 평가
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators=200, random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)

#RMSLE
from sklearn.metrics import root_mean_squared_log_error
result = root_mean_squared_log_error(y_val, pred)
print('\n rmsle ', result)

# 7. 예측 및 결과 파일 생성
pred = rf.predict(test)
submit = pd.DataFrame({'pred':pred})
submit.to_csv("result.csv", index=False)