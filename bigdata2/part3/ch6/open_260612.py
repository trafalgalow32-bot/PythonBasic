# print("\n Q1")
# import pandas as pd
# exam1 = pd.DataFrame({
#     'Caffeine(mg)': [
#         94.2, 93.7, 95.5, 93.9, 94.0, 95.2, 94.7, 93.5, 92.8, 94.4,
#         93.8, 94.6, 93.3, 95.1, 94.3, 94.9, 93.9, 94.8, 95.0, 94.2,
#         93.7, 94.4, 95.1, 94.0, 93.6
#     ]
# })

# print("표본평균")
# print(exam1.mean())

# print("\n Shapiro-Wilk p-value")
# from scipy import stats
# print(stats.shapiro(exam1['Caffeine(mg)']))

# print(stats.ttest_1samp(exam1['Caffeine(mg)'], 95, alternative='less'))

# statistic, pvalue = stats.ttest_1samp(exam1['Caffeine(mg)'], 95, alternative='less')
# print(f"{statistic}:4f", f"{pvalue:.10f}")

# print("\n Q2")
# import pandas as pd

# exam2 = pd.DataFrame({
#     '충전기': ['New'] * 10 + ['Old'] * 10,
#     '충전시간': [
#         1.5, 1.6, 1.4, 1.7, 1.5, 1.6, 1.7, 1.4, 1.6, 1.5,
#         1.7, 1.8, 1.7, 1.9, 1.8, 1.7, 1.8, 1.9, 1.7, 1.6
#     ]
# })
# # print(exam2)
# # exam2['new'] = exam2['충전기' == "New"]
# # exam2['old'] = exam2['충전기' == "Old"]

# # from scipy import stats
# # print(stats.ttest_ind(exam2['new'], exam2['old'], alternative='less'))

# ##### 모범 답안!!

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

# print((exam3['새로운방법'] - exam3['기존방법']).mean())

# from scipy import stats
# print(stats.ttest_rel(exam3['새로운방법'], exam3['기존방법'], alternative='less'))

# print("\n Q4")
# import pandas as pd
# exam4 = pd.read_csv("bigdata2/part3/ch6/math.csv")

# # print(exam4)

# from scipy import stats

# conda = exam4['groups'] == 'group_A'
# print(stats.shapiro((exam4[conda]['scores'])))

# condb = exam4['groups'] == 'group_B'
# print(stats.shapiro((exam4[condb]['scores'])))

# condc = exam4['groups'] == 'group_C'
# print(stats.shapiro((exam4[condc]['scores'])))

# condd = exam4['groups'] == 'group_D'
# print(stats.shapiro((exam4[condd]['scores'])))

# print(stats.levene(exam4[conda]['scores'], exam4[condb]['scores'], exam4[condc]['scores'], exam4[condd]['scores']))

# ##### 여기부터 오픈북!
# from statsmodels.formula.api import ols
# model = ols('scores ~ groups', exam4).fit()

# from statsmodels.stats.anova import anova_lm
# print(anova_lm(model))

# print("\n Q5")
# import pandas as pd
# exam5 = pd.read_csv("bigdata2/part3/ch6/tomato2.csv")

# import statsmodels.api as sm
# from statsmodels.formula.api import ols
# from statsmodels.stats.anova import anova_lm

# model = ols('수확량 ~ C(비료유형) * C(물주기)', data=exam5).fit()
# anova_table = sm.stats.anova_lm(model)
# print(anova_table)

# print("\n")
# print(30 / 1000)

# from scipy.stats import chisquare
# observed = [550, 250, 100, 70, 30]
# expected = [1000 * 0.6, 1000 * 0.25, 1000* 0.08, 1000*0.05, 1000*0.02]
# print(chisquare(observed, expected))

# print("\n Q7")
# import pandas as pd
# from scipy.stats import chi2_contingency

# observed = pd.DataFrame([50, 30],[60, 40])
# print(chi2_contingency(observed))

# exam7 = pd.DataFrame({
#     '캠프' : ['빅분기']*80 + ['정처기']*100,
#     '등록여부' : ['등록']*50 + ['등록안함']*30 + ['등록']*60 + ['등록안함']*40
# })
# exam7 = pd.crosstab(exam7['캠프'], exam7['등록여부'])

# print(chi2_contingency(exam7))

print("\n Q8")
import pandas as pd
exam8 = pd.DataFrame({
    '할인율': [28, 24, 13, 0, 27, 30, 10, 16, 6, 5, 7, 11, 11, 30, 25, 4, 7, 24, 19, 21, 6, 10, 26, 13, 15, 6, 12, 6, 20, 2],
    '온도': [15, 34, 15, 22, 29, 30, 14, 17, 28, 29, 19, 19, 34, 10, 29, 28, 12, 25, 32, 28, 22, 16, 30, 11, 16, 18, 16, 33, 12, 22],
    '광고비': [342, 666, 224, 764, 148, 499, 711, 596, 797, 484, 986, 347, 146, 362, 642, 591, 846, 260, 560, 941, 469, 309, 730, 305, 892, 147, 887, 526, 525, 884],
    '주문량': [635, 958, 525, 25, 607, 872, 858, 732, 1082, 863, 904, 686, 699, 615, 893, 830, 856, 679, 918, 951, 789, 583, 988, 631, 866, 549, 910, 946, 647, 943]
})

from statsmodels.formula.api import ols
model = ols(' 주문량 ~ 할인율 + 온도 + 광고비', data = exam8).fit()

print("1. 상관 계수 : ", round(exam8['할인율'].corr(exam8['온도']), 2))

print("2. 결정 계수(R-squared) : ", round(model.rsquared, 2))

print("3. 회귀 계수 : ", round(model.params, 4))

print("4. 절편 : ", round(model.pvalues['온도'], 4))

print("5. pvalue : ", round(model.pvalues['온도'], 4))

new_data = pd.DataFrame({"할인율": [10], "온도":[20], "광고비":[500]})
result = model.predict(new_data)
print("6. 새로운 데이터 : ", int(result[0]))

exam8['잔차'] = exam8['주문량'] - model.predict(exam8)
print("7. 잔차 제곱합 : " , round(sum(exam8['잔차']**2), 2))

mse = (exam8['잔차'] ** 2).mean()
print("8. MSE : " , round(mse, 4))

print("9. 신뢰구간: \n", model.conf_int(alpha=0.1))

new_data = pd.DataFrame({"할인율": [15], "온도": [25], "광고비" : [300]})
pred = model.get_prediction(new_data)
result = pred.summary_frame(alpha=0.1)
print("10. 예측값의 신뢰 구간과 예측 구간:\n", result)

cond = model.pvalues['광고비'] < 0.05
if cond:
    result = "기각"
else:
    result = "채택"
print("11. 귀무가설", result)

print(model.summary())