##### 기출문제 8회
##### 작업형 2유형

#####  문제1.

import pandas as pd
train = pd.read_csv('bigdata2/part4/ch8/churn_train.csv')
test = pd.read_csv('bigdata2/part4/ch8/churn_test.csv')

# print(train.shape, test.shape)

# print(train.info())

# print(train.isnull().sum().sum())
# print(test.isnull().sum().sum())

# print(train.describe(include='object'))
# print(test.describe(include='object'))

# 데이터 전처리
train = train.drop('customerID', axis=1)
test = test.drop(['customerID'], axis=1)
target = train.pop('TotalCharges')

# 레이블 인코딩
from sklearn.preprocessing import LabelEncoder
cols = train.select_dtypes(include='object').columns

for col in cols:
    le = LabelEncoder()
    train[col] = le.fit_transform(train[col])
    test[col] = le.fit_transform(test[col])

# 검증 데이터 분리
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# 랜덤 포레스트
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)

# MAE
from sklearn.metrics import mean_absolute_error
print(mean_absolute_error(y_val, pred))

# LightGBM 
import lightgbm as lgb
lg = lgb.LGBMRegressor(random_state=0, verbose=-1)
lg.fit(X_tr, y_tr)
pred = lg.predict(X_val)
print(mean_absolute_error(y_val, pred))

# 최종 제출 파일
pred = rf.predict(test)
result = pd.DataFrame({'pred':pred})

result.to_csv("result.csv", index=False)

# 검증
# print(pred.shape)

# csv 확인
print(pd.read_csv("result.csv").head())