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
# print(stats.shapiro(exam1['Caffeine(mg)']))

# print(stats.ttest_1samp(exam1['Caffeine(mg)'], 95, alternative='less'))

# statistic, pvalue = stats.ttest_1samp(exam1['Caffeine(mg)'], 95, alternative='less')
# print("{:.10f}".format(pvalue))

# print("\n Q2")
# import pandas as pd

# exam2 = pd.DataFrame({
#     '충전기': ['New'] * 10 + ['Old'] * 10,
#     '충전시간': [
#         1.5, 1.6, 1.4, 1.7, 1.5, 1.6, 1.7, 1.4, 1.6, 1.5,
#         1.7, 1.8, 1.7, 1.9, 1.8, 1.7, 1.8, 1.9, 1.7, 1.6
#     ]
# })
# # print(exam2.head(2))

# from scipy import stats

# new = exam2['충전기'] == 'New'
# old = exam2['충전기'] == 'Old'
# print(stats.ttest_ind(exam2[new]['충전시간'], exam2[old]['충전시간'],
#                       alternative='less', equal_var=True))

print("\n Q3")
import pandas as pd
exam3 = pd.DataFrame({
    'User': list(range(1, 11)),
    '기존방법': [60.4, 60.7, 60.5, 60.3, 60.8, 60.6, 60.2, 60.5, 60.7, 60.4],
    '새로운방법': [59.8, 60.2, 60.1, 59.9, 59.7, 58.4, 57.0, 60.3, 59.6, 59.8]
})

print(exam3.head(2))

exam3['diff'] = exam3['새로운방법'] - exam3['기존방법']
print(exam3['diff'].mean())

from scipy import stats
print(stats.ttest_rel(exam3['새로운방법'], exam3['기존방법'], alternative='less'))