##### 기출문제 8회
##### 작업형 1유형

#####  문제1.

# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch8/drinks.csv')
# # print(df)

# # 대륙별 맥주 소비량의 평균, 평균이 가장 큰 대륙
# continent = df.groupby('continent')['beer_servings'].mean()
# top = continent.idxmax()

# cond = df['continent'] == top
# df = df[cond]
# df = df.sort_values('beer_servings', ascending=False)
# print(df.iloc[4]['beer_servings'])

#####  문제2.

# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch8/tourist.csv')
# # print(df)

# df['방문객합계'] = df['관광'] + df['공무'] + df['사업'] + df['기타']
# df['관광객비율'] = df['관광'] / df['방문객합계']

# a = df.sort_values('관광객비율', ascending=False).iloc[1]['사업']
# # print(a.iloc[1]['사업'])
# b = df.sort_values('관광', ascending=False).iloc[1]['공무']
# # print(b.iloc[1]['사업'])
# print(a+b)

#####  문제3.

import pandas as pd
df = pd.read_csv('bigdata2/part4/ch8/chem.csv')
# print(df)

# minmax스케일링
# from sklearn.preprocessing import MinMaxScaler
co = (df['co'] -df['co'].min()) / (df['co'].max() - df['co'].min())
nmhc = (df['nmhc'] -df['nmhc'].min()) / (df['nmhc'].max() - df['nmhc'].min())

std1 = co.std()
std2 = nmhc.std()

print(round(std1 - std2, 3))