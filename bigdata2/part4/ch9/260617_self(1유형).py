##### 기출문제 9회
##### 작업형 1유형(역대 초고난도 회차)

#####  문제1.
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch9/loan.csv')
# # print(df)

# df['총대출액'] = df['신용대출'] + df['담보대출']

# result = df.groupby(['지역코드','성별'])['총대출액'].sum().unstack()

# # print(result)

# result['차이'] = abs(result[1] - result[2])
# print(result['차이'].idxmax())


##### 문제2.
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch9/crime.csv')
# # print(df)

# # df['검거율'] = len(df['구분'] == '검거건수') / len(df['구분'] == '발생건수')
# # print(df)

# # 발생건수와 검거건수 따로 분리
# cond1 = df['구분'] == '발생건수'
# cond2 = df['구분'] == '검거건수'
# df1 = df[cond1].iloc[:,2:] # 발생건수만 가져오기
# df2 = df[cond2].iloc[:,2:] # 검거건수만 가져오기

# # 검거율 계산 (검거건수 / 발생건수)
# df1 = df1.reset_index(drop=True)
# df2 = df2.reset_index(drop=True)
# df3 = df2 / df1

# # 각 연도에서 검거율이 가장 높은 범죄유형 찾기
# listbox = df3.idxmax(axis=1)

# # 가장 높은 검거율을 기록한 범죄유형의 검거건수 가져오기
# result = 0
# for index, item in enumerate(listbox):
#     result = result + df2.loc[index, item]
# print(result)

##### 문제3.
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch9/hr.csv')
# print(df)

# 만족도의 결측치 평균으로 대체
m = df['만족도'].mean()
df['만족도'] = df['만족도'].fillna(m)

# 근속연수 결측치 처리(부서와 성과등급 기준 평균값으로 채움)
gm = df.groupby(['부서','성과등급'])['근속연수'].transform('mean')
gm = gm.astype(int)
df['근속연수'] = df['근속연수'].fillna(gm)

# 연봉/ 근속연수 계산 후 세 번째로 높은 사람의 근속연수 (A)
df['연봉_근속연수'] = df['연봉'] / df['근속연수']
df_year = df.nlargest(3, '연봉_근속연수')
# print(df_year)
a = df_year.iloc[-1]['근속연수']
# print(a)

# 연봉 / 만족도 계산 후 두 번째로 높은 사람의 교육 참가 횟수 (B)
df['연봉_만족도'] = df['연봉'] / df['만족도']
df_like = df.nlargest(2, '연봉_만족도')
# print(df_like)
b = df_like.iloc[-1]['교육참가횟수']
# print(b)

result = a + b
print(result)