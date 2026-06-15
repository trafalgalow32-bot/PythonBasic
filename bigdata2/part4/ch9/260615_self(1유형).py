##### 기출문제 9회
##### 작업형 1유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch9/loan.csv')
# # print(df)

# df['총대출액'] = df['신용대출'] + df['담보대출']
# # print(df)

# answer = df.groupby(['지역코드', '성별'])['총대출액'].sum().unstack()
# answer['차이'] = abs(answer[1] - answer[2])
# # print(answer)
# result = answer['차이'].idxmax()
# print(result)

# ##### 문제2.
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch9/crime.csv')
# # print(df)

# cond1 = df['구분'] == "발생건수"
# cond2 = df['구분'] == "검거건수"
# df1 = df[cond1].iloc[:,2:]
# df2 = df[cond2].iloc[:,2:]

# df1 = df1.reset_index(drop=True)
# df2 = df2.reset_index(drop=True)
# df3 = df2 / df1

# # print(df3)
# listbox = df3.idxmax(axis=1)

# result = 0
# for index, item in enumerate(listbox):
#     result = result + df2.loc[index, item]

# # print(result)

##### 문제3.
import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch9/hr.csv')

# df['만족도'] = df['만족도'].fillna(df['만족도'].mean())
# # print(df.head(30))

# gm = df.groupby(['부서', '성과등급'])['근속연수'].transform('mean')
# gm = gm.astype(int)
# df['근속연수'] = df['근속연수'].fillna(gm)

# df['연봉_근속연수'] = df['연봉'] / df['근속연수']
# df_year = df.nlargest(3, '연봉_근속연수')
# A = df_year.iloc[-1]['근속연수']

# df['연봉_만족도'] = df['연봉'] / df['만족도']
# df_like = df.nlargest(2, '연봉_만족도')
# B = df_like.iloc[-1]['교육참가횟수']

# result = A + B
# print(result)