##### 기출문제 8회
##### 작업형 1유형

#####  문제1.

# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch8/drinks.csv')
# # print(df)

# m = df.groupby('continent')['beer_servings'].mean()
# # print(m) # 평균이 가장 큰 대륙 : Europe
# top_continent = m.idxmax()
# # 맥주 소비량이 5번째로 많은 국가의 맥주 소비량
# # m2 = df.groupby(['continent'])['beer_servings']
# # # m2 = m2.sort_values('beer_servings', ascending=False)
# # print(m2)

# # 모범 답안!
# cond = df['continent'] == top_continent
# df = df[cond]
# df = df.sort_values('beer_servings', ascending=False)
# print(df) # 정답 313

#####  문제2.

# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch8/tourist.csv')
# # print(df)

# df['방문객합계'] = df['관광'] + df['공무'] + df['사업'] + df['기타']
# df['관광객비율'] = df['관광'] / df['방문객합계']
# # df = df.sort_values('관광객비율', ascending=False)
# # print(df) # 관광객비율 두번째로 높은 국가 : 국가86, 사업 따라서 a = 203

# # df = df.sort_values('관광', ascending=False)
# # print(df) #  관광 두번째로 높은 국가: 국가42, 공무, 따라서 b = 238

# # print(203 + 238) # 하드코딩

# # 정석대로!
# a = df.sort_values('관광객비율', ascending=False).iloc[1,3]
# b = df.sort_values('관광', ascending=False).iloc[1,2]
# print(a+b)

#####  문제3.

# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch8/chem.csv')
# # print(df)

# co = (df['co'] - df['co'].min()) / (df['co'].max() - df['co'].min())
# nmhc = (df['nmhc'] - df['nmhc'].min()) / (df['nmhc'].max() - df['nmhc'].min())

# std1 = co.std()
# std2 = nmhc.std()
# diff = std1 - std2

# print(round(diff,3))