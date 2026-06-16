##### 기출문제 5회
##### 작업형 1유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch5/data5-1.csv")
# # print(df)


# cond1 = df['종량제봉투종류'] == '규격봉투'
# cond2 = df['종량제봉투용도'] == '음식물쓰레기'
# cond3 = df['2ℓ가격'] != 0

# df = df[cond1 & cond2 & cond3]

# print(round(df['2ℓ가격'].mean()))

##### 문제2.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch5/data5-2.csv")
# # print(df)
# # 179cm = 1.79m
# # 100cm = 1m
# df['bmi'] = df['Weight'] / (df['Height'] / 100) ** 2
# # print(df)

# cond1 = (df['bmi'] >= 18.5) & (df['bmi'] < 23) # 정상체중 조건
# cond2 = (df['bmi'] >= 23) & (df['bmi'] < 25) # 위험체중 조건
# normal = df[cond1]
# danger = df[cond2]
# print(abs(len(normal) - len(danger)))
# """
# 까비... 공식 세우는 거, 조건 세우는 거 진짜 다 안보고 했는데 마지막에 len 함수 적용에서 아깝게 실패! 
# """

# # 문제3.
# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch5/data5-3.csv")
# # print(df)
# df['순전입학생'] = df['전입학생수(계)'] - df['전출학생수(계)']
# # print(df)

# df = df.sort_values('순전입학생', ascending=False) # 정답은 230명? 정답은 맞췄으나, 마지막 필터링이 아쉬웟으!
# print(df.iloc[0,-2]) # 내가 쓴 답 : df[0,-2]