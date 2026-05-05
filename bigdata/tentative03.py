# tentative03.py

"""
part3. 통계분석
1장. 가설검정
: 추론 통계학에서는 연구자 본인의 의견을 주장하고, 이를 통계적으로 입증하기 위한 방법으로 가설 검정을 이용한다. 
가설 검정은 모집단에 대한 어떤 가설을 설정한 후 그 가설의 타당성 여부를 검정하는 것으로, 주로 모집단의 모수를 검정한다. 
본 장에서는 이러한 가설 검정을 파이썬으로 실습하는 방법에 대해 알아보도록 한다. 

3절. 모평균과 모분산 검정
1. 모평균 검정
 - 모평균 검정은 크게 표본의 수에 따라 단일표본, 이표본 등으로 구분된다. 여기서는 세 가지의 t-검정
 (단일표본 t-검정, 대응표본 t-검정, 독립표본 t-검정)을 파이썬으로 수행하는 방법에 대해 알아보자.

 가. 단일표본 t-검정
  - 파이썬에서 하나의 표본에 대한 t-검정을 수행하기 위해서는 SciPy패키지의 stats 서브패키지를 호출한 후 stats에서
  제공하는 ttest_1samp 함수를 사용한다.

  scipy.stats.ttest_1samp(a, popmean, alternative = 'two-sided', ...)

Q. 몸무게 데이터를 임의로 생성해보고 모집단의 평균이 70이라고 할 수 있는지 단일표본 t-검정을 수행해보자.(정규성 만족 가정)
"""

import numpy as np
print("단일 표본 t-검정")
# 몸무게 데이터 임의 생성
kg = np.array([75.5, 83.9, 75.7, 56.2, 73.4, 67.7, 79.0, 50.7, 58.4, 74.1, 65.1, 77.8, 48.1, 46.3])

# 표본 평균
kg_mean = np.mean(kg)
print(kg_mean)

# 단일 표본 t-검정 실행
from scipy.stats import ttest_1samp
kg_ttest = ttest_1samp(kg, 70)
print(kg_ttest)

"""
ttest_1samp 결과는 (t통계량값, p-value) 형태로 제공되며, (statistic=-1.0289933120202257, pvalue=0.3222484823978743)로
p-value가 0.322이므로 유의수준 5%에서 귀무가설을 기각하지 못하기 때문에 모집단의 평균은 70과 같다고 할 수 있다.
"""

"""
나. 대응표본 t-검정
 - 파이썬에서 대응표본에 대한 t-검정을 수행하기 위해서는 SciPy 패키지의 stats 서브패키지를 호출한 후, stats에서 제공하는
 ttest_rel 함수를 사용한다.
 scipy.stats.ttest_rel(a, b, alternative = 'two-sided', ...)

Q. 남녀 몸무게 데이터를 임의로 생성하고, "두 데이터가 서로 짝지어져 있다고 가정"하고, 두 데이터에 대한 모평균이 서로 다르다고 
할 수 잇는지 대응표본 t-검정을 수행해보자(정규성 만족 가정)
"""
print("\n 대응 표본 t-검정")
import pandas as pd

# 남녀 몸무게 데이터를 임의로 생성
female = np.array([50.7, 58.4, 74.1, 65.1, 77.8, 48.1, 46.3])
male = np.array([75.5, 83.9, 75.7, 56.2, 73.4, 67.7, 79.0])

# 두 데이터의 차이의 평균
diff = female - male
diff_mean = np.mean(diff)
print(diff_mean)

# 대응표본 t-검정 실행
from scipy.stats import ttest_rel
ttest_both = ttest_rel(female, male)
print(ttest_both)

"""
ttest_rel() 함수의 결과는 (t통계량, p-value) 형태로 제공되며, (statistic=-2.078446933064972, pvalue=0.08291274205610201)로
p-value가 0.083이므로 유의수준 5% 내에서 귀무 가설을 기각하지 못하기 때문에 모평균이 서로 다르다고 할 수 없다.
"""

print("\n 독립표본 t-검정")
"""
다. 독립표본 t-검정
 - 파이썬에서 독립표본에 대한 t-검정을 수행하기 위해서는 SciPy 패키지의 stats 서브패키지를 호출한 후 stats에서 제공하는
 ttest_ind 함수를 사용한다.
 scipy.stats.ttest_ind(a, b, equal_var = True, alternative = 'two-sided', ...)

Q. 위의 남녀 몸무게 데이터를 활용해 "두 데이터가 독립이라고 가정"하고, 두 데이터에 대한 모평균이 서로 다르다고 할 수 있는지
독립표본 t-검정을 수행해보자. (정규성, 등분산성 만족 가정)
"""

# 독립표본 t-검정 실행
from scipy.stats import ttest_ind
result_ttest_ind = ttest_ind(female, male)
print(result_ttest_ind)

"""
ttest_ind() 함수의 결과는 (t통계량, p-value) 형태로 제공되며, (statistic= -2.2186641577772956, pvalue=0.046550122110569664)
로 p-value가 0.046이므로 유의수준 5%에서 귀무 가설을 기각하기 때문에 모평균은 서로 다르다고 할 수 있다.
"""

"""
2. 모분산 검정
 - 모분산 검정도 모평균과 동일하게 표본의 수에 따라 구분될 수 있다. 여기서는 단일표본에 대한 모분산 검정, 이표본에 대한 분산비 검정, 
 이표본 이상에 대한 Bartlett 검정, Levene 검정을 파이썬으로 수행하는 방법에 대해 알아보자. 
 가. 단일표본 검정
  - SciPy 패키지는 하나의 표본에 대한 모분산 검정을 바로 수행하는 함수를 지원하지 않는다. 
  - 따라서 SciPy 패키지의 stats 서브패키지를 호출한 후 stats에서 제공하는 chi2 클래스를 통해 카이제곱 분포(chi2) 객체를 생성한 후,
  해당 객체의 메소드 cdf()를 이용해 유의확률(p-value)를 구한다.
  scipy.stats.chi2(df, ...)

  카이제곱분포객체.cdf(x, ...)

Q. 임의의 점수 데이터를 임의로 생성하고, 모분산이 1,100보다 작다고 할 수 있는 주장의 입증을 위한 가설검정을 수행해보자.(정규성 만족 가정)
"""

print("\n 단일표본 검정")
score = np.array([80.5, 60.2, 70, 87, 45, 91, 85])

# 검정 통계량 = (n-1) * 표본분산/귀무가설에서 설정한 모분산
var0 = 1100 # 귀무가설에서 설정한 모분산
var = np.var(score, ddof = 1 ) # 표본 분산
# print(var) # 247.9747619047619

stat = (len(score)-1)*var/var0 # 검정 통계량
# print(stat) # 1.3525896103896105

# 카이분포를 통해 직접 유의확률 계산
# 좌측 검정이므로 Pr[chisq2(자유도) < 검정통계량]으로 계산
from scipy.stats import chi2
print(chi2.cdf(stat, len(score)-1))

"""
검정결과 p-value가 0.0416이므로 유의수준 5%에서 귀무가설을 기각하기 때문에 모분산이 1,100보다 작다고 할 수 있다. 
"""

"""
나. 분산비 검정
 - 분산비 검정은 일반적으로 통계학엣허 이표본에 대한 등분산 검정을 의미하지만, SciPy 패키지는 이를 바로 수행하는 함수를 지원하지 않는다.
 - 따라서 SciPy 패키지의 stats 서브패키지를 호출한 후 stats에서 제공하는 f 클래스를 통해 F분포(f) 객체를 생성한 후, 해당 객체의 
 메소드 cdf()를 이용해 유의확률(p-value)를 구한다. 
 scipy.stats.f(dfn, dfd, ...)

 F분포객체.cdf(x, ...)

 Q. 두 집단(a, b)에 대한 점수 데이터를 임의로 생성하고 a 집단의 모분산이 b 집단의 모분산보다 작다고 할 수 있는지 
 검정해 보자. (가설은 a 모분산 < b 모분산으로 가정, 정규성 만족 가정) 
"""

print("\n 분산비 검정")
# 두 집단(a, b)에 대한 점수 데이터 임의 생성
a = np.array([70, 80, 75, 65, 100, 98])
b = np.array([20, 100, 50, 94, 28, 80, 95, 30])

# 표본 분산 계산
print("표본 분산 계산")
var_a = np.var(a, ddof = 1)
var_b = np.var(b, ddof = 1)
print(var_a, var_b)

# 검정통계량 = 집단 a의 분산 / 집단 b의 분산(가설: a 모분산 < b 모분산)
print("검정통계량")
stat = var_a / var_b
print(stat)

# 자유도 계산
print("자유도 계산")
df1, df2 = len(a)-1, len(b)-1
print(df1, df2)

# F분포를 통해 직접 유의확률 계산
# 좌측 검정이므로 Pr[F(자유도1,자유도2) < 검정통계량]으로 계산
# 좌측 검정인 이유? 가설: a 모분산 < b 모분산 <=> a 모분산 / b 모분산 < 1)
from scipy.stats import f
pval = f.cdf(stat, df1, df2)
print(pval)

"""
검정결과 p-value가 0.0415이므로 유의수준 5%에서 귀무가설을 기각하기 때문에 a 집단의 모분산이 b 집단의 모분산보다 작다고 할 수 있다. 
"""

"""
다. Bartlett 검정
 - Bartlett 검정은 이표본 이상에 대한 등분산 검정 방법 중 하나로 정규성을 충족하는 데이터에 유용하게 쓰인다.
 - 파이썬 Bartlett 검정을 수행하기 위해서는 SciPy 패키지의 stats 서브패키지를 호출한 후 stats에서 제공하는 bartlett 함수를 사용한다.

 scipy.stats.bartlett(a,b,c,...)

Q. 임의로 세 그룹의 점수 데이터를 생성한 후, 생성된 표본들 간의 등분산성 확인을 위한 Bartlett 검정을 수행해보자(정규성 만족 가정)
"""

print("\n Bartlett 검정")
# 두 집단 (a,b)에 대한 점수 데이터 임의로 생성
# 임의로 세 그룹의 점수 데이터를 생성
a = np.array([70, 80, 75, 65, 100, 98])
b = np.array([20, 100, 50, 94, 28, 80])
c = np.array([90, 97, 95, 94, 99, 100])

# Bartlett 검정 수행
from scipy.stats import bartlett
print(bartlett(a, b, c))

"""
bartlett() 함수의 결과는 (검정통계량, p-value) 형태로 제공되며, (statistic=19.367242643763486), pvalue=6.229550274334215e-05)
로 p-value가 매우 작으므로 유의수준 5%에서 귀무가설을 기각하기 때문에 그룹 간의 분산에 유의미한 차이가 있다고 할 수 있다.
"""

"""
라. Levene 검정
 - Levene 검정은 이표본 이상에 대한 등분산 검정 방법 중 하나로 정규성을 충족하지 않는 데이터에 유용하게 사용된다.
 - 파이썬에서 Levene 검정을 수행하기 위해서는 SciPy 패키지의 stats 서브패키지를 호출한 후 stats에서 제공하는 levene 함수를 사용한다.
 scipy.stats.levene(a, b, c, ...)

Q. 위에서 생성한 데이터를 활용하여, 정규성을 충족하지 않는다고 가정한 후 Levene 검정을 수행해보자.
"""

print("\n Levene 검정")
from scipy.stats import levene
print(levene(a, b, c))

"""
levene() 함수의 결과는 (검정통계량, p-value) 형태로 제공되며, (statistic=14.365736704446384, pvalue=0.0003271362104550012)
로 p-value가 매우 작으므로 유의수준 5%에서 귀무가설을 기각하기 때문에 그룹 간의 분산에 유의미한 차이가 있다고 할 수 있다.
"""

"""
3. 분산분석(ANOVA)
 - 분산분석(ANOVA) 두 집단 이상의 평균을 검정하기 위한 방법으로, 실험 설계와 반응변수나 요인의 수에 따라 다양하게 구분될 수 있다.
 본 수험서에서는 일원배치 분산분석과 반복이 없는 이원배치 분산분석만 다루고자 한다.
 - 파이썬에서 이를 수행하는 방법과 이후 사후 검정을 수행하는 방법까지 함께 알아보자. 

 가. 일원배치 분산분석
  - 일원배치 분산분석은 파이썬에서 Scipy 패키지나 statsmodels 패키지를 통해 수행할 수 있다. 
  - 그러나 사후검정이나 이원배치분산분석이 Scipy에서 지원하지 않아 여러 함수를 익히기 보다 하나의 함수를 익히고자 하므로, 
  본 수험서에서는 statsmodels 패키지를 활용한 방법만 다루고자 한다. 
  - 일반적으로 statsmodels 패키지의 formula.api 서브패키지를 불러와 ols 클래스를 통해 ols 모형 객체를 생성한 후,
  해당 객체의 메소드 fit()를 이용해 적합한다.
  - 다음으로 statsmoedels.stats.anova(statsmodels 패키지의 stats 서브 패키지 내 anova) 모듈에서
  anova_lm() 함수를 불러와 분산분석표를 출력한다.

  statsmodels.formula.api.ols(formula, data)

  statsmodels.stats.anova(args, ...)

Q. A~C 세 개 학교에서 각 1,000명씩 층화 추출한 데이터를 활용해 세 학교 간 기말고사 성적의 평균이 서로 차이가 있는지 검정하고자 한다.
(성별, 학년의 비율은 세 학교가 동일, 정규성, 등분산성 등 만족 가정)
"""

# 데이터 호출한 후 데이터프레임으로 변환
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

df = pd.read_csv('data/예제/school_score.csv')
print(df)

# one way ols 모형객체를 생성
print("\n one way ols 모형객체를 생성")
one_way = ols('Final ~ C(School)', data = df).fit()

# anova_lm 함수를 사용해 분산분석
result_anova = anova_lm(one_way)
print(result_anova)

"""
- anova_lm() 함수의 결과를 통해 df(자유도), sum_sq(합계 제곱), mean_sq(평균 제곱), F, Pr(>F) 값을 알 수 있다.
C(School)의 Pr(>F) 값이 매우 작으므로 유의수준 5%에서 귀무가설을 기각하기 때문에 세 학교 간 기말고사 성적의 평균이
서로 차이가 있다고 할 수 있다.
- 세 학교 간에 차이는 분산분석을 통해 확인할 수 있지만, 세 학교가 모두 다른 지, A, B 학교는 비슷하고
C만 다르다고 할 수 있는지 등은 확인할 수 없다. 이를 위해서는 사후검정을 수행해야 한다.
"""

"""
나. 사후검정
 - 사후검정에는 여러 검정 방법이 있지만, 본 수험서에서는 Tukey의 HSD 검정 방법만을 다루고자 한다. 파이썬에서 Tukey의 HSD
 검정은 statsmodels 내 서브패키지 stats 내 multicomp 내 pairwise_tukeyhsd() 함수를 통해 수행할 수 있다. 

statsmodels.stats.multicomp.pairwise_tukeyhsd(endog, groups, alpma)

Q. 위에서 수행된 분산분석 이후 과정인 사후 검정을 수행해보자. (튜키의 다중비교로 진행)
"""

print("\n 사후검정")
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# tukey의 다중비교 시행
tukey_result = pairwise_tukeyhsd(endog = df['Final'],
                                 groups = df['School'],
                                 alpha = 0.05)
print(tukey_result)

"""
- pairwise_tukeyhsd() 함수의 결과를 통해 두 그룹 간 쳥균 차이(meandiff)와 95%의 신뢰구간(lower,upper)을 확인할 수 있다.
- A와 B, A와 C는 신뢰구간에 0을 포함하지 않기 때문에 A와 B 학교 간, A와 C 학교 간에는 기말고사 평균은 차이가 있고
B와 C는 신뢰구간에 0을 포함하지 않으므로 B와 C학교 간 기말 고사 평균에는 차이가 없다고 해석할 수 있다.
- 신뢰구간을 보지 않더라도 reject의 결과를 통해 False인 경우 유의미한 차이가 없고, True인 경우 유의미한 차이가
있다는 해석이 가능하다.
- (참고) sandbox 내 서브패키지 stats 안의 서브패키지 multicomp(즉, 이를 디렉토리 구조로 작성하면 
statsmodels.sandbox.stats.multicomp) 내 MultiComparison() 클래스를 통해 다중비교 객체를 생성한 후,
여러 메소드들을 통해서도 다양한 사후 감정을 수행할 수 있다.
"""

"""
다. 이원배치 분산분석
 - 이원배치 분산분석은 일원배치 분산분석과 유사한 방법으로 진행하지만 formula의 입력 방법에 차이가 있다.
 - 교호작용이 있는 경우: '반응변수 ~ C(그룹1) + C(그룹2) + C(그룹1):C(그룹2)'
 - 교호작용이 없는 경우: '반응변수 ~ C(그룹1) + C(그룹2)

Q. 위에서 사용한 데이터를 활용해 학교와 성별이 기말고사 성적이 영향을 주는지 알아보기 위해 이원배치 분산분석을 수행해보자.
"""

print("\n 이원배치 분산분석")
# two way ols 모형객체를 생성(교호작용O)
two_way = ols('Final ~ C(School) + C(Grade) + C(School):C(Grade)', data = df).fit()

# anova_lm 함수를 사용해 이원배치 분산분석
result_twoway = anova_lm(two_way)
print(result_twoway)

"""
- 이원배치 분산분석에서 anova_lm() 함수의 결과를 통해 학교(School)와 학년(Grade)에 따른 기말고사 점수의 영향을 알 수 
있으며, 교호작용 효과까지 알 수 있다.
- 이원배치 분산분석에서는 상호작용항의 유의성을 먼저 고려한다. C(School) : C(Grade)의 PR(>F)로부터 p-value가 매우 크므로
상호작용 효과가 통계적으로 유의하지 않은 것을 확인할 수 있다.
- 교호작용이 유의하지 않으므로 이를 고려하지 않고 다시 분산분석을 수행한다.
"""

# two way ols 모형객체를 생성(교호작용X)
print("\n 교호작용 없는 분산분석")
two_way = ols('Final ~ C(School) + C(Grade)', data = df).fit()

# anova_lm 함수를 사용해 이원배치 분산분석
result_twoway2 = anova_lm(two_way)
print(result_twoway2)
"""
C(School)의 PR(>F)로부터 p-value가 매우 작아 학교 간 기말 고사 평균에는 차이가 있음을 확인할 수 있으며, 
C(Grade)의 PR(>F)로부터 p-value가 0.155로 0.05보다 크기 때문에 유의 수준 5%에서 학년에 따른 기말고사 평균
은 유의한 차이가 없음이 확인되었다.
"""