# linearModel01.py

# 필요없는 경고창을 숨겨주는 코드 (※ 필요없으면 삭제!)
import warnings
warnings.filterwarnings('ignore')

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
2. 사이킷런을 활용한 로지스틱 회귀모형

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

# iris 데이터셋을 

# macro f1-score
from sklearn.metrics import f1_score
y_pred = model_lr_multi.predict(X_test)
macro_f1 = f1_score(y_test, y_pred, average = "macro")
print(macro_f1)