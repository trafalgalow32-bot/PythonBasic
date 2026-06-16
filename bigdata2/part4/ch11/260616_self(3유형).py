##### 기출문제 11회
##### 작업형 3유형
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch11/elderly_health.csv')
# print(df)
#####  문제1.

train = df[:2000].copy() # df[df['id'] <= 2000]
test = df[2000:].copy() # df[df['id'] > 2000]
# print(train.shape)
# print(test.shape)

# 1-1.
import numpy as np
from statsmodels.formula.api import logit

# 로지스틱 회귀분석 수행
model = logit("predicted ~ age + diabetic + activity + glus_fast + bmi + blood_pressure", data=train).fit()

print(model.summary())

# diabetic='yes' 의 오즈비 계산 및 출력
odds = np.exp(model.params["diabetic[T.yes]"])
print(round(odds,2)) # 정답 20.36

# 1-2. 
# test 데이터 예측 확률 계산
pred = model.predict(test)

# 최대 확률을 가진 데이터의 인덱스 찾기
max_idx = pred.idxmax()

# 해당 데이터의 glus_fast 값 출력
print(test.loc[max_idx]) # 정답 181