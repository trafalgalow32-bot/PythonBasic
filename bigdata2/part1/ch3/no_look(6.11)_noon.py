# """
# 11. 슬라이싱, 사분위수, 결측치 제거
# 데이터에서 결측치가 있는 데이터(행)를 모두 제거하시오.
# 결측치가 제거된 데이터를 사용하여 앞에서부터 70% 데이터를 구하시오. 
# (단, 데이터 70% 지점의 index 가 소수점으로 계산될 경우 소수점 이하는 버림)
# 앞에서 구한 70% 데이터 중 'views' 컬럼의 3사분위수에서 1사분위수를 뺀 값을 소수점 이하를 버리고 정수 부분만 구하시오.
# """
# print("\n Q11")
# import pandas as pd
# exam11 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# exam11 = exam11.dropna()
# # print(exam11)


# # data = exam11[:len(exam11)*0.7]
# # print(data)
# # a = len(exam11)*0.7 # int(len(exam11)*0.7)로!
# # print(a)

# data = exam11[:49] # 49를 콕 집어서 하드코딩은 자제! 그래도 정답을 맞췄으니 다행!
# # print(data)
# q3 = data['views'].quantile(.75)
# q1 = data['views'].quantile(.25)
# print(int(q3 - q1))

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
# sum = exam19.groupby(['city', 'f2']).sum(numeric_only=True) # reset_index() 여기에!!!
# sum = sum.sort_values('views', ascending=False)
# # print(sum)

# print(sum.iloc[2,0])

# """
# 02. 카테고리, 인덱스, 문자열 슬라이싱

# 'subscribed' 컬럼에서 가장 빈도수가 많은 날짜를 구하시오.
# 앞에서 구한 날짜의 일(day) 값을 정수로 구하시오.
# """
# print("\n Q2")
# import pandas as pd
# exam2 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# # print(exam2['subscribed'].value_counts())

# cnt = exam2['subscribed'].value_counts()
# # print(cnt)
# # print(cnt.head())

# # print(cnt.iloc[0:-2])

# ## .index[][] 꼴을 못 떠올렸음.......
# day = int(cnt.index[0][-2:])
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

# # 지역별 평균 판매금액 계산에서부터 난항!!
# # mean = exam36.groupby('지역코드').transform(exam36['판매금액'].mean())
# # exam36['판매금액'] = exam36['판매금액'].dropna(mean)
# # print(exam36)

# m = exam36.groupby('지역코드')['판매금액'].transform('mean')
# exam36['판매금액'] = exam36['판매금액'].fillna(m)

# exam36['지역평균'] = exam36.groupby('지역코드')['판매금액'].transform('mean')

# exam36['차이'] = abs(exam36['판매금액'] - exam36['지역평균'])

# result = exam36.groupby('지역코드')['차이'].mean().idxmax()

# print(result)

# """
# 30. 주말, 평일 구분
# 주말 주문 건수와 평일 주문 건수를 구하시오.
# 주말 주문 건수와 평일 주문 건수의 차이를 절대값으로 구하고 정수형으로 구하시오.
# """
# print("\n Q30")
# import pandas as pd
# exam30 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')

# exam30['주문시간'] = pd.to_datetime(exam30['주문시간'])

# exam30['dayofweek'] = exam30['주문시간'].dt.dayofweek
# exam30['주말'] = exam30['dayofweek'] >= 5

# weekend = sum(exam30['주말'])
# weekday = len(exam30) - weekend

# print(abs(weekend - weekday))

# """
# 13. 결측 데이터 찾기, 필터링, 평균값
# 'f1' 컬럼에 결측치가 있는 데이터만 선택하시오.
# 선택된 데이터에서 'age' 컬럼의 평균값을 구하시오. (반올림 후 소수 첫째 자리까지 계산)
# """
# print("\n Q13")
# import pandas as pd
# exam13 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# exam13 = exam13[exam13['f1'].isna()]
# # print(exam13)

# m = exam13['age'].mean()
# print(round(m,1))

# """
# 15. 컬럼 삭제, 행 단위 합계, 필터링
# 주어진 데이터에서 문자 자료형 컬럼을 삭제하시오.
# 숫자 자료형 컬럼의 결측치를 0으로 대체하시오.
# 각 행의 합이 3000보다 큰 값의 개수를 정수로 구하시오. (각 행의 합: 'age' + 'f1' + 'f2' + 'f5' + 'views')
# """
# ##### 완전 오픈북 ㅋㅋㅋ!! 컬럼 삭제하는 방법 모름. 문자 자료형만 걸러내는 것도 모르고!
# print("\n Q15")
# import pandas as pd
# exam15 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# # exam15 = exam15.drop # 이렇게 하지 말고
# cols = exam15.select_dtypes(exclude='object').columns
# exam15 = exam15[cols]

# # print(exam15)

# exam15 = exam15.fillna(0)
# exam15 = exam15.T

# print(sum(exam15.sum() > 3000))
