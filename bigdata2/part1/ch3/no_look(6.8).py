# """
# 35. 데이터 합치기(merge)
# school_data.csv와 school_data_social.csv 파일을 '이름'을 기준으로 합치시오.
# 영어교사가 장선생이면서 사회교사가 오선생인 학생들을 필터링하시오.
# 필터링된 학생들의 수학 점수를 모두 더한 후 정수로 구하시오.
# """
# print("\n Q35")
# import pandas as pd
# data1 = pd.read_csv('bigdata2/part1/ch3/school_data.csv')
# data2 = pd.read_csv('bigdata2/part1/ch3/school_data_social.csv')

# merge = pd.merge(data1, data2, on='이름')
# # print(merge)

# cond1 = merge['영어교사'] == '장선생'
# cond2 = merge['사회교사'] == '오선생'

# result = merge[(cond1)&(cond2)]['수학'].sum()
# print(int(result))

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
# # print(exam23['실제도착시간'])
# exam23['예상도착시간'] = pd.to_datetime(exam23['예상도착시간'])

# # exam23['지연시간'] = (exam23['예상도착시간'] - exam23['실제도착시간']) # 이렇게 말고!

# exam23['지연시간'] = (exam23['실제도착시간'] - exam23['예상도착시간']).dt.total_seconds() / 60

# # exam23['지연시간'] = pd.to_datetime(exam23['지연시간']) # 이거 필요 없음!
# # print(exam23['지연시간'])
# exam23['지연여부'] = exam23['지연시간'] > 0

# delay = exam23.groupby('결제종류')['지연여부'].mean() # 여기 mean()을 왜 붙이지?
# # print(delay)
# delay = delay.max()
# print(round(delay,2))

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

# # exam4= exam4.sort_values('views', ascending=False)
# exam4 = exam4.sort_values('views', ascending=False) # 데이터 전체를 내림차순으로, 기준을 'views' 컬럼으로해서! 
# # print(exam4)

# # print(exam4[10:30])
# # print(exam4)
# # top10 = exam4['views'][:9]
# # print(top10)

# min = exam4.iloc[:10]['views'].min()
# exam4.iloc[:10,-1] = min
# # print(min)

# print(int(exam4['views'].sum()))


# """
# 22. 시간 간의 차이 계산(분), 그룹핑
# 주문 시간과 실제 도착 시간의 차이를 분 단위로 계산하시오.
# 앱 종류별로 평균 도착 시간(분)을 계산하시오.
# 평균적으로 가장 빠른 앱 종류를 찾고, 해당 앱의 평균 도착 시간을 분으로 반올림하여 정수로 구하시오.
# """
# print("\n Q22")
# import pandas as pd
# exam22 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')

# # exam22['주문시간'] = exam22['주문시간'].pd.to_datetime # 문법오류!! 다시!
# exam22['주문시간'] = pd.to_datetime(exam22['주문시간'])
# exam22['실제도착시간'] = pd.to_datetime(exam22['실제도착시간'])
# # print(exam22)

# exam22['diff'] = (exam22['실제도착시간'] - exam22['주문시간']).dt.total_seconds() / 60

# diff_mean = exam22.groupby('앱종류')['diff'].mean()

# print(int(round(diff_mean.min())))

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

# result = exam16['views'][(exam16['views'] < cond1) | (exam16['views'] > cond2)].sum()
# print(int(result))