# """
# 23. 시간 간의 차이 계산(분), 비율
# 각 결제 종류별로 실제 도착 시간이 예상 도착 시간보다 늦은 주문의 비율을 계산하시오.
# 비율 중 가장 큰 값을 반올림하여 소수 둘째 자리까지 구하시오.
# """
# print("\n Q23")
# import pandas as pd
# exam23 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')

# # print(exam23)
# exam23['실제도착시간'] = pd.to_datetime(exam23['실제도착시간'])
# exam23['예상도착시간'] = pd.to_datetime(exam23['예상도착시간'])

# exam23['시간차이'] = (exam23['실제도착시간'] - exam23['예상도착시간']).dt.total_seconds() / 60
# exam23['지연여부'] = exam23['시간차이'] > 0 
# # print(exam23['지연여부'])
# # print(exam23)
# ratio = exam23.groupby('결제종류')['지연여부'].mean() # '앱종류'가 아닌 '결제종류'!! 발문 똑바로..
# print(round(ratio.max(),2))

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
# # exam22['평균도착시간'] = exam22['시간차이'].mean() # 평균은 굳이 []로 하지 않음... 
# mean = exam22.groupby('앱종류')['시간차이'].mean()
# # print(exam22)
# # mean = exam22.groupby('앱종류')[]

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
# # print(exam4.head(40))

# exam4 = exam4.sort_values('views', ascending=False).reset_index(drop=True)
# # print(exam4)
# # print(exam4.loc[0:1])

# # 여기부터가 안됨! iloc, loc 구분!! 
# min = exam4['views'].iloc[9]

# exam4.loc[0:9, 'views'] = min
# # print(min)
# print(int(exam4['views'].sum()))


# """
# 02. 카테고리, 인덱스, 문자열 슬라이싱

# 'subscribed' 컬럼에서 가장 빈도수가 많은 날짜를 구하시오.
# 앞에서 구한 날짜의 일(day) 값을 정수로 구하시오.
# """
# print("\n Q2")
# import pandas as pd
# exam2 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# #### 이거 무한 반복 필수임!! 어렵네.... ####

# exam2 = exam2['subscribed'].value_counts()
# # print(exam2.head())
# day = int(exam2.index[0][-2:])
# print(day)

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
# # exam36['판매금액'] = exam36.transform() # transform 함수 사용법을 몰러!!
# m = exam36.groupby('지역코드')['판매금액'].transform('mean')
# exam36['판매금액'] = exam36['판매금액'].fillna(m)

# exam36['지역평균'] = exam36.groupby('지역코드')['판매금액'].transform('mean')
# exam36['차이'] = abs(exam36['판매금액'] - exam36['지역평균'])

# result = exam36.groupby('지역코드')['차이'].mean().idxmax()
# print(result)

# """
# 19.결측치(뒤의 값으로 대체), 그룹합
# 결측치를 바로 뒤에 있는 값으로 대체하시오. (바로 뒤의 값도 결측치일 경우, 뒤에 있는 데이터 중 가장 가까운 값으로 대체)
# 'city'와 'f2'컬럼을 기준으로 그룹합을 계산하시오.
# 'views' 값이 세 번째로 큰 city 이름을 구하시오.
# """
# print("\n Q19")
# import pandas as pd
# exam19 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# # b = exam19.bfill()
# # exam19 = exam19.fillna(b) # 이렇게 해도 좋지만 코드를 최소/효율화!
# exam19 = exam19.bfill()
# # print(exam19)

# sum = exam19.groupby(['city','f2']).sum(numeric_only=True).reset_index() # ['views'].sum() 숫자만 계산해야 하니 numeric_only!
# # print(sum)

# exam19 = exam19.sort_values('views', ascending=False)

# print(exam19.iloc[2,2])