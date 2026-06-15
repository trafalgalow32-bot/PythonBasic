##### 기출문제 11회
##### 작업형 3유형
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch11/elderly_health.csv')
#####  문제1.

import numpy as np
from statsmodels.formula.api import logit

##### 1-1.
# train = df[:2000].copy()
# test = df[2000:].copy()

# model = logit("predicted~age + diabetic + activity + glus_fast + bmi + blood_pressure", data=train).fit()

# # print(model.summary())

# odds_ratio = np.exp(model.params["diabetic[T.yes]"])
# # print(round(odds_ratio, 2))

# ##### 1-2.
# pred = model.predict(test)

# max_idx = pred.idxmax()

# # print(test.loc[max_idx])

# ##### 103.
# from sklearn.metrics import recall_score

# pred = model.predict(test)

# pred = (pred > 0.2).astype(int)

# sensitivity = recall_score(test['predicted'], pred)
# # print(round(sensitivity, 2))

##### 문제2.
# 2-1
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch11/promotion_data.csv')
# print(df)
# from statsmodels import ttest_1nd
from scipy.stats import ttest_1samp

t_stat, pvalue = ttest_1samp(df['sales'], 35000)

# print(round(pvalue, 3))

# 2-2
# print(df.corr())

# 2-3
from statsmodels.formula.api import ols
model = ols("sales ~ visit_count + page_time + ad_clicks + promotion_budget", data=df).fit()

# print(model.summary())

min_var = model.pvalues.idxmin()
# print(min_var)

coef = model.params[min_var]
print(round(coef, 3))