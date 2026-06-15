##### 기출문제 8회
##### 작업형 3유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch8/churn.csv')
# # print(df)

# # 1-1.
# # 로지스틱 회귀 분석을 위한 포뮬라 생성
# formula = "Churn ~ AccountWeeks + ContractRenewal + DataPlan + DataUsage + CustServCalls + DayMins + DayCalls + MonthlyCharge + OverageFee + RoamMins"

# # 로지스틱 회귀 모델 생성 및 학습
# from statsmodels.formula.api import logit
# model = logit(formula, data=df).fit()

# print(model.summary())
# print(sum(model.pvalues[1:] > 0.05))

# # 1-2.
# # 유의한 변수 선택
# # print(model.pvalues < 0.05)
# formula = "Churn ~ DataUsage + DayMins"

# # 로지스틱 회귀
# model = logit(formula, data=df).fit()

# print(model.summary())
# print(round(sum(model.params), 3))

# # 1-3.
# # 변수의 회귀 계수 추출
# import numpy as np
# coef = model.params['DataUsage']

# result = round(np.exp(coef * 5), 3)
# print(result)

##### 문제2. 
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch8/piq.csv')
# print(df)

# 2-1.
# 다중 선형 회귀 분석
from statsmodels.formula.api import ols
model = ols('PIQ ~ Brain + Height + Weight', data=df).fit()

print(model.summary())

# 2-2.
# 결정 계수 (R-squared 값)
print(round(model.rsquared,2))

# 2-3.
# 새로운 데이터 생성 및 PIQ 예측
new_data = pd.DataFrame({'Brain' : [90], 'Height' : [70], 'Weight': [150]})

pred = model.predict(new_data)
print(pred)
print(round(pred[0]))