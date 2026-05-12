# ensemble01.py

"""
Part 4. 머신 러닝
1장. 지도 학습 모형
9절. 앙상블
 - 사이킷런에서 지원하는 앙상블 모형은 배깅(Bagging), 랜덤포레스트(Random Forest), 에이다부스트(AdaBoost), 
 그래디언트부스팅(Gradient Boosting) 등이 있다. 본 절에서는 해당 모형들의 모형객체를 생성하는 방법
 을 다루고자 한다.
 - 추가적으로 사이킷런에서는 지원하지 않지만 별도의 패키지에서 사용 가능한 앙상블 모형인 XGBoost와 LightGBM의 모형객체를 생성하는 방법에
 대해서도 알아보자. 

 1. 배깅 : 배깅은 사이킷런의 서브패키지 ensemble 내 클래스 BaggingClassifier(), BaggingRegressor() 등을 통해 모형객체를 생성할 수 있다.
 클래스들의 사용법은 아래와 같으며, BaggingClassifier는 이진분류와 다지분류, BaggingRegressor는 연속형 타겟변수에 사용된다.

sklearn.ensemble.BaggingClassifier(best_estimator = None, n_estimators = 10, max_samples = 1.0, max_feature = 1.0, ...)

Q. 사이킷런 패키지 내 breast_cancer 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 BaggingClassifier()를 통해 
이진분류 모형객체를 생성하고 학습한 후 평가 데이터로 목푯값을 예측하고 성능을 측정하는 코드를 작성해보자.
(단, 학습과 평가 데이터의 비율은 8대 2로하고, target의 비율을 반영하고 평가지표는 AUC를 사용해 보자.)
"""

# 패키지로부터 클래스, 함수를 호출
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
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
dtr = DecisionTreeClassifier(max_depth = 3, min_samples_leaf = 10)
bag_bin = BaggingClassifier(estimator = dtr, # base_estimator 버젼 업 이후엔 안씀!
                            n_estimators = 500,
                            random_state =2022)

# 모델학습
model_bag_bin = bag_bin.fit(X_train, y_train)

"""
- breast_cancer 데이터셋을 8대 2의 비율로 학습 데이터와 평가 데이터로 분할한 후 배깅 모형객체를 생성한 후 모형을 학습하였다.
"""

# ROC
from sklearn.metrics import roc_curve, auc
y_score = model_bag_bin.predict_proba(X_test)[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_score)

# AUC
AUC = auc(fpr, tpr) # roc_curve()에서 반환된 fpr을 x축, tpr을 y축
print(AUC)

"""
 - AUC를 계산한 결과 0.9974로 매우 높게 나타났다.
 - 이 결과는 무조건 높다고 해서 좋은 모형은 아니며, 분석 분야에 따라 다양한 지표들을 활용하여  분석 모형을  선택할 수 
 있음을 참고하자.
"""

"""
Q. 사이킷런 패키지 내 iris 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 BaggingClassifier()를 통해
다지분류 모형객체를 생성하고 학습한 후 평가 데이터로 목푯값을 예측하고 성능을 측정하는 코드를 작성해보자.
(단, 학습과 평가 데이터의 비율은 8대 2로 하고, target의 비율을 반영하고 평가지표는 macro f1-score를 사용해 보자.)
"""

# 패키지로부터 클래스, 함수를 호출
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
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
dtr = DecisionTreeClassifier(max_depth = 3, min_samples_leaf = 10)

bag_multi = BaggingClassifier(estimator = dtr, # base_estimator
                              n_estimators = 500,
                              random_state = 2022)

# 모델학습
model_bag_multi = bag_multi.fit(X_train, y_train)
"""
iris 데이터셋을 8대 2의 비율로 학습 데이터와 평가 데이터로 분할한 후 배깅 모형객체를 생성한 후 모형을 학습하였다.
"""

# macro f1-score
from sklearn.metrics import f1_score

"""
 - macro f1-score를 계산한 결과 0.9666으로 매우 높게 나타났다.
 - 이 결과는 무조건 높다고 해서 좋은 모형은 아니며, 분석 분야에 따라 다양한 지표들을 활용하여  분석 모형을  선택할 수 
 있음을 참고하자.

 sklearn.ensemble.BaggingRegressor(best_estimator = None, n_estimators = 10, max_samples = 1.0, max_feature = 1.0, ...)
"""

"""
Q. 사이킷런 패키지 내 diabetes 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 BaggingRegressor()를 통해 연속형 예측 모형객체를 
생성하고 학습한 후 평가 데이터로 목표값을 예측하고 성능을 측정하는 코드를 작성해보자.
(단, 학습과 평가 데이터의 비율은 8대 2로 하고 평가 지표는 RMSE를 사용해보자.)
"""

# 패키지로부터 클래스, 함수를 호출
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import train_test_split

# diabetes 데이터셋 호출
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
data = diabetes.data
target = diabetes.target

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(data,
                                                    target,
                                                    test_size = 0.2,
                                                    random_state = 2205)

# 모형객체 생성
dtr = DecisionTreeRegressor(max_depth = 3, min_samples_leaf = 10)
bag_conti = BaggingRegressor(estimator = dtr, #base_estimator 안 씀!
                             n_estimators = 500,
                             random_state = 2022)

# 모델학습
model_bag_conti = bag_conti.fit(X_train, y_train)

"""
diabetes 데이터셋을 8대 2의 비율로 학습 데이터와 평가 데이터로 분할한 후 배깅 모형객체를 생성한 후 모형을 학습하였다.
"""

# RMSE
from sklearn.metrics import mean_squared_error
y_pred = model_bag_conti.predict(X_test)

# rmse = mean_squared_error(y_test, y_pred, squared = False) # squared=False 쓰지마셈!
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
print(rmse)