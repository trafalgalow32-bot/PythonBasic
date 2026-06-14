print("Q1")
import pandas as pd

train = pd.read_csv("bigdata2/part2/ch7/score_train.csv")
test = pd.read_csv("bigdata2/part2/ch7/score_test.csv")

print("train.shape")
print(train.shape)
print("test.shape")
print(test.shape)

print(train.info())

# print(train.isnull().sum().sum())
# print(test.isnull().sum().sum())

print(train['Credit_Score'].value_counts())

target= train.pop('Credit_Score')

train = pd.get_dummies(train)
test = pd.get_dummies(test)

# 검증 데이터 나누기
from sklearn.model_selection import train_test_split
X_tr, X_val, y_tr, y_val = train_test_split(train, target, test_size=0.2, random_state=0)

print(X_tr.shape, X_val.shape, y_tr.shape, y_val.shape)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=0)
rf.fit(X_tr,y_tr)
pred = rf.predict(X_val)

from sklearn.metrics import f1_score
f1 = f1_score(y_val, pred, average='macro')
print('\n f1-macro : ', f1)

pred = rf.predict(test) # 여기 오류 여부 확인할 것!!
submit = pd.DataFrame({'pred' : pred})
submit.to_csv("result.csv", index=False)

print(pd.read_csv("result.csv"))

from sklearn.metrics import roc_auc_score
roc_auc = roc_auc_score(y_val, pred[:,1])
print('\n roc_auc: ' , roc_auc)

pred = rf.predict_proba(test)
submit = pd.DataFrame({'pred' : pred[:,1]})
submit.to_csv("result.csv", index=False)

print(pd.read_csv("result.csv").head())