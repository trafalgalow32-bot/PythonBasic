##### 기출문제 6회
##### 작업형 2유형
#####  문제1.

import pandas as pd
train = pd.read_csv("bigdata2/part4/ch6/energy_train.csv")
test = pd.read_csv("bigdata2/part4/ch6/energy_test.csv")


# 데이터전처리
target = train.pop('Heat_Load')

train = pd.get_dummies(train)
test = pd.get_dummies(test)
# print(train.shape, test.shape)

# 검증데이터 분할
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# print(X_tr.shape, X_val.shape, y_tr.shape, y_val.shape)

# 머신 러닝 학습 및 평가
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xg
import lightgbm as lgb
from sklearn.metrics import f1_score

# 의사결정나무
dt= DecisionTreeClassifier(random_state=0)
dt.fit(X_tr, y_tr)
pred = dt.predict(X_val)
print(f1_score(y_val, pred, average='macro'))

# 랜덤포레스트
rf = RandomForestClassifier(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)
print(f1_score(y_val, pred, average='macro'))

# # xgboost
# xg = xg.XGBClassifier(random_state=0)
# xg.fit(X_tr, y_tr)
# pred = xg.predict(X_val)
# print(f1_score(y_val, pred, average='macro'))

# target 인코딩
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_tr_adjusted = le.fit_transform(y_tr)

# 모델 학습 및 예측
xg = xg.XGBClassifier(random_state=0)
xg.fit(X_tr, y_tr_adjusted)
pred = xg.predict(X_val)

# 예측값을 문자로 변경
pred = le.inverse_transform(pred)

print(f1_score(y_val, pred, average='macro'))

# lightGBM
lg = lgb.LGBMClassifier(random_state=0, verbose=-1)
lg.fit(X_tr, y_tr)
pred = lg.predict(X_val)
print(f1_score(y_val, pred, average='macro'))

# 예측 결과 파일 생성
pred= lg.predict(test)
submit = pd.DataFrame({'pred':pred})

submit.to_csv("result.csv", index=False)