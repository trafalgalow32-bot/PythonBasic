# practice01.py
# Part2(작업형2) 연습문제
"""
문제는 md 파일 참조!

1 베이스라인 기초
데이터를 불러오고, 간단한 탐색적 데이터 분석을 진행했다. 주어진 데이터는 결측치가 없고 모두 수치형이다.
"""
# 1. 문제 정의
# 평가: roc-auc
# target: Outcome
# 최종 파일: result.csv(컬럼 1개 pred, 1 확률값)
# 2. 라이브러리 및 데이터 불러오기
print("\n Q1")
import pandas as pd

train = pd.read_csv("bigdata2/part2/ch6/diabetes_train.csv")
test = pd.read_csv("bigdata2/part2/ch6/diabetes_test.csv")

# 3. 탐색적 데이터 분석(EDA)
print("===== 데이터 크기 =====")
print("Train Shape : ", train.shape)
print("Test Shape : ", test.shape)

print("\n===== train 데이터 샘플 =====")
print(train.head(1))


print("\n===== test 데이터 샘플 =====")
print(test.head(1))

print("\n===== 데이터 정보(자료형) =====")
print(train.info())

print("\n===== train 결측치 수 =====")
print(train.isnull().sum().sum())

print("\n===== test 결측치 수 =====")
print(test.isnull().sum().sum())

print("\n===== target 빈도 =====")
print(train['Outcome'].value_counts())

"""
모두 수치형 데이터고 결측치가 없다면 베이스라인에서는 전처리를 생략하자. 
검증 데이터를 학습용(train) 데이터에서 20% 정도를 사용한다. 
"target = train.pop('Outcome')"으로 target 변수를 분리했다. 
데이터를 분할하기 전에 target을 분리하지 않는다면 
X_tr, X_val, y_tr, y_val = train_test_split(train.drop('target', axis=1), train['target'], test_size=0.2, random_state=0)과 같이 사용한다.
랜덤포레스트로 모델을 만들고 예측한 결과 ROC-AUC가 0.80이다. 
시험에서는 pd.read_csv("result.csv")로 생성된 csv를 확인한 후 베이스라인을 1차 제출한다.
"""

# 4. 데이터 전처리
target = train.pop('Outcome')

# 5. 검증 데이터 나누기
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

print("\n ===== 분할된 데이터 크기 =====")
print(X_tr.shape, X_val.shape, y_tr.shape, y_val.shape)

# 6. 머신러닝 학습 및 평가
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict_proba(X_val)

print("\n ===== 예측 결과 확인 (샘플 5개) =====")
print(pred[:5])

from sklearn.metrics import roc_auc_score
roc_auc = roc_auc_score(y_val, pred[:,1])
print('\n roc_auc:' , roc_auc)

# 7. 예측 및 결과 파일 생성
pred = rf.predict_proba(test)
submit = pd.DataFrame({'pred': pred[:,1]})
submit.to_csv("result.csv", index=False)

# 제출 파일 확인
print("\n ===== 제출파일 (샘플 5개) =====")
print(pd.read_csv("result.csv").head())

"""
2 성능 개선 (심화)
성능 개선은 베이스라인을 도움 없이 만들 수 있을 때부터 시작하자. 
가장 쉬운 성능개선은 lightgbm과 같은 모델로 변경해 보는 것이다. 
작업형2는 정답이 있는 문제가 아니라 평가지표로 제출한 csv를 평가하며 
평가지표에서의 기준은 공개하지 않고 있다. 40점 기준이 상향될 수도 있기 때문에 
안정적인 40점 확보를 위해 간단한 성능 개선을 해보자. 
성능 개선의 목적은 베이스라인보다 좋은 결과를 얻는 데 있다.
다음과 같은 방법으로 성능을 개선한다. 순서는 전처리를 먼저 하고, 하이퍼파라미터를 튜닝한다. 
그 이유는 데이터가 달라지면 하이퍼파라미터 튜닝도 다시 해야 하기 때문이다. 
성능 개선에서의 기준은 성능이 베이스라인보다 올라가면 적용하고, 
수정된 마지막 점수보다 내려가면 적용하지 않는다. 
작업 내용을 코드 주석 또는 메모장에 작성해 두자.

① 데이터 전처리

모두 수치형 데이터므로 스케일링 세 가지를 적용했다. 
그중에서 Min-Max Scaler 적용값이 가장 높다.

② 하이퍼파라미터 튜닝
랜덤포레스트 모델에서 하이퍼파라미터는 max_depth와 n_estimators 두 가지만 다루자.

- max_depth: 트리의 최대 깊이를 나타낸다. 트리의 깊이를 제한함으로써 과적합을 방지할 수 있다. 
기본값은 없다.
- n_estimators: 트리의 개수다. 높을수록 안정적으로 예측 가능하나, 학습 시간이 늘어난다. 
기본값은 100이다. 랜덤포레스트 분류에서 max_depth는 3에서 7 정도,
 n_estimators는 200에서 500 정도 적용해 보자.
"""

# 2. 라이브러리 및 데이터 불러오기
import pandas as pd

train = pd.read_csv("bigdata2/part2/ch6/diabetes_train.csv")
test = pd.read_csv("bigdata2/part2/ch6/diabetes_test.csv")

# 4. 데이터 전처리
# 스케일링
target = train.pop('Outcome')
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
train = scaler.fit_transform(train)
test = scaler.transform(test)

# 5. 검증 데이터 나누기
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# 6. 머신러닝 학습 및 평가
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(max_depth=5, n_estimators=500, random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict_proba(X_val)

from sklearn.metrics import roc_auc_score
roc_auc = roc_auc_score(y_val, pred[:,1])
print('roc_auc:', roc_auc)

# 7. 예측 및 결과 파일 생성
pred = rf.predict_proba(test)
submit = pd.DataFrame({'pred':pred[:,1]})
submit.to_csv("result.csv", index=False)