# practice01.py
# Part3 연습문제
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
대립가설을 기준으로 df['Caffeine(mg)']가 95보다 작아야 한다. 따라서 alternative는 less다.
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