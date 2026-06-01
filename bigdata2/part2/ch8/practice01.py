# practice01.py
# Part2 연습문제
"""
문제는 md 파일 참조!
"""
print("\n Q1")
import pandas as pd
exam1 = pd.DataFrame({
    'Caffeine(mg)': [
        94.2, 93.7, 95.5, 93.9, 94.0, 95.2, 94.7, 93.5, 92.8, 94.4,
        93.8, 94.6, 93.3, 95.1, 94.3, 94.9, 93.9, 94.8, 95.0, 94.2,
        93.7, 94.4, 95.1, 94.0, 93.6
    ]
})

# 평균
print(exam1.mean())

# 정규성 검정
from scipy import stats
print(stats.shapiro(exam1['Caffeine(mg)']))

# 단일 표본 t검정
print(stats.ttest_1samp(exam1['Caffeine(mg)'], 95, alternative='less'))


"""
Shapiro–Wilk 검정의 p–value는 0.9321980476379395로 p–value가 0.05보다 크므로 데이터가 정규 분포를 따른다.
단일 표본 t–검정의 검정 통계량은 –5.501737036221897이고, p–value는 0.0000058687(5.8686553916715e–06)이다.
대립가설을 기준으로 exam1['Caffeine(mg)']가 95보다 작아야 한다. 따라서 alternative는 less다.
p–value가 0.05보다 작으므로 귀무가설을 기각한다.
지수 표기법을 일반 소수점 형태로 변경하기 위해 "{:.10f}".format(pvalue)를 사용했다. 소수 10번째 자리까지로 변경한다.
"""

statistic, pvalue = stats.ttest_1samp(exam1['Caffeine(mg)'], 95, alternative='less')
print("{:.10f}".format(pvalue)) # 출력값 0.0000058687

"""
정답
1. 94.264
2. 0.9321980476379395
3. –5.501737036221897
4. 0.0000058687(5.8686553916715e–06)
5. 기각
"""

print("\n Q2")
import pandas as pd

exam2 = pd.DataFrame({
    '충전기': ['New'] * 10 + ['Old'] * 10,
    '충전시간': [
        1.5, 1.6, 1.4, 1.7, 1.5, 1.6, 1.7, 1.4, 1.6, 1.5,
        1.7, 1.8, 1.7, 1.9, 1.8, 1.7, 1.8, 1.9, 1.7, 1.6
    ]
})
print(exam2.head(2))

# 독립 표본 t-검정
new = exam2['충전기'] == 'New'
old = exam2['충전기'] == 'Old'
print(stats.ttest_ind(exam2[new]['충전시간'], exam2[old]['충전시간'],
                      alternative='less', equal_var=True))

"""
📝 해설
스마트폰 충전기의 효과를 비교하는 데 있어서 두 독립된 집단 간의 평균을 비교하는 데 초점을 맞추고 있다.

독립성 검정은 ttest_ind()를 사용한다. 분산이 같다고 가정했기 때문에 equal_var=True로 설정한다.

t-test 결과, p-value가 0.05보다 작으므로 귀무가설을 기각한다.

정답
1. -4.582575694955849

2. 0.00011546547787696304

3. 기각
"""

print("\n Q3")
import pandas as pd
exam3 = pd.DataFrame({
    'User': list(range(1, 11)),
    '기존방법': [60.4, 60.7, 60.5, 60.3, 60.8, 60.6, 60.2, 60.5, 60.7, 60.4],
    '새로운방법': [59.8, 60.2, 60.1, 59.9, 59.7, 58.4, 57.0, 60.3, 59.6, 59.8]
})

print(exam3.head(2))

# 표본 평균
exam3['diff'] = exam3['새로운방법'] - exam3['기존방법']
print(exam3['diff'].mean())

# 대응 표본 t-검정
print(stats.ttest_rel(exam3['새로운방법'], exam3['기존방법'], alternative='less'))

"""
📝 해설
μ₀는 새로운 방법 − 기존 방법이다. 차이 값을 diff 컬럼에 대입하고, 평균을 구한다.
대응 표본 t-검정은 ttest_rel()을 활용한다.
μ₀는 순서대로 새로운 방법, 기존 방법을 넣고 alternative에는 대립가설 기준 첫 번째 값이 두 번째보다 작아야 하므로 less를 입력한다.
t-test 결과, p-value가 0.05보다 작으므로 귀무가설을 기각한다.

정답
1. -1.0300000000000005

2. -3.407973078114844

3. 0.0038872633380070652

4. 기각
"""

print("\n Q4")
import pandas as pd
exam4 = pd.read_csv("bigdata2/part3/ch6/math.csv")
print(exam4.head())

from scipy import stats

# Shapiro-Wilk 검정 (정규성)
conda = exam4['groups'] == 'group_A'
print(stats.shapiro(exam4[conda]['scores']))

condb = exam4['groups'] == 'group_B'
print(stats.shapiro(exam4[condb]['scores']))

condc = exam4['groups'] == 'group_C'
print(stats.shapiro(exam4[condc]['scores']))

condd = exam4['groups'] == 'group_D'
print(stats.shapiro(exam4[condd]['scores']))

# Levene 검정 (등분산성)
print(stats.levene(exam4[conda]['scores'], exam4[condb]['scores'], exam4[condc]['scores'], exam4[condd]['scores']))

"""
shapiro()를 활용해 정규성 검정을 실시한다. 4개 그룹 모두 정규성을 만족한다.
4개 그룹의 성적이 등분산성을 갖는지 Levene 검정을 사용해 확인한다. 등분산성을 만족한다.
"""

# 일원분산분석을 위한 모델 학습
from statsmodels.formula.api import ols
model = ols('scores ~ groups', exam4).fit()

# ANOVA 테이블
from statsmodels.stats.anova import anova_lm
print(anova_lm(model))

"""
일원 분산 분석을 실시한 결과, p-value가 0.05보다 작으므로 귀무가설을 기각한다.
ols()를 사용해 모델을 학습하고, ANOVA 테이블을 출력한다.
자유도(df), 총 제곱합(sum_sq), 평균 제곱합(mean_sq), F-통계량(F), p-value(PR(>F))를 의미한다.
독립변수 groups 변수는 문자이다. C() 사용 여부와 관계없이 결과는 같다.

정답
1. (0.9051811695098877, 0.6678178906440735, 0.4473262727605896, 0.2582412362098694)
2. 0.17270284963232108
3. 기각
4. 3
5. 36
6. 411.8
7. 137.266667
8. 34.174274
9. 1.240642e-10 (0.000000000124)
"""

print("\n Q5")
import pandas as pd
exam5 = pd.read_csv("bigdata2/part3/ch6/tomato2.csv")
print(exam5.head())

import statsmodels.api as sm
from statsmodels.formula.api import ols

# 이원 분산 분석
model = ols('수확량 ~ C(비료유형) * C(물주기)', data=exam5).fit()
anova_table = sm.stats.anova_lm(model)
print(anova_table)

"""
비료 유형에 대한 분석: F-통계량(3.184685), p-value(0.059334) → 귀무가설 채택
물 주기에 대한 분석: F-통계량(3.661490), p-value(0.026460) → 귀무가설 기각
비료 유형과 물 주기 간의 상호작용 효과에 대한 분석: F-통계량(0.863491), p-value(0.535426) → 귀무가설 채택

※ exam5(자유도), sum_sq(총 제곱합), mean_sq(평균 제곱)

✅ 정답
1. 3.184685
2. 0.059334
3. 채택
4. 3.661490
5. 0.026460
6. 기각
7. 0.863491
8. 0.535426
9. 채택
"""

print("\n Q6")
# 교통사고 5회 이상 경험 비율
print(30 / 1000)

# 적합도 검정
from scipy.stats import chisquare
observed = [550, 250, 100, 70, 30]
expected = [1000 * 0.60, 1000 * 0.25, 1000 * 0.08, 1000 * 0.05, 1000 * 0.02]
print(chisquare(observed, expected))

"""
교통사고 5회 이상 경험은 1,000명 중 30명이다. (비율: 0.03)
적합도 검정을 위해 관측치와 기대 값을 리스트에 담는다. 이때 중요한 부분은 모두 빈도 수로 통일해야 한다.
관측치인 한 도시의 교통사고 경험 수(빈도)는 observed 변수에 순서대로 입력한다.
기대 값인 전국적인 교통사고 경험 수(빈도)는 expected 변수에 입력한다. 전국적인 경험(확률 값)에 1,000을 곱해 빈도 값을 구한다.
chisquare() 함수를 통해 적합도 검정을 실시하고 검정 통계량, p-value를 확인한다.
p-value가 0.00018로 유의수준 0.05보다 작으므로 귀무가설을 기각한다.
이 도시의 교통사고 경험 수 분포는 전국적인 경향을 따르지 않는다.

✅ 정답
1. 0.03
2. 22.166666666666668
2. 0.00018567620386641427
4. 기각
"""

print("\n Q7")
# (1) 교차표 데이터가 주어졌을 때
import pandas as pd
from scipy.stats import chi2_contingency

# 독립성 검정
observed = pd.DataFrame([[50, 30], [60, 40]])
print(chi2_contingency(observed))

# (2) 로우 데이터가 주어졌을 때
import pandas as pd
exam7 = pd.DataFrame({
    '캠프' : ['빅분기']*80 + ['정처기']*100,
    '등록여부' : ['등록']*50 + ['등록안함']*30 + ['등록']*60 + ['등록안함']*40
})
print(exam7.head())

# 교차로로 변경
exam7 = pd.crosstab(exam7['캠프'], exam7['등록여부'])
print(exam7)

# 독립성 검정
print(chi2_contingency(exam7))

"""
pd.crosstab() 함수를 사용해 교차표 형태로 변경한다.
chi2_contingency() 함수를 활용해 검정 통계량과 p-value를 구한다.
p-value가 0.85로 유의수준 0.05보다 크므로 귀무가설을 채택한다.
빅분기 캠프에서 등록할 것으로 기대되는 빈도는 48.9, 등록하지 않을 것으로 기대되는 빈도는 31.1이다.
정처기 캠프에서 등록할 것으로 기대되는 빈도는 61.1, 등록하지 않을 것으로 기대되는 빈도는 38.9이다.

✅ 정답
1. 0.03535714285714309
2. 0.8508492527705047
3. 채택
4. 0.03535714285714309
5. 0.8508492527705047
6. 채택
"""

print("\n Q8")
import pandas as pd
exam8 = pd.DataFrame({
    '할인율': [28, 24, 13, 0, 27, 30, 10, 16, 6, 5, 7, 11, 11, 30, 25, 4, 7, 24, 19, 21, 6, 10, 26, 13, 15, 6, 12, 6, 20, 2],
    '온도': [15, 34, 15, 22, 29, 30, 14, 17, 28, 29, 19, 19, 34, 10, 29, 28, 12, 25, 32, 28, 22, 16, 30, 11, 16, 18, 16, 33, 12, 22],
    '광고비': [342, 666, 224, 764, 148, 499, 711, 596, 797, 484, 986, 347, 146, 362, 642, 591, 846, 260, 560, 941, 469, 309, 730, 305, 892, 147, 887, 526, 525, 884],
    '주문량': [635, 958, 525, 25, 607, 872, 858, 732, 1082, 863, 904, 686, 699, 615, 893, 830, 856, 679, 918, 951, 789, 583, 988, 631, 866, 549, 910, 946, 647, 943]
})
print(exam8.head(3))

# 다중 선형 회귀 모델 적합
from statsmodels.formula.api import ols
model = ols(' 주문량 ~ 할인율 + 온도 + 광고비', data = exam8).fit()

# 상관 계수
print("1. 상관 계수 : ", round(exam8['할인율'].corr(exam8['온도']), 2))

# 결정 계수
print("2. 결정 계수(R-squared) : ", round(model.rsquared, 2))

# 회귀 계수(기울기)
print("3. 회귀 계수 : ", round(model.params, 4))

# 절편
print("4. 절편 : ", round(model.pvalues['온도'], 4))

# 회귀 계수 검정
print("5. pavlue : ", round(model.pvalues['온도'], 4))

# 예측 판매량
new_data = pd.DataFrame({"할인율": [10], "온도":[20], "광고비":[500]})
result = model.predict(new_data)
print("6.새로운 데이터 : ", int(result[0]))

# 잔차 제곱합
exam8['잔차'] = exam8['주문량'] - model.predict(exam8)
print("7. 잔차 제곱합 : ", round(sum(exam8['잔차']**2), 2))

# MSE(Mean Squared Error)
mse = (exam8['잔차'] ** 2).mean()
print("8. MSE : ", round(mse, 4))

# 각 변수에 대한 90% 신뢰 구간
print("9. 신뢰구간:\n", model.conf_int(alpha=0.1))

# 새로운 데이터의 예측값의 90% 신뢰 구간과 예측 구간
new_data = pd.DataFrame({"할인율": [15], "온도": [25], "광고비": [300]})
pred = model.get_prediction(new_data)
result = pred.summary_frame(alpha=0.1)
print("10. 예측값의 신뢰 구간과 예측 구간:\n", result)

# 광고비는 배달 주문량에 영향을 주는지 가설 검정
cond = model.pvalues['광고비'] < 0.05
if cond:
    result = "기각"
else:
    result = "채택"
print("11. 귀무가설", result)

# 선형 회귀 모델의 요약 결과
print(model.summary())

"""
11번 문제에서 "독립변수 할인율과 온도가 고정될 때..."라는 표현은 이런 변수들의 값이 변하지 않는 상황에서 광고비가 배달 주문량에 미치는 영향만을 분리해 검토하겠다는 의미다. 
즉, 다중 회귀 분석에서 광고비의 회귀 계수를 검토하여 유의성을 검정한다. 
회귀 계수의 유의성 검정은 t-test를 사용하며 광고비의 p-value가 0.003으로 유의수준 0.05보다 작으므로 귀무가설을 기각한다. 
따라서 광고비는 주문량에 유의미한 영향을 미친다.

✅ 정답
1. 0.09
2. 0.4
3. Intercept: 267.6609, 할인율: 4.2068, 온도: 9.4798, 광고비: 0.4148
4. 267.6609
5. 0.0289
6. 706
7. 732197.9
8. 24406.5966
9. 2.490702, 16.468984
10. 신뢰 구간: 614.507283, 769.907488 / 예측 구간: 395.622293, 988.792478
11. 귀무가설 기각
"""

print("\n Q9")
import pandas as pd
exam9 = pd.read_csv("bigdata2/part3/ch6/customer_travel.csv")

# 데이터 분할
midpoint = len(exam9) // 2
a = exam9.iloc[:midpoint]
b = exam9.iloc[midpoint:]

# 데이터 확인
print(a.shape , b.shape)

# 유의하지 않은 독립변수의 개수
from statsmodels.formula.api import logit
formula = "target ~ age + service + social + booked"
model = logit(formula, data=a).fit()
# print(model.summary())
print("1. ", sum(model.pvalues[1:] >= 0.05)) # 상수항(Intercept) 제외

# 수정된 모델에서 가장 큰 p-value를 가진 변수의 이름
formula = 'target ~ age + booked'
model = logit(formula, data=a).fit()
# print(model.summary())
print("2. ", model.pvalues[1:].idxmax()) # 상수항(Intercept) 제외

# 수정된 모델에서 독립변수 중 절댓값이 가장 큰 회귀계수를 가진 변수의 이름
print("3. ", model.params[1:].abs().idxmax())

# 로그 우도
print("4. ", model.llf)

# 잔차이탈도
print("5. ", -2 * model.llf)

# 'booked' 변수가 3 증가할 때 오즈비
import numpy as np
print("6. ", np.exp(model.params['booked'] * 3))

# p-value가 0.05보다 작은 회귀계수의 총합
print("7. ", model.params[model.pvalues<0.05].sum()) # 상수항(절편)도 포함

# 정확도
pred = model.predict(b)
pred = (pred>0.5).astype(int)
from sklearn.metrics import accuracy_score
accuarcy = accuracy_score(b['target'], pred)
print("8. ", accuarcy)

# 오류율
error = 1 - accuarcy
# error
print("9. ", error)

"""
데이터프레임 df를 절반으로 나누어 a와 b로 분할하고, a 데이터를 사용해 모델을 만든다.
적합된 모델에서 변수를 묻는 문제라면 일반적으로 상수항(절편)은 제외하고 해석할 필요가 있다.
로그 우도는 summary() 출력창에서 Log-Likelihood 값으로 손쉽게 확인할 수 있다.

✅ 정답
1. 2
2. age
3. booked
4. -211.4323825144558
5. 422.8647650289116
6. 0.058533122917711476
7. 1.409468270586192
8. 0.765
9. 0.235
"""