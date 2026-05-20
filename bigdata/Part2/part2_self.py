import pandas as pd
# """
# 1. Cars93 데이터셋의 Wheelbase 컬럼에 대해서 평균 값에서 표준편차의 1.5배, 2배, 2.5배를 더하거나 뺀 값들의 구간 내의 데이터들의 
# 평균을 각각 구한 후 원래의 데이터 평균에서 뺏을 때 차이들의 합을 출력하여라.
# (단, 소수점 다섯째 자리에서 반올림하여 표현할 것)
# """

# exam1 = pd.read_csv('data/연습문제/Cars93.csv')

# wb = exam1['Wheelbase']
# wb_mean = wb.mean()
# wb_std = wb.std()

# lower1 = wb_mean - wb_std * 1.5
# upper1 = wb_mean + wb_std * 1.5
# case1 = wb_mean - wb[(wb > lower1)&(wb < upper1)].mean()

# lower2 = wb_mean - wb_std * 2
# upper2 = wb_mean + wb_std * 2
# case2 = wb_mean - wb[(wb > lower2)&(wb < upper2)].mean()

# lower3 = wb_mean - wb_std * 2.5
# upper3 = wb_mean + wb_std * 2.5
# case3 = wb_mean - wb[(wb > lower3)&(wb < upper3)].mean()

# result1 = case1 + case2 + case3
# print(round(result1, 4))

# """
# 2. Cars93 데이터셋의 Length 컬럼에 대해서 순위를 부여한 후, 1위부터 30위까지 
# 값들의 표준편차를 구하고, 소수점 셋째까지 반올림하여 나타내어라.
# (단, 동점은 동일한 순위를 부여하되 평균내어 등수를 산정하며 최솟값을 1위로 함)
# """

# exam2 = pd.read_csv('data/연습문제/Cars93.csv')
# rank = exam2['Length'].rank(method='average')
# # rank30 = exam2.sort_values(ignore_index=True)[rank < 30]
# rank30 = exam2['Length'][rank <= 30]
# std = rank30.std()

# print(round(std, 3))

# """
# 3. Cars93 데이터셋의 Max_Price 컬럼과 Min_Price 컬럼에 대해서 각각 정렬한 후
# 정렬된 순서에 따라 레코드별로 Max_Price와 Min_Price의 차이를 산출하고 
# 차이값에 대해 표준편차를 구하여라.
# (단, Max_Price의 정렬은 내림차순, Min_Price의 정렬은 오름차순으로 하며, 
# 출력시 표준편차는 소수점 넷째 자리에서 반올림하여 표현할 것.)
# """
# exam3 = pd.read_csv('data/연습문제/Cars93.csv')

# maxp = exam3['Max_Price'].sort_values(ascending=False, ignore_index=True)
# minp = exam3['Min_Price'].sort_values(ascending=True, ignore_index=True)
# diff = maxp - minp
# std = diff.std()

# print(round(std, 3))

# """
# 4. Cars93 데이터셋의 Weight 컬럼을 Min-Max 정규화로 변환한 후, 0.5보다 작은 값들의 분산과 0.5보다 큰 값들의 분산의 차이를 구하여라.
# (단, 차이는 큰 값에서 작은 값을 빼서 구하며, 소수점 넷째 자리에서 반올림하여 표현할 것)
# """

# exam4 = pd.read_csv('data/연습문제/Cars93.csv')
# wt = exam4['Weight']
# mms = (wt - wt.min()) / (wt.max() - wt.min())

# small = mms[mms < 0.5].var()
# big = mms[mms > 0.5].var()

# diff = abs(big - small)
# print(round(diff, 3))

# """
# 5. Cars93 데이터셋을 이용하여 Manufacturer, Origin 컬럼의 유일값 조합의 수와 
# Manufacturer 컬럼의 앞 두글자만 추출한 결과와 Origin 컬럼과의
# 유일값 조합 수의 차이를 구하여라.
# (단, 원래 유일값 조합 수에서 추출 이후 수를 뺄 것)
# """

# exam5 = pd.read_csv('data/연습문제/Cars93.csv')
# uniq_raw = exam5[['Manufacturer', 'Origin']].drop_duplicates()
# num_uniq_raw = uniq_raw.shape[0]

# exam5['sub_str'] = exam5['Manufacturer'].str[:2]

# uniq_new = exam5[['sub_str', 'Origin']].drop_duplicates()
# num_uniq_new = uniq_new.shape[0]

# result5 = num_uniq_raw - num_uniq_new

# print(result5)

# """
# 6.Cars93 데이터셋을 이용하여 컬럼 Type, Man_trans_avail에 대한 그룹별 RPM 레코드 
# 수와 RPM 합계, 중앙값을 모두 구한 후, 그룹별 중앙값에서 그룹별 합계에서 
# 레코드 수를 나눈 값들을 빼서 나온 결과의 총 원소 합을 구하여라. 
# (단, 출력시 소수점은 첫째 자리에서 반올림하여 표현할 것)
# """

# exam6 = pd.read_csv('data/연습문제/Cars93.csv')

# rpmcnt = exam6.groupby(['Type', 'Man_trans_avail'])['RPM'].count()

# rpmsum = exam6.groupby(['Type', 'Man_trans_avail'])['RPM'].sum()

# rpmmid = exam6.groupby(['Type', 'Man_trans_avail'])['RPM'].median()

# calcul = sum(rpmmid - rpmsum / rpmcnt)

# result6 = round(calcul, 0)
# print(result6)

# exam7 = pd.read_csv('data/연습문제/Cars93.csv')

# rpmavg = exam7['RPM'].mean()
# exam7['RPM'] = exam7['RPM'].fillna(rpmavg)

# rpmz = (exam7['RPM'] - exam7['RPM'].mean()) / exam7['RPM'].std()

# wbz = (exam7['Wheelbase'] - exam7['Wheelbase'].mean()) / exam7['Wheelbase'].std()

# diff = wbz * (-36) - rpmz

# std = diff.std()

# result7 = round(std, 3)
# print(result7)