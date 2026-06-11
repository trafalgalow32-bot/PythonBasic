# practice02.py
# Part2(작업형2) 연습문제
"""
문제는 md 파일 참조!

1 베이스라인 기초
베이스라인에서 f1 평가 점수의 결과가 높게(1에 가깝게) 나올 경우를 살펴보자.
"""
# 1. 문제 정의
# 평가: f1-macro
# target: Drug
# 최종 파일: result.csv(컬럼 1개 pred, 1 확률값)

# 2. 라이브러리 및 데이터 불러오기
import pandas as pd
train = pd.read_csv("bigdata2/part2/ch7/drug_train.csv")
test = pd.read_csv("bigdata2/part2/ch7/drug_test.csv")

# 3. 탐색적 데이터 분석(EDA)
print("===== 데이터 정보(자료형) =====")
print(train.info())

print("\n ===== train 결측치 수 =====")
print(train.isnull().sum().sum())

print("\n ===== test 결측치 수 =====")
print(test.isnull().sum().sum())

print("\n ===== target 빈도 =====")
print(train['Drug'].value_counts())

"""
f1 평가 점수가 낮게 나와도 문제지만, 너무 높게 나올 경우 특히 f1 점수가 0~1 중에 1점이 나온다면 더 이상 개선의 여지가 없다. 원인은 크게 두 가지다.

 - 첫째, 수험생이 데이터를 나눌 때 또는 전처리할 때 잘못한 부분이 있는 경우다. model.fit(X, y)에서 모델을 학습할 때 사용하는 X 데이터를 head()로 출력해 눈으로 확인하자. 
   간혹 target이 학습용 데이터 X에 포함된 경우에는 이미 답을 알고 있기 때문에 만점이 나온다.
 - 둘째, 검증 데이터가 너무 쉽게 나눠졌을 수도 있다.

이번 문제는 두 번째에 해당한다. 따라서 평소대로 20%의 검증 데이터로 평가했을 때 1점이 나왔다. 시험이었다면 매우 당황스러웠을 상황이다. 검증 데이터를 평가하는 다른 방식이 필요하다. 
심화 학습으로 크로스 밸리데이션을 활용해 보자. 단, 반드시 알아야 할 내용은 아니다. 시험은 train_test_split()만으로도 충분하다.
"""

# 4. 데이터 전처리
# 원-핫 인코딩
target = train.pop('Drug')
train = pd.get_dummies(train)
test = pd.get_dummies(test)

# 5. 검증 데이터 나누기
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# 6. 머신러닝 학습 및 평가
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)

from sklearn.metrics import f1_score
f1 = f1_score(y_val, pred, average='macro')
print('\n f1-macro: ', f1)

# 7. 예측 및 결과 파일 생성
pred = rf.predict(test)
submit = pd.DataFrame({'pred' : pred})
submit.to_csv("result.csv", index=False)

"""
2 시험의 성능 개선 심화
6회 시험의 작업형2에서는 검증 데이터를 활용한 f1 평가 점수가 0.9점대가 나왔다. 빅데이터 분석기사 검증 데이터 평가 결과는 0.5점대가 나올 때도 있고 0.9점대가 나올 때도 있다.
데이터에 따라 달라지는 것으로 다른 데이터로 경험한 점수와 비교하지 말고, 베이스라인 모델 점수와 성능 개선 모델 점수를 비교하자.
만약 성능 개선을 시도한 모델이 베이스라인과 같다면 베이스라인 모델을 최종 제출하자. 
Drug 데이터는 레이블 인코딩, 스케일링, 하이퍼파라미터 튜닝을 시도했지만, 성능이 개선되지 않았고 크로스 밸리데이션을 기준으로 베이스라인과 같은 점수가 나왔다. 
앞서 진행했던 방식으로는 성능이 개선되지 않아 데이터 전처리 및 하이퍼파라미터 튜닝 결과표는 생략한다.

① 데이터 전처리
레이블 인코딩
스케일: Standard Scaler, Min-Max Scaler, Robust Scaler

② 하이퍼파라미터 튜닝
max_depth: 7, 10
n_estimators: 200, 500
"""

# 2. 라이브러리 및 데이터 불러오기
import pandas as pd
train = pd.read_csv("bigdata2/part2/ch7/drug_train.csv")
test = pd.read_csv("bigdata2/part2/ch7/drug_test.csv")

# 4. 데이터 전처리
target = train.pop('Drug')

# # 스케일링
# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler()
# train['Age'] = scaler.fit_transform(train[['Age']])
# test['Age'] = scaler.fit_transform(test[['Age']])

# 원-핫 인코딩(Drug 컬럼 제외)
train = pd.get_dummies(train)
test = pd.get_dummies(test)

# # 레이블 인코딩(Drug 컬럼 제외)
# target = train.pop['Drug']
# from sklearn.preprocessing import LabelEncoder
# cols = train.select_dtypes(include='object').columns
# for col in cols:
#     le = LabelEncoder()
#     train[col] = le.fit_transform(train[col])
#     test[col] = le.fit_transform(test[col])

# 5. 크로스 벨리데이션(cross-validation)
from sklearn.metrics import f1_score
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(random_state=0)
f1_scores = cross_val_score(rf, train, target, cv=3, scoring='f1_macro')
print(f1_scores.mean())

# 6. 머신러닝 학습
rf.fit(train, target)

# 7. 예측 및 결과 파일 생성
pred = rf.predict(test)
submit = pd.DataFrame({'pred' : pred})
submit.to_csv("result.csv", index=False)