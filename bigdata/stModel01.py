# stModel01.py

"""
part3. 통계분석
2장. 통계 모형
1절. 선형 회귀 모형
 - 파이썬에서 선형 회귀분석을 수행하는 패키지는 세 가지이다. 
 - 첫 번째는 statsmodels의 서브패키지인 api 내의 OLS 함수를 사용하는 방법이다. statsmodels이
 통계 분석을 위한 패키지인 만큼 가장 많은 통계 분석 결과를 동시에 제공한다.
 - 두 번째는 SciPy의 서브패키지인 stats 내의 linregress 함수를 이용하는 방법이다. 이는 일부 통계분석
 결과를 제공한다.
 - 마지막은 scikitlearn의 linear_model에서 LinearRegression 클래스를 이용하는 방법으로 머신러닝을 위한
 패키지인 만큼 예측 결과를 산출하고 성능을 평가, 향상하는 데 용이하다.
 - 본 절에서는 SciPy와 statsmodels를 활용한 방법에 대해 알아보고, scikitlearn 활용법은 Part 4에서 알아본다.

 1. SciPy를 활용한 단순 선형 회귀 분석 : SciPy를 활용해 단순 선형회귀 모형객체를 생성하는 방법은 아래와 같다.
 
 scipy.stats.linregress(x, y)

 Q. 위에서 호출한 diabetes 데이터에서 'bmi' 컬럼을 독립변수로 설정하고, 'target' 변수를 종속변수로 설정하여
 선형 회귀분석을 실시해 보자. 
"""
print("SciPy를 활용한 단순 선형 회귀 분석")
import pandas as pd
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
data = pd.DataFrame(diabetes.data, columns = diabetes.feature_names)

# 'target' 컬럼 호출
target = diabetes.target

# 단순 선형회귀 모델 생성(scipy.stats.linregress())
from scipy.stats import linregress
model = linregress(x = data['bmi'], y = target)
print(model)
"""
- 전체 결과에서 slope는 독립변수에 대한 추정된 회귀계수, intercept는 상수항을 나타내며, rvalue는 모형의
설명력, pvalue는 기울기에 대한 통계적 유의성, stderr와 intercept_stderr는 회귀계수들에 대한 
표준오차를 의미한다. 
"""
# 독립변수에 대한 추정된 회귀계수(beta1)
print("독립변수에 대한 추정된 회귀계수(beta1)")
print(model.slope)
# 상수항에 대한 추정된 회귀계수(beta0)
print("상수항에 대한 추정된 회귀계수(beta0)")
print(model.intercept)
"""
- 회귀분석 결과를 기준으로 target과 bmi 사이에는 [target = 152.13 + 949.44 * sex]라는 회귀식을
도출할 수 있다.
"""
# beta1에 대한 통계적 유의성(p-value)
print("beta1에 대한 통계적 유의성(p-value)")
print(model.pvalue)
# 결정계수(모형의 설명력)
print("결정계수")
print(model.rvalue)
"""
- 독립변수의 회귀계수에 대한 p-value가 매우 작기 때문에 통계적으로 유의하다고 판단할 수 있다. 이 검정에
사용되는 귀무가설은 '회귀계수는 0이다'이며, 대립가설은 '회귀계수는 0이 아니다'이다.
- 해당 회귀모형이 현 데이터의 약 58.65%를 설명할 수 있다는 것을 의미한다.
- 상수항에 대한 통계적 유의성이나 모형의 통계적 유의성의 결과는 별도 제공하지 않아 따로 산출해야하지만 단순
선형회귀 분석에서 모델의 통계적 유의성의 결과는 독립변수의 회귀계수에 대한 유의성과 같고 상수항의 유의성은
보통 고려되지 않는다. 
- 이를 구하는 방법은 통계학 이론을 통해 직접 코드를 작성하여 구할 수 있지만, 본 수험서에서는 제외한다. 
"""

"""
2. Statsmodels를 활용한 다중 선형 회귀 분석
가. 회귀 모형 적합
 - Statsmodels를 활용해 다중 선형회귀 분석을 수행하는 방법은 회귀 모형객체를 생성한 후, 해당 객체의 메소드 
 fit()를 이용해 적합하는 방식인데, 이 과정에서 formula를 활용하는 방법과 X, y를 각각 입력하는 방법으로
 구분된다.
 - 본 수험서에서는 두 가지 방법 중 후자에 대해서만 다룬다.
 - statsmodels.api의 OLS 클래스를 통해 OLS 모형객체를 생성한 후, 해당 객체의 메소드 fit()를 이용해 적합하고,
 메소드 summary()를 이용하면 회귀분석의 결과를 요약해서 볼 수 있다.

 statsmodels.ap.OLS(endog, exog, ...)

 Q. 제공된 tips 데이터를 불러와 총액(total_bill)과 사람 수(size)를 독립변수로 하고, 팁(tip)을
 종속변수로 하는 다중 선형 회귀분석을 수행해보자.
"""

# 필요 데이터 추출
import pandas as pd
tips = pd.read_csv('data/예제/tips.csv')
print("\n 회귀 모형 적합")
# print(tips)

import statsmodels.api as sm

# 독립변수(total_bill, size)와 종속변수 지정
X = tips[['total_bill', 'size']] # 독립 변수
y = tips['tip'] # 종속 변수

# 상수항 추가
X = sm.add_constant(X)

# 다중 선형 회귀분석 수행, OLS 객체 생성 후 적합
model = sm.OLS(y, X).fit()
print(model.summary()) # 회귀분석 결과

"""
- summary() 결과를 통해 독립변수(total_bill, size)들이 종속변수(tip)에 미치는 영향과 각 변수의
통계적 유의성을 확인할 수 있다. const(절편), total_bill, size의 p-value가 모두 0.05보다 작기 때문에
tip의 크기에 영향을 미치는 것을 확인할 수 있으며(P>|t|로 확인 가능), F-Statistic이 105.9로 크고 Prob(F-Statistic)
값이 0에 가깝기 때문에 모델이 전반적으로 매우 유의미하다는 것을 확인할 수 있다.

나. 반응 변수의 기댓값 추정 : 적합된 결과에 메소드 predict()를 사용하면 반응 변수의 기댓값에 대한 점추정 값을 계산할
수 있게 된다. 이 때 적합에 사용했던 독립변수들의 배열을 입력 값으로 지정한다.

Q. 위에서 적합한 회귀모형을 활용하여, 5번째 관측치에 대한 tip의 기댓값을 추정해보자.
"""
print("\n 반응 변수의 기댓값 추정")
# 5번째 관측치에 대한 tip의 기댓값을 추정
X.iloc[4]

# 5번째 관측치에 대한 tip의 기댓값을 추정
print(model.predict(X.iloc[4]))
"""
- 5번째 관측치에 대한 tip의 기댓값을 추정한 결과, 3.719로 추정되었다.
"""

"""
다. 반응 변수의 기댓값 예측
 - 예측 방법은 적합된 결과에 메소드 predict()를 사용하는 것은 동일하나 적합에 사용했던 독립 변수
 가 아닌 새로운 독립변수의 배열을 입력 값으로 지정하는 것이 차이점이다.
 - 추가로 get_prediction()에 새로운 데이터에 입력하게 되면, 구간까지도 계산이 가능하며, 계산된 값
 에 summary_frame()를 활용하면 이 결과를 데이터프레임의 형태로 볼 수 있게 된다.

Q. 위에서 적합한 회귀모형을 활용하여, total_bill이 24.59이고 size가 4인 경우의 tips의 기댓값을 예측해보자.
"""

print("\n 반응 변수의 기댓값 예측")
# 새로운 독립변수의 배열을 값으로 지정
new_data = pd.DataFrame({'const': [1], 'total_bill': [24.59], 'size': [4]})

# 예측 기댓값 결과 얻기
result_new_data = model.get_prediction(new_data)

# 요약 프레임으로 결과 보기
print(result_new_data.summary_frame())

"""
- predict() 함수 결과를 통해 time과 smoker, size에 기반한 tip 값은 3.29로 예측되는 
total_bill이 24.59이고 size가 4인 경우의 tips의 기댓값은 3.719로 예측되었으며, 95%에서 예측 구간
[3.480, 3.957]을 가지는 것을 확인하였다.
"""