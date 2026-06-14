# practice03.py
# Part2(작업형3) 연습문제
"""
문제는 md 파일 참조!

1 베이스라인 기초
데이터를 불러오고, 간단한 탐색적 데이터 분석을 진행했다. train 데이터의 OCCUPATION_TYPE 컬럼에 결측치가 있다. 이 데이터는 불균형이 심하다. 
정상(채무 이행)은 25,085개가 있는 반면에 비정상(채무 불이행)은 434개밖에 없다. 머신러닝에서 흔히 발생하는 문제다. 
특히 분류 문제에서 한 클래스가 다른 클래스의 수보다 월등히 많을 경우 모델은 다수의 클래스를 예측하는 데 편향될 수 있다.
"""
# 1. 문제 정의
# 평가: f1
# target: STATUS
# 최종 파일: result.csv(컬럼 1개 pred)

# 2. 라이브러리 및 데이터 불러오기
print("\n Q3")
import pandas as pd

train = pd.read_csv("bigdata2/part2/ch6/creditcard_train.csv")
test = pd.read_csv("bigdata2/part2/ch6/creditcard_test.csv")

# 3. 탐색적 데이터 분석(EDA)
print("===== 데이터 크기 =====")
print(train.shape, test.shape)

print("\n===== 데이터 정보(자료형) =====")
print(train.info())

print("\n ===== train 결측치 수 =====")
print(train.isnull().sum())

print("\n ===== test 결측치 수 =====")
print(test.isnull().sum())

print("\n ===== 범주형 데이터 카테고리 =====")
cols = train.select_dtypes(include='object').columns
for col in cols:
    set_train = set(train[col])
    set_test = set(test[col])
    same = (set_train == set_test)
    if same:
        print(col, "\t카테고리 동일함")
    else:
        print(col, "\t 카테고리 동일하지 않음")

print("\n ===== target 빈도 =====")
print(train['STATUS'].value_counts())

"""
데이터(행 또는 컬럼)를 삭제할 때는 반드시 삭제 전과 후의 크기를 비교하자. 예상한 숫자만큼 삭제가 진행되었는지 검증할 필요가 있다. 
또한 행을 삭제한다면 타켓 컬럼은 행을 삭제한 이후에 변수로 옮기자. 베이스라인에서 범주형 자료형은 원-핫 인코딩을 적용했다. 
평가지표가 F1 스코어므로 예측은 predict()로 하고, 0 또는 1의 결괏값을 얻게 된다. 점수는 0.236이다. 
수험생들이 많이 묻는 질문 중 하나가 0.23이면 괜찮은 점수인지다. 공개된 기준이 없어 정확히 알 수 없지만, 
이 베이스라인을 경쟁 점수로 두고 성능 개선에서 이 점수보다 높은 점수를 받으면 작업형2 만점은 무난할 것이다.
"""

# 4. 데이터 전처리
print("\n 삭제 전: ", train.shape)
train.dropna(subset=['OCCUPATION_TYPE'], inplace=True)
print("\n 삭제 후: ", train.shape)

target = train.pop('STATUS')

# 원-핫 인코딩
train = pd.get_dummies(train)
test = pd.get_dummies(test)

# 5. 검증 데이터 분할
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# 6. 머신러닝 학습 및 평가
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)

from sklearn.metrics import f1_score
score = f1_score(y_val, pred)
print('\n f1:', score)

# 7. 예측 및 결과 파일 생성
pred = rf.predict(test)
submit = pd.DataFrame({'pred': pred})
submit.to_csv("result.csv", index=False)

"""
2 성능 개선 (심화)
심각한 불균형 데이터일 경우 평가지표가 낮게 나올 수도 있다. F1 스코어는 1에 가까울수록 좋은 성능이다.
하이퍼파라미터로는 큰 효과를 보기 어려웠다. 트리의 깊이를 제한하는 max_depth는 결과가 0점으로 매우 성능이 저하되었고, n_estimators는 약간의 차이만 있었다. 
랜덤포레스트에는 불균형한 클래스를 자동으로 균형 있게 조정할 수 있는 class_weight를 활용하는 방법이 있다. 
기본값은 모든 클래스에 동일한 가중치를 두고 있으나, 불균형 데이터일 경우 class_weight='balanced'로 설정해 적은 수의 샘플을 가진 클래스에 더 큰 가중치를 자동으로 부여할 수 있다.

① 데이터 전처리
레이블 인코딩: 베이스라인에 있는 원-핫 인코딩을 레이블 인코딩으로 변경한다.
스케일링(Standard Scaler, Min-Max Scaler, Robust Scaler) 효과가 없다. (주석 처리함)
id 제거로 성능이 향상되었다.

② 하이퍼파라미터 튜닝
max_depth: 3〜7
n_estimators: 200〜500
class_weight='balanced'
"""

# 2. 라이브러리 및 데이터 불러오기
import pandas as pd
train = pd.read_csv("bigdata2/part2/ch6/creditcard_train.csv")
test = pd.read_csv("bigdata2/part2/ch6/creditcard_test.csv")

# 4. 데이터 전처리
# 결측치 처리(최빈값)
freq = train['OCCUPATION_TYPE'].mode()[0]
train['OCCUPATION_TYPE'] = train['OCCUPATION_TYPE'].fillna(freq)
test['OCCUPATION_TYPE'] = test['OCCUPATION_TYPE'].fillna(freq)
target = train.pop('STATUS')

# # 스케일링(성능 개선 효과 없음)
# from sklearn.preprocessing import RobustScaler
# scaler = RobustScaler()
# n_cols = train.select_dtypes(exclude='object').columns[:-1] # STATUS를 제외한 int, float
# train[n_cols] = scaler.fit_transform(train[n_cols])
# test[n_cols] = scaler.fit_transform(test[n_cols])

# ID 제외
train = train.drop('ID', axis=1)
test = test.drop('ID', axis=1)

# 레이블 인코딩
from sklearn.preprocessing import LabelEncoder
cols = train.select_dtypes(include='object').columns
for col in cols:
    le = LabelEncoder()
    train[col] = le.fit_transform(train[col])
    test[col] = le.transform(test[col])

# 5. 검증 데이터 나누기
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# 6. 머신러닝 학습 및 평가
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)

from sklearn.metrics import f1_score
score = f1_score(y_val, pred)
print('f1: ', score)

# 7. 예측 및 결과 파일 생성
pred = rf.predict_proba(test)
submit = pd.DataFrame({'pred':pred})
submit.to_csv("result.csv", index=False)