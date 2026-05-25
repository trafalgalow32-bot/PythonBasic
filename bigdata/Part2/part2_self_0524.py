# """
# 1. Cars93 데이터셋의 Wheelbase 컬럼에 대해서 평균 값에서 표준편차의 1.5배, 2배, 2.5배를 더하거나 뺀 값들의 구간 내의 데이터들의 
# 평균을 각각 구한 후 원래의 데이터 평균에서 뺏을 때 차이들의 합을 출력하여라.
# (단, 소수점 다섯째 자리에서 반올림하여 표현할 것)
# """
# import pandas as pd
# exam1 = pd.read_csv('data/연습문제/Cars93.csv')
# wb = exam1['Wheelbase']
# avg = wb.mean()
# std = wb.std()

# lower1 = avg - std * 1.5
# upper1 = avg + std * 1.5
# case1 = avg - wb[(wb > lower1) & (wb < upper1)].mean()

# lower2 = avg - std * 2
# upper2 = avg + std * 2
# case2 = avg - wb[(wb > lower2) & (wb < upper2)].mean()

# lower3 = avg - std * 2.5
# upper3 = avg + std * 2.5
# case3 = avg - wb[(wb > lower3) & (wb < upper3)].mean()

# result1 = case1 + case2 + case3
# result1 = round(result1, 4)
# print(result1)

# """
# 2. Cars93 데이터셋의 Length 컬럼에 대해서 순위를 부여한 후, 1위부터 30위까지 값들의 표준편차를 구하고, 소수점 셋째까지 반올림하여
# 나타내어라.
# (단, 동점은 동일한 순위를 부여하되 평균내어 등수를 산정하며 최솟값을 1위로 함)
# """
# import pandas as pd
# exam2 = pd.read_csv('data/연습문제/Cars93.csv')
# rank = exam2['Length'].rank(method='average')
# rank30 = exam2['Length'][rank <= 30]
# std = rank30.std()
# std = round(std, 3)
# print(std)

# """
# 3. Cars93 데이터셋의 Max_Price 컬럼과 Min_Price 컬럼에 대해서 각각 정렬한 후 정렬된 순서에 따라 레코드별로 Max_Price와 Min_Price의
# 차이를 산출하고 차이값에 대해 표준편차를 구하여라.
# (단, Max_Price의 정렬은 내림차순, Min_Price의 정렬은 오름차순으로 하며, 출력시 표준편차는 소수점 넷째 자리에서 반올림하여 표현할 것.)
# """
# import pandas as pd
# exam3 = pd.read_csv('data/연습문제/Cars93.csv')
# maxp = exam3['Max_Price'].sort_values(ascending=False, ignore_index=True)
# minp = exam3['Min_Price'].sort_values(ascending=True, ignore_index=True)
# # print(maxp)
# # print(minp)
# diff = maxp - minp
# std = diff.std()
# std = round(std,3)
# print(std)

# """
# 4. Cars93 데이터셋의 Weight 컬럼을 Min-Max 정규화로 변환한 후, 0.5보다 작은 값들의 분산과 0.5보다 큰 값들의 분산의 차이를 구하여라.
# (단, 차이는 큰 값에서 작은 값을 빼서 구하며, 소수점 넷째 자리에서 반올림하여 표현할 것)
# """
# import pandas as pd
# exam4 = pd.read_csv('data/연습문제/Cars93.csv')

# mms = (exam4['Weight'] - exam4['Weight'].min()) / (exam4['Weight'].max() - exam4['Weight'].min())
# cond1 = mms < 0.5
# cond2 = mms > 0.5
# var1 = mms[cond1].var()
# var2 = mms[cond2].var()
# # print(var1)
# # print(var2)
# diff = var1 - var2
# diff = round(diff, 3)
# print(diff)

# """
# 5. Cars93 데이터셋을 이용하여 Manufacturer, Origin 컬럼의 유일값 조합의 수와 Manufacturer 컬럼의 앞 두글자만 추출한 결과와 Origin 컬럼과의
# 유일값 조합 수의 차이를 구하여라.
# (단, 원래 유일값 조합 수에서 추출 이후 수를 뺄 것)
# """
# import pandas as pd
# exam5 = pd.read_csv('data/연습문제/Cars93.csv')
# comb1 = exam5[['Manufacturer', 'Origin']].drop_duplicates()
# cntcomb1 = comb1.shape[0]

# exam5['sub_str'] = exam5['Manufacturer'].str[:2]

# comb2 = exam5[['sub_str', 'Origin']].drop_duplicates()
# cntcomb2 = comb2.shape[0]

# result5 = cntcomb1 - cntcomb2
# print(result5)

# """
# 6. Cars93 데이터셋을 이용하여 컬럼 Type, Man_trans_avail에 대한 그룹별 RPM 레코드 수와 RPM 합계, 중앙값을 모두 구한 후, 그룹별 중앙값에서 
# 그룹별 합계에서 레코드 수를 나눈 값들을 빼서 나온 결과의 총 원소 합을 구하여라. 
# (단, 출력시 소수점은 첫째 자리에서 반올림하여 표현할 것)
# """
# import pandas as pd
# exam6 = pd.read_csv('data/연습문제/Cars93.csv')
# # exam6 = exam6['Man_trans_avail']
# # print(exam6)
# rpmcnt = exam6.groupby(['Type', 'Man_trans_avail'])['RPM'].count()
# rpmsum = exam6.groupby(['Type', 'Man_trans_avail'])['RPM'].sum()
# rpmmid = exam6.groupby(['Type', 'Man_trans_avail'])['RPM'].median()

# calcul = (rpmmid - (rpmsum / rpmcnt)).sum()
# calcul = round(calcul, 0)
# print(calcul)
# # print(rpmcnt)

# """
# 7. Cars93 데이터셋을 이용하여 RPM 컬럼의 결측치를 평균으로 대체하고 RPM과 Wheelbase 컬럼을 각각 z-점수 표준화한 후 표준화된 Wheelbase에 상수 -36
# 을 곱한 값과 표준화된 RPM 컬럼의 차이값을 구하고 표준편차를 산출하여라. 
# (단, 소수점 셋째 자리까지 반올림하여 표현할 것)
# """
# import pandas as pd
# exam7 = pd.read_csv('data/연습문제/Cars93.csv')


# exam7['RPM'] = exam7['RPM'].fillna(exam7['RPM'].mean())
# # print(rpm)

# zrpm = (exam7['RPM'] - exam7['RPM'].mean()) / exam7['RPM'].std()
# # print(zrpm)
# zwb = (exam7['Wheelbase'] - exam7['Wheelbase'].mean()) / exam7['Wheelbase'].std()
# diff = (zwb * (-36)) - zrpm
# std = diff.std()
# std = round(std, 3)
# print(std)

"""
8. Cars93 데이터셋을 이용하여 먼저, Price 컬럼의 결측치를 평균으로 대체하고 Max_Price 변수와 Min_Price의 평균보다 작은 레코드만을 추출해 산출된
Origin 그룹별 Price의 합계를 구하고 다음으로 Price 컬럼의 결측치를 중앙값으로 대체하고 Price 컬럼이 Min_Price 컬럼의 제 3사분위수보다 
작은 레코드만을 추출해 산출된 Origin별 Price의 합계를 Origin 그룹별로 합한 후 큰 값을 출력하여라. 
(단, 소수점 이하는 모두 절삭하여 정수로 표현할 것)
"""






"""
9. Cars93 데이터셋에서 'Price' 컬럼은 'Min_Price'와 'Max_Price'의 평균으로 알려져 있다. 이와 같은 사실을 통해 'Price' 컬럼의 결측치의 원래의 값을
계산한 후, 'Price'가 14.7보다 작거나 25.3보다 크면서 'Large' 타입인 레코드 수를 계산하여라. 

10. Cars93 데이터셋에서 'Make' 컬럼을 이용하여 제조사가 'Chevrolet', 'Pontiac', 'Hyundai'이면서 'AirBags'이 'Driver'에만 있는 경우의 
레코드 수를 계산하여라.

11. Rabbit  데이터셋을 불러와 Dose 컬럼의 제 3사분위수와 제 2사분위수를 구하고 두 값의 차이의 절댓값을 구한 후 소수점을 버린 값을 출력하여라.

12. Boston 데이터셋을 불러와 medv 컬럼에 대해서 동일한 폭으로 binning한 후 가장 많은 빈도를 가지는 구간을 산출하고 해당 구간 내 dis
컬럼의 중앙값을 구하여라.13. Melanoma 데이터셋을 불러와 1번째~122번째 레코드와 123번째 이후 레코드로 데이터셋을 분리하고 각 데이터셋별로 thickness 컬럼을 
z-score 정규화로 변환한 후 -1과 1 사이 값들의 중앙값을 각각 산출한 후 합계를 구하여라. 
(단, z-score 정규화 변환 계산에 사용되는 평균과 표준편차는 분리된 것과 관계없이 1번째~123번째 레코드로 이루어진 데이터셋을 기준으로 하고
출력 시 소수점 넷째 자리까지 반올림하여 나타낼 것, 레코드 번호는 가장 위에 위치한 레코드를 1번으로 가정함)
(폭은 10을 기준으로 하고 소수점은 둘째 자리까지 나타내시오.)

"""