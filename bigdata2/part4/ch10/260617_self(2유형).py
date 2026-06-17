##### 기출문제 10회
##### 작업형 1유형
#####  문제1.

import pandas as pd
train = pd.read_csv("bigdata2/part4/ch10/gas_train.csv")
test = pd.read_csv("bigdata2/part4/ch10/gas_test.csv")
# print(train.shape, test.shape)

# print(train.info())

# print(train.describe(include='object'))

# print(test.describe(include='object'))

# print(train.isnull().sum().sum())

# print(test.isnull().sum().sum())

# print(train['총가스사용량'].describe())

# 데이터 전처리
target = train.pop('총가스사용량')

# 원핫 인코딩
train = pd.get_dummies(train)
test = pd.get_dummies(test)

# 검증 데이터 분리
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# RMSE
from sklearn.metrics import root_mean_squared_error

# 랜덤포레스트
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)
print(root_mean_squared_error(y_val, pred))

# LightGBM
import lightgbm as lgb
lg = lgb.LGBMRegressor(random_state=0, verbose=-1)
lg.fit(X_tr, y_tr)
pred = lg.predict(X_val)
print(root_mean_squared_error(y_val, pred))

# 최종 제출 파일
pred = rf.predict(test)
result = pd.DataFrame({'pred' : pred})
result.to_csv("result.csv", index=False)