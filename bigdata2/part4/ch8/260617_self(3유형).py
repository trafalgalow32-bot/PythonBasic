##### 기출문제 8회
##### 작업형 3유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch8/churn.csv')
# # print(df)

# # 1-1.
# from statsmodels.formula.api import logit
# model = logit("Churn ~ AccountWeeks + ContractRenewal + DataPlan + DataUsage + CustServCalls + DayMins + DayCalls + MonthlyCharge + OverageFee + RoamMins"
#               , data=df).fit()
# # print(model.summary()) # 유의하지 않은 독립변수의 개수 8개!

# # 1-2.
# model = logit("Churn ~ DataUsage + DayMins", data=df).fit()
# # print(model.summary()) # 유의한 회귀 계수 3개의 합(상수항 포함) -1.0395 -0.1697 - 0.0039
# result = -1.0395 -0.1697 - 0.0039
# # print(round(result, 3))

# # 1-3. 
# # 오즈비
# import numpy as np
# # odds = np.exp(model.params("DataUsage"), 5)
# # print(round(odds, 3))
# coef = model.params['DataUsage']

# print(round(np.exp(coef * 5), 3)) 
# # print(round(np.exp(model.params['DataUsage'] * 5), 3))

#####  문제2.

import pandas as pd
df = pd.read_csv('bigdata2/part4/ch8/piq.csv')
# print(df)

# 2-1.
from statsmodels.formula.api import ols
model = ols("PIQ ~ Brain + Height + Weight", data=df).fit()
print(model.summary()) # 유의확률이 가장 작은 변수 : Brain, 이에 해당하는 회귀계수는 2.3431
print(round(2.3431, 3)) # 정답 2.343

# 2-2.
# 결정 계수(R-squared) : 0.37

# 2-3.
new = pd.DataFrame({"Brain" :[90], "Height" : [70], "Weight":[150]})

pred = model.predict(new)
print(pred)
print(round(106.38302))