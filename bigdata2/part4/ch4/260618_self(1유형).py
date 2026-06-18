##### 기출문제 4회
##### 작업형 1유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch4/data4-1.csv")
# # print(df)

# q3 = df['age'].quantile(.75)
# q1 = df['age'].quantile(.25)
# iqr = q3 - q1

# print(round(abs(iqr)))

#####  문제2.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch4/data4-2.csv")
# # print(df)

# # 비율이 40%보다 크고 50%보다 작은 조건
# cond1 = (df['loves'] + df['wows']) / df['reactions'] > 0.4
# cond2 = (df['loves'] + df['wows']) / df['reactions'] < 0.5

# cond3 = df['type'] == 'video'

# print(len(df[cond1 & cond2 & cond3]))

#####  문제3.

import pandas as pd
df = pd.read_csv("bigdata2/part4/ch4/data4-3.csv")
# print(df)

df['date_added'] = pd.to_datetime(df['date_added'])

df['year'] = df['date_added'].dt.year
df['month'] = df['date_added'].dt.month

cond1 = df['country'] == "United Kingdom"
cond2 = df['year'] == 2018
cond3 = df['month'] == 1

print(len(df[cond1 & cond2 & cond3]))