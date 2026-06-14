# practice01.py
# Part2(작업형2) 연습문제
"""
문제는 md 파일 참조!

1 베이스라인 기초
데이터를 불러오고, 간단한 탐색적 데이터 분석을 진행했다. 연습문제에서 탐색적 데이터 분석(EDA)은 간단하게 진행한다. 
train 데이터의 자료형을 살펴보면 float가 17개, object가 4개다. target은 세 가지 카테고리(클래스)가 있는 object 자료형이다. 결측치는 없다.
"""
# 1. 문제 정의
# 평가: f1-macro
# target: Credit_Score
# 최종 파일: result.csv(컬럼 1개 pred)

# 2. 라이브러리 및 데이터 불러오기
print("Q1")
import pandas as pd

train = pd.read_csv("bigdata2/part2/ch7/score_train.csv")
test = pd.read_csv("bigdata2/part2/ch7/score_test.csv")

# 3. 탐색적 데이터 분석(EDA)
print("===== 데이터 크기 =====")
print("Train Shape : ", train.shape)
print("Test Shape : ", test.shape)
print("\n")

print("===== 데이터 정보(자료형) =====")
print(train.info())
print("\n")

print("===== train 결측치 수 =====")
print(train.isnull().sum().sum())
print("\n")

print("===== test 결측치 수 =====")
print(test.isnull().sum().sum())
print("\n")

print("===== target 빈도 =====")
print(train['Credit_Score'].value_counts())

"""
베이스라인을 살펴보자. target 변수가 object형이다. 따라서 인코딩할 경우 target 컬럼은 제외하자. 
target 컬럼을 원-핫 인코딩할 경우 target 컬럼이 1개가 아니라 여러 개가 만들어진다. 
레이블 인코딩은 가능하다. 다만, 0, 1, 2로 변경한 후 마지막 csv 제출에서 다시 Good, Standard, Poor로 복원해야 한다. 
다행히 연습문제에서 사용할 랜덤포레스트 모델은 target이 object더라도 자동으로 인식해 수치형으로 인코딩 없이도 사용 가능하다.
평가지표는 f1-macro다. 이진 분류와 같이 F1 스코어 평가지표를 사용하되, average='macro'를 설정한다. 베이스라인 f1 점수는 0.7이다.
"""

# 4. 데이터 전처리
# 원-핫 인코딩(target 컬럼이 object형이라 제외)
target = train.pop('Credit_Score')

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

from sklearn.metrics import f1_score
f1 = f1_score(y_val, pred, average='macro')
print('\n f1-macro: ', f1)

# 7. 예측 및 결과 파일 생성
pred = rf.predict(test)
submit = pd.DataFrame({'pred' : pred})
submit.to_csv("result.csv", index=False)

print("\n ===== 예측 결과 확인 (샘플 5개) =====")
print(pd.read_csv("result.csv"))

from sklearn.metrics import roc_auc_score
roc_auc = roc_auc_score(y_val, pred[:,1])
print('\n roc_auc:' , roc_auc)

# 7. 예측 및 결과 파일 생성
pred = rf.predict_proba(test)
submit = pd.DataFrame({'pred': pred[:,1]})
submit.to_csv("result.csv", index=False)

# 제출 파일 확인
print("\n ===== 제출파일 (샘플 5개) =====")
print(pd.read_csv("bigdata2/part2/ch7/result.csv").head())

"""
2 성능 개선 (심화)
간단한 하이퍼파라미터 튜닝으로는 성능을 향상시키지 못했다. 이처럼 성능이 향상되지 않는 케이스도 충분히 있을 수 있다. 
이런 상황에서는 더 많은 시간을 들여 하이퍼파라미터를 튜닝하기보다 작업한 내용 중에 최고 점수를 제출하자.

① 데이터 전처리
레이블 인코딩: 성능이 오히려 떨어졌다. (주석 처리함)
스케일링(Standard Scaler): 약간의 변화가 있다.

② 하이퍼파라미터 튜닝
max_depth: 5~10, 이진 분류보다는 좀 더 깊이를 깊게 설정해 본다.
n_estimators: 200~500
"""

# 2. 라이브러리 및 데이터 불러오기
import pandas as pd

train = pd.read_csv("bigdata2/part2/ch7/score_train.csv")
test = pd.read_csv("bigdata2/part2/ch7/score_test.csv")

# 4. 데이터 전처리
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
cols = train.select_dtypes(include=['int', 'float']).columns
train[cols] = scaler.fit_transform(train[cols])
test[cols] = scaler.fit_transform(test[cols])

# 원-핫 인코딩
train = pd.get_dummies(train)
test = pd.get_dummies(test)

# # 레이블 인코딩
# target = train.pop('Credit_Score')
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
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict_proba(X_val)

from sklearn.metrics import f1_score
f1 = f1_score(y_val, pred, average='macro')
print('\n f1-macro: ', f1)

# 7. 예측 및 결과 파일 생성
pred = rf.predict(test)
submit = pd.DataFrame({'pred':pred})
submit.to_csv("result.csv", index=False)