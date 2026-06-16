##### 기출문제 10회
##### 작업형 3유형

# #####  문제1.
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch10/attrition.csv')
# # print(df)

# # 1-1.
# from statsmodels.formula.api import logit
# model = logit("attrition ~ age + income + overtime", data=df).fit()

# print(model.summary()) # 정답 : -0.002( 0.025 쪽!)

# # 1-2.
# # 오즈비 계산
# import numpy as np
# result = np.exp(model.params['age'])

# # 결과 출력
# print(round(result,3))

# # 1-3.
# # 새 데이터 입력
# new = pd.DataFrame({"age" : [40], "income" : [4500], "overtime" : [1]})

# # 예측
# pred = model.predict(new)
# print(pred)

# # print(round(pred[0],3)) # 정답 0.697

##### 문제2.
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch10/heating.csv')
# print(df)

# 2-1.
from statsmodels.formula.api import ols
model = ols("heating_load ~ wall + roof + glazing + height", data=df).fit()

print(model.summary())
# print(round(0.0304 + 0.2483 + 0.2217 - 0.2469),3)
result = 0.0304 + 0.2483 + 0.2217 - 0.2469
# print(round(result,3))

# 2-2.
model = ols("heating_load ~ roof + glazing + height", data=df).fit()
print(model.summary()) # 정답 : 0.754

# 2-3.
new = pd.DataFrame({"wall" : [20], "roof":[150], "glazing":[20], "height":[5]})

pred = model.predict(new)

print(round(pred[0], 3)) # 정답 79.612