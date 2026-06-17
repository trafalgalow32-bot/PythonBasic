##### 기출문제 6회
##### 작업형 3유형

#####  문제1.

# import pandas as pd
# df = pd.DataFrame({
#     "항암약":[4,4,3,4,1,4,1,4,1,4,4,2,1,4,2,3,2,4,4,4]
#     })
# # print(df)

# # 1-1.
# # 항암약을 투여받은 환자 중 이상 없음의 비율 : 이상없음(4) 환자 수 / 전체 환자 수
# normal = sum(df["항암약"] == 4) / len(df)
# print(normal) # 정답 0.55

# # 1-2.
# from scipy.stats import chisquare

# # 카테고리의 비율을 리스트로 만들기
# prob = [0.1, 0.05, 0.15, 0.7]

# # 기대 빈도 수 계산
# expected = [0.1*20, 0.05*20, 0.15*20, 0.7*20]
# # print(expected)

# # 관찰 빈도 수 계산
# observed = df['항암약'].value_counts().sort_index().to_list()
# print(observed)

# # 카이제곱 검정 수행
# print(chisquare(f_obs=observed, f_exp=expected))

# # 1-3.
# # pvalue : 0.07266054733847571

##### 문제2.
import pandas as pd
df = pd.read_csv("bigdata2/part4/ch6/data6-3-2.csv")
# print(df)

# 2-1.
from statsmodels.formula.api import ols
model = ols("temperature ~ solar + wind + o3",data=df).fit()
print(model.summary()) # o3 회귀계수 : 0.0749

# 2-2.
# 위 실행결과 wind의 pvalue: 0.780

# 2-3.
new = pd.DataFrame({"solar":[100], "wind":[5], "o3":[30]})
# print(new)
pred = model.predict(new)
print(pred) # 정답 : 21.56163