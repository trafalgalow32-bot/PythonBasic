##### 기출문제 11회
##### 작업형 1유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch11/greenhouse_gas.csv")
# # print(df)

# # 1-1.
# # 연도 컬럼만 선택
# cols = df.columns[1:] # Country를 제외한 나머지
# # print(cols)

# # 각 연도별 최댓값의 행 번호 찾기
# max = df[cols].idxmax()
# # print(max)

# # 해당 행의 국가명 가져오기
# df2 = df.loc[max]
# # print(df2)

# print(df2['Country'].value_counts())

# # 1-2.
# # CAGR 계산
# df['CAGR'] = (df['2021'] / df['2001']) ** (1/20) - 1

# # 최댓값 구하기
# result = df['CAGR'].max()
# print(round(result,3))

##### 문제2.
# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch11/sensor_data.csv")
# # print(df)

# # cond1 = df.isnull()
# # print(len(df[cond1]))

# # 각 컬럼의 결측치 개수 확인
# print(df.isnull().sum()) # S2_Temp 컬럼

# # 결측치가 가장 많은 컬럼 찾기
# col = df.isnull().sum().idxmax()
# # print(col) # S2_Temp 컬럼

# # 해당 컬럼의 중앙값
# m = df[col].median()
# print(m) # 25.0

# # 결측치 중앙값으로 대체
# df[col] = df[col].fillna(m)

# print(round(df[col].mean(), 3)) # 정답 25.055

##### 문제3.
import pandas as pd
df = pd.read_csv("bigdata2/part4/ch11/order_data.csv")
# print(df)

df['order_amt'] = df['quantity'] * df['price']
df['cancel_TF'] = df['order_no'].str.contains('C')

cond = df['cancel_TF'] == True
df.loc[cond, 'order_amt'] = df.loc[cond, 'order_amt'] * -1
# print(df)

# 3-1.
# 취소 주문만 필터링
cond = df['cancel_TF'] == True
df2 = df[cond]

# order_amt 절댓값이 가장 큰 행의 인덱스
im = df2['order_amt'].abs().idxmax()

# 특정 인덱스의 전체 행 출력
print(df2.loc[im]) # C542426

# 3-2.
# 고객별 order_amt 합계 계산
df = df.groupby('cus_id')['order_amt'].sum()

# 합계 중 최댓값
ma = df.max()

# 소수점 둘째 자리까지 출력
print(round(ma, 2)) # 정답 2877.21