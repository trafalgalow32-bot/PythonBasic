##### 기출문제 6회
##### 작업형 1유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch6/data6-1-1.csv")
# # print(df)

# # 출동시간과 도차기간 차이가 평균적으로 가장 오래 걸린 소방서의 시간을 분으로 변환해 출력! 
# df['출동시간'] = pd.to_datetime(df['출동시간'])
# df['도착시간'] = pd.to_datetime(df['도착시간'])
# df['시간차'] = (df['도착시간'] - df['출동시간']).dt.total_seconds() / 60
# # print(df)

# df = df.sort_values('시간차', ascending=False)
# # print(df)

# df = df.groupby('소방서')['시간차'].mean()
# print(df.max()) # 81분!

#####  문제2.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch6/data6-1-2.csv")
# # print(df)

# # 학교에서 교사 한 명당 맡은 학생 수가 가장 많은 학교 찾고, 그 학교의 전체 교사 수 구하기! 

# df['교사/학생'] = (df['1학년'] + df['2학년'] + df['3학년'] + df['4학년'] + df['5학년'] + df['6학년']) / df['교사수']
# # print(df)
# df = df.sort_values('교사/학생', ascending=False)
# print(df) # 정답 19

#####  문제3.

import pandas as pd
df = pd.read_csv("bigdata2/part4/ch6/data6-1-3.csv")
# print(df)

# 연도별 총 범죄 건수의 월평균 값 구하고, 값이 가장 큰 연도를 찾아 해당 연도의 총 범죄 건수의 월 평균 값을 출력

df['총범죄건수'] = df['강력범죄'] + df['절도범죄'] + df['폭력범죄'] + df['지능범죄'] + df['풍속범죄'] + df['교통범죄']
# print(df)

# 연도 슬라이싱
df['연도'] = df['날짜'].str[:4]
# print(df)

# 연도별 총 범죄 건수 합 계산
result = df['총범죄건수'].groupby(df['연도']).sum()

print(round(result.max() / 12))