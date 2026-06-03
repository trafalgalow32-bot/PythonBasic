"""
01. 필터링, 최솟값, 중앙값

'f5' 컬럼이 0이 아닌 데이터(행)를 구하시오. 
앞에서 구한 데이터에 'views' 컬럼 결측치를 'views'컬럼의 최솟값으로 채워주세요.
그리고 'views' 컬럼의 중앙값을 계산해 정수로 구하시오.
type1_data1.csv
"""

import pandas as pd
exam1 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')
# print(exam1)

cond = exam1['f5'] != 0
# print(exam1[cond].head())
m = exam1[cond]['views'].fillna(exam1['views'].min())
# print(m)
mid = m.median()
print(int(mid))

"""
02. 카테고리, 인덱스, 문자열 슬라이싱

'subscribed' 컬럼에서 가장 빈도수가 많은 날짜를 구하시오.
앞에서 구한 날짜의 일(day) 값을 정수로 구하시오.
"""

import pandas as pd
exam2 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

exam2 = exam2['subscribed'].value_counts()
# print(exam2.head())
# print(exam2)

day = int(exam2.index[0][-2:])
print(day)