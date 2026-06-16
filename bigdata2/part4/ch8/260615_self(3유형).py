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

# # 유의하지 않은 독립변수 개수 구하기
# print(model.summary()) # 8개!? 

# # 1-2.
# # 유의한 변수 선택 및 로지스틱 회귀
# model = logit("Churn ~ DataUsage + DayMins", data=df).fit()

# # 유의한 회귀 계수 합계
# print(model.summary())
# print(round(-1.0395 - 0.1697 - 0.0039,3))

# # 1-3.
# # 변수의 회귀 계수 추출
# import numpy as np
# coef = model.params['DataUsage']

# # 오즈비 계산
# print(round(np.exp(coef * 5), 3))

##### 문제2.
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch8/piq.csv')
# print(df)

# 2-1.
# 다중 선형 회귀 분석
from statsmodels.formula.api import ols
model = ols("PIQ ~ Brain + Height + Weight", data=df).fit()

# 가장 작은 pvalue를 가진 변수의 회귀 계수 찾기
print(model.summary()) # Brain

# 2-2. R-squared 는 실행 결과 0.370으로 결과 창에서 확인 가능하다!

# 2-3. 
# 새로운 데이터 생성
new = pd.DataFrame({"Brain" :[90], "Height" : [70], "Weight" : [150]})

# PIQ 예측
pred = model.predict(new)
print(pred) # 106.38302를 정수로 반올림하면 결과값은 106!