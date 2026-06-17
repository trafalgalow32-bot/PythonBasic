##### 기출문제 11회
##### 작업형 2유형
#####  문제.

# 문제정의
# 평가: f1-macro
# target: User_Level
# 최종파일 : result.csv(컬럼 1개 pred)

# 라이브러리 및 데이터 불러오기
import pandas as pd
train = pd.read_csv("bigdata2/part4/ch11/game_train.csv")
test = pd.read_csv("bigdata2/part4/ch11/game_test.csv")

# 탐색적 데이터 분석
print(train.shape, test.shape)

# 데이터 샘플
print(train.head())

# 데이터 정보
print(train.info())

# 결측치 수(train)
print(train.isnull().sum().sum())

# 결측치 수(test)
print(test.isnull().sum().sum())

# unique
print(train['User_Level'].value_counts())

#############################################################################
# 데이터 전처리
target = train.pop('User_Level')

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
pred = lg.predict(X_val)
print(f1_score(y_val, pred, average='macro'))

# 최종 제출 파일
pred = lg.predict(test)
result = pd.DataFrame({'pred' : pred})
result.to_csv("result.csv", index=False)