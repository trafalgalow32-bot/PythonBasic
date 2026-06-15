##### 기출문제 11회
##### 작업형 1유형
#####  문제1.

import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch11/greenhouse_gas.csv")

# #### 1-1. 온실가스 배출량이 가장 많은 국가(각 연도별), 그중 1위를 가장 많이 차지한 국가
# # print(df)
# cols = df.columns[1:]

# max_index = df[cols].idxmax()

# df2 = df.loc[max_index]

# print(df2['Country'].value_counts())

# ##### 문제2.
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch11/sensor_data.csv')
# # print(df.isnull().sum()) # 2-1. S2_Temp 

# mid = df["S2_Temp"].median()
# # print(mid) # 25
# df["S2_Temp"] = df["S2_Temp"].fillna(mid)
# # print(df)
# answer = df["S2_Temp"].mean()
# print(round(answer, 3)) # 정답 : 25.055

##### 문제3.
import pandas as pd
df = pd.read_csv('bigdata2/part4/ch11/order_data.csv')
# print(df)
df['order_amt'] = df['quantity'] * df['price']
# print(df)
df['cancel_TF'] = df['order_no'].str.contains('C')
# print(df)
cond = df['cancel_TF'] == True
df.loc[cond, 'order_amt'] = df.loc[cond, 'order_amt'] * -1
# print(df)

##### 3-1.
# print(df['order_amt'].max())
cond = df['cancel_TF']==True
cancel_df = df[cond]

im = cancel_df['order_amt'].abs().idxmax()

# print(cancel_df.loc[im])

df = df.groupby('cus_id')['order_amt'].sum()

ma = df.max()

print(round(ma,2))