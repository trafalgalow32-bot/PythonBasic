##### 기출문제 4회
##### 작업형 2유형
#####  문제1.

import pandas as pd
train = pd.read_csv("bigdata2/part4/ch4/train.csv")
test = pd.read_csv("bigdata2/part4/ch4/test.csv")

# print(train.shape, test.shape)

# 데이터 전처리
target = train.pop('Segmentation')

train = pd.get_dummies(train)
test = pd.get_dummies(test)

# 검증 데이터 분할
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# print(X_tr.shape, X_val.shape, y_tr.shape, y_val.shape)

# 머신러닝 학습 및 평가
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import lightgbm as lgb
from sklearn.metrics import f1_score

# 로지스틱 회귀
lr = LogisticRegression(random_state=0)
lr.fit(X_tr, y_tr)
pred = lr.predict(X_val)
print(f1_score(y_val, pred, average='macro'))

# 의사 결정 나무
dt = DecisionTreeClassifier(random_state=0)
dt.fit(X_tr, y_tr)
pred = dt.predict(X_val)
print(f1_score(y_val, pred, average='macro'))

# 랜덤포레스트
rf = RandomForestClassifier(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)
print(f1_score(y_val, pred, average='macro'))

# # Xgboost
# xg = xgb.XGBClassifier(random_state=0)
# xg.fit(X_tr, y_tr)
# pred = xg.predict(X_val)
# print(f1_score(y_val, pred, average='macro'))

# LightGBM 
lg = lgb.LGBMClassifier(random_state=0, verbose=-1)
lg.fit(X_tr, y_tr)
pred = lg.predict(X_val)
print(f1_score(y_val, pred, average='macro'))

# 예측 및 결과 파일 생성
pred = lg.predict(test)
submit = pd.DataFrame({'ID': test['ID'], 'Segmentation' : pred})
submit.to_csv("result.csv", index=False)

pd.read_csv("result.csv")