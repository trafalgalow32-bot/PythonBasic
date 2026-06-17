##### 기출문제 7회
##### 작업형 1유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch7/student_assessment.csv")
# # print(df)

# df = df.dropna()
# # print(df)

# # 가장 많이 수강한 과목 필터링
# id = df['id_assessment'].value_counts().idxmax()
# cond = df['id_assessment'] == id
# df = df[cond]

# # 과목점수 스탠더드 스케일
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# df['score'] = scaler.fit_transform(df[['score']])

# print(round(df['score'].max(), 3))

#####  문제2.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch7/stock_market.csv")
# # print(df)

# # close와의 상관 관계(절댓값)
# df_corr = df.corr()['close'].abs()

# # 상관 관계가 높은 변수명
# col = df_corr.loc['DE1' : 'DE77'].idxmax()

# print(round(df[col].mean(), 4))

#####  문제3.

import pandas as pd
df = pd.read_csv("bigdata2/part4/ch7/air_quality.csv")
# print(df)

q1 = df['CO2'].quantile(.25)
q3 = df['CO2'].quantile(.75)
iqr = q3 - q1

lower = q1 - iqr * 1.5
upper = q3 + iqr * 1.5

outlier = df[(df['CO2'] < lower) | (df['CO2'] > upper)]
print(len(outlier))