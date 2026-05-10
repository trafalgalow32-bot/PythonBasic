# linearModel01.py

# 필요없는 경고창을 숨겨주는 코드 (※ 필요없으면 삭제!)
import warnings
warnings.filterwarnings('ignore')

"""
Part 4. 머신 러닝
1장. 지도 학습 모형
3절. 선형 모델
1. 사이킷런을 활용한 다중 선형 회귀 분석
가. 다중 선형 회귀 모형 : 사이킷런을 활용한 방법의 경우 먼저, 클래스 sklearn.linear_model.LinearRegression()를 통해 
선형회귀(Linearregression) 객체를 생성한 후, 해당 객체의 메소드 fit()을 이용해 회귀모형을 적합한다.

선형회귀객체.fit(X, y, ...)

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

"""
print(model.coef), print(model.intercept_)을 통해 회귀계수를 확인해 본 결과, 추정된 회귀식은 
[target = 152.13 + 608.94 * bmi + 301.13 * bp + 990.87 * s1 -938.97 * s2 -597.46 * s3]
"""

# 결정계수
print(model.score(X = X, y = y))

"""
- 결정계수는 0.4772이므로 회구모형이 전체 데이터의 약 47.72%를 설명할 수 있다. 결정계수 값이 조금 낮게 나타났기 때문에 해당
회구추정식이 데이터를 적절하게 설명하고 있다고는 할 수 없다.
- 사이킷런의 회귀분석 방법은 모형의 통계적 유의성이나 회귀계수의 유의성을 바로 제공하지 않는다. 따라서 유의성 확인을 위해선느 그 결과
를 바로 제공하는 statsmodels 패키지를 사용하는 것이 편리하다.
"""

"""
나. 릿지(Ridge) : 릿지 회귀모형은 사이킷런 패키지를 활용해 클래스 sklearn.linear_model.Ridge()를 통해 릿지회귀객체를 생성한 후,
해당 객체의 메소드 fit()을 이용해 회귀모형을 적합한다. (릿지 회귀는 능형 회귀라고도 함)

릿지회귀객체.fit(X, y, ...)

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
print(model.coef_), print(model.intercept_)을 통해 회귀계수를 확인해 본 결과, 추정된 회귀식은 
[target = 152.13 + 595.99 * bmi + 339.09 + bp + 397.34 * s1 - 339.00 * s2 - 406.35 * s3]이다.
"""

"""
다. 라쏘(LASSO) : 라쏘 회귀모형은 사아킷런 패키지를 활용해 클래스 sklearn.linear_model.Lasso()를 통해 라쏘 회귀객체를 생성한 후,
해당 객체의 메소드 fit()을 이용해 회귀 모형을 적합한다.

sklearn.linear_model.Lasso(alpha = 1.0, fit_intercept = True, ...)

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
 - print(model.coef_), print(model.intercept_)을 통해 회귀계수를 확인해 본 결과, 추정된 회귀식은
 [target = 152.13 + 574.04 * bmi + 237.23 * bp - 165.17 * s3]이다.
 - 이를 통해 라쏘 회귀모형은 중요한 변수를 선택하는 역할을 수행할 수 있음을 확인할 수 있다.
"""

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

# 데이터 분할
colnm = ['bmi','bp','s1','s2','s3'] # 컬럼명 리스트
X_train = df[colnm].loc[:310] # 0~309번 행과 'bmi','bp','s1','s2','s3' 컬럼
X_test = df[colnm].loc[310:] # 310~441번 행 'bmi','bp','s1','s2','s3' 컬럼
y_train = df['target'].loc[:310] # 0~309번 행과 'target' 컬럼

# 라쏘회귀객체 생성
model = Lasso(alpha = 0.5)
model.fit(X = X_train, y = y_train) # X_train과 t_train으로 라쏘 회구모형 적합

# X_test를 통해 새로운 'target' 변수를 예측
target = model.predict(X_test)
target = pd.Series(target, name = 'target') # array -> series
print(target)

"""
 - print(model.coef_), print(model.intercept_)을 통해 train 데이터셋만으로 회귀계수를 적합한 결과, 추정된 회귀식은
 [target = 151.20 + 604.06 * bmi + 205.38 * bp - 144.63 * s3]이다.
 - target을 추정하는 데 중요한 변수는 bmi, bp, s3로 나타남을 확인할 수 있다. 이 결과는 라쏘 객체 생성 시 alpha 값에 따라 달라지며,
 alpha 값이 0에 가까울수록 가장 많은 변수를 가지는 회귀모형이 되며, 무한대에 가까울수록 절편항만을 포함하는 가장 간단한 회귀모형이 된다.
 - 따라서 적절한 alpha 값을 그리드 서치(Grid Search) 방법이나 k-겹 교차검증(k-fold CV) 통계량을 통해 찾아야 한다. 그러나 현재 시험
 환경은 실행 시간에 제약을 두기 때문에 본 수험서에서는 해당 과정을 제외하고자 한다.
"""

"""
2. 사이킷런을 활용한 로지스틱 회귀모형
 - 로지스틱 회귀모형은 서브패키지 linear_model 내 클래스 LogisticRegression()을 통해 모형 객체를 생성할 수 있다.
 클래스 사용법은 다음과 같다.
 - (참) 선형 회귀모델과 달리 로지스틱 회구모형은 클래스 LogisticRegression()가 릿지와 라쏘를 함께 지원하낟.

 sklearn.linear_model.LogitsticRegression(penalty = '12', C= 1.0, multi_class = 'auto', max_iter = 100, ...)


Q. 사이킷런 패키지 내 breast_cancer 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 
LogisticRegression()을 통해 이진분류 모형객체를 생성하고 학습한 후 평가 데이터로 목푯값을 예측하고
성능을 측정하는 코드를 작성해보자.
(단, 학습과 평가 데이터의 비율은 8대 2로 하고, target의 비율을 반영하고 평가지표 AUC를 사용해보자.)
"""
print("\n 사이킷런을 활용한 로지스틱 회귀모형")

# 패키지로부터 클래스, 함수를 호출
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# breast_cancer 데이터셋 호출
from sklearn.datasets import load_breast_cancer
breast_cancer = load_breast_cancer()
data = breast_cancer.data
target = breast_cancer.target

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(data,
                                                    target,
                                                    test_size = 0.2,
                                                    random_state = 2205,
                                                    stratify = target)

# 모형객체 생성
lr_bin = LogisticRegression(C = 0.5, # 규제 강도
                            max_iter = 2000) # 수렴까지 걸리는 최대 반복 횟수

# 모델학습
model_lr_bin = lr_bin.fit(X_train, y_train)

"""
breast_cancer 데이터셋을
"""

# ROC
from sklearn.metrics import roc_curve, auc
y_score = model_lr_bin.predict_proba(X_test)[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_score)

# AUC
AUC = auc(fpr, tpr) # roc_curve()에서 반환된 fpr을 x축, tpr을 y축
print(AUC)

"""
 - AUC를 계산하기 위해 먼저, ROC Curve를 생성하였다. 이때, 함수 roc_curve()의 인자 y_score는 모형에서 예측된 결과가
 확률의 형태를 입력 받아야하므로 모형객체의 메소드 predict_proba()를 이용하였다.
 - predict_proba(X_test)의 결과는 2차원 배열 ㅎ여태를 반환하며, 첫 번째 열은 0이 될 확률, 두 번째 열은 1이 될 확률을 
 반환한다. 따라서 두 번째 열을 선택하기 위해 [:,1]을 통하여 인덱싱한다.
 - 마지막으로 roc_curve()에서 반환되는 결과 중 fpr과 tpr을 각각 x, y축으로 함수 auc()의 인자로 사용한다. 그 결과
 AUC 값은 0.9983으로 매우 높게 나타났다.
 - 이 결과는 무조건 높다고 해서 좋은 모형은 아니며, 분석 분야에 따라 다양한 지표들을 활용하여 분석 모형을 선택할 수 있음을 참고하자.
"""

"""
Q. 사이킷런 패키지 내 iris 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 
LogisticRegression()을 통해 다지분류 모형객체를 생성하고 학습한 후 평가 데이터로 목푯값을 예측하고
성능을 측정하는 코드를 작성해보자. 
(단, 학습과 평가 데이터의 비율은 8대 2로 하고, target의 비율을 반영하고 평가지표는 macro f1-score를
사용해보자.)
"""
# 패키지로부터 클래스, 함수를 호출
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# iris 데이터셋 호출
from sklearn.datasets import load_iris
iris = load_iris()
data = iris.data
target = iris.target

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(data,
                                                    target,
                                                    test_size = 0.2,
                                                    random_state = 2205,
                                                    stratify = target)

# 모형객체 생성
lr_multi = LogisticRegression(C = 0.05, #규제 강도
                              max_iter = 200) # 수렴까지 걸리는 최대 반복 횟수

# 모델 학습
model_lr_multi = lr_multi.fit(X_train, y_train)

# iris 데이터셋을 8대 2의 비율로 학습 데이터와 평가 데이터로 분할한 후 로지스틱 모형객체를 생성한 후 메소드 fit()을 통하여 적합하고
# 모형을 학습하였다.

# macro f1-score
from sklearn.metrics import f1_score
y_pred = model_lr_multi.predict(X_test)
macro_f1 = f1_score(y_test, y_pred, average = "macro")
print(macro_f1)

"""
 - macro f1-score를 계산하기 위한 함수인 f1_score()의 y_pred의 인자에 입력될 예측값을 구하기 위해 모형객체의 메소드 predict를
 이용하였다.
 - 파이썬에서 macro f1-score를 계산하는 방법은 average = "macro"의 옵션을 추가함으로써 수행이 가능하다. macro f1-score를 계산한
 결과 0.9666으로 매우 높게 나타났다.
 - 이 결과는 무조건 높다고 해서 좋은 모형은 아니며, 분석 분야에 따라 다양한 지표들을 활용하여 분석 모형을 선택할 수 있음을 참고하자.
"""