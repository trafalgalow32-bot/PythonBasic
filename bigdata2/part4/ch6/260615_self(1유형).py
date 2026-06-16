##### 기출문제 6회
##### 작업형 1유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch6/data6-1-1.csv")
# # print(df)

# df['출동시간'] = pd.to_datetime(df['출동시간'])
# df['도착시간'] = pd.to_datetime(df['도착시간'])
# df['시간차이'] = (df['도착시간'] - df['출동시간']).dt.total_seconds() / 60
# print(df)

# m = df.groupby('소방서')['시간차이'].mean()
# print(round(m.max()))

##### 문제2. 
# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch6/data6-1-2.csv")
# # print(df)

# # 교사 한 명당 맡은 학생수
# df['교사1인당학생수'] = (df['1학년'] + df['2학년'] + df['3학년'] + df['4학년'] + df['5학년'] + df['6학년']) / df['교사수']  
# # print(df)

# # 교사1인당하갱수 컬럼을 내림차순으로 정렬
# df = df.sort_values('교사1인당학생수', ascending=False)

# #  틀리게 작성한 노룩 코드
# # filtered = df.groupby('학교명')['교사1인당학생수'].sum()
# # print(filtered.idxmax())

# # 최상단 행의 교사 수 값 출력
# print(df.iloc[0,1])

##### 문제3.
# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch6/data6-1-3.csv")
# # print(df)

# # 총 범죄 건수 계산
# df['총범죄건수'] = (df['강력범죄'] + df['절도범죄'] + df['폭력범죄'] + df['지능범죄'] + df['풍속범죄'] + df['교통범죄'])

# # 연도 슬라이싱
# df['연도'] = df['날짜'].str[:4]

# # 연도별 총 범죄 건수 합 계산
# result = df['총범죄건수'].groupby(df['연도']).sum()

# # 가장 큰 값의 월평균 계산
# print(round(result.max()/12))