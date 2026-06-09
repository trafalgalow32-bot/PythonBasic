# """
# 23. 시간 간의 차이 계산(분), 비율
# 각 결제 종류별로 실제 도착 시간이 예상 도착 시간보다 늦은 주문의 비율을 계산하시오.
# 비율 중 가장 큰 값을 반올림하여 소수 둘째 자리까지 구하시오.
# """
# print("\n Q23")
# import pandas as pd
# exam23 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')

# exam23['실제도착시간'] = pd.to_datetime(exam23['실제도착시간'])
# exam23['예상도착시간'] = pd.to_datetime(exam23['예상도착시간'])

# exam23['지연시간'] = (exam23['실제도착시간'] - exam23['예상도착시간']).dt.total_seconds() / 60
# exam23['지연여부'] = exam23['지연시간'] > 0
# # print(exam23)

# # ratio = exam23['지연여부'].mean()
# # print(round(ratio,2)) # 오답! groupby 안함!!
# ratio = exam23.groupby('결제종류')['지연여부'].mean()
# print(round(ratio.max(),2))

"""
04. 값 변경, 정렬, 합계
'views' 컬럼의 결측 데이터를 0으로 대체하시오.
'views' 컬럼에서 상위 10번째 값을 구하시오.
'views' 컬럼에서 상위 10개의 값을 상위 10번째 값으로 대체하시오.
'views' 컬럼의 전체 합을 정수로 구하시오.
"""
print("\n Q4")
import pandas as pd
exam4 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')\

exam4['views'] = exam4['views'].fillna(0)
exam4 = exam4.sort_values('views', ascending=False).reset_index(drop=True)
# print(exam4)
top10 = exam4.iloc[9]
# print(top10)
exam4.loc[0:9, 'views'] = top10

print(int(exam4['views'].sum()))