# stModel01.py

"""
part3. 통계분석
2장. 통계 모형
2절. 로지스틱 회귀모형
1. Statsmodels를 활용한 로지스틱 회귀분석
 - Statsmodels를 활용해 로지스틱 회귀분석을 수행하는 방법은 Logit 클래스와 GLM 클래스를 활용하는 두 가지 방법
 이 있다.
 - GLM 클래스는 로지스틱 모형보다 더 다양한 경우를 다루는 일반화선형모형을 만드는 것이기 때문에 이를 활용할 경우 주의할
 점은 family 옵션에 분포와 연결 함수를 지정할 수 있는데, 이 옵션을 알맞게 지정해야 한다는 점이다. 
 - 두 가지 방법은 GLM 클래스를 사용한 방법이 더 많은 통계결과를 지원하므로 본 수험서에서는 GLM 클래스 사용법만 다룬다.
 - statsmodels.api의 GLM 클래스를 통해 glm 모형객체를 생성한 후, 해당 객체의 메소드 fit()를 이용해 적합하고,
 메소드 summary()를 이용하면 회귀분석의 결과를 요약해서 볼 수 있다.

 statsmodels.api.GLM(endog, exog, family, ...)
 
 Q. 제공된 survived 데이터를 불러와 객실등급(pclass)을 독립변수로 하고, 생존여부(survived)를 종속변수로 하는 로지스틱
 회귀분석을 수행해보자. (객실등급은 A등급인 경우 1, B등급인 경우는 0으로 인코딩 되어 있다.) 
"""

# 필요 데이터 추출
import pandas as pd
survived = pd.read_csv('data/예제/survived.csv')
# print(survived)

# 독립변수와 종속변수 지정
X = survived['pclass'] # 독립변수
y = survived['survived'] # 종속변수

### 로지스틱 회귀 분석
import statsmodels.api as sm

# 상수항 추가
X = sm.add_constant(X)

# GLM 객체 생성 후 적합
model = sm.GLM(y, X, family= sm.families.Binomial()).fit()
print(model.summary()) # 로지스틱회귀분석 결과

"""
- summary() 함수의 결과를 통해 독립변수(pclass)가 종속변수(survived)에 미치는 영향과 각 변수의 
통계적 유의성을 확인할 수 있다. const(절편), pclass의 p-값이 모두 0에 가깝기 때문에 통계적으로 유의미하며,
객실등급이 A등급인 경우의 생존의 오즈가 B등급인 경우에 비해 exp(1.8009)=6.055배 높은 것이 확인되었다. 또한 등그별
추정 생존 확률은 각 0.239, 0.656로 B등급의 생존 확률이 더 높다.
"""

import numpy as np
print("(A등급의 추정 생존 확률, (B등급의 추정 생존 확률))")
# A등급의 추정 생존 확률
Prob_A = np.exp(-1.1558 + 0*1.8009)/(1+np.exp(-1.1558 + 0*1.8009))

# B등급의 추정 생존 확률
Prob_B = np.exp(-1.1558 + 1*1.8009)/(1+np.exp(-1.1558 + 1*1.8009))

print(Prob_A, Prob_B)
"""
- 추가로 영모형(절편만 있는 모형)의 이탈도(.null_deviance로 출력)는 719.89이고 적합모형의 이탈도
(결과의 Deviance 또는 .deviance로 출력)는 630.26인 것을 확인할 수 있는데 이 차이를 계산하면 89.62가 된다.
- 이는 자유도가 1(=적합모형의 회귀계 수의 수 - 영모형의 회귀 계수의 수 = 2 - 1)인 카이제곱 분포 하의 모형적합성
검정을 위한 검정통계랑이 된다. 이에 대한 유의확률은 0.000으로 계산되므로 모형 데이터를 잘 적합하고 있음을 알 수 있다.
"""

#### 모형 적합도 검정

# 적합모형의 이탈도
print("적합모형의 이탈도")
dev = model.deviance
print(dev)

# 영모형의 이탈도
print("영모형의 이탈도")
dev0 = model.null_deviance
print(dev0)

# 카이제곱통계량과 자유도
print("카이제곱통계량과 자유도")
stat = dev0 - dev
df = 2 - 1 # 적합모형의 회귀계수의 수 - 영모형의 회귀계수의 수
print(stat, df)

from scipy.stats import chi2
print("유의 확률")
pval = 1 - chi2.cdf(stat, df) # 유의 확률
print(pval)