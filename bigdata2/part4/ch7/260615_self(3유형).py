##### 기출문제 7회
##### 작업형 3유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch7/clam.csv")
# # print(df)

# # 데이터셋 분할
# train = df.iloc[:210]
# test = df.iloc[210:]
# # print(train.shape)

# # 1-1. 
# from statsmodels.formula.api import logit
# import numpy as np

# # 로지스틱 회귀 모델 생성 및 학습
# model = logit("gender ~ weight", data=train).fit()

# # 오즈비 계산
# odds = np.exp(model.params['weight'])
# print(round(odds, 4))

# # 1-2.
# # 로지스틱 회귀 모델 생성 및 학습
# model = logit("gender ~ age + length + diameter + height + weight", data=train).fit()

# # print(model.summary())
# # 잔차 이탈도
# print(round(-2 * model.llf, 2))
# # print(model.llf)
# # # print(round(-2 * -143.47, 2))

# # 1-3.
# from sklearn.metrics import accuracy_score

# # test 데이터를 사용해 예측(0.5 미만 : 0, 0.5 이상 : 1)
# target = test.pop('gender')
# pred = model.predict(test)
# pred = (pred > 0.5).astype(int)

# # 실제 값과 예측값을 사용해 정확도 계산
# accuracy = accuracy_score(target, pred)

# # 오류율 계산
# error = 1 - accuracy
# print(round(error, 3))

##### 문제2.
import pandas as pd
df = pd.read_csv("bigdata2/part4/ch7/system_cpu.csv")
# print(df)

# 2-1.
# ERP와 각 변수 사이의 상관계수 계산
corr_matrix = df.corr()

# ERP와 다른 변수들간의 상관계수 출력
erp_corr = corr_matrix['ERP'].sort_values(ascending=False)
print(erp_corr) # 0.882194 를 소수점 셋째자리까지 반올림하여 0.882 정답 도출!

# 2-2.
from statsmodels.formula.api import ols

# CPU가 100 미만인 데이터 필터링
filtered = df[df['CPU'] < 100]

# 선형 회귀 모델 생성: ERP를 종속변수, 나머지 변수들을 독립변수로 설정
model = ols("ERP ~ Feature1 + Feature2 + Feature3 + CPU", data=filtered).fit()

# 모델 요약 정보 출력
print(model.summary()) # 결정계수 0.755

# 2-3.
# 독립변수 중 pvalue가 가장 높은 값 : 0.684