##### 기출문제 8회
##### 작업형 1유형

#####  문제1.

# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch8/drinks.csv')
# # print(df)

# # 대륙별 맥주 소비량의 평균
# continent = df.groupby("continent")['beer_servings'].mean() # Europe
# top = continent.idxmax()

# # print(top)

# # 국가별 맥주 소비량
# cond = df['continent'] == top
# df = df[cond]
# df = df.sort_values('beer_servings', ascending=False)
# df.iloc[4, 1] # 또는 df.iloc[4]['beer_servings']
# print(df.iloc[4, 1])

##### 문제2.
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch8/tourist.csv')
# # print(df)

# # 방문객 합계 및 관광객 비율 계산
# df['방문객합계'] = df['관광'] + df['공무'] + df['사업'] + df['기타']
# df['관광객비율'] = df['관광'] / df['방문객합계']

# # 조건에 맞는 값 찾기
# a = df.sort_values('관광객비율', ascending=False).iloc[1,3] 
# b = df.sort_values('관광', ascending=False).iloc[1,2] 

# print(a+b)

##### 문제3.
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch8/chem.csv')
# print(df)

# Min-Max 스케일링
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['co_scaled'] = scaler.fit_transform(df[['co']])
df['nmhc_scaled'] = scaler.fit_transform(df[['nmhc']])

# 표준편차
std1 = df['co_scaled'].std()
std2 = df['nmhc_scaled'].std()
print( std1, std2)

# 표준편차 차이 계산 및 반올림
diff = round(std1 - std2, 3)
print(diff)