##### 기출문제 9회
##### 작업형 1유형(역대 초고난도 회차)

#####  문제1.
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch9/loan.csv')
# # print(df)

# df['총대출액'] = df['신용대출'] + df['담보대출']
# # print(df)

# grouped = df.groupby(['지역코드', '성별'])['총대출액'].sum().unstack()
# grouped['차이'] = abs(grouped[1] - grouped[2])
# result = grouped['차이'].idxmax()
# print(result)
# # print(df)

#####  문제2.
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch9/crime.csv')
# # print(df)

# # df['검거율'] = len(df[df['구분'] == '검거건수')] / len(df[df['구분'] == '발생건수')]
# # print(df)

# cond1 = df['구분'] == '발생건수'
# cond2 = df['구분'] == '검거건수'
# df1 = df[cond1].iloc[:,2:]
# df2 = df[cond2].iloc[:,2:]

# df1 = df1.reset_index(drop=True)
# df2 = df2.reset_index(drop=True)
# df3 = df2/df1

# listbox = df3.idxmax(axis=1)

# result = 0
# for index, item in enumerate(listbox):
#     result = result + df2.loc[index, item]

# print(result)

#####  문제3.
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch9/hr.csv')
m = df['만족도'].mean()
df['만족도'] = df['만족도'].fillna(m)
# print(df.head(30))

# 근속연수 결측치 처리(부서와 성과등급 기준 평균값으로 채움)
gm = df.groupby(["부서", "성과등급"])["근속연수"].transform("mean")
gm = gm.astype(int)
df["근속연수"] = df["근속연수"].fillna(gm)

# 연봉 / 근속연수 계산 후 세번째로 높은 사람의 근속 연수 (a)
df["연봉_근속연수"] = df["연봉"] / df["근속연수"]
df_year = df.nlargest(3, "연봉_근속연수")
a = df_year.iloc[-1]["근속연수"]

# 연봉 / 만족도 계산 후 두번째로 높은 사람의 교육 참가 횟수 (b)
df["연봉_만족도"] = df["연봉"] / df["만족도"]
df_like = df.nlargest(2, "연봉_만족도")
b = df_like.iloc[-1]["교육참가횟수"]

result = a + b
print(result)