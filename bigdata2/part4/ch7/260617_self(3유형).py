##### 기출문제 7회
##### 작업형 3유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch7/clam.csv")
# # print(df)

# train = df.iloc[:210]
# test = df.iloc[210:]

# # print(train.shape, test.shape)

# # print(train)

# # 1-1.
# from statsmodels.formula.api import logit
# model = logit("gender ~ weight", data=train).fit()

# # 오즈비
# import numpy as np
# odds = np.exp(model.params['weight'])
# print(round(odds,4)) # 정답 1.0047

# # 1-2.
# model = logit("gender ~ age + length + diameter + height + weight", data=train).fit()
# print(model.summary()) # Log-Likelihood 에 -2를 곱한 값!!
# # print(round(-143.47 * -2, 2))
# print(round(-2 * model.llf, 2))

# # 1-3. 
# from sklearn.metrics import accuracy_score

# # test데이터를 사용해 예측(0.5 미만: 0, 0.5 이상 : 1)
# target = test.pop('gender')
# pred = model.predict(test)
# pred = (pred > 0.5).astype(int)

# # 실제 값과 예측값을 사용해 정확도 계산
# accuracy = accuracy_score(target, pred)

# # 오류율 계산
# error  = 1 - accuracy
# print(round(error, 3))

#####  문제2.

import pandas as pd
df = pd.read_csv("bigdata2/part4/ch7/system_cpu.csv")
# print(df)

# 2-1.
# ERP와 각 변수 사이의 상관계수 계산
corr = df.corr()

# ERP와 다른 변수들과의 상관계수 출력
erp_corr = corr['ERP'].sort_values(ascending=False)
# print(erp_corr) # 정답 0.882194

# 2-2.
# CPU 컬럼 100 미만인 컬럼 필터링
filtered = df[df['CPU'] < 100]
# print(filtered)

from statsmodels.formula.api import ols
model = ols("ERP ~ Feature1 + Feature2 + Feature3 + CPU", data=filtered).fit()
print(model.summary()) # 정답 0.755

# 2-3. 가장 pvalue가 높은 값은? 0.684
