##### 기출문제 10회
##### 작업형 3유형

# #####  문제1.
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch10/attrition.csv')
# # print(df)

# # 1-1.
# # 로지스틱 회귀분석 수행
# from statsmodels.formula.api import logit
# model = logit("attrition ~ age+income+overtime", data=df).fit()

# # 회귀 분석 결과 출력
# print(model.summary())

# # 1-2.
# # 오즈비 계산
# import numpy as np
# result = np.exp(model.params["age"])

# # 결과 출력
# print(round(result,3)) #정답 0.996

# # 1-3.
# # 새로운 직원 데이터
# new = pd.DataFrame({"age" : [40], "income" : [4500], "overtime": [1]})

# # 예측
# pred = model.predict(new)
# # print(pred)

# # 결과 출력
# print(round(pred[0],3)) # 정답 0.697

##### 문제2.

# 2-1.
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch10/heating.csv')
# # print(df)

# # 다중선형회귀분석
# from statsmodels.formula.api import ols
# model = ols("heating_load ~ wall + roof + glazing + height", data=df).fit()

# # 결과 출력
# print(model.summary())
# result = 0.0304 + 0.2483 + 0.2217 - 0.2469
# print(round(result, 3)) # 정답 0.253

# # 2-2. 
# # 회귀 분석 다시(유의한 변수만!)
# model = ols("heating_load ~ roof + glazing + height", data=df).fit()

# # 결정계수 확인(R-squared)
# print(model.summary()) # 정답 0.754

# # 2-3.
# # 새로운 데이터
# new = pd.DataFrame({"wall" : [20], "roof" : [150], "glazing" : [20], "height" : [5]})

# # 난방 부하 예측
# pred = model.predict(new)

# print(round(pred[0],3)) # 79.611549를 셋째자리까지 반올림!