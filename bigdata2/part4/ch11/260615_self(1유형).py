##### 기출문제 11회
##### 작업형 1유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch11/greenhouse_gas.csv")
# # print(df)

# # 1-1.
# # 연도 컬럼만 선택
# cols = df.columns[1:] # Country를 제외한 나머지

# # 각 연도별 최댓값의 행 번호 찾기
# max_index = df[cols].idxmax()

# # 해당 행의 국가명 가져오기
# df2 = df.loc[max_index]

# # 국가별 1위 횟수 세기
# print(df2['Country'].value_counts()) # 정답 11

# # 1-2.
# # CAGR 계산
# df['CAGR'] = (df['2021'] / df['2001']) ** (1/20) -1

# # 최댓값 구하기
# result = df['CAGR'].max()
# print(round(result, 3)) # 정답 0.047

##### 문제2.
# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch11/sensor_data.csv")

# # 각 컬럼의 결측치 개수 확인
# print(df.isnull().sum())

# # 결측치가 가장 많은 컬럼 찾기
# col = df.isnull().sum().idxmax()
# # print(col) # S2_Temp

# # 해당 컬럼의 중앙값 계산
# m = df[col].median()

# # 결측치를 중앙값으로 대체
# df[col] = df[col].fillna(m)

# print(round(df[col].mean(), 3)) # 정답 25.055

##### 문제3.
import pandas as pd
df = pd.read_csv("bigdata2/part4/ch11/order_data.csv")

# order_amt 생성
df['order_amt'] = df['quantity'] * df['price']

# is_cancel 생성
df['is_cancel'] = df['order_no'].str.contains('C')

# 취소 주문을 음수로 변환
cond = df['is_cancel'] == True
df.loc[cond, 'order_amt'] = df.loc[cond, 'order_amt'] * -1
# print(df.head())

# 3-1.
# 취소 주문만 필터링
cond = df['is_cancel'] == True
cancel_df = df[cond]

# order_amnt 절댓값이 가장 큰 행의 인덱스
im = cancel_df['order_amt'].abs().idxmax()

# 특정 인덱스의 전체 행 출력(모든 컬럼)
print(cancel_df.loc[im])

# 3-2. 
# 고객별 order_amt 합계 계산
df = df.groupby('cus_id')['order_amt'].sum()

# 합계 중 최댓값
ma = df.max()

# 소수점 둘째 자리까지 출력
print(round(ma, 2))