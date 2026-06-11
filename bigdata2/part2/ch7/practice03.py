# practice03.py
# Part2(작업형2) 연습문제
"""
문제는 md 파일 참조!
Section 03. 유리 종류 예측
1 베이스라인 기초
데이터를 불러오고, 간단한 탐색적 데이터 분석을 진행했다. 데이터 자료형이 모두 수치형 데이터고, 결측치는 없다. target은 6가지다.
"""
# 1. 문제 정의
# 평가: f1-weighted
# target: Type
# 최종 파일: result.csv(컬럼 1개 pred)

# 2. 라이브러리 및 데이터 불러오기
import pandas as pd
train = pd.read_csv("bigdata2/part2/ch7/glass_train.csv")
test = pd.read_csv("bigdata2/part2/ch7/glass_test.csv")

# 3. 탐색적 데이터 분석(EDA)
print("===== 데이터 크기 =====")
print(train.shape, test.shape)

print("\n ===== train 데이터 샘플 =====")
print(train.head(1))

print("\n ===== test 데이터 샘플 =====")
print(test.head(1))

print("\n ===== 데이터 정보(자료형) =====")
print(train.info())

print("\n ===== train 결측치 수 =====")
print(train.isnull().sum().sum())

print("\n ===== test 결측치 수 =====")
print(test.isnull().sum().sum())

print("\n ===== target 빈도 =====")
print(train['Type'].value_counts())

"""
모두 수치형 데이터므로 별도 전처리 없이 베이스라인을 구축했다. f1 점수는 0.61의 결과가 나왔다.
"""

# 4. 데이터 전처리
target = train.pop('Type')

# 5. 검증 데이터 나누기
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# 6. 머신러닝 학습 및 평가
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)

from sklearn.metrics import f1_score
score = f1_score(y_val, pred, average='weighted')
print('\n f1: ', score)

# 7. 예측 및 결과 파일 생성
pred = rf.predict(test)
submit = pd.DataFrame({'pred' : pred})
submit.to_csv("result.csv", index=False)

"""
2 성능 개선 심화
랜덤포레스트는 여러 개의 의사결정 나무로 이루어진 앙상블 모델이다. 트리 기반의 모델은 피처의 대소 관계를 중심으로 학습하기 때문에 스케일링에 크게 민감하지 않다. 
이 데이터에서 스케일링은 성능에 변화가 없다. n_estimators 설정으로 성능에 변화가 있을 때 같은 결과라면 낮은 설정을 선택하는 것이 좋다. 
n_estimators값이 크면 트리의 수가 많아져 연산 속도가 느려질 수 있다.

① 데이터 전처리
스케일링: 성능 변화가 없다.

② 하이퍼파라미터 튜닝
max_depth: 5, 7, 10
n_estimators: 200, 500
"""

# 2. 라이브러리 및 데이터 불러오기
import pandas as pd
train = pd.read_csv("bigdata2/part2/ch7/glass_train.csv")
test = pd.read_csv("bigdata2/part2/ch7/glass_test.csv")

# 4. 데이터 전처리
target = train.pop('Type')

# 스케일링 효과 없음

# 5. 검증 데이터 나누기
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# 6. 머신러닝 학습
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(max_depth=5, n_estimators=200, random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)

from sklearn.metrics import f1_score
score = f1_score(y_val, pred, average='weighted')
print('\n f1 :', score)

# 7. 예측 및 결과 파일 생성
pred = rf.predict(test)
submit = pd.DataFrame({'pred' : pred})
submit.to_csv("result.csv", index=False)