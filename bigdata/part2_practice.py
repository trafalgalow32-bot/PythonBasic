# part2_practice.py

"""
1. Cars93 데이터셋의 Wheelbase 컬럼에 대해서 평균 값에서 표준편차의 1.5배, 2배, 2.5배를 더하거나 뺀 값들의 구간 내의 데이터들의 
평균을 각각 구한 후 원래의 데이터 평균에서 뺏을 때 차이들의 합을 출력하여라.
(단, 소수점 다섯째 자리에서 반올림하여 표현할 것)
"""

import pandas as pd
exam1 = pd.read_csv('data/연습문제/Cars93.csv')
# print(exam1)
# 필요 값 : Wheelbase 컬럼 데이터프레임, 평균(Wheelbase 컬럼), 
# 표준편차(Wheelbase 컬럼), 조건들(1.5배, 2배, 2.5 +-)
print("연습 문제1.")

# Wheelbase
wb = exam1['Wheelbase']

# Wheelbase 평균
wb_mean = wb.mean()

# Wheelbase 표준편차
wb_std = wb.std()

# Case1. 평균 값에서 표준편차의 1.5배를 더하거나 빼는 경우
# 구간의 하한(lower1)과 상한(upper1) 계산
lower1 = wb_mean - 1.5 * wb_std
upper1 = wb_mean + 1.5 * wb_std

# 원 데이터 평균 - 구간 내 데이터들의 평균
case1 = wb_mean - wb[(wb > lower1) & (wb < upper1)].mean()


# Case2. 평균 값에서 표준편차의 2배를 더하거나 빼는 경우
# 구간의 하한(lower2)과 상한(upper2) 계산
lower2 = wb_mean - 2 * wb_std
upper2 = wb_mean + 2 * wb_std

# 원 데이터 평균 - 구간 내 데이터들의 평균
case2 = wb_mean - wb[(wb > lower2) & (wb < upper2)].mean()

# Case3. 평균 값에서 표준편차의 2.5배를 더하거나 빼는 경우
# 구간의 하한(lower3)과 상한(upper3) 계산
lower3 = wb_mean - 2.5 * wb_std
upper3 = wb_mean + 2.5 * wb_std

# 원 데이터 평균 - 구간 내 데이터들의 평균
case3 = wb_mean - wb[(wb > lower3) * (wb < upper3)].mean()


# 결과를 result에 할당
result1 = round(case1 + case2 + case3, 4)

# 결과 출력 : 정답 0.4845
print(result1)

print("\n 연습 문제2.")
"""
2. Cars93 데이터셋의 Length 컬럼에 대해서 순위를 부여한 후, 1위부터 30위까지 값들의 표준편차를 구하고, 소수점 셋째까지 반올림하여
나타내어라.
(단, 동점은 동일한 순위를 부여하되 평균내어 등수를 산정하며 최솟값을 1위로 함)
"""
# 필요 데이터 : 데이터프레임(Length 컬럼), Length 순위, 
# 순위(1~30) 값들의 표준편차
exam2 = pd.read_csv('data/연습문제/Cars93.csv')

# Length의 순위
rank = exam2['Length'].rank(method = 'average')

# 1위 ~ 30위까지만 추출
top30 = exam2['Length'][rank <= 30]

# sub 의 표준편차
top30_std = top30.std()

# 결과를 result에 할당
result2 = round(top30_std, 3)

# 결과 출력 : 정답 8.884
print(result2)

"""
3. Cars93 데이터셋의 Max_Price 컬럼과 Min_Price 컬럼에 대해서 각각 정렬한 후 정렬된 순서에 따라 레코드별로 Max_Price와 Min_Price의
차이를 산출하고 차이값에 대해 표준편차를 구하여라.
(단, Max_Price의 정렬은 내림차순, Min_Price의 정렬은 오름차순으로 하며, 출력시 표준편차는 소수점 넷째 자리에서 반올림하여 표현할 것.)
"""
print("\n 연습문제 3.")
exam3 = pd.read_csv('data/연습문제/Cars93.csv')
# 필요 데이터 : Max_Price 컬럼, Min_Price 컬럼, 차이(Max - Min)
# , 차이값에 대한 표준 편차

# 내림차순으로 정렬해 maxp에 할당
maxp = exam3['Max_Price'].sort_values(ascending = False, ignore_index = True)

# 오름차순으로 정렬해 minp에 할당
minp = exam3['Min_Price'].sort_values(ascending = True, ignore_index = True)

# 차이 계산
# 메소드 .sort_values()에 ignore_index = True을 하지 않을 경우
# 정렬과 무관하게 정렬 전의 인덱스가 같은 값들끼리 차이를 계산하게 됨
# Pandas는 무조건 인덱스가 같은 것끼리 짝을 지어 연산하는 특징이 있음.
# 따라서 기껏 데이터를 정렬/분류 했는데, 바뀌지 않은 인덱스로 인한 계산 오류를 방지하는 것! 
diff = maxp - minp

# 차이에 대한 표준 편차
diff_std = diff.std()

# 결과를 result에 할당
result3 = round(diff_std, 3)

# 결과를 출력 : 18.584
print(result3)

"""
4. Cars93 데이터셋의 Weight 컬럼을 Min-Max 정규화로 변환한 후, 0.5보다 작은 값들의 분산과 0.5보다 큰 값들의 분산의 차이를 구하여라.
(단, 차이는 큰 값에서 작은 값을 빼서 구하며, 소수점 넷째 자리에서 반올림하여 표현할 것)
"""
# 필요데이터 : 데이터프레임(Weight 컬럼), min-max 정규화한 값, 
# 분산(0.5보다 작은, 0.5보다 큰) 차이
print("\n 연습문제 4.")
exam4 = pd.read_csv('data/연습문제/Cars93.csv')

# Weight 컬럼 Min_Max 정규화로 변환 ( ※ mms: MinMaxScaling의 약어)
weight = exam4['Weight']
weight_mms = (weight - min(weight)) / (max(weight) - min(weight))

# 0.5보다 작은 weight들의 분산
var_under = weight_mms[weight_mms < 0.5].var()

# 0.5보다 큰 weight들의 분산
var_over = weight_mms[weight_mms > 0.5].var()

# 차이 계산
diff = abs(var_over - var_under)

# 결과를 result에 할당
result4 = round(diff, 3)

# 결과를 출력
print(result4) # 정답 : 0.001

"""
5. Cars93 데이터셋을 이용하여 Manufacturer, Origin 컬럼의 유일값 조합의 수와 Manufacturer 컬럼의 앞 두글자만 추출한 결과와 Origin 컬럼과의
유일값 조합 수의 차이를 구하여라.
(단, 원래 유일값 조합 수에서 추출 이후 수를 뺄 것)
"""
print("\n 연습문제 5.")
import pandas as pd
exam5 = pd.read_csv('data/연습문제/Cars93.csv')

# 원래 유일값 조합의 수
# .unique() : 시리즈의 유일값을 추출하는 메소드
# .nunique() : 데이터프레임의 각 컬럼별 유일값 수를 계산하는 메소드
# .drop_duplicates(): 데이터프레임의 여러 컬럼들의 조합에 대한 유일값을 추출하는 메소드
uniq_raw = exam5[['Manufacturer', 'Origin']].drop_duplicates()
num_uniq_raw = uniq_raw.shape[0]

# Manufacturer 컬럼 앞 두 글자만 추출한 결과와 Origin과 유일값 조합의 수
# Manufacturer 컬럼 앞 두 글자 추출
exam5['sub_str'] = exam5['Manufacturer'].str[:2]

# 유일값 조합의 수
uniq_new = exam5[['sub_str', 'Origin']].drop_duplicates()
num_uniq_new = uniq_new.shape[0]

# 결과를 result에 할당
result5 = num_uniq_raw - num_uniq_new

# 출력
print(result5)

"""
6.Cars93 데이터셋을 이용하여 컬럼 Type, Man_trans_avail에 대한 그룹별 RPM 레코드 수와 RPM 합계, 중앙값을 모두 구한 후, 그룹별 중앙값에서 
그룹별 합계에서 레코드 수를 나눈 값들을 빼서 나온 결과의 총 원소 합을 구하여라. 
(단, 출력시 소수점은 첫째 자리에서 반올림하여 표현할 것)
"""
print("\n 연습문제 6.")
import pandas as pd
exam6 = pd.read_csv('data/연습문제/Cars93.csv')

# 그룹별 RPM 레코드 수
rpmcnt = exam6.groupby(['Type', 'Man_trans_avail'])['RPM'].count()

# 그룹별 RPM 합계
rpmsum = exam6.groupby(['Type', 'Man_trans_avail'])['RPM'].sum()

# 그룹별 RPM 중앙값
rpmmid = exam6.groupby(['Type', 'Man_trans_avail'])['RPM'].median()

# 그룹별 중앙값 - (그룹별 합계/레코드 수)을 계산한 후 모든 원소 합
calcul = sum(rpmmid - rpmsum / rpmcnt)

# 결과
result6 = round(calcul, 0)

# 출력
print(result6)

"""
7. Cars93 데이터셋을 이용하여 RPM 컬럼의 결측치를 평균으로 대체하고 RPM과 Wheelbase 컬럼을 각각 z-점수 표준화한 후 표준화된 Wheelbase에 상수 -36
을 곱한 값과 표준화된 RPM 컬럼의 차이값을 구하고 표준편차를 산출하여라. 
(단, 소수점 셋째 자리까지 반올림하여 표현할 것)
"""
print("\n 연습문제 7.")
import pandas as pd
exam7 = pd.read_csv('data/연습문제/Cars93.csv')

# RPM 컬럼 결측치 평균 대체
rpmavg = exam7['RPM'].mean() # RPM 컬럼의 결측치를 제외한 평균
exam7['RPM'] = exam7['RPM'].fillna(rpmavg)

# RPM 컬럼 z-점수 표준화
rpmz = (exam7['RPM'] - exam7['RPM'].mean()) / exam7['RPM'].std()

# Wheelbase 컬럼 z-점수 표준화
wbz = (exam7['Wheelbase'] - exam7['Wheelbase'].mean()) / exam7['Wheelbase'].std()

# 표준화된 Wheelbase에 상수 -36을 곱한 값과 표준화된 RPM 변수의 차이값
diff = wbz * (-36) - rpmz

# 차이값의 표준 편차
diff_std = diff.std()

# 결과 할당
result7 = round(diff_std, 3)

# 출력
print(result7)

"""
8. Cars93 데이터셋을 이용하여 먼저, Price 컬럼의 결측치를 평균으로 대체하고 Max_Price 변수와 Min_Price의 평균보다 작은 레코드만을 추출해 산출된
Origin 그룹별 Price의 합계를 구하고 다음으로 Price 컬럼의 결측치를 중앙값으로 대체하고 Price 컬럼이 Min_Price 컬럼의 제 3사분위수보다 
작은 레코드만을 추출해 산출된 Origin별 Price의 합계를 Origin 그룹별로 합한 후 큰 값을 출력하여라. 
(단, 소수점 이하는 모두 절삭하여 정수로 표현할 것)
"""
print("\n 연습문제 8.")
import pandas as pd
exam8 = pd.read_csv('data/연습문제/Cars93.csv')

# 결측치 대체를 같은 컬럼에 두 번 해야 하는 문제이므로 이에 데이터프레임을 따로 복사함
df1 = exam8.copy()
df2 = exam8.copy()

# Case1. Price 컬럼의 결측치를 평균으로 대체
priceavg = df1['Price'].mean() # Price 컬럼의 결측치를 제외한 평균
df1['Price'] = df1['Price'].fillna(priceavg)

# Price가 Max_Price와 Min_Price의 평균보다 작은 데이터프레임을 추출
# Max_Price와 Min_Price의 컬럼별 평균
minmaxavg = df1[['Max_Price', 'Min_Price']].mean(axis = 1)

# Price가 위의 평균보다 작은 프레임
subdf1 = df1[df1['Price'] < minmaxavg]

# Origin 그룹별 Price의 합계
sum1 = subdf1.groupby('Origin')['Price'].sum()

# Case2. Price 변수의 결측치를 중앙값으로 대체
med = df2['Price'].median() # Price 컬럼의 결측치를 중앙값으로 대체
df2['Price'] = df2['Price'].fillna(med)

# Price가 위의 제 3사분위수보다 작은 데이터프레임을 추출
# Min_Price의 제 3사분위수
q3 = exam8['Min_Price'].quantile(.75)

# Price가 위의 제 3사분위수보다 작은 데이터프레임
subdf2 = df2[df2['Price'] < q3]

# Origin 그룹별 Price의 합계
sum2 = subdf2.groupby('Origin')['Price'].sum()

# 두 결과를 합한 후 가장 큰 원소
maxval = max(sum1 + sum2)

# 결과
import numpy as np
result8 = int(np.floor(maxval)) # int(maxval)만 해도 됨!

# 출력
print(result8)

"""
9. Cars93 데이터셋에서 'Price' 컬럼은 'Min_Price'와 'Max_Price'의 평균으로 알려져 있다. 이와 같은 사실을 통해 'Price' 컬럼의 결측치의 원래의 값을
계산한 후, 'Price'가 14.7보다 작거나 25.3보다 크면서 'Large' 타입인 레코드 수를 계산하여라. 
"""
print("\n 연습문제 9.")
import pandas as pd
exam9 = pd.read_csv('data/연습문제/Cars93.csv')

# 'Price' 컬럼의 결측치의 원래의 값을 계산
# 컬럼들 시리즈로 별도 저장
price = exam9['Price'].copy()
maxp = exam9['Max_Price'].copy()
minp = exam9['Min_Price'].copy()
type = exam9['Type'].copy()

# 'Price' 컬럼이 결측인 조건
condna = price.isna()

# 'Price'가 결측치인 경우만 'Min_Price'와 'Max_Price'의 평균을 할당
price[condna] = (maxp[condna] + minp[condna]) / 2

# 'Price'가 14.7보다 작거나 25.3보다 크면서 'Large' 타입인 레코드 수
# 조건1
cond1 = price < 14.7

# 조건2
cond2 = (price > 25.3) & (type =='Large')

# 해당 조건
cond = cond1 | cond2

# 결과 할당
result9 = exam9[cond].shape[0]

# 출력
print(result9) # 정답 35

"""
10. Cars93 데이터셋에서 'Make' 컬럼을 이용하여 제조사가 'Chevrolet', 'Pontiac', 'Hyundai'이면서 'AirBags'이 'Driver'에만 있는 경우의 
레코드 수를 계산하여라.
"""
print("\n 연습문제 10.")
import pandas as pd
exam10 = pd.read_csv('data/연습문제/Cars93.csv')

# 컬럼들 시리즈로 별도 저장
make = exam10['Make'].copy()
airbag = exam10['AirBags'].copy()

# 제조사가 'Chevrolet', 'Pontiac', 'Hyundai'인 경우
# (위치 인덱스 기준) 12, 16, 72, 74번 문자열 앞에 공백이 포함되어 있음
# 확인 코드
# print(make[make.str[0] == ''])

make = make.str.strip()

### 조건
# 튜플로 입력 시 여러 문자열로 시작하는 경우에 대한 Bool 결가를 찾을 수 있음
# 문자열이 'Chevrolet' 또는 'Pontiac' 또는 'Hyundai'로 시작하면 True를 반환함
cond1 = make.str.startswith(('Chevrolet', 'Pontiac', 'Hyundai'))

# 'AirBags'이 'Driver'에만 있는 경우
cond2 = (airbag == 'Driver only')

# 결과 할당
result10 = sum(cond1 & cond2)

# 출력
print(result10) # 정답 3

