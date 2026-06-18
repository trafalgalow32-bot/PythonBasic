##### 기출문제 5회
##### 작업형 1유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch5/data5-1.csv")
# # print(df)

# cond1 = df['종량제봉투종류'] == "규격봉투"
# cond2 = df['종량제봉투용도'] == "음식물쓰레기"
# # 이건 몰랐음! 
# cond3 = df['2ℓ가격'] != 0

# filter = df[cond1 & cond2 & cond3]
# print(round(filter['2ℓ가격'].mean()))

#####  문제2.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch5/data5-2.csv")
# # print(df)

# df['bmi'] = (df['Weight'] / (df['Height'] / 100)** 2) 
# # print(df)

# cond1 = (df['bmi'] >= 18.5 ) & (df['bmi'] < 23) # 정상체중
# cond2 = (df['bmi'] >= 23 ) & (df['bmi'] < 25) # 과체중(위험체중)

# diff = abs((len(df[cond1]) - len(df[cond2])))
# print(int(diff))

#####  문제3.

import pandas as pd
df = pd.read_csv("bigdata2/part4/ch5/data5-3.csv")
# print(df)

df['순전입학생'] = df['전입학생수(계)'] - df['전출학생수(계)']
# print(df)

# idxmax = df['순전입학생'].idxmax()
# # print(idxmax)

df = df.sort_values('순전입학생', ascending=False)

# print(df['순전입학생'].idxmax())
print(int(df.iloc[0,-2]))
# print(int(df.loc[df['순전입학생'].idxmax(), '전체학생수(계)'])) 이렇게 해도 되긴 한데, 코드가 너무 지저분!!