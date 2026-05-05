# part2_practice.py

"""
1. Cars93 데이터셋의 Wheelbase 컬럼에 대해서 평균 값에서 표준편차의 1.5배, 2배, 2.5배를 더하거나 뺀 값들의 구간 내의 데이터들의 
평균을 각각 구한 후 원래의 데이터 평균에서 뺏을 때 차이들의 합을 출력하여라.
(단, 소수점 다섯째 자리에서 반올림하여 표현할 것)
"""

import pandas as pd
exam1 = pd.read_csv('data/연습문제/Cars93.csv')
# print(exam1)

print("연습 문제1.")
# Wheelbase
Wheelbase = exam1['Wheelbase']

# Wheelbase 평균
Wheelbase_avg = Wheelbase.mean()

# Wheelbase 표준편차
Wheelbase_std = Wheelbase.std()

# Case1. 평균 값에서 표준편차를 1.5배를 더하거나 빼는 경우, 구간의 하한(Low_1)과 상한(Upp_1) 계산
Low_1 = Wheelbase_avg - 1.5 * Wheelbase_std
Upp_1 = Wheelbase_avg + 1.5 * Wheelbase_std

# 구간 내 데이터들의 평균
Avg_1 = Wheelbase[(Wheelbase > Low_1) & (Wheelbase < Upp_1)].mean()

# 원래의 데이터 평균에서 뺌
Case1 = Wheelbase_avg - Avg_1

# Case2. 평균 값에서 표준편차를 2배를 더하거나 빼는 경우
# 구간의 하한(Low_2)과 상한(Upp_2) 계산
Low_2 = Wheelbase_avg - 2 * Wheelbase_std
Upp_2 = Wheelbase_avg + 2 * Wheelbase_std

# 구간 내 데이터들의 평균
Avg_2 = Wheelbase[(Wheelbase > Low_2) & (Wheelbase < Upp_2)].mean()

# 원래의 데이터 평균에서 뺌
Case2 = Wheelbase_avg - Avg_2

# Case3. 평균 값에서 표준편차를 2.5배를 더하거나 빼는 경우
# 구간의 하한(Low_3)과 상한(Upp_2) 계산
Low_3 = Wheelbase_avg - 2.5 * Wheelbase_std
Upp_3 = Wheelbase_avg + 2.5 * Wheelbase_std

# 구간 내 데이터들의 평균
Avg_3 = Wheelbase[(Wheelbase > Low_3) * (Wheelbase < Upp_3)].mean()

# 원래의 데이터 평균에서 뺌
Case3 = Wheelbase_avg - Avg_3

# 결과를 result에 할당
result1 = round(Case1 + Case2 + Case3, 4)

# 결과 출력
print(result1)

print("연습 문제2.")
"""
2. Cars93 데이터셋의 Length 컬럼에 대해서 순위를 부여한 후, 1위부터 30위까지 값들의 표준편차를 구하고, 소수점 셋째까지 반올림하여
나타내어라.
(단, 동점은 동일한 순위를 부여하되 평균내어 등수를 산정하며 최솟값을 1위로 함)
"""
exam2 = pd.read_csv('data/연습문제/Cars93.csv')

# Length의 순위
rank = exam2['Length'].rank(method = 'average')

# 1위 ~ 30위까지만 추출
sub = exam2['Length'][rank <= 30]

# sub 의 표준편차
sub_std = sub.std()

# 결과를 result에 할당
result2 = round(sub_std, 3)

# 결과 출력
print(result2)

"""
3. Cars93 데이터셋의 Max_Price 컬럼과 Min_Price 컬럼에 대해서 각각 정렬한 후 정렬된 순서에 따라 레코드별로 Max_Price와 Min_Price의
차이를 산출하고 차이값에 대해 표준편차를 구하여라.
(단, Max_Price의 정렬은 내림차순, Min_Price의 정렬은 오름차순으로 하며, 출력시 표준편차는 소수점 넷째 자리에서 반올림하여 표현할 것.)
"""
print("\n 연습문제 3.")
exam3 = pd.read_csv('data/연습문제/Cars93.csv')

# 내림차순으로 정렬해 MaxPrice_sort에 할당
MaxPrice_sort = exam3['Max_Price'].sort_values(ascending = False, ignore_index = True)

# 오름차순으로 정렬해 MinPrice_sort에 할당
MinPrice_sort = exam3['Min_Price'].sort_values(ascending = True, ignore_index = True)

# 차이 계산
# 메소드 .sort_values()에 ignore_index = True을 하지 않을 경우
# 정렬과 무관하게 정렬 전의 인덱스가 같은 값들끼리 차이를 계산하게 됨
diff = MaxPrice_sort - MinPrice_sort

# 차이에 대한 표준 편차
diff_std = diff.std()

# 결과를 result에 할당
result3 = round(diff_std, 3)

# 결과를 출력
print(result3)

"""
4. Cars93 데이터셋의 Weight 컬럼을 Min-Max 정규화로 변환한 후, 0.5보다 작은 값들의 분산과 0.5보다 큰 값들의 분산의 차이를 구하여라.
(단, 차이는 큰 값에서 작은 값을 빼서 구하며, 소수점 넷째 자리에서 반올림하여 표현할 것)
"""
print("\n 연습문제 4.")
exam4 = pd.read_csv('data/연습문제/Cars93.csv')

# Weight 컬럼 Min_Max 정규화로 변환
Weight = exam4['Weight']
Weight_std = (Weight - min(Weight)) / (max(Weight) - min(Weight))

# 0.5보다 작은 Weight들의 분산
var_under = Weight_std[Weight_std < 0.5].var()

# 0.5보다 큰 Weight들의 분산
var_over = Weight_std[Weight_std > 0.5].var()

# 차이 계산
diff = abs(var_over - var_under)

# 결과를 result에 할당
result4 = round(diff, 3)

# 결과를 출력
print(result4)