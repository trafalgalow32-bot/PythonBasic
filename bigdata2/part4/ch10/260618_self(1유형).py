##### 기출문제 10회
##### 작업형 1유형
#####  문제1.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch10/subject_performance.csv")
# # print(df)

# # 소주제별 정답률 계산
# acc = df.groupby("sub_topic")["is_correct"].mean()

# # 내림차순 정렬 후 중복 제거
# result = acc.sort_values(ascending=False).drop_duplicates()
# print(round(result,3))

#####  문제2.

# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch10/cafe_sales.csv")
# # print(df)

# # 2-1.
# df['order_date'] = pd.to_datetime(df['order_date'])
# # df['year'] = df['order_date'].dt.year
# # df['month'] = df['order_date'].dt.month
# df['year_month'] = df['order_date'].dt.to_period("M")

# # 연월 단위로 그룹화하여 각 월의 총 매출액 계산
# m_sales = df.groupby('year_month')['price'].sum()

# # 연-월별 총매출액 중 상위 2번째 값
# print(m_sales.nlargest(3)) # 정답 328741

# # 2-2.
# # 연-월별 총매출액 중 상위 4개만 추출
# top4 = m_sales.nlargest(4)
# target_ym = top4.index[3]

# # 4번째로 큰 연-월에 해당하는 데이터만 추출
# cond = df['year_month'] == target_ym
# df = df[cond]

# # 해당 연-월의 카테고리별 매출 합계 중 최댓값 계산
# cate = df.groupby('category')['price'].sum()

# print(cate.max())

#####  문제3.

import pandas as pd
df = pd.read_csv("bigdata2/part4/ch10/hamspam.csv")
# print(df)

df['단어'] = df['text'].str.split()
df['단어수'] = df['단어'].str.len()

m = df.groupby('label')['단어수'].mean()

diff = abs(m['spam'] - m['ham'])

print(round(diff,3))
