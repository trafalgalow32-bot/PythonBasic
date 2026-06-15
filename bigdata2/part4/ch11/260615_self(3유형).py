##### 기출문제 11회
##### 작업형 3유형
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch11/elderly_health.csv')
#####  문제1.

# import numpy as np
# from statsmodels.formula.api import logit

# # 1.1
# # Train/Test  데이터 분할
# train = df[:2000].copy()
# test = df[2000:].copy()

# # 로지스틱 회귀분석 수행
# model = logit("predicted ~ age + diabetic + activity + glus_fast + bmi + blood_pressure", data=train).fit()

# # 회귀 분석 결과 출력
# # print(model.summary())

# # diabetic='yes'의 오즈비 계산 및 출력
# odds_ratio = np.exp(model.params["diabetic[T.yes]"])
# print(round(odds_ratio, 2))

# # 1.2
# # test 데이터 예측 확률 계산
# pred = model.predict(test)

# # 최대 확률을 가진 데이터의 인덱스 찾기
# max_idx = pred.idxmax()

# # 해당 데이터의 glus_fast 값 출력
# print(test.loc[max_idx])

# # 1.3
# # test 데이터 예측
# from sklearn.metrics import recall_score
# pred = model.predict(test)

# # 임계값 0.2 적용하여 분류
# pred = (pred > 0.2).astype(int)

# # 민감도 계산 및 출력
# sensitivity = recall_score(test['predicted'], pred)
# print(round(sensitivity, 2))

##### 문제2.
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch11/promotion_data.csv')

# 2-1.
from scipy.stats import ttest_1samp

# 단일표본 t검정 수행
t_stat, p_value = ttest_1samp(df['sales'], 35000)

# p_value 추출 및 출력
print(round(p_value, 3))

# 2-2.
# 상관계수 행렬 계산
print(df.corr())
# print(round(0.575396, 3))

# 2-3.
from statsmodels.formula.api import ols

# ols 회귀분석 수행
model = ols("sales ~ visit_count + page_time + ad_clicks + promotion_budget", data=df).fit()

# 회귀분석 결과 확인
print(model.summary())

# pvalue가 가장 작은 변수 찾기
min_var = model.pvalues.idxmin()
# print(min_var)

# 해당 변수의 회귀계수 출력
coef = model.params[min_var]
print(round(coef,3))