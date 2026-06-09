# practice02.py
# Part1 연습문제 20~37
"""
20. 시계열 데이터, 월별 집계, 인덱스
연도 구분 없이 월별로 숫자형 컬럼의 합을 구하시오.
합계 중 'views'가 가장 작은 값들을 가진 월을 정수로 구하시오.
"""
print("\n Q20")
import pandas as pd
exam20 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# 자료형 변환
exam20['subscribed'] = pd.to_datetime(exam20['subscribed'])

# 파생변수 생성
exam20['month'] = exam20['subscribed'].dt.month

# 월별로 데이터 합 집계
exam20 = exam20.groupby('month').sum(numeric_only=True)

# 오름차순 정렬 및 가장 작은 값 출력
print(exam20.sort_values('views').index[0]) # 출력값 11

"""
21. 시간 간의 차이 계산(분), 필터링
예상 도착 시간보다 늦게 도착한 건수를 구하시오.
이 중 거리가 7km 이상인 데이터의 수를 정수로 구하시오.
"""
print("\n Q21")
import pandas as pd
exam21 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')
# print(exam21)
# 자료형 변경
exam21['실제도착시간'] = pd.to_datetime(exam21['실제도착시간'])
exam21['예상도착시간'] = pd.to_datetime(exam21['예상도착시간'])

# 지연 시간 계산(분)
exam21['지연시간'] = (exam21['실제도착시간'] - exam21['예상도착시간']).dt.total_seconds() / 60
# print(exam21)

# 조건1 - 예상 도착 시간보다 늦게 도착한 건
cond1 = exam21['지연시간'] > 0

# 조건2 - 거리가 7이상인 건
cond2 = exam21['거리'] >= 7

# 출력
print(len(exam21[cond1 & cond2])) # 출력값 311

"""
22. 시간 간의 차이 계산(분), 그룹핑
주문 시간과 실제 도착 시간의 차이를 분 단위로 계산하시오.
앱 종류별로 평균 도착 시간(분)을 계산하시오.
평균적으로 가장 빠른 앱 종류를 찾고, 해당 앱의 평균 도착 시간을 분으로 반올림하여 정수로 구하시오.
"""
print("\n Q22")
import pandas as pd
exam22 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')

# 자료형 변경
exam22['실제도착시간'] = pd.to_datetime(exam22['실제도착시간'])
exam22['주문시간'] = pd.to_datetime(exam22['주문시간'])

# 실제 도착 시간과 주문 시간 차이 계산(분)
exam22['diff'] = (exam22['실제도착시간'] - exam22['주문시간']).dt.total_seconds() / 60

# 앱 종류별 도착 시간과 주문 시간 차이의 평균 계산
diff_mean = exam22.groupby('앱종류')['diff'].mean()

# 가장 작은 시간(분) 반올림 후 출력
print(int(round(diff_mean.min()))) # 출력값 62

"""
23. 시간 간의 차이 계산(분), 비율
각 결제 종류별로 실제 도착 시간이 예상 도착 시간보다 늦은 주문의 비율을 계산하시오.
비율 중 가장 큰 값을 반올림하여 소수 둘째 자리까지 구하시오.
"""
print("\n Q23")
import pandas as pd
exam23 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')

# 자료형 변경
exam23['실제도착시간'] = pd.to_datetime(exam23['실제도착시간'])
exam23['예상도착시간'] = pd.to_datetime(exam23['예상도착시간'])

# 지연 시간 계산(분)
exam23['지연시간'] = (exam23['실제도착시간'] - exam23['예상도착시간']).dt.total_seconds() / 60 # 분 단위로 계산

# 실제 도착 시간이 예상 도착 시간보다 늦은 경우를 체크하는 컬럼 생성
exam23['지연여부'] = exam23['지연시간'] > 0

# 결제 종류별 지연된 주문 수의 비율 계산
result = exam23.groupby('결제종류')['지연여부'].mean()

# 가장 비율 높은 값
print(round(result.max(), 2)) # 출력값 0.56

"""
24. 그룹핑, 값 찾기, 필터링
사용자별 주문 거리의 합계가 50km 이상인 사람들의 결제 방식을 구하시오.
이 결제 방식 중 가장 빈도가 높은 수를 구하시오.
"""
print("\n Q24")
import pandas as pd
exam24 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')
# print(exam24)

# 사용자별로 주문 거리의 합계 계산
exam24_dis = exam24.groupby('user')['거리'].sum()

# 주문 거리의 합계가 50km 이상인 사용자만 필터링
cond = exam24_dis >= 50
exam24_dis = exam24_dis[cond]

# 주문 거리의 합계가 50km 이상인 사용자들의 데이터 필터링
filtered_data = exam24[exam24['user'].isin(exam24_dis.index)]
filtered_data

# 해당 사용자들의 선호 결제 방식 중 큰 값
pay_way = filtered_data['결제종류'].value_counts()
# print(pay_way)
print(pay_way.iloc[0]) # 출력값 48

"""
25. 시간 간의 차이 계산(일)
각 사용자별로 첫 주문과 마지막 주문 사이의 시간 간격을 일 단위로 계산하시오.
시간차가 0일인 사용자를 제외하고, 나머지 사용자들의 평균 시간 간격(일 단위)을 계산하시오.
평균 시간 간격보다 긴 시간 간격을 가진 사용자의 수를 정수로 구하시오.
"""
print("\n Q25")
import pandas as pd
exam25 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')

# 각 사용자별로 첫 주문과 마지막 주문 사이의 시간 간격(일 단위)을 계산
exam25['주문시간'] = pd.to_datetime(exam25['주문시간'])
min = exam25.groupby('user')['주문시간'].min()
max = exam25.groupby('user')['주문시간'].max()
time_diff = (max - min).dt.days

# 1일 이하 주문 제외
cond1 = time_diff > 0
m = time_diff[cond1].mean()

# 평균보다 기간이 긴 유저 수
cond2 = time_diff > m
print(len(time_diff[cond2])) # 출력값 146

"""
26. 날짜와 시간 정보 변환, 비율
주문이 가장 많이 발생한 연-월을 찾으시오.
해당 연-월에 '배고팡' 앱을 통한 주문 중 '앱결제'로 결제된 주문의 비율을 계산하시오.
(반올림 후 소수 둘째 자리까지 계산)
"""
print("\n Q26")
import pandas as pd
exam26 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')

# 주문이 가장 많이 발생한 연-월 찾기
exam26['주문시간'] = pd.to_datetime(exam26['주문시간'])
exam26['주문월'] = exam26['주문시간'].dt.to_period('M')
year_month = exam26['주문월'].value_counts().idxmax()

# 해당 연-월에 배고팡 앱을 통한 주문 중 '앱 결제'로 결제된 주문의 비율 계산
cond1 = exam26['주문월'] == year_month
cond2 = exam26['앱종류'] == '배고팡'
filtered = exam26[cond1 & cond2]
cond3 = filtered['결제종류'] == '앱결제'
result = len(filtered[cond3]) / len(filtered)
print(round(result, 2)) # 출력값 0.31

"""
27. 시간 범위, 속도(km/h)
점심 시간(10시부터 13시 전까지)에 주문된 배달 데이터를 찾으시오.
점심시간 주문 건 중 과속(평균 속도가 50km/h 이상)하는 주문 수를 정수로 구하시오.
배달 시간 = 실제도착시간 - 주문시간
속도(km/h) = 거리(km) / 시간(h)
"""
print("\n Q27")
import pandas as pd
exam27 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')

# 자료형 변경
exam27['주문시간'] = pd.to_datetime(exam27['주문시간'])
exam27['실제도착시간'] = pd.to_datetime(exam27['실제도착시간'])

# 점심 시간 주문 선택
exam27['시간'] = exam27['주문시간'].dt.hour
cond1 = exam27['시간'] >= 10
cond2 = exam27['시간'] < 13
exam27 = exam27[cond1 & cond2]

# 속도(km/h) = 거리(km) / 시간(h)
exam27['배달시간'] = exam27['실제도착시간'] - exam27['주문시간']
exam27['배달시간'] = exam27['배달시간'].dt.total_seconds() / 60 / 60 # 시간 단위로 변경
exam27['속도'] = exam27['거리'] / exam27['배달시간']
print(sum(exam27['속도'] >= 50)) # 출력값 1


"""
28. 날짜와 시간, 문자열
연도와 월을 기준으로 주문 수를 집계하시오.
가장 많은 주문이 있었던 연도와 월을 예시와 같은 형식으로 숫자로만 구하시오. 
(예: 2024년 2월인 경우 '202402', 2024년 10월인 경우 '202410')
"""
print("\n Q28")
import pandas as pd
exam28 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')

# 주문 연월 추출(연도-월)
exam28['주문시간'] = pd.to_datetime(exam28['주문시간'])
exam28['주문월'] = exam28['주문시간'].dt.to_period('M')

# 주문 월을 기준으로 빈도 수(주문 횟수) 계산
cnt_month = exam28.groupby('주문월').size()

# 주문 횟수가 가장 많은 월의 인덱스 추출
year_month = cnt_month.idxmax()

# 문자열로 변경 및 하이픈(-) 제거
year_month = str(year_month)
result = year_month.replace("-","")
print(result) # 출력값 202209

"""
29. 함수, 월별 집계
배달료 계산 기준표에 따라 각 주문에 대한 배달료를 계산하시오.
연도-월별로 배달료의 총합을 집계하시오.
배달료가 가장 많이 발생한 월을 찾고, 그 월의 총 배달료를 정수로 구하시오.
[배달료 기준표]
- 5km 미만: 2,000원
- 5km 이상 ~ 10km 미만: 4,000원
- 10km 이상 ~ 15km 미만: 6,000원
- 15km 이상 ~ 20km 미만: 8,000원

"""
print("\n Q29")
import pandas as pd
exam29 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')

# 배달료 계산 함수
def fee(distance):
    if distance < 5:
        return 2000
    elif distance < 10:
        return 4000
    elif distance < 15:
        return 6000
    elif distance < 20:
        return 8000

# 각 주문에 대한 배달료 계산
exam29['배달료'] = exam29['거리'].apply(fee)

# 월별로 배달료 집계
exam29['주문시간'] = pd.to_datetime(exam29['주문시간'])

# 월별로 배달료의 총집합 집계
exam29['주문시간'] = pd.to_datetime(exam29['주문시간'])
period_m = exam29['주문시간'].dt.to_period("M")
monthly = exam29.groupby(period_m)['배달료'].sum()

# 가장 많은 배달료가 발생한 월과 그 월의 총 배달료 찾기
max_fee_month = monthly.idxmax()
max_fee_value = monthly[max_fee_month]
print(max_fee_value) # 출력값 448000

"""
30. 주말, 평일 구분
주말 주문 건수와 평일 주문 건수를 구하시오.
주물 주문 건수와 평일 주문 건수의 차이를 절대값으로 구하고 정수형으로 구하시오.
"""
print("\n Q30")
import pandas as pd
exam30 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')
exam30['주문시간'] = pd.to_datetime(exam30['주문시간'])

# 주말/평일 구분 0: 월, 1: 화 ~ 5: 토, 6: 일
exam30['dayofweek'] = exam30['주문시간'].dt.dayofweek
exam30['주말'] = exam30['dayofweek'] >= 5

# 주말 개수, 평일 개수 계산
weekend = sum(exam30['주말'])
weekday = len(exam30) - weekend # sum(~exam30['주말']) 보다 리스크 덜한 코드로 변경!

# 차이 절댓값 출력
print(abs(weekend - weekday)) # 출력값 412

"""
31. 문자열, 형 변환
'user' 컬럼에서 user 뒤에 있는 숫자 값만 추출하시오.
추출된 숫자 값을 모두 합한 값을 정수로 구하시오.
"""
print("\n Q31")
import pandas as pd
exam31 = pd.read_csv('bigdata2/part1/ch3/delivery_time.csv')
# print(exam31)

# 문자 슬라이싱
exam31['user_int'] = exam31['user'].str[5:]
# print(exam31['user_int'])

# 자료형 변환
exam31['user_int'] = exam31['user_int'].astype(int)

# 합계
print(exam31['user_int'].sum()) # 출력값 261387

"""
32. 합계(열 방향), 상위 값 선택
수학, 영어, 국어 점수의 합을 구하시오.
합이 가장 큰 상위 10명을 찾으시오.
찾은 10명의 수학 평균 점수를 구하시오. (반올림 후 정수 출력)
"""
print("\n Q32")
import pandas as pd
exam32 = pd.read_csv('bigdata2/part1/ch3/school_data.csv')
# print(exam32)

# 수학, 영어, 국어 점수 합계
exam32['total_score'] = exam32[['수학', '영어', '국어']].sum(axis=1) # exam32['total_score'] = exam32['수학'] + exam32['영어'] + exam32['국어'] 가능!
# print(exam32['total_score'])

# 합계 점수를 기준으로 상위 10명 선택
top10 = exam32.nlargest(10, 'total_score')

# 선택된 10명의 수학 평균 점수 계산
result = top10['수학'].mean()
print(round(result)) # 출력값 82

"""
33. 데이터프레임 재구조화
과목에 상관없이 점수가 가장 작은 점수 25개를 찾으시오.
찾은 점수 25개의 합을 정수로 구하시오.
"""
print("\n Q33")
import pandas as pd
exam33 = pd.read_csv('bigdata2/part1/ch3/school_data.csv')

# 이름을 유지하면서 수학, 영어, 국어 형태 변경
melted_exam33 = exam33.melt(id_vars=['이름'], value_vars=['수학', '영어', '국어'])

# 가장 작은 값 25개의 합
result = melted_exam33['value'].nsmallest(25).sum()
print(result) # 출력값 420

"""
34. 데이터 합치기(concat)
주어진 두 csv 파일(school_data.csv와 school_data_science.csv)을 학생 순서를 기준으로 병합하시오.
(단, 두 파일의 학생 순서는 동일하다)
학생별로 수학, 영어, 국어, 과학 점수의 평균을 구하시오.
평균 점수가 60점 이상인 인원 수를 계산하시오.
"""
print("\n Q34")
import pandas as pd
exam34 = pd.read_csv('bigdata2/part1/ch3/school_data.csv')
exam34_sci = pd.read_csv('bigdata2/part1/ch3/school_data_science.csv')

# 두 데이터프레임 합치기(axis=1)
exam34 = pd.concat([exam34, exam34_sci], axis=1)
# print(exam34)

# 수평(열)으로 평균 계산
exam34['수영국과 평균'] = exam34[['수학', '영어', '국어', '과학']].mean(axis=1)

# 수학, 영어, 국어, 과학 평균이 60점 이상
result = sum(exam34['수영국과 평균'] >= 60)
print(result) # 출력값 9

"""
35. 데이터 합치기(merge)
school_data.csv와 school_data_social.csv 파일을 '이름'을 기준으로 합치시오.
영어교사가 장선생이면서 사회교사가 오선생인 학생들을 필터링하시오.
필터링된 학생들의 수학 점수를 모두 더한 후 정수로 구하시오.
"""
print("\n Q35")
import pandas as pd
exam35 = pd.read_csv('bigdata2/part1/ch3/school_data.csv')
exam35_soc = pd.read_csv('bigdata2/part1/ch3/school_data_social.csv')

# 이름을 기준으로 두 데이터프레임 합치기
merge = pd.merge(exam35, exam35_soc, on='이름')

# 교사 필터링
cond1 = merge['영어교사'] == '장선생'
cond2 = merge['사회교사'] == '오선생'

# 필터링된 데이터에서 수학 점수 합
result = merge[cond1 & cond2]['수학'].sum()
print(result) # 출력값 602

"""
36. 조건별 변환
결측된 판매금액은 해당 지역의 평균 판매금액으로 결측값을 대체하시오.
각 거래마다 "판매금액"과 해당 지역의 평균 판매금액의 "차이"를 절대값으로 구하시오.
각 지역에서 차이값의 평균을 구한 후, 이 값이 가장 큰 지역의 지역코드를 구하시오.
"""
print("\n Q36")
import pandas as pd
exam36 = pd.read_csv('bigdata2/part1/ch3/sales.csv')

# 지역별 평균 판매금액 계산 후, 결측값 대체
m = exam36.groupby('지역코드')['판매금액'].transform('mean')
exam36['판매금액'] = exam36['판매금액'].fillna(m)

# 각 거래별 해당 지역의 평균 판매금액 구하기
exam36['지역평균'] = exam36.groupby('지역코드')['판매금액'].transform('mean')

# 판매금액과 지역평균의 차이(절대값) 계산하여 새로운 컬럼 생성
exam36['차이'] = abs(exam36['판매금액'] - exam36['지역평균'])

# 지역별 차이 평균 계산 후, 최대값을 가지는 지역코드 출력
result = exam36.groupby('지역코드')['차이'].mean().idxmax()
print(result) # 출력값 103

"""
37. 재구조화 (unstack), 맵핑
각 행에서 판매수량과 단가를 이용하여 매출액을 계산하시오.
요일을 평일과 주말로 구분하고, 매장별 평일과 주말 매출액 합계를 구하시오.
매장별 평일과 주말 매출액 차이를 절대값으로 구하시오. 이후, 모든 매장 중 가장 큰 절대값 차이를 찾으시오.
"""
print("\n Q37")
import pandas as pd
exam37 = pd.read_csv('bigdata2/part1/ch3/store_sales.csv')

# 매출액 계산
exam37['매출액'] = exam37['판매수량'] * exam37['단가']

# 요일별 평일/주말 구분 딕셔너리
day_mapping = {'월' : '평일', '화' : '평일', '수' : '평일', '목' : '평일', '금' : '평일', '토' : '주말', '일' : '주말'}

# 매핑을 활용하여 새로운 열 추가
exam37['구분'] = exam37['요일'].map(day_mapping)

# 매장코드 & 평일/주말별 매출액 합계
store_sales = exam37.groupby(['매장코드', '구분'])['매출액'].sum().unstack()

# 평일과 주말 매출액 차이 계산
store_sales['차이'] = abs(store_sales['평일'] - store_sales['주말'])

# 전체 매장 중 매출액 차이가 가장 큰 매장의 차이 값 찾기
store_sales['차이'].max()
print(store_sales['차이'].max()) # 출력값 241975

"""
38. 피벗테이블
각 Region과 Channel 조합별로 제품(Product) A, B의 총 판매액을 계산하시오.
제품 A의 매출 비율(A비율)을 구하시오. A비율 = (제품 A 판매액) / (제품 A 판매액 + 제품 B 판매액)
A비율 중 최댓값을 찾아 반올림하여 소수 둘째 자리까지 구하시오.
"""
print("\n Q38")
import pandas as pd
exam38 = pd.read_csv('bigdata2/part1/ch3/region_sales.csv')

# 피벗 테이블 생성: Region, Channel별로 Product별 Sales 합계 계산
pivot = pd.pivot_table(exam38, index=['Region', 'Channel'], columns='Product', 
                                values='Sales', aggfunc='sum')

# A 비율 계산: 제품 A의 판매액 / 총매출
pivot['총매출'] = pivot['A'] + pivot['B']
pivot['A비율'] = pivot['A'] / pivot['총매출']

# 최대 A비율 값 출력
result = pivot['A비율'].max()
print(round(result,2)) # 출력값 0.51

"""
39. 재구조화(melt), 그룹핑
지역(Region)과 월(Jan, Feb, Mar)별 매출(Sales) 합계를 구하시오.
위에서 구한 결과 중, 매출 합계(Sales)가 1400을 초과하는 경우가 몇 건인지 구하시오.
"""
print("\n Q39")
import pandas as pd
exam39 = pd.read_csv('bigdata2/part1/ch3/monthly_sales.csv')

# melt로 Wide(가로) -> Long(세로) 변환
melted_exam39 = pd.melt(
    exam39,
    id_vars='Region',
    value_vars=['Jan','Feb','Mar'],
    var_name='Month',
    value_name='Sales'
) 

# Region, Month별 매출 합계 구하기
group = melted_exam39.groupby(['Region', 'Month'])['Sales'].sum().reset_index()

# 매출 합계가 1400을 초과하는 건수
cond = group['Sales'] > 1400
result = len(group[cond])
print(result) # 출력값 6