##### 기출문제 6회
##### 작업형 1유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch6/data6-1-1.csv")
# # print(df)

# df['도착시간'] = pd.to_datetime(df['도착시간'])
# df['출동시간'] = pd.to_datetime(df['출동시간'])

# df['시간지연'] = (df['도착시간'] - df['출동시간']).dt.total_seconds() / 60
# # print(df)
# result = df.groupby('소방서')['시간지연'].mean()
# print(round(result.max())) # round 처리하면 81!

#####  문제2.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch6/data6-1-2.csv")
# # print(df)

# df['총학생수'] = df['1학년'] + df['2학년'] + df['3학년'] + df['4학년'] + df['5학년'] + df['6학년']
# df['교사당학생수'] = df['총학생수'] / df['교사수']
# # print(df)

# # result = df.groupby('학교명')['교사당학생수']
# # print(result)

# df = df.sort_values('교사당학생수', ascending=False)

# print(df) # 정답 19

#####  문제3.

import pandas as pd
df = pd.read_csv("bigdata2/part4/ch6/data6-1-3.csv")
# print(df)

df['총범죄건수'] = df['강력범죄'] + df['절도범죄'] + df['폭력범죄'] + df['지능범죄'] + df['풍속범죄'] + df['교통범죄']

# 연도 슬라이싱
df['연도'] = df['날짜'].str[:4]

# 연도별 총 범죄 건수 합 계산
result = df['총범죄건수'].groupby(df['연도']).sum()

# 가장 큰 값의 월평균 계산
print(round(result.max()/12)) # 정답 533