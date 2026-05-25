# part3_practice.py

"""
(a): 표본 평균을 계산하는 것으로 데이터로부터 (실험군 혈압 변화-대조군 혈압변화)을 계산한 후 문제에서 요구하는 
형태에 맞게 출력한다.
"""
print("연습 문제1.")
import pandas as pd
exam1 = pd.read_csv('data/연습문제/Rabbit_Five.csv', encoding= 'cp949')

from scipy.stats import ttest_rel

# 필요한 컬럼 각각 할당
bp = exam1['BP_change']
treat = exam1['Treatment'] # Control, MDL의 컬럼임!

# Treatment가 Control인 경우(대조군)와 MDL인 경우(실험군)의 BP_change 값 각각 할당
mdl = bp[treat == "MDL"].reset_index(drop = True)
control = bp[treat == "Control"].reset_index(drop = True)

# (a) 점추정량 = mean(PC_Treat - PC_Control)
diff_avg = (mdl - control).mean()
diff_avg = round(diff_avg, 2)
print(diff_avg) # 출력값 -4.68

"""
(b)-(c) ttest_rel() 함수를 통해 가설 검정을 수행하고 결과에서 제공하는 검정통계량과 p-값을 각각 문제에서 
요구하는 형태에 맞게 출력한다. 
"""
# (b)-(c)

# 대응표본 t검정 수행
a = ttest_rel(mdl, control)

# (b) 검정 통계량
stat = a.statistic
stat = round(stat, 2)
print(stat) # 출력값 -3.67

# (c) p-값/기각여부
pval = a.pvalue
pval = round(pval, 3)
print(pval) # 출력값 0.001
"""
p-값이 0.001이므로 본 가설 검정은 '기각'한다.
"""
print('기각')

print("\n 연습 문제2.")
import pandas as pd
exam2 = pd.read_csv('data/연습문제/mtcars2.csv', encoding = 'cp949')

from scipy.stats import f

am = exam2['am']
hp = exam2['hp']

# 수동변속기(am=1)인 자동차의 마력(hp), 자동변속기(am=0)인 자동차의 마력(hp) 각각 할당
manual = hp[am==1].reset_index(drop = True)
auto = hp[am==0].reset_index(drop = True)

# (a) 수동변속 표본분산 / 자동변속 표본분산
var_ratio = manual.var() / auto.var()
print(round(var_ratio, 2)) # 출력값 2.43

# (b)-(c)

# F검정 수행
# (b) 검정통계량 = (a)와 같음
stat = var_ratio
print(round(stat,2)) # 출력값 2.43

# (c) 유의 확률
# 자유도
df1, df2 = len(manual) - 1, len(auto) -1

# F분포로 확률 계산
pval = 1 - f.cdf(stat, dfn = df1, dfd = df2) # Pr[F> stat]

# 반올림
a = round(var_ratio, 2)
b = round(stat, 2)
c = round(pval, 3)

# 출력
print(a) # (a) 출력값 2.43
print(b) # (b) 검정통계량, 출력값 2.43
print(c) # (c) p-값 , 출력값 0.043
print('기각') # 유의수준 0.05 이내!

print("\n 연습 문제3.")
import pandas as pd
exam3 = pd.read_csv('data/연습문제/고객_등급리스트.csv', encoding = 'cp949')

from scipy.stats import chi2_contingency
import numpy as np

# 교차표 생성
tb = pd.crosstab(exam3['Segment'], exam3['Region'])

# 카이제곱 검정 수행
# ch2_contingency의 결과는 카이제곱통계량, 유의확률, 자유도, 기대도수를 반환함
chi2, pval, df, expected = chi2_contingency(tb)

# (a)E23 : expected의 (1,2) 인덱스 번호 추출
e23 = expected[1,2]
e23 = round(e23, 2)
print(e23) # 출력값 15.74

# (b) 검정 통계량
chi2 = chi2.astype('int') # 정수 변환
print(chi2) # 출력값 9

# (c) p-값 / 기각여부
pval = round(pval, 3)
print(pval) # 출력값 0.148
print('채택')

print("\n 연습 문제4.")
import pandas as pd
exam4 = pd.read_csv('data/연습문제/Cars93.csv', encoding = 'cp949')

from scipy.stats import shapiro
price = exam4['Price'].copy().dropna()

# (a) 표본평균
avg = price.mean()
avg = round(avg, 2)
print(avg) # 출력값 19.05

#(b)-(c)
# 샤피로 윌크 검정 수행
stat, pval = shapiro(price)

# (b) 검정 통계량
stat = round(stat, 2)
print(stat) # 출력값 0.85

# (c) p-값 기각 여부
pval = round(pval, 4) # 출력값 0.0
pval = int(pval) # 출력값 0
print(pval)
print('기각')

print("\n 연습 문제5.")
import pandas as pd
import numpy as np
exam5 = pd.read_csv('data/연습문제/Cars93.csv')

# 상관분석에 필요한 컬럼명 저장
hp = exam5['Horsepower']
rpm = exam5['Rev_per_mile']

from scipy.stats import pearsonr

# 상관계수 검정 수행
corr, pval = pearsonr(hp, rpm)

# (a) 표본상관계수
corr = round(corr, 3)
print(corr) # 출력값 -0.502

# (b) 검정통계량
stat = corr/np.sqrt( (1-corr**2) / (len(hp) - 2))
stat = round(stat, 2)
print(stat) # 출력값 -5.54

# (c) p-값 / 기각여부
pval = int(pval)
print(pval) # 출력값 0
print('기각')

print("\n 연습 문제6.")
import pandas as pd
exam6 = pd.read_csv('data/연습문제/USArrests.csv')

from sklearn.decomposition import PCA

# PCA 수행
pca = PCA(n_components = 4) # 주성분 객체 생성
pca.fit_transform(exam6)

# (a) 첫번째 주성분의 폭력범죄 기여 가중치
# pca.components_.T에서 행은 기존 컬럼(Murder, Assault, UrbanPop, Rape)
# 열은 1~4 주성분임
weight= pca.components_.T[1, 0]
weight = round(weight, 3)
print(weight) # 출력값 0.995

# (b) 34번째 도시의 1주성분의 주성분 점수
score = pca.fit_transform(exam6)[33,0]
score = round(score, 3)
print(score)   # 출력값 -127.496

# (c) 주성분별 설명되는 분산비율을 시리즈 객체로 저장
var_ratio = pd.Series(pca.explained_variance_ratio_)
result = round(var_ratio[0], 2)
print(result) # 출력값 0.97
print(3)

print("\n 연습 문제7.")
import pandas as pd
exam7 = pd.read_csv('data/연습문제/Cars93.csv')

import statsmodels.api as sm

# 회귀분석 수행: 회귀 분석에 필요한 컬럼 별도 지정
colnm = ['Price', 'Rev_per_mile', 'Weight', 'Length', 'EngineSize']
samp = exam7[colnm].dropna() # 결측치 제거

# y, X에 각각 할당
y = samp['Price']
X = samp[['Rev_per_mile', 'Weight', 'Length', 'EngineSize']]
X = sm.add_constant(X) # 절편항 적합을 위해 상수벡터 추가

# 모델 적합
model = sm.OLS(y,X) # OLS 객체 생성
result = model.fit() # fit 메소드를 통해 모형 적합

# result.params # 회귀 계수만 추출
# result.tvalues # t통계량만 추출
result.summary() # 해당 코드를 통해 회귀분석 통합 결과를 확인하고 값을 입력하면 됨
# print(result.summary())

# (a) 결정계수
# r_square = 0.396
# print(r_square)

# (b) 문제의 의도는 Weight의 추정 회귀 계수를 출력하는 것이다.
b = 0.0023 # result.summary() 했을 때 Weight coef가 가리키는 첫번째 값? (이건 짚고 넘어가기!)

# (c) 문제의 의도는 Weight의 P>|t|을 통해 회귀계수를 검정하는 것이다. 
pval = 0.158
print(pval)

# (d) 문제의 의도는 Weight의 회귀계수에 대한 95% 신뢰구간을 구하는 것이다. 
# 이 코드의 상한 값을 입력! result.conf_int(alpha = 0.05, cols = None)
# print(result.conf_int(alpha = 0.05, cols = None))
upper = 0.005406
upper = round(upper, 4)
print(upper)

print("\n 연습 문제8.")
import pandas as pd
exam8 = pd.read_csv('data/연습문제/job.csv')

import statsmodels.api as sm
import numpy as np

# x2 컬럼 : M -> 1, F -> 0
exam8['x2'] = exam8['x2'].map({'M' : 1, 'F': 0})

# y, X에 각각 할당
y = exam8['y']
X = exam8[['x1', 'x2', 'x3']]
X = sm.add_constant(X) # 절편항 적합을 위해 상수벡터 추가

# 모델 적합
model = sm.GLM(y, X, family = sm.families.Binomial())
result = model.fit()

# (a) 절편항 추정 회귀 계수
# print(result.summary()) # 확인 코드
b0 = -0.808
print(b0)

# (b) 여성에 비해 남성의 성공에 대한 오즈가 몇 배인지를 구하려면
# 오즈비 = 남성의 성공 오즈 / 여성의 성공 오즈
#       = x2 컬럼이 성별이므로 exp(beta2)를 구하면 됨
odds_ratio = round(np.exp(-0.1575), 3) # result.summary()로 확인
print(odds_ratio) # 출력값 0.854

# (c) 9번째 사람의 성공 예측 확률
y_prob = round(result.predict(X)[8], 4)
print(y_prob) # 출력값 0.5344
print(0)

print("\n 연습 문제9.")
import pandas as pd
exam9 = pd.read_csv('data/연습문제/영화_순위리스트.csv', encoding = 'cp949')

from scipy.stats import bartlett
import numpy as np

genre = exam9['장르']
budget = exam9['예산']

# 장르별 예산 값 할당
b_thirller = budget[genre == 'Thriller']
b_comedy = budget[genre == 'Comedy']
b_drama = budget[genre == 'Drama']
b_action = budget[genre == 'Action']

# (a) 합동 분산(pooled variance)
# 집단별 표본 분산
var_i = [b_thirller.var(), b_comedy.var(), b_drama.var(), b_action.var()]

# 집단별 관측치 수
n_i = [len(b_thirller), len(b_comedy), len(b_drama), len(b_action)]

# log(합동분산) 계산
N = sum(n_i)
k = 4 # 집단의 수

log_sp2 = np.log(sum(np.subtract(n_i, 1) * var_i) / (N-k))
log_sp2 = round(log_sp2, 3)

print(log_sp2) # 출력값 16.542

# (b)-(c) : Bartlett Test 수행
stat, pval = bartlett(b_thirller, b_comedy, b_drama, b_action)

#(b) 검정통계량
stat = round(stat, 2)
print(stat) # 출력값 13.44

# (c) p-값 / 기각여부
pval = round(pval, 4)
print(pval) # 출력값 0.0038

print('기각')