##### 기출문제 9회
##### 작업형 1유형(역대 초고난도 회차)

#####  문제1.

# 1-1.
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch9/design.csv')
# # print(df)

# # train, test 데이터 분리
# from statsmodels.formula.api import ols

# cond1 = df['id'] <= 140
# cond2 = df['id'] > 140
# train = df[cond1].copy()
# test = df[cond2].copy()

# # 전체 변수 사용 회귀 분석
# model = ols("design ~ c1 + c2 + c3 + c4 +c5", data=train).fit()
# print(model.summary()) # pvalue 값이 0.05보다 작은 값은 세 개!

# # 1-2.
# # 유의한 변수만 사용한 회귀 분석
# model = ols("design ~ c1 + c2 + c4", data=train).fit()

# # train 데이터에서 design의 예측
# train['pred_design'] = model.predict(train)

# # 상관계수 계산(기본값: 피어슨)
# result = train['design'].corr(train['pred_design'])
# print(round(result,3))

# # 1-3.
# # test 데이터에서 design값 계산
# test['pred_design'] = model.predict(test)

# # test 데이터에 대한 RMSE 계산
# from sklearn.metrics import root_mean_squared_error
# rmse = root_mean_squared_error(test['design'], test['pred_design'])
# print(round(rmse,3))

##### 문제2.
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch9/retention.csv')
# print(df)

# 2-1.
from statsmodels.formula.api import logit

# 로지스틱 회귀분석 수행
formula = 'Churn ~ MonthlyCharges + CustomerTenure + HasPhoneService + HasTechInsurance'
model = logit(formula, data=df).fit()

# 학습된 모델의 회귀 분석 결과 출력
print(model.summary()) # 정답 0.008

# 2-2
# 오즈비 계산
import numpy as np
result = np.exp(model.params['HasPhoneService'])
print(round(result, 3))

# 2-3
# 각 고객의 이탈 확률 예측
pred_probs = model.predict(df)

print(sum(pred_probs > 0.3))