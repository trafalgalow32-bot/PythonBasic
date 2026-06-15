##### 기출문제 8회
##### 작업형 1유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch8/drinks.csv')
# # print(df)

# # 대륙별 맥주 소비량 평균
# continent = df.groupby('continent')['beer_servings'].mean() # Europe
# # print(continent) # top_continent = continent.idxmax() 로도 확인 가능!
# top_continent = continent.idxmax()

# # 국가별 맥주 소비량
# cond = df['continent'] == top_continent
# df = df[cond]
# df = df.sort_values('beer_servings', ascending=False)
# print(df.iloc[4,1])

##### 문제2.
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch8/tourist.csv')
# # print(df)

# df['방문객합계'] = df['관광'] + df['공무'] + df['사업'] + df['기타']
# df['관광객비율'] = df['관광'] / df['방문객합계']

# a = df.sort_values('관광객비율', ascending=False).iloc[1]['사업']
# b = df.sort_values('관광', ascending=False).iloc[1]['공무']
# print(a+b)

##### 문제3.
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch8/chem.csv')
# print(df)

sc1 = (df['co'] - df['co'].min()) / (df['co'].max() - df['co'].min())
sc2 = (df['nmhc'] - df['nmhc'].min()) / (df['nmhc'].max() - df['nmhc'].min())

std1 = sc1.std()
std2 = sc2.std()

print(std1, std2)

result = std1 - std2
print(round(result,3))

"""
모범 답안에서는 minmaxscaler를 import해서 풀이했으나, 위 방법대로 진행해도 정답은 도출 됨!
"""

