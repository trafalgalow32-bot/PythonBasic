##### 기출문제 9회
##### 작업형 2유형(역대 초고난도 회차)

#####  문제1.
import pandas as pd
train = pd.read_csv('bigdata2/part4/ch9/farm_train.csv')
test = pd.read_csv('bigdata2/part4/ch9/farm_test.csv')

# 문제정의
# 평가 : f1-score
# target : 농약검출여부
# 최종 파일 : result.csv(컬럼 1개 pred)

# 탐색적 데이터 분석
# print(train.shape, test.shape)

# print(train.head())

# print(train.info())

# print(train.describe(include='object'))
# print(test.describe(include='object'))

# print(train.isnull().sum().sum())
# print(test.isnull().sum().sum())

# print(train['농약검출여부'].value_counts())

# 데이터 전처리
target = train.pop('농약검출여부')

# 원핫 인코딩
train = pd.get_dummies(train)
test = pd.get_dummies(test)

# 검증 데이터 분리
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# 랜덤포레스트
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)

# macro F1 score
from sklearn.metrics import f1_score
print(f1_score(y_val, pred, average='macro'))

# LightGBM
import lightgbm as lgb
lg = lgb.LGBMClassifier(random_state=0, verbose=-1)
lg.fit(X_tr, y_tr)
pred= lg.predict(X_val)
print(f1_score(y_val, pred, average='macro'))

# 최종 제출 파일
pred = lg.predict(test)
result = pd.DataFrame({'pred':pred})

result.to_csv("result.csv", index=False)

# 최종 검증
# print(pred.shape)
print(pd.read_csv("result.csv").head())