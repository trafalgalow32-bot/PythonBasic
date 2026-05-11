# kNeighbor01.py

"""
Part 4. 머신 러닝
1장. 지도 학습 모형
6절. K-최근접이웃 : K-최근접이웃은 서브패키지 neighbors 클래스 KNeighborsClassifier(), KNeighborsRegression() 등을 통해 모형객체를
생성할 수 있다. 클래스들의 사용법은 아래와 같으며, KNeighborsClassifier는 이진분류와 다지분류, KNeighborsRegressor은 연속형 타겟변수에
사용된다.

sklearn.neighbors.KNeighborsClassifier(n_neighbors = 5, weights = 'uniform')

Q. 사이킷런 패키지 내 breast_cancer 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 KNeighborsClassifier()을 통해 
이진분류 모형체계를 생성하고 학습한 후 평가 데이터로 목푯값을 예측하고 성능을 측정하는 코드를 작성해보자.
(단, 학습과 평가 데이터의 비율은 8대 2로하고, target의 비율을 반영하고 평가지표는 AUC를 사용해 보자.)
"""

# 패키지로부터 클래스, 함수를 호출
from sklearn.neighbors import KNeighborsClassifier
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
knn_bin = KNeighborsClassifier(n_neighbors = 5, weights = 'distance')

# 모델학습 
model_knn_bin = knn_bin.fit(X_train, y_train)

"""
breast_cancer 데이터셋을 8대 2의 비율로 학습 데이터와 평가 데이터로 분할한 후 K-최근접 이웃모형객체를 생성한 후 모형을 학습하였다.
"""

#ROC
from sklearn.metrics import roc_curve, auc
y_score = model_knn_bin.predict_proba(X_test)[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_score)

#AUC
AUC = auc(fpr, tpr) # roc_curve()에서 반환된 fpr을 x축, tpr을 y축
print(AUC)

"""
 - AUC 값은 0.9993으로 매우 높게 나타났다.
 - 이 결과는 무조건 높다고 해서 좋은 모형은 아니며, 분석 분야에 따라 다양한 지표들을 활용하여 분석 모형을 선택할 수 있음을 참고하자.
"""

"""
Q. 사이킷런 패키지 내 iris 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 KNeighborsClassifier()를 통해 다지분류 모형객체를
생성하고 학습한 후 평가 데이터로 목푯값을 예측하고 성능을 측정하는 코드를 작성해보자.
(단, 학습과 평가 데이터의 비율은 8대 2로 하고, target의 비율을 반영하고 평가지표는 macro f1-score를 사용해 보자.)
"""

# 패키지로부터 클래스, 함수를 호출
from sklearn.neighbors import KNeighborsClassifier
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
knn_multi = KNeighborsClassifier(n_neighbors = 10, weights = 'distance')

# 모델학습
model_knn_multi = knn_multi.fit(X_train, y_train)

"""
iris 데이터셋을 8대 2의 비율로 학습 데이터와 평가 데이터로 분할한 후 K-최근접이웃 모형객체를 생성한 후 모형을 학습하였다.
"""

# macro f1-score
from sklearn.metrics import f1_score
y_pred = model_knn_multi.predict(X_test)

macro_f1 = f1_score(y_test, y_pred, average = "macro")
print(macro_f1)

"""
 - macro f1-score를 계산한 결과 1.0으로 매우 높게 나타났다.
 - 이 결과는 무조건 높다고 해서 좋은 모형은 아니며, 분석 분야에 따라 다양한 지표들을 활용하여 분석 모형을 선택할 수 있음을 참고하자.

 sklearn.neighbors.KNeighborsRegressor(n_neighbors = 5, weights = 'uniform')
"""

"""
Q. 사이킷런 패키지 내 diabetes 데티어를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 KNeighborsRegressor()를 통해 연속형 예측
모형객체를 생성하고 학습한 후 평가 데이터로 목표값을 예측하고 성능을 측정하는 코드를 작성해보자.
(단, 학습과 평가 데이터의 비율은 8대 2로 하고 평가 지표는 RMSE를 사용해보자.)
"""

# 패키지로부터 클래스, 함수를 호출
from sklearn.neighbors import KNeighborsRegressor
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
knn_conti = KNeighborsRegressor(n_neighbors = 5, weights = 'distance')

# 모델학습
model_knn_conti = knn_conti.fit(X_train, y_train)

"""
diabetes 데이터셋을 8대 2의 비율로 학습 데이터와 평가 데이터로 분할한 후 K-최근접이웃 모형 객체를 생성한 후 모형을 학습하였다.
"""

# RMSE
from sklearn.metrics import mean_squared_error
y_pred = model_knn_conti.predict(X_test)

# rmse = mean_squared_error(y_test, y_pred, squared = False) # squared=False 쓰지마셈!
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
print(rmse)

"""
RMSE를 계산한 결과 64.3410으로 나타났다.
"""