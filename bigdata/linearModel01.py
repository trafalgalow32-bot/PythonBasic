# linearModel01.py

"""
Part 4. 머신 러닝
1장. 지도 학습 모형
3절. 선형 모델
1. 사이킷런을 활용한 다중 선형 회귀 분석
가. 다중 선형 회귀 모형

Q. 위에서 호출한 diabetes 데이터에서 'bmi','bp','s1','s2','s3' 컬럼을 독립변수로 설정하고, 'target' 변수를 종속변수로 설젛아여 선형 휘귀 분석을 
실시해 보자. 
"""
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
diabetes = load_diabetes()
data = pd.DataFrame(diabetes.data, columns = diabetes.feature_names)

# 'target' 컬럼 호출
target = diabetes.target

print("\n 선형회귀")

colnm = ['bmi','bp','s1','s2','s3'] # 컬럼명 리스트
X = data[colnm]
y = target

# 선형회귀 객체 생성
model = LinearRegression()

# 선형회귀 적합
model.fit(X = X, y = y)

# 독립변수들에 대한 추정 회귀 계수들
print(model.coef_)

# 절편항에 대한 추정 회귀 계수
print(model.intercept_)

# 결정계수
print(model.score(X = X, y = y))

"""
나. 릿지(Ridge)

Q. 위에서 호출한 diabetes 데이터에서 'bmi','bp','s1','s2','s3' 컬럼을 독립변수로 설정하고, 'target' 변수를 종속변수로 설정하여 
릿지 회귀분석을 실시해보자.
"""
print("\n 릿지(Ridge)")
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Ridge
diabetes = load_diabetes()
data = pd.DataFrame(diabetes.data, columns = diabetes.feature_names)

# 'target' 컬럼 호출
target = diabetes.target

colnm = ['bmi','bp','s1','s2','s3']
X = data[colnm]
y = target

# 릿지회귀객체 생성
model = Ridge(alpha = 0.1)

# 적합
model.fit(X = X, y = y)

# 독립변수들에 대한 추정 회귀 계수들
print(model.intercept_)
print(model.coef_)

"""
다. 라쏘(LASSO)

Q. 위에서 호출한 diabetes 데이터에서 'bmi','bp','s1','s2','s3' 컬럼을 독립변수로 설정하고, 'target' 변수를 종속변수로 설정하여
라쏘 회귀 분석을 실시해보자.
"""
print("\n 라쏘(LASSO)")
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Lasso
diabetes = load_diabetes()
data = pd.DataFrame(diabetes.data, columns = diabetes.feature_names)

# 'target' 컬럼 호출
target = diabetes.target

colnm = ['bmi','bp','s1','s2','s3']
X = data[colnm]
y = target

# 라쏘회귀객체 생성
model = Lasso(alpha = 0.5)

# 적합
model.fit(X = X, y = y)

# 독립변수들에 대한 추정 회귀 계수들
print(model.intercept_)
print(model.coef_)

"""
Q. 위에서 호출한 diabetes 데이터를 0~309번 행을 train, 310~441번 행을 test로 각각 데이터 프레임을 추출한 후, train과 test에서 
'bmi','bp','s1','s2','s3' 컬럼을 독립변수로 설정하여 각각 X_train과 X_test로 저장하고, train에서 'target' 컬럼을 종속변수로 설정하여 
y_train으로 저장하자. 다음으로 X_train과 y_train으로 라쏘 회귀모형을 적합한 후 X_test를 통해 새로운 'target' 변수를 예측해 보자.
(라쏘 L1 규제의 상수항은 0.5로 지정할 것)
"""

# 패키지 및 데이터셋, 클래스 호출
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Lasso

# diabetes 데이터셋 호출 후 데이터프레임으로 변환
diabetes = load_diabetes()
data = pd.DataFrame(diabetes.data, columns = diabetes.feature_names)
target = pd.Series(diabetes.target, name = 'target')
df = pd.concat([data, target], axis = 1) # 데이터 프레임과 시리즈를 열 결합