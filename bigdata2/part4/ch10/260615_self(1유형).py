##### 기출문제 10회
##### 작업형 1유형
#####  문제1.



# 1-1.
# import pandas as pd
# df = pd.read_csv("bigdata2/part4/ch10/subject_performance.csv")
# print(df)
# df['소주제정답률'] = df.groupby('sub_topic')['is_correct'] / df.groupby('sub_topic')
# print(df)

# acc = df.groupby('sub_topic')['is_correct'].mean()
# # print(acc)

# result = acc.sort_values(ascending=False).drop_duplicates()
# print(round(result,3))

# 1-2. 
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch10/cafe_sales.csv')
# # df = df.sort_values('price', ascending=False)
# # print(df)

# df['order_date'] = pd.to_datetime(df['order_date'])
# df['year_month'] = df['order_date'].dt.to_period('M')
# # print(df)

# monthly_sales = df.groupby('year_month')['price'].sum()
# monthly_sales = monthly_sales.sort_values(ascending=False)
# print(monthly_sales)

# 1-3.
# import pandas as pd
# df = pd.read_csv('bigdata2/part4/ch10/hamspam.csv')
# # print(df)
# df['단어'] = df['text'].str.split()
# df['단어수'] = df['단어'].str.len()
# # print(df)

# # print(df['text'][1])
# # print(df['단어'][1])
# # print(df['단어수'][1])

# m = df.groupby('label')['단어수'].mean()

# diff = abs(m['spam'] - m['ham'])

# print(round(diff,3))

