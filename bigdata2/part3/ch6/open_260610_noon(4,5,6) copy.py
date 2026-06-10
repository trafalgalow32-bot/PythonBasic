# print("\n Q4")
# import pandas as pd
# exam4 = pd.read_csv("bigdata2/part3/ch6/math.csv")
# # print(exam4)

# from scipy import stats
# conda = exam4['groups'] == 'group_A'
# print(stats.shapiro(exam4[conda]['scores']) )

# condb = exam4['groups'] == 'group_B'
# print(stats.shapiro(exam4[condb]['scores']) )

# condc = exam4['groups'] == 'group_C'
# print(stats.shapiro(exam4[condc]['scores']) )

# condd = exam4['groups'] == 'group_D'
# print(stats.shapiro(exam4[condd]['scores']) )

# print(stats.levene(exam4[conda]['scores'], exam4[condb]['scores'], exam4[condc]['scores'], exam4[condd]['scores']))

# from statsmodels.formula.api import ols
# model = ols('scores ~ groups', exam4).fit()

# from statsmodels.stats.anova import anova_lm
# print(anova_lm(model))

# print("\n Q5")
# import pandas as pd
# exam5 = pd.read_csv("bigdata2/part3/ch6/tomato2.csv")
# # print(exam5)

# import statsmodels.api as sm
# from statsmodels.formula.api import ols

# model = ols('수확량 ~ C(비료유형) * C(물주기)', data=exam5).fit()
# anova_table = sm.stats.anova_lm(model)
# print(anova_table)

# print("\n Q6")
# # 교통사고 5회 이상 경험 비율
# print(30 / 1000)

# # 적합도 검정
# from scipy.stats import chisquare
# observed = [550, 250, 100, 70, 30]
# expected = [1000 * 0.60, 1000 * 0.25, 1000 * 0.08, 1000 * 0.05, 1000 * 0.02]
# print(chisquare(observed, expected))

