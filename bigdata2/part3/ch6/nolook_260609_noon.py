# print("\n Q1")
# import pandas as pd
# exam1 = pd.DataFrame({
#     'Caffeine(mg)': [
#         94.2, 93.7, 95.5, 93.9, 94.0, 95.2, 94.7, 93.5, 92.8, 94.4,
#         93.8, 94.6, 93.3, 95.1, 94.3, 94.9, 93.9, 94.8, 95.0, 94.2,
#         93.7, 94.4, 95.1, 94.0, 93.6
#     ]
# })

# print(exam1.mean())

# from scipy import stats
# # exam1.stats # 여기서 막힘 ㅋㅋㅋㅋㅋㅋㅋ 제기랄!!
# # 샤피로 정규성 검정부터! 
# print(stats.shapiro(exam1['Caffeine(mg)']))

# # 단일 표본 t검정
# print(stats.ttest_1samp(exam1['Caffeine(mg)'], 95, alternative='less'))

# statistic, pvalue = stats.ttest_1samp(exam1['Caffeine(mg)'], 95, alternative='less')
# print(f"{ statistic:4f}", f"{pvalue:.10f}")

# print("\n Q2")
# import pandas as pd

# exam2 = pd.DataFrame({
#     '충전기': ['New'] * 10 + ['Old'] * 10,
#     '충전시간': [
#         1.5, 1.6, 1.4, 1.7, 1.5, 1.6, 1.7, 1.4, 1.6, 1.5,
#         1.7, 1.8, 1.7, 1.9, 1.8, 1.7, 1.8, 1.9, 1.7, 1.6
#     ]
# })

# # print(exam2.head())
# # print(exam2)

# from scipy import stats

# new = exam2['충전기'] == 'New'
# old = exam2['충전기'] == 'Old'
# print(stats.ttest_ind(exam2[new]['충전시간'], exam2[old]['충전시간'],
#                       alternative='less', equal_var=True))

# print("\n Q3")
# import pandas as pd
# exam3 = pd.DataFrame({
#     'User': list(range(1, 11)),
#     '기존방법': [60.4, 60.7, 60.5, 60.3, 60.8, 60.6, 60.2, 60.5, 60.7, 60.4],
#     '새로운방법': [59.8, 60.2, 60.1, 59.9, 59.7, 58.4, 57.0, 60.3, 59.6, 59.8]
# })

# # print(exam3)
# mean = (exam3['새로운방법'] - exam3['기존방법']).mean()
# # print(mean)

# from scipy import stats # 역시 여기까지만 ㅎ...
# print(stats.ttest_rel(exam3['새로운방법'], exam3['기존방법'], alternative='less'))

# print("\n Q4")
# import pandas as pd
# exam4 = pd.read_csv("bigdata2/part3/ch6/math.csv")

# # print(exam4.head())
# # print(exam4)

# from scipy import stats
# # print(stats.shapiro) # 샤피로 쓰려면 그룹별로(그룹이 4개자너...)

# conda = exam4['groups'] == 'group_A'
# print(stats.shapiro(exam4[conda]['scores']))

# condb = exam4['groups'] == 'group_B'
# print(stats.shapiro(exam4[condb]['scores']))

# condc = exam4['groups'] == 'group_C'
# print(stats.shapiro(exam4[conda]['scores']))

# condd = exam4['groups'] == 'group_D'
# print(stats.shapiro(exam4[condd]['scores']))

# # 등분산성
# print(stats.levene(exam4[conda]['scores'], exam4[condb]['scores'], exam4[condc]['scores'], exam4[condd]['scores']))

# from statsmodels.formula.api import ols
# model = ols('scores ~ groups', exam4).fit()

# from statsmodels.stats.anova import anova_lm
# print(anova_lm(model))