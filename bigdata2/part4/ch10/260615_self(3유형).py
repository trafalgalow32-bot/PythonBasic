##### 기출문제 10회
##### 작업형 3유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch10/attrition.csv')

# #1-1.
# from statsmodels.formula.api import logit
# model = logit("attrition ~ age + income + overtime", data=df).fit()

# print(model.summary())

# print(round(model.params['income'], 3))

# #1-2.
# import numpy as np
# result = np.exp(model.params['age'])

# print(round(result, 3))

# #1-3.
# new = pd.DataFrame({"age":[40], "income":[4500], "overtime":[1]})

# pred = model.predict(new)

# print(round(pred[0],3))

# ##### 문제2.
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch10/heating.csv')

# # 2-1.
# from statsmodels.formula.api import ols
# model = ols("heating_load ~ wall + roof + glazing + height", data=df).fit()

# print(model.summary())

# result = model.params[1:].sum()
# print(round(result,3))

# # 2-2.
# model = ols("heating_load ~ roof + glazing + height", data=df).fit()

# print(model.summary())

# # 2-3.
# new = pd.DataFrame({"wall":[20], "roof":[150], "glazing":[20], "height":[5]})

# pred = model.predict(new)

# print(round(pred[0], 3))