# Part3. 연습문제

# 연습문제1.
# print("연습 문제1.")
# import pandas as pd
# exam1 = pd.read_csv('data/연습문제/Rabbit_Five.csv', encoding= 'cp949')

# from scipy.stats import ttest_rel

# bp = exam1['BP_change']
# treat = exam1['Treatment']

# mdl = bp[treat == "MDL"].reset_index(drop = True)
# control = bp[treat == "Control"].reset_index(drop = True)

# diff_avg = (mdl - control).mean()
# diff_avg = round(diff_avg, 2)
# print(diff_avg)

# a = ttest_rel(mdl, control)

# stat = a.statistic
# stat = round(stat, 2)
# print(stat)

# pval = a.pvalue
# pval = round(pval, 3)
# print(pval)

# print('기각')

# 연습문제2.
# print("\n 연습 문제2.")
# import pandas as pd
# exam2 = pd.read_csv('data/연습문제/mtcars2.csv', encoding = 'cp949')

# from scipy.stats import f

# am = exam2['am']
# hp = exam2['hp']

# manual = hp[am==1].reset_index(drop = True)
# auto = hp[am==0].reset_index(drop = True)

# var_ratio = manual.var() / auto.var()
# print(round(var_ratio, 2))

# stat = var_ratio
# print(round(stat,2))

# df1, df2 = len(manual) - 1, len(auto) - 1

# pval = 1 - f.cdf(stat, dfn = df1, dfd = df2)

# a = round(var_ratio, 2)
# b = round(stat, 2)
# c = round(pval, 3)

# print(a)
# print(b)
# print(c)
# print('기각')

# 연습문제3.
# print("\n 연습 문제3.")
# import pandas as pd
# exam3 = pd.read_csv('data/연습문제/고객_등급리스트.csv', encoding = 'cp949')

# from scipy.stats import chi2_contingency
# import numpy as np

# tb = pd.crosstab(exam3['Segment'], exam3['Region'])

# chi2, pval, df, expected = chi2_contingency(tb)

# e23 = expected[1,2]
# e23 = round(e23, 2)
# print(e23)

# chi2 = chi2.astype('int')
# print(chi2)

# pval = round(pval, 3)
# print(pval)
# print('채택')

# 연습문제4.
# print("\n 연습 문제4.")
# import pandas as pd
# exam4 = pd.read_csv('data/연습문제/Cars93.csv', encoding= 'cp949')

# from scipy.stats import shapiro
# price = exam4['Price'].copy().dropna()

# avg = price.mean()
# avg = round(avg, 2)
# print(avg)

# stat, pval = shapiro(price)

# stat = round(stat, 2)
# print(stat)

# pval = round(pval, 4)
# pval = int(pval)
# print(pval)
# print('기각')


# 연습문제5.
# print("\n 연습 문제5.")
# import pandas as pd
# import numpy as np
# exam5 = pd.read_csv('data/연습문제/Cars93.csv')
# # print(exam5)
# hp = exam5['Horsepower']
# rpm = exam5['Rev_per_mile']

# from scipy.stats import pearsonr

# corr, pval = pearsonr(hp, rpm)
# corr = round(corr, 3)
# print(corr)

# stat = corr / np.sqrt( (1-corr**2) / (len(hp) - 2))
# stat = round(stat,2)
# print(stat)

# print(int(pval))

# 연습문제6.
# print("\n 연습 문제6.")
# import pandas as pd
# exam6 = pd.read_csv('data/연습문제/USArrests.csv')

# from sklearn.decomposition import PCA

# pca = PCA(n_components = 4)
# pca.fit_transform(exam6)

# weight = pca.components_.T[1, 0]
# weight = round(weight, 3)
# print(weight)

# score = pca.fit_transform(exam6)[33,0]
# score = round(score, 3)
# print(score)

# var_ratio = pd.Series(pca.explained_variance_ratio_)
# result = round(var_ratio[0], 2)
# print(result)

# 연습문제7.
# print("\n 연습 문제7.")
# import pandas as pd
# exam7 = pd.read_csv('data/연습문제/Cars93.csv')

# import statsmodels.api as sm

# colnm = ['Price', 'Rev_per_mile', 'Weight' , 'Length', 'EngineSize']
# samp = exam7[colnm].dropna()

# y = samp['Price']
# X = samp[['Rev_per_mile', 'Weight' , 'Length', 'EngineSize']]
# X = sm.add_constant(X)

# model = sm.OLS(y, X)
# result = model.fit()
# # print(result.summary())
# # r_square = 0.396
# # print(r_square)
# pval = 0.158
# print(pval)

# upper = 0.005406
# upper = round(upper, 4)
# print(upper)

# 연습문제8.
# print("\n 연습 문제8.")
# import pandas as pd
# exam8 = pd.read_csv('data/연습문제/job.csv')

# import statsmodels.api as sm
# import numpy as np

# exam8['x2'] = exam8['x2'].map({'M' : 1, 'F' : 0})

# y = exam8['y']
# X = exam8[['x1', 'x2', 'x3']]
# X = sm.add_constant(X)

# model = sm.GLM(y, X, family = sm.families.Binomial())
# result = model.fit()
# # print(result.summary())

# b0 = -0.808

# odds_ratio = round(np.exp(-0.1575), 3)

# y_prob = round(result.predict(X)[8], 4)
# print(y_prob)

# 연습문제9.
print("\n 연습 문제9.")
import pandas as pd
exam9 = pd.read_csv('data/연습문제/영화_순위리스트.csv', encoding='cp949')

from scipy.stats import bartlett
import numpy as np

genre = exam9['장르']
budget = exam9['예산']

b_thriller = budget[genre =='Thriller']
b_comedy = budget[genre =='Comedy']
b_drama = budget[genre =='Drama']
b_action = budget[genre =='Action']

var_i = [b_thriller.var(), b_comedy.var(), b_drama.var(), b_action.var()]

n_i = [len(b_thriller), len(b_comedy), len(b_drama), len(b_action)]

N = sum(n_i)
k = 4

log_sp2 = np.log(sum(np.subtract(n_i, 1) * var_i) / (N-k))
log_sp2 = round(log_sp2, 3)

print(log_sp2)

stat, pval = bartlett(b_thriller, b_comedy, b_drama, b_action)

stat = round(stat,2)
print(stat)

pval = round(pval, 4)
print(pval)