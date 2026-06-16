##### 기출문제 6회
##### 작업형 3유형

#####  문제1.

import pandas as pd
# df = pd.DataFrame({
#     "항암약":[4,4,3,4,1,4,1,4,1,4,4,2,1,4,2,3,2,4,4,4]
#     })
# # print(df)

# # 1-1.
# # 이상 없음(4)의 빈도 계산
# cnt = sum(df['항암약']==4)

# # 항암약을 투여받은 환자 중 '이상 없음' 비율 계산
# ratio = cnt / len(df)
# print(ratio)

# # 1-2. 
# from scipy.stats import chisquare

# # 각 카테고리의 비율을 리스트로 만들기
# prob = [0.1, 0.05, 0.15, 0.7]

# # 기대 빈도 수 계산
# print("데이터 수: ", len(df))
# expected = [0.1 * 20, 0.05 * 20, 0.15 * 20, 0.7 * 20]
# print(expected)

# # 관찰 빈도 수 계산
# observed = df['항암약'].value_counts().sort_index().to_list()
# print(observed)

# # 카이제곱 검정 수행
# print(chisquare(f_obs=observed, f_exp=expected))

# # 1-3. 위 결과값에서 pvalue 값은 0.07266054733847571로 확인!

##### 문제2.
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch6/data6-3-2.csv')
# print(df)

# 2-1.
from statsmodels.formula.api import ols
model = ols("temperature ~ solar + wind + o3", data=df).fit()
print(model.summary()) # 0.0749, 안보고 했다,  개이득!!
print(model.params['o3'])

# 2-2. 
print(model.pvalues['wind'])

# 2-3. 
# 새 데이터를 데이터프레임으로 만들기
new = pd.DataFrame({'solar' : [100], 'wind' : [5], 'o3' : [30]})
# print(new)

pred = model.predict(new)
print(pred)