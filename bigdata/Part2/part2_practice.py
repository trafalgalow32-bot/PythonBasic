# part2_practice.py

"""
1. Cars93 데이터셋의 Wheelbase 컬럼에 대해서 평균 값에서 표준편차의 1.5배, 2배, 2.5배를 더하거나 뺀 값들의 구간 내의 데이터들의 
평균을 각각 구한 후 원래의 데이터 평균에서 뺏을 때 차이들의 합을 출력하여라.
(단, 소수점 다섯째 자리에서 반올림하여 표현할 것)
"""

# 필요 값 : Wheelbase 컬럼 데이터프레임, 평균(Wheelbase 컬럼), 
# 표준편차(Wheelbase 컬럼), 조건들(1.5배, 2배, 2.5배 +-)

import pandas as pd
exam1 = pd.read_csv('data/연습문제/Cars93.csv')
# print(exam1)
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
case3 = wb_mean - wb[(wb > lower3) & (wb < upper3)].mean()


# 결과 할당
result1 = round(case1 + case2 + case3, 4)

# 결과 출력
print(result1) # 정답 0.4845

print("\n 연습 문제2.")
"""
2. Cars93 데이터셋의 Length 컬럼에 대해서 순위를 부여한 후, 1위부터 30위까지 
값들의 표준편차를 구하고, 소수점 셋째까지 반올림하여 나타내어라.
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

# 결과 할당
result2 = round(top30_std, 3)

# 결과 출력 : 정답 8.884
print(result2)

"""
3. Cars93 데이터셋의 Max_Price 컬럼과 Min_Price 컬럼에 대해서 각각 정렬한 후
정렬된 순서에 따라 레코드별로 Max_Price와 Min_Price의 차이를 산출하고 
차이값에 대해 표준편차를 구하여라.
(단, Max_Price의 정렬은 내림차순, Min_Price의 정렬은 오름차순으로 하며, 
출력시 표준편차는 소수점 넷째 자리에서 반올림하여 표현할 것.)
"""
print("\n 연습문제 3.")
exam3 = pd.read_csv('data/연습문제/Cars93.csv')


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
# MinMax 정규화 공식: (변량 - 최소값) / (최대값 - 최소값)
wt = exam4['Weight']
mms = (wt - wt.min()) / (wt.max() - wt.min())

# Min_max 정규화 값이 0.5보다 작은 weight들의 분산
cond1 = mms[mms < 0.5].var()

# Min_max 정규화 값이 0.5보다 큰 weight들의 분산
cond2 = mms[mms > 0.5].var()

# 차이 계산
diff = abs(cond1 - cond2)

# 결과 할당
result4 = round(diff, 3)

# 결과 출력
print(result4) # 정답 : 0.001

"""
5. Cars93 데이터셋을 이용하여 Manufacturer, Origin 컬럼의 유일값 조합의 수와 
Manufacturer 컬럼의 앞 두글자만 추출한 결과와 Origin 컬럼과의
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
comb1 = exam5[['Manufacturer', 'Origin']].drop_duplicates()
cntcomb1 = comb1.shape[0] # 32개의 조합 도출

# Manufacturer 컬럼 앞 두 글자만 추출한 결과와 Origin과 유일값 조합의 수
# Manufacturer 컬럼 앞 두 글자 추출
# 기존 csv 파일에 없는 'sub_str'이라는 새 컬럼명을 만들어서 데이터 조회! 앞 두 글자만 따서!
exam5['sub_str'] = exam5['Manufacturer'].str[:2]

# 유일값 조합의 수
comb2 = exam5[['sub_str', 'Origin']].drop_duplicates()
cntcomb2 = comb2.shape[0] # 28개의 조합 도출

# 결과 할당
result5 = cntcomb1 - cntcomb2

# 결과 출력
print(result5) # 정답 4

"""
6.Cars93 데이터셋을 이용하여 컬럼 Type, Man_trans_avail에 대한 그룹별 RPM 레코드 
수와 RPM 합계, 중앙값을 모두 구한 후, 그룹별 중앙값에서 그룹별 합계에서 
레코드 수를 나눈 값들을 빼서 나온 결과의 총 원소 합을 구하여라. 
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
print(result6) # 정답 442.0

"""
7. Cars93 데이터셋을 이용하여 RPM 컬럼의 결측치를 평균으로 대체하고 RPM과 Wheelbase 컬럼을 
각각 z-점수 표준화한 후 표준화된 Wheelbase에 상수 -36을 곱한 값과 표준화된 RPM 컬럼의 차이값을 
구하고 표준편차를 산출하여라. 
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
print(result7) # 정답 35.561

"""
8. Cars93 데이터셋을 이용하여 먼저, Price 컬럼의 결측치를 평균으로 대체하고 Max_Price 변수와 
Min_Price의 평균보다 작은 레코드만을 추출해 산출된 Origin 그룹별 Price의 합계를 구하고 다음으로 
Price 컬럼의 결측치를 중앙값으로 대체하고 Price 컬럼이 Min_Price 컬럼의 제 3사분위수보다 
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
pavg = df1['Price'].mean() # Price 컬럼의 결측치를 제외한 평균
df1['Price'] = df1['Price'].fillna(pavg)

# Price가 Max_Price와 Min_Price의 평균보다 작은 데이터프레임을 추출
# Max_Price와 Min_Price의 컬럼별 평균
mavg = df1[['Max_Price', 'Min_Price']].mean(axis = 1)

# Price가 위의 평균보다 작은 프레임
subdf1 = df1[df1['Price'] < mavg]

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
# import numpy as np # numpy 안 쓰는 방향으로!
# result8 = int(np.floor(maxval)) # int(maxval)만 해도 됨!
result8 = int(maxval)

# 출력
print(result8) # 정답 856

"""
9. Cars93 데이터셋에서 'Price' 컬럼은 'Min_Price'와 'Max_Price'의 평균으로 알려져 있다. 
이와 같은 사실을 통해 'Price' 컬럼의 결측치의 원래의 값을 계산한 후, 
'Price'가 14.7보다 작거나 25.3보다 크면서 'Large' 타입인 레코드 수를 계산하여라. 
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
isna = price.isna()

# 'Price'가 결측치인 경우만 'Min_Price'와 'Max_Price'의 평균을 할당
price[isna] = (maxp[isna] + minp[isna]) / 2

# 'Price'가 14.7보다 작거나 25.3보다 크면서 'Large' 타입인 레코드 수
# 조건1
cond1 = price < 14.7

# 조건2
cond2 = (price > 25.3) & (type =='Large')

# 해당 조건
cond = cond1 | cond2

# 결과 할당
# .shape(행&레코드개수;0, 열&변수의 개수;1) 그래서! 
result9 = exam9[cond].shape[0] 

# 출력
print(result9) # 정답 35

"""
10. Cars93 데이터셋에서 'Make' 컬럼을 이용하여 제조사가 'Chevrolet', 'Pontiac', 'Hyundai'이면서 
'AirBags'이 'Driver'에만 있는 경우의 레코드 수를 계산하여라.
"""
print("\n 연습문제 10.")
import pandas as pd
exam10 = pd.read_csv('data/연습문제/Cars93.csv')

# 컬럼들 시리즈로 별도 저장
make = exam10['Make'].copy()
airbag = exam10['AirBags'].copy()
"""
공백을 애초에 원천 봉쇄! 이것도 고려해보셈!
make = exam10['Make'].str.strip()
airbag = exam10['AirBags'].str.strip()
"""


# 제조사가 'Chevrolet', 'Pontiac', 'Hyundai'인 경우
# (위치 인덱스 기준) 12, 16, 72, 74번 문자열 앞에 공백이 포함되어 있음
# 확인 코드
# print(make[make.str[0] == ' '])

make = make.str.strip()

### 조건
# 튜플로 입력 시 여러 문자열로 시작하는 경우에 대한 Bool 결과를 찾을 수 있음
# 문자열이 'Chevrolet' 또는 'Pontiac' 또는 'Hyundai'로 시작하면 True를 반환함
cond1 = make.str.startswith(('Chevrolet', 'Pontiac', 'Hyundai'))

# 'AirBags'이 'Driver'에만 있는 경우
cond2 = (airbag == 'Driver only')

# 결과 할당
result10 = sum(cond1 & cond2)

# 출력
print(result10) # 정답 3

"""
11. Rabbit  데이터셋을 불러와 Dose 컬럼의 제 3사분위수와 제 2사분위수를 구하고 두 값의 차이의 
절댓값을 구한 후 소수점을 버린 값을 출력하여라.
"""
print("\n 연습문제 11.")
import pandas as pd
exam11 = pd.read_csv('data/연습문제/Rabbit.csv')

# 제 3 사분위수, 제 2사분위수 별도 저장
q3 = exam11['Dose'].quantile(.75)
q2 = exam11['Dose'].median() # quantile(.5)도 됨!

# 두 값 차이의 절댓값
diff = abs(q3 - q2)

# 결과
result11 = diff.astype('int64') # int(diff) 도 됨!

# 출력
print(result11) # 정답: 62

"""
12. Boston 데이터셋을 불러와 medv 컬럼에 대해서 동일한 폭으로 binning한 후 가장 많은 빈도를 가지는 
구간을 산출하고 해당 구간 내 dis 컬럼의 중앙값을 구하여라.
(폭은 10을 기준으로 하고 소수점은 둘째 자리까지 나타내시오.)
"""
print("\n 연습문제 12.")
import pandas as pd
exam12 = pd.read_csv('data/연습문제/Boston.csv')

### 왜 0~50 범위로 폭을 10으로 binning을 하는지 알아보기 위해!
# print(exam12['medv'].max())
# print(exam12['medv'].min())

# medv 컬럼에 대해서 동일한 폭으로 binning
medv_cut = pd.cut(exam12['medv'], bins = [0, 10, 20, 30, 40, 50])
# medv_cut = pd.cut(exam12['medv'], bins = 5) 이것도 됨! 이게 더 효율적일지도...

# 가장 많은 빈도를 가지는 구간 산출
mode = medv_cut.value_counts().idxmax()

# 해당 구간 내 dis 컬럼의 중앙값
# 조건
cond = (medv_cut == mode)

#중앙값
med = exam12['dis'][cond].median()

# 결과
result12 = round(med, 2)

# 출력
print(result12) # 정답 3.95

"""
13. Melanoma 데이터셋을 불러와 1번째~122번째 레코드와 123번째 이후 레코드로 데이터셋을 분리하고 
각 데이터셋별로 thickness 컬럼을 z-score 정규화로 변환한 후 -1과 1 사이 값들의 중앙값을 각각 산출한
후 합계를 구하여라. 
(단, z-score 정규화 변환 계산에 사용되는 평균과 표준편차는 분리된 것과 관계없이 1번째~123번째 레코드로 
이루어진 데이터셋을 기준으로 하고 출력 시 소수점 넷째 자리까지 반올림하여 나타낼 것, 레코드 번호는 
가장 위에 위치한 레코드를 1번으로 가정함)
"""
print("\n 연습문제 13.")
import pandas as pd
exam13 = pd.read_csv('data/연습문제/Melanoma.csv')

# 1번째~123번째 레코드와 123번째 이후 레코드로 데이터셋을 분리
df1 = exam13.iloc[:123]
df2 = exam13.iloc[123:]

# thickness 컬럼을 z-score 정규화로 변환
# 1번째~123번째 레코드로 이루어진 데이터셋의 thickness 평균
avg = df1['thickness'].mean()

# 1번째~123번째 레코드로 이루어진 데이터셋의 thickness 표준편차
std = df1['thickness'].std()

# z-score 변환 (※ z-score 정규화 공식 암기할 것!)
zstd1 = (df1['thickness'] - avg)/std
zstd2 = (df2['thickness'] - avg)/std

# -1과 1 사이 값들의 중앙값을 각각 산출
# -1과 1사이 값
cond1 = zstd1[(zstd1 >= -1) & (zstd1 <= 1)]
cond2 = zstd2[(zstd2 >= -1) & (zstd2 <= 1)]

# 중앙값
med1 = cond1.median()
med2 = cond2.median()

# 결과 
result13 = round(med1 + med2, 4)

# 출력
print(result13) # 정답 -1.0027
