# print("\n Q1")
# import pandas as pd

# train = pd.read_csv("bigdata2/part2/ch6/diabetes_train.csv")
# test = pd.read_csv("bigdata2/part2/ch6/diabetes_test.csv")

# # EDA
# print("== 데이터 크기==")
# print("Train shape : ", train.shape)
# print("Test shape : ", test.shape)

# print("\n == train 데이터 샘플 ==")
# print(train.head(1))

# print("\n == test 데이터 샘플")
# print(test.head(1))

# print("\n == 데이터 정보(자료형)")
# print(train.info())

# print("\n ==train 결측치 수==")
# print(train.isnull().sum().sum())

# print("\n ==test 결측치 수==")
# print(test.isnull().sum().sum())

# # 데이터 전처리
# target = train.pop('Outcome')

# # 검증 데이터 나누기
# from sklearn.model_selection import train_test_split
# X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# print("\n == 분할된 데이터 크기")
# print(X_tr.shape, X_val.shape, y_tr.shape, y_val.shape)

# # 머신러닝 학습 및 평가
# from sklearn.ensemble import RandomForestClassifier
# rf = RandomForestClassifier(random_state=0)
# rf.fit(X_tr, y_tr)
# pred = rf.predict_proba(X_val)

# print("\n == 예측 결과 확인 (샘플 5개) ==")
# print(pred[:5])

# from sklearn.metrics import roc_auc_score
# roc_auc = roc_auc_score(y_val, pred[:,1])
# print('\n roc_auc:', roc_auc)

# # 예측 및 결과 파일 생성
# pred = rf.predict_proba(test)
# submit = pd.DataFrame({'pred': pred[:,1]})
# submit.to_csv("result.csv", index=False)

# # 제출 파일 확인
# print("\n == 제출파일 (샘플 5개)")
# print(pd.read_csv("result.csv").head())

# print("\n Q2")
# import pandas as pd

# train = pd.read_csv("bigdata2/part2/ch6/hr_train.csv")
# test = pd.read_csv("bigdata2/part2/ch6/hr_train.csv")

# # 탐색적 데이터 분석
# print("데이터 정보(자료형)")
# print(train.info())

# print("train 결측치 수")
# print(train.isnull().sum())

# print("test 결측치 수")
# print(test.isnull().sum())

# print("target 빈도")
# print(train.nunique())
# print(test.nunique())

# # 데이터 전처리
# target = train.pop('target')

# # train과 test 합쳐서 원-핫 인코딩
# combined = pd.concat([train, test])
# combined_dummies = pd.get_dummies(combined)
# n_train = len(train)
# train = combined_dummies[:n_train]
# test = combined_dummies[n_train:]

# # 검증 데이터 나누기
# from sklearn.model_selection import train_test_split
# X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

# # 머신 러닝 학습 및 평가
# from sklearn.ensemble import RandomForestClassifier
# rf = RandomForestClassifier(random_state=0)
# rf.fit(X_tr, y_tr)
# pred = rf.predict_proba(X_val)

# from sklearn.metrics import roc_auc_score
# roc_auc = roc_auc_score(y_val, pred[:,1])
# print('roc_auc', roc_auc)

# # 예측 및 결과 파일 생성
# pred = rf.predict_proba(test)
# submit = pd.DataFrame({'pred' : pred[:,1]})
# submit.to_csv("result.csv", index=False)

print("\n Q3") 
import pandas as pd

train = pd.read_csv("bigdata2/part2/ch6/creditcard_train.csv")
test = pd.read_csv("bigdata2/part2/ch6/creditcard_test.csv")

# 탐색적 데이터 분석
# print(train.shape, test.shape)

# 데이터 정보(자료형)
# print(train.info())

# train 결측치 수
# print(train.isnull().sum())

# test 결측치 수
# print(test.isnull().sum())

# 범주형 데이터 카테고리
# cols = train.select_dtypes(include='object').columns
# for col in cols:
#     set_train = set(train[col])
#     set_test = set(test[col])
#     same = (set_train == set_test)
#     if same:
#         print(col, "\t 카테고리 동일함")
#     else:
#         print(col, "\t 카테고리 동일하지 않음")

# print(train['STATUS'].value_counts())

# 데이터 전처리
# print(train.shape)
# train.dropna(subset=['OCCUPATION_TYPE'], inplace=True)
# print("\n 삭제 후: ", train.shape)

target = train.pop('STATUS')

# 원-핫 인코딩
train = pd.get_dummies(train)
test = pd.get_dummies(test)

# 검증 데이터 분할
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=0)
rf.fit(X_tr, y_tr)
pred = rf.predict(X_val)

from sklearn.metrics import f1_score
score = f1_score(y_val, pred)
print('\n f1: ', score)

# 파일 생성
pred = rf.predict(test)
submit = pd.DataFrame({'pred': pred})
submit.to_csv("result.csv", index=False)