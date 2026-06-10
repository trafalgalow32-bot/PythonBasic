# """
# 22. 시간 간의 차이 계산(분), 그룹핑
# 주문 시간과 실제 도착 시간의 차이를 분 단위로 계산하시오.
# 앱 종류별로 평균 도착 시간(분)을 계산하시오.
# 평균적으로 가장 빠른 앱 종류를 찾고, 해당 앱의 평균 도착 시간을 분으로 반올림하여 정수로 구하시오.
# """
# print("\n Q22")
# import pandas as pd
# exam22 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')

# # print(exam22)
# exam22['주문시간'] = pd.to_datetime(exam22['주문시간'])
# exam22['실제도착시간'] = pd.to_datetime(exam22['실제도착시간'])

# exam22['시간차이'] = (exam22['실제도착시간'] - exam22['주문시간']).dt.total_seconds() / 60

# mean = exam22.groupby('앱종류')['시간차이'].mean()
# print(int(round(mean.min())))

# """
# 04. 값 변경, 정렬, 합계
# 'views' 컬럼의 결측 데이터를 0으로 대체하시오.
# 'views' 컬럼에서 상위 10번째 값을 구하시오.
# 'views' 컬럼에서 상위 10개의 값을 상위 10번째 값으로 대체하시오.
# 'views' 컬럼의 전체 합을 정수로 구하시오.
# """
# print("\n Q4")
# import pandas as pd
# exam4 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# exam4['views'] = exam4['views'].fillna(0)
# # print(exam4['views'].head(30))
# exam4 = exam4.sort_values('views', ascending=False).reset_index(drop=True)
# # print(exam4[:10])
# top10 = exam4['views'][9]
# # print(top10)
# exam4['views'][:10] = top10 ## ? iloc 안 쓰고 이런 식으로 해도 되는지?
# # print(exam4[:11])
# sum = exam4['views'].sum()
# print(int(sum))

# """
# 19.결측치(뒤의 값으로 대체), 그룹합
# 결측치를 바로 뒤에 있는 값으로 대체하시오. (바로 뒤의 값도 결측치일 경우, 뒤에 있는 데이터 중 가장 가까운 값으로 대체)
# 'city'와 'f2'컬럼을 기준으로 그룹합을 계산하시오.
# 'views' 값이 세 번째로 큰 city 이름을 구하시오.
# """
# print("\n Q19")
# import pandas as pd
# exam19 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# exam19 = exam19.bfill()
# # print(exam19)
# sum = exam19.groupby(['city', 'f2']).sum(numeric_only=True).reset_index() # 왜 reset_index() 여기에?

# sum = sum.sort_values('views', ascending=False) # .reset_index(drop=True) # 이걸 왜 여기 쓰면 안됨? 
# # print(sum)
# print(sum.iloc[2,0])

# """
# 36. 조건별 변환
# 결측된 판매금액은 해당 지역의 평균 판매금액으로 결측값을 대체하시오.
# 각 거래마다 "판매금액"과 해당 지역의 평균 판매금액의 "차이"를 절대값으로 구하시오.
# 각 지역에서 차이값의 평균을 구한 후, 이 값이 가장 큰 지역의 지역코드를 구하시오.
# """
# print("\n Q36")
# import pandas as pd
# exam36 = pd.read_csv('bigdata2/part1/ch3/sales.csv')

# # print(exam36)
# # mean1 = exam36.groupby('지역코드')['판매금액'].mean() # transform을 여기에 써야...

# # exam36['판매금액'] = exam36['판매금액'].fillna(transform('mean1')) # 또 transform을....!!!

# # 오픈북으로 다시! 
# mean1 = exam36.groupby('지역코드')['판매금액'].transform('mean')
# exam36['판매금액'] = exam36['판매금액'].fillna(mean1)

# exam36['지역평균'] = exam36.groupby('지역코드')['판매금액'].transform('mean')

# exam36['차이'] = abs(exam36['판매금액'] - exam36['지역평균'])

# result = exam36.groupby('지역코드')['차이'].mean().idxmax()
# print(result)