# """
# 35. 데이터 합치기(merge)
# school_data.csv와 school_data_social.csv 파일을 '이름'을 기준으로 합치시오.
# 영어교사가 장선생이면서 사회교사가 오선생인 학생들을 필터링하시오.
# 필터링된 학생들의 수학 점수를 모두 더한 후 정수로 구하시오.
# """
# print("\n Q35")
# import pandas as pd
# exam35 = pd.read_csv('bigdata2/part1/ch3/school_data.csv')
# exam35_soc = pd.read_csv('bigdata2/part1/ch3/school_data_social.csv')

# merge = pd.merge(exam35, exam35_soc, on='이름')
# # print(merge)

# cond1 = merge['영어교사'] == '장선생'
# cond2 = merge['사회교사'] == '오선생'

# filter = merge[(cond1)&(cond2)]
# # print(filter)
# math = filter['수학'].sum()
# print(int(math))

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

# exam23['지연시간'] = (exam23['실제도착시간'] - exam23['예상도착시간']).dt.total_seconds() / 60
# exam23['지연여부'] = exam23['지연시간'] > 0
# # print(exam23['지연여부'])

# ratio = exam23.groupby('결제종류')['지연여부'].mean()
# print(ratio)
##### 보류

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

# exam4 = exam4.sort_values('views', ascending=False).reset_index(drop=True)
# # print(exam4)
# min = exam4['views'].iloc[9]
# # print(min)

# exam4.loc[0:9, 'views'] = min
# # print(min)

# print(int(exam4['views'].sum()))

# # print(top10.iloc[10,-1])
# # min = top10['views']

# ### 보류

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
# # print(exam22)
# # exam22['평균도착시간'] = exam22.groupby('앱종류')['시간차이'].mean() # ['평균도착시간'] 이거 할 필요 엄슴...
# # print(exam22['평균도착시간'])
# diff_mean = exam22.groupby('앱종류')['시간차이'].mean()
# print( int(round(diff_mean.min())))
# # exam22['평균 도착 시간(분)'] = exam22.groupby('앱종류')['평균도착시간']
# # print(exam22['평균 도착 시간(분)'])
# #### 또 보류...

# """
# 16. 이상치, IQR
# 'views' 컬럼의 1사분위수, 3사분위수 그리고 IQR을 계산하시오.
# 이상치 조건에 맞는 데이터를 찾으시오. (이상치는 1분위수 - (IQR * 1.5)보다 작은 값과 3사분위수 + (IQR  * 1.5)보다 큰 값)
# 이상치 데이터의 'views' 컬럼 합을 정수로 구하시오.
# """
# print("\n Q16")
# import pandas as pd
# exam16 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# q3 = exam16['views'].quantile(.75)
# q1 = exam16['views'].quantile(.25)
# iqr = q3 - q1

# cond1 = q1 - (iqr * 1.5)
# cond2 = q3 + (iqr * 1.5)

# outlier = exam16[(exam16['views'] < cond1) | (exam16['views'] > cond2)]
# # print(outlier)
# result = outlier['views'].sum()
# print(int(result))


# """
# 36. 조건별 변환(transform)
# 결측된 판매금액은 해당 지역의 평균 판매금액으로 결측값을 대체하시오.
# 각 거래마다 "판매금액"과 해당 지역의 평균 판매금윽애 "차이"를 절대값으로 구하시오.
# 각 지역에서 차이값의 평균을 구한 후, 이 값이 가장 큰 지역의 지역코드를 구하시오.
# """
# print("\n Q36")
# import pandas as pd
# exam36 = pd.read_csv('bigdata2/part1/ch3/sales.csv')

# # print(exam36)
# mean = exam36.groupby('지역코드')['판매금액'].transform('mean') #.mean()이 아닌!
# # print(mean)

# exam36['판매금액'] = exam36['판매금액'].fillna(mean)
# # print(exam36) ####?? 지역코드별 판매금액 평균을 구했는데, 이걸 어떻게 각 지역코드 별 결측값을 대체해야 하는지!

# exam36['지역평균'] = exam36.groupby('지역코드')['판매금액'].transform('mean')

# exam36['차이'] = abs(exam36['판매금액'] - exam36['지역평균'])

# result = exam36.groupby('지역코드')['차이'].mean().idxmax()
# print(result)

# """
# 06. 필터링, 분산
# 'f3' 컬럼이 gold이면서 'f2'컬럼이 2인 데이터를 찾으시오.
# 찾은 데이터에서 'f1' 컬럼의 분산을 구하시오. (반올림 후 소수 둘째 자리까지 계산)
# """
# print("\n Q6")
# import pandas as pd
# exam6 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# filter = exam6[(exam6['f3'] == 'gold') & (exam6['f2'] == 2)]
# # print(filter)
# var = filter['f1'].var()
# print(round(var,2))

# """
# 02. 카테고리, 인덱스, 문자열 슬라이싱

# 'subscribed' 컬럼에서 가장 빈도수가 많은 날짜를 구하시오.
# 앞에서 구한 날짜의 일(day) 값을 정수로 구하시오.
# """
# print("\n Q2")
# import pandas as pd
# exam2 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# # print(exam2['subscribed'].count())
# # exam2['subscribed'] = pd.to_datetime(exam2['subscribed']) # 이것도 필요 엄슴..
# # cnt = exam2['subscribed']. # 에라이!! 그룹별 카운팅도, 인덱스도, 문자열 슬라이싱도 다 모르것어! 

# exam2 = exam2['subscribed'].value_counts()
# # print(exam2.head())

# day = int(exam2.index[0][-2:])
# print(day)

# """
# 07. 값 변경(연산), 필터링 절댓값
# 모든 나이(age)에 1을 더하시오.
# 20대의 'views' 평균과 30대의 'views' 평균의 차이의 절댓값을 구하시오. (반올림 후 소수 둘째자리까지 계산)
# """
# print("\n Q7")
# import pandas as pd
# exam7 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')
# exam7['age'] = exam7['age'] + 1
# # print(exam7)

# cond1 = (exam7['age'] >= 20) & (exam7['age'] < 30)
# cond2 = (exam7['age'] >= 30) & (exam7['age'] < 40)
# # print(exam7[cond1])
# mean1 = exam7[cond1]['views'].mean()
# # print(mean1)
# mean2 = exam7[cond2]['views'].mean()
# # print(mean2)
# diff = abs(mean1 - mean2)
# print(round(diff,2))