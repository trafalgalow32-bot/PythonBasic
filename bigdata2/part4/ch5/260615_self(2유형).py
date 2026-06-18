##### 기출문제 5회
##### 작업형 2유형
#####  문제1.

import pandas as pd
train = pd.read_csv("bigdata2/part4/ch5/train.csv")
test = pd.read_csv("bigdata2/part4/ch5/test.csv")
# print(train.shape, test.shape)

# 데이터전처리
target= train.pop('price')
train = pd.get_dummies(train)
test = pd.get_dummies(test)

# 검증 데이터 분할
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# print(X_tr.shape, X_val.shape, y_val.shape, y_val.shape)

# 머신러닝 학습 및 평가
from sklearn.metrics import root_mean_squared_error

# 선형 회귀
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_tr, y_tr)
pred = lr.predict(X_val)
print(root_mean_squared_error(y_val, pred))

# 랜덤포레스트
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)
print(root_mean_squared_error(y_val, pred))

# Xgboost 
import xgboost as xgb
xg = xgb.XGBRegressor(random_state=0)
xg.fit(X_tr, y_tr)
pred= xg.predict(X_val)
print(root_mean_squared_error(y_val, pred))

# LightGBM
import lightgbm as lgb
lg = lgb.LGBMRegressor(random_state=0, verbose=-1)
lg.fit(X_tr, y_tr)
pred = lg.predict(X_val)
print(root_mean_squared_error(y_val, pred))

# 예측 및 결과 파일 생성
pred = lg.predict(test)
result = pd.DataFrame({'pred':pred})

result.to_csv("result.csv", index=False)