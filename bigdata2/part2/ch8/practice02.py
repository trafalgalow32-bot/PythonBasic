# practice01.py
# Part2(작업형2) 연습문제
"""
CHAPTER 08 | 회귀 연습문제 
SECTION 02 | 노트북 가격 예측
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
train = pd.read_csv("bigdata2/part2/ch8/laptop_train.csv")
test = pd.read_csv("bigdata2/part2/ch8/laptop_test.csv")

# 3. 탐색적 데이터 분석(EDA)
print("===== 데이터 크기 =====")
print("Train Shape : ", train.shape)
print("Test Shape : ", test.shape)

print("\n ===== 데이터 정보(자료형) =====")
print(train.info())

print("\n ===== train 결측치 수 =====") # 왜 어떤 데는 sum().sum() 이고 여긴 sum() 이지?
print(train.isnull().sum())

print("\n ===== test 결측치 수 =====")
print(test.isnull().sum())

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
베이스라인에서는 결측치 처리를 위해 범주형 컬럼에는 X값을 대입하고, 수치형 데이터에는 -1값을 대입했다. 모두 결측치를 표시하기 위한 임의값이다. 
인코딩에서는 train과 test를 합쳐서 인코딩하고, 다시 train과 test로 나눴다. r2는 사이킷런에서 평가지표 함수를 제공한다. 
베이스라인에서는 대략 0.75 정도의 결과가 나왔다.
"""
# train['price'].hist() # 히스토그램 소환!

# 4. 데이터 전처리
target = train.pop('price')

# 결측치 처리(범주형)
c_cols = ['Model', 'Series', 'Processor', 'Processor_Gen', 'Hard_Disk_Capacity', 'OS']
train[c_cols] = train[c_cols].fillna("X")
test[c_cols] = test[c_cols].fillna("X")

# 결측치 처리(수치형)
n_cols = ['RAM']
train[c_cols] = train[c_cols].fillna(-1)
test[c_cols] = test[c_cols].fillna(-1)

# 원-핫 인코딩
combined = pd.concat([train, test])
combined_dummies = pd.get_dummies(combined)
n_train = len(train)
train = combined_dummies[:n_train]
test = combined_dummies[n_train:]

# 5. 검증 데이터 나누기
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# 6. 머신러닝 학습 및 평가
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)

from sklearn.metrics import r2_score
result = r2_score(y_val, pred)
print('\n r2 : ', result)

# 7. 예측 및 결과 파일 생성
pred = rf.predict(test)
submit = pd.DataFrame({'pred' : pred})
submit.to_csv("result.csv", index=False)

# # 제출 파일 확인
# print("\n ===== 예측 결과 확인 (샘플 5개) =====")
# print(pd.read_csv("bigdata2/part2/ch8/result.csv").head())

"""
2 성능 개선 심화
이번 성능 개선에서는 40% 정도의 결측치를 갖고 있는 Series 컬럼을 삭제했다. 0.77로 성능이 향상되었다. 
그리고 Brand가 Model의 정보를 부분적으로 포함하고 있고, 특정 모델이 희소하게 나타난다. 추가적으로 'Model' 삭제 후 평가지표를 확인해 보니 성능이 0.8로 향상되었다.

① 데이터 전처리
Series 컬럼 삭제: 40% 결측치를 대체하는 대신 이 컬럼을 삭제해 모델의 성능을 높였다.
Model 컬럼 삭제: 여러 희소한 카테고리 값이 있었다. 또한, Brand 컬럼이 Model의 정보를 부분적으로 포함하고 있다. 이런 이유로 Model 컬럼을 삭제하니 모델 성능이 향상되었다.

② 하이퍼파라미터 튜닝
간단한 튜닝을 시도해 보았지만, 뚜렷한 개선이 관찰되지 않았다.
"""

# 2. 라이브러리 및 데이터 불러오기
import pandas as pd
train = pd.read_csv("bigdata2/part2/ch8/laptop_train.csv")
test = pd.read_csv("bigdata2/part2/ch8/laptop_test.csv")

# 4. 데이터 전처리
target = train.pop('Price')

# 결측치 삭제
train = train.drop('Series', axis=1)
test = test.drop('Series', axis=1)

# 결측치 삭제
train = train.drop('Model', axis=1)
test = test.drop('Model', axis=1)

# 결측치 처리(범주형)
c_cols = ['Processor', 'Processor_Gen', 'Hard_Disk_Capacity', 'OS']
train[c_cols] = train[c_cols].fillna("X")
test[c_cols] = test[c_cols].fillna("X")

# 결측치 처리(수치형)
c_cols = ['RAM']
train[c_cols] = train[c_cols].fillna(-1)
test[c_cols] = test[c_cols].fillna(-1)

# 원-핫 인코딩
combined = pd.concat([train, test])
combined_dummies = pd.get_dummies(combined)
n_train = len(train)
train = combined_dummies[:n_train]
test = combined_dummies[n_train:]

# 5. 검증 데이터 나누기
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# 6. 머신러닝 학습 및 평가
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)

from sklearn.metrics import r2_score
result = r2_score(y_val, pred)
print('\n r2: ', result)

# 7. 예측 및 결과 파일 생성
pred = rf.predict(test)
submit = pd.DataFrame({'pred':pred})
submit.to_csv("result.csv", index=False)