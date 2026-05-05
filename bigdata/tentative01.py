# tentative01.py

"""
part3. 통계분석
1장. 가설검정
: 추론 통계학에서는 연구자 본인의 의견을 주장하고, 이를 통계적으로 입증하기 위한 방법으로 가설 검정을 이용한다. 
가설 검정은 모집단에 대한 어떤 가설을 설정한 후 그 가설의 타당성 여부를 검정하는 것으로, 주로 모집단의 모수를 검정한다. 
본 장에서는 이러한 가설 검정을 파이썬으로 실습하는 방법에 대해 알아보도록 한다. 

1절. 상관분석  
 - 파이썬에서 두 데이터 간 상관계수를 산출하고 피어슨 상관계수(Pearson Correlation Coefficient)에 대한 가설 검정을
 수행하기 위해서는 사이파이(SciPy) 패키지의 stats 서브패키지를 호출한 후 stats에서 제공하는 pearsonr 함수를 사용한다.
 - 상관계수에 대한 귀무가설 : 두 변수 간의 상관계수는 0이다. (즉, 아무 상관관계가 없다)
 - 아래의 함수는 피어슨 상관계수를 구하는 함수로 결과는 피어슨 상관계수와 p-value를 반환한다.
 - (참고) 상관 분석을 진행하는 데이터가 정규분포를 따르지 않을 경우나 순위 데이터일 경우에는 비모수적인 방법은 스피어만
 상관계수 검정과 켄달의 타우 검정을 사용해야하고 이에 대한 방법은 '5절 비모수검정'에서 다루고자 한다.
 scipy.stats.pearsonr(x, y)

 Q. 사이킷런 패키지로부터 내장 데이터 diabetes를 데이터프레임 형태로 호출하고, 'age'와 'bmi' 두 개의 컬럼에 대하여 
 두 데이터가 상관관계가 있는지 피어슨 상관계수를 이용해 분석해보자(정규성 만족 가정)
"""

# 데이터 호출한 후 데이터프레임으로 변환
import pandas as pd
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
data = pd.DataFrame(diabetes.data, columns = diabetes.feature_names)
# print(data)

from scipy.stats import pearsonr
print(pearsonr(x = data['age'], y = data['bmi']))

"""
pearsonr() 함수의 결과는 (상관계수, p-value) 형태로 제공되며, (0.18508466614655553, 9.076791865417336e-05)로 상관계수가
0.185로 두 컬럼은 서로 상관관계가 적은 것으로 나타났다. 또한 p-value가 매우 작으므로 유의 수준 5%에서 귀무가설을 기각하기 때문에
상관계수는 작지만 유의하다는 것을 확인할 수 있다.
또한, 단순한 상관계수의 산출은 데이터프레임객체.corr()로도 가능하다.
"""

# 단순한 상관계수의 산출은 데이터프레임객체.corr()로도 가능
print("\n 단순한 상관계수의 산출은 데이터프레임객체.corr()로도 가능")
data_corr = data[['sex', 'bmi']].corr()
print(data_corr)