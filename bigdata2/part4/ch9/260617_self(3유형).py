##### 기출문제 9회
##### 작업형 3유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch9/design.csv')
# # print(df)

# train = df[df['id'] <= 140]
# test = df[df['id'] > 140]

# # print(train.shape, test.shape)
# # 1-1.
# from statsmodels.formula.api import ols
# model = ols("design ~ c1 + c2 + c3 + c4 + c5", data=train).fit()
# print(model.summary()) # 정답 세 개

# # 1-2.
# # pvalue 0.05 기준 유의한 독립변수 : c1, c2, c4
# model = ols("design ~ c1 + c2 + c4", data=train).fit()
# # pred = model2.predict(train)
# # print(pred)

# train['pred_design'] = model.predict(train)

# # 상관계수 계산(기본값: 피어슨)
# result = train['design'].corr(train['pred_design'], method='pearson')
# print(round(result,3)) # 정답 0.501

# # 1-3.
# # test 데이터에서 design값 계산
# test['pred_design'] = model.predict(test)

# # test 데이터에 대한 RMSE 계산
# from sklearn.metrics import root_mean_squared_error
# rmse = root_mean_squared_error(test['design'], test['pred_design'])
# print(round(rmse,3)) # 정답 8.488

##### 문제2.
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch9/retention.csv')
# print(df)

# 2-1.
from statsmodels.formula.api import logit
model = logit("Churn ~ MonthlyCharges + CustomerTenure + HasPhoneService + HasTechInsurance", data=df).fit()
print(model.summary()) # MonthlyCharges의 pvalue 값 : 0.008

# 2-2.
import numpy as np
result = np.exp(model.params['HasPhoneService'])
print(round(result, 3))

# 2-3.
# 각 고객의 이탈 확률 예측
pred_probs = model.predict(df)

# 예측한 이탈 확률이 0.3 초과하는 고객의 수
print(sum(pred_probs > 0.3)) # 정답 65