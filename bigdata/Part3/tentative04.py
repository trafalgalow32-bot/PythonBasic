# tentative03.py

"""
part3. 통계분석
1장. 가설검정
: 추론 통계학에서는 연구자 본인의 의견을 주장하고, 이를 통계적으로 입증하기 위한 방법으로 가설 검정을 이용한다. 
가설 검정은 모집단에 대한 어떤 가설을 설정한 후 그 가설의 타당성 여부를 검정하는 것으로, 주로 모집단의 모수를 검정한다. 
본 장에서는 이러한 가설 검정을 파이썬으로 실습하는 방법에 대해 알아보도록 한다. 

4절. 카이제곱 검정
- 주로 범주형 자료 분석에 사용되는 카이제곱 검정은 카이제곱 분포에 근거한 통계적 검정 방법으로 본 절에서는 적합성 검정, 
동질성 검정, 독립성 검정을 파이썬에서 수행하는 방법에 대해 알아보자. 

1. 적합성 검정 : 파이썬에서 적합성 검정을 수행하기 위해서는 SciPy 패키지의 stats 서브패키지를 호출한 후 stats에서 제공
하는 chisquare 함수를 사용한다.

scipy.stats.chisquare(f_obs, f_exp, ...)

Q. A 회사에서 출시되는 제품 공정 결과의 예를 보고 색상과 관계없이 동일한 비율로 제품을 생산하는지 적합성 검정을 수행해보자.
"""

import numpy as np

print("적합성 검정")
color = ['Black', 'Gold', 'Purple', 'Red', 'White'] # 색상(분석엔 필요없음)
counts = [423, 304, 274, 205, 294] # 수량
expected = 300 # 기대도수(동일한 비율 = 1500/5)

# 적합성 검정 수행
from scipy.stats import chisquare
print(chisquare(f_obs = counts, f_exp = expected))

"""
chisquare() 함수의 결과는 (카이제곱통계량, p-value) 형태로 제공되며, (statistic=82.94, pvalue=4.14849046718008e-17)로
카이제곱 통계량이 82.94으로 매우 크게 나타났고 p-value 또한 매우 작으므로 유의수준 5%에서 귀무가설을 기각하기 때문에 색상별로
동일한 비율로 생산되지 않다고 볼 수 있다.
"""

"""
2. 동질성 검정 : 파이썬에서 동질성 검정을 수행하기 위해서는 SciPy 패키지의 stats 서브패키지를 호출한 후 stats에서 제공하는
chi2_contingency 함수를 사용한다.

scipy.stats.chi2_contingency(observed, ...)

Q. A 회사의 성별에 따른 제품 선호도 조사의 예를 보고 성별 간 선호도의 차이 검증을 위한 동질성 검정을 수행하자.
"""

print("\n 동질성 검정")
import pandas as pd
from scipy.stats import chi2_contingency

# 교차표에 맞게 데이터프레임 생성
obj = {"Good" : [400, 350],
       "Bad" : [350, 800]}
cross = pd.DataFrame(obj)

# 동질성 검정 수행
chi, p, df, expected = chi2_contingency(cross)
print(chi) # 카이제곱 통꼐량

print(p) # p-값

print(df) # 자유도

print(expected) # 기대빈도

"""
chi2_contingency() 함수는 카이제곱 통계량(Chi2 Stat), p-값(p-value), 자유도(Degrees of Freedom), 
기대 빈도(Expected Frequencies)를 반환한다. 결과로부터 p-value가 매우 작으므로 유의수준 5%에서 귀무가설
을 기각하기 때문에 성별에 따라 선호도의 비율이 다르다고 할 수 있다.
"""

"""
3. 독립성 검정: 파이썬에서 독립성 검정을 수행하기 위해서는 SciPy 패키지의 stats 서브패키지를 호출한 후 stats에서 제공하는 
chi2_contingency 함수를 사용한다.
scipy.stats.chi2_contingency(observed, ...)

Q. A 회사의 출시된 제품의 한 달 간 판매량의 예이다. 이를 통해 성별과 색상이 서로 관련이 있는지 알아보기 위해 독립성 검정을 수행해보자.
"""
print("\n 독립성 검정")

# 교차표에 맞게 데이터프레임 생성
obj = {'Black' : [1620, 2380],
       'Gold' : [385, 615],
       'Purple' : [778, 1230],
       'Red' : [394, 610],
       'White' : [800, 180]}
cross = pd.DataFrame(obj)

# 동질성 검정 수행
print("카이제곱 검정 통계량")
from scipy.stats import chi2_contingency
chi, p, df, expected = chi2_contingency(cross)
print(chi) # 카이제곱 검정 통계량
print("p-값")
print(p) # p-값
print("자유도")
print(df) # 자유도
print("기대빈도")
print(expected) # 기대빈도

"""
결과로부터 p-value가 매우 작으므로 유의수준 5%에서 귀무가설을 기각하기 때문에 두 변수는 종속적이다. 즉, 성별과 색상은 서로 관련이 있다.
"""