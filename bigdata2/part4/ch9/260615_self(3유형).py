##### 기출문제 9회
##### 작업형 3유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch9/design.csv')
# # print(df)

# # 1-1.
# from statsmodels.formula.api import ols
# cond1 = df['id'] <= 140
# cond2 = df['id'] > 140
# train = df[cond1].copy()
# test = df[cond2].copy()

# model = ols("design ~ c1 + c2 + c3 + c4 + c5", data = train).fit()
# print(model.summary())

# print(model.pvalues[1:] < 0.05)
# sum(model.pvalues[1:] < 0.5)

# # 1-2.
# model = ols("design ~ c1 + c2 + c4", data=train).fit()

# train['pred_design'] = model.predict(train)

# result = train['design'].corr(train['pred_design'])
# print(round(result,3))

# # 1-3. 
# test['pred_design'] = model.predict(test)

# from sklearn.metrics import root_mean_squared_error
# rmse = root_mean_squared_error(test['design'], test['pred_design'])
# print(round(rmse,3))

# ##### 문제2.
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch9/retention.csv')
# # print(df)

# # 2-1.
# from statsmodels.formula.api import logit

# formula = 'Churn ~ MonthlyCharges + CustomerTenure + HasPhoneService + HasTechInsurance'
# model = logit(formula, data=df).fit()

# print(model.summary())

# print(round(model.pvalues['MonthlyCharges'], 3))

# # 2-2. 
# import numpy as np
# result = np.exp(model.params['HasPhoneService'])
# print(round(result, 3))

# # 2-3.
# pred_probs = model.predict(df)

# print(sum(pred_probs > 0.3))