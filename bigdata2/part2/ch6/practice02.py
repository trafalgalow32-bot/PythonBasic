# practice02.py
# Part2(작업형2) 연습문제
"""
문제는 md 파일 참조!

1 베이스라인 기초
데이터를 불러오고, 간단한 탐색적 데이터 분석을 진행했다. 
수치형 컬럼(변수)은 4개, 범주형 컬럼(변수)은 10개다. 결측치도 train과 test 모두 8개의 컬럼에서 보여진다. 
nunique()를 활용해 컬럼별 카테고리 수를 확인해 보자. 
단, object 외의 자료형도 포함한다. 만약 object형만 확인하고 싶을 때는 train.select_dtypes(include=['object']).nunique()와 같이 사용한다. 
city 컬럼은 train과 test가 다르다.
"""
# 1. 문제 정의
# 평가: roc-auc
# target: target
# 최종 파일: result.csv(컬럼 1개 pred, 1 확률값)
# 2. 라이브러리 및 데이터 불러오기
print("\n Q2")
import pandas as pd

train = pd.read_csv("bigdata2/part2/ch6/hr_train.csv")
test = pd.read_csv("bigdata2/part2/ch6/hr_train.csv")

# 3. 탐색적 데이터 분석(EDA)
print("===== 데이터 정보(자료형) =====")
print(train.info())
print("\n")

print("===== train 결측치 수 =====")
print(train.isnull().sum())

print("\n ===== test 결측치 수 =====")
print(test.isnull().sum())

print("\n ===== train/test 카테고리별 수 =====")
print(train.nunique())
print(test.nunique())

print("\n ===== target 빈도 =====")
print(train['target'].value_counts())

"""
결측치가 있는 컬럼은 8개로 모두 object 자료형이다. 빈 값은 별도로 X로 표기했다. 
컬럼의 수가 달라 train과 test를 합쳐서 원-핫 인코딩을 진행하고, 다시 train과 test로 나눴다. 
랜덤포레스트로 모델을 만들고 예측한 결과 ROC-AUC가 0.77이다.
"""

# 4. 데이터 전처리
target = train.pop('target')

# train과 test 합쳐서 원-핫 인코딩
combined = pd.concat([train, test])
combined_dummies = pd.get_dummies(combined)
n_train = len(train)
train = combined_dummies[:n_train]
test = combined_dummies[n_train:]

# 5. 검증 데이터 나누기
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# 6. 머신러닝 학습 및 평가
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict_proba(X_val)

from sklearn.metrics import roc_auc_score
roc_auc = roc_auc_score(y_val, pred[:,1])
print('roc_auc', roc_auc)

# 7. 예측 및 결과 파일 생성
pred = rf.predict_proba(test)
submit = pd.DataFrame({'pred': pred[:,1]})
submit.to_csv("result.csv", index=False)

"""
2 성능 개선 (심화)
① 데이터 전처리
레이블 인코딩: 베이스라인에 있는 원-핫 인코딩을 레이블 인코딩으로 변경한다.
스케일링(Standard Scaler, Min-Max Scaler, Robust Scaler)
id 제거

② 하이퍼파라미터 튜닝
max_depth: 3〜7
n_estimators: 200〜500
결측치가 object 자료형이라 일괄 X로 처리했지만, 각 컬럼별로 다른 결측 처리를 할 수도 있다.
"""

# 2. 라이브러리 및 데이터 불러오기
import pandas as pd
train = pd.read_csv("bigdata2/part2/ch6/hr_train.csv")
test = pd.read_csv("bigdata2/part2/ch6/hr_train.csv")

# 4. 데이터 전처리
target = train.pop('target')

# 결측치 처리
train = train.fillna("X")
test = test.fillna("X")

# 레이블 인코딩
from sklearn.preprocessing import LabelEncoder
combined = pd.concat([train, test])
cols = train.select_dtypes(include='object').columns
for col in cols:
    le = LabelEncoder()
    combined[col] = le.fit_transform(combined[col])
n_train = len(train)
train = combined[:n_train].copy()
test = combined[n_train:].copy()
# .copy()가 없어도 문제 없으나 스케일링으로 값을 변경할 때 워닝이 발생할 수 있음

# id 제거(성능 떨어짐)
# train = train.drop('enrollee_id', axis=1)
# test = test.drop('enrollee_id', axis=1)

# 스케일링
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
n_cols = train.select_dtypes(exclude='object').columns
train[n_cols]  = scaler.fit_transform(train[n_cols])
test[n_cols] = scaler.transform(test[n_cols])

# 5. 검증 데이터 분할
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# 6. 머신러닝 학습 및 평가
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(max_depth=7, n_estimators=200, random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict_proba(X_val)

from sklearn.metrics import roc_auc_score
roc_auc = roc_auc_score(y_val, pred[:,1])
print('roc_auc:', roc_auc)

# 7. 예측 및 결과 파일 생성
pred = rf.predict_proba(test)
submit = pd.DataFrame({'pred':pred[:,1]})
submit.to_csv("result.csv", index=False)