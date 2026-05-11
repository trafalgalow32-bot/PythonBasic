# neural01.py

"""
Part 4. 머신 러닝
1장. 지도 학습 모형
7절. 인공신경망 : 인공신경망은 서브패키지 neural_network 내 클래스 MLPClassifier(), MLPRegressor() 등을 통해 모형객체를 생성할 수 있다.
클래스들의 사용법은 아래와 같으며, MLPClassifier는 이진분류와 다지분류, MLPRegressor는 연속형 타겟변수에 사용된다.

sklearn.neural_network.MLPClassifier(hidden_layer_sizes = (100, ),
        activation = 'relu', solver = 'adam', alpha = 0.0001,
    betch_size = 'auto', learning_rate_init = 0.001, max_iter = 200, ...)


Q. 사이킷런 패키지 내 breast_cancer 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 MLPClassifier()를 통해 이진분류 모형객체
를 생성하고 학습한 후 평가 데이터로 목표값을 예측하고 성능을 측정하는 코드를 작성해보자. (단, 학습과 펴악 데이터의 비율은 8대 2로 하고, 
target의 비율을 반영하고 평가지표는 AUC를 사용해보자.)
"""

# 패키지로부터 클래스, 함수를 호출
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

# breast_cancer 데이터셋 호출
from sklearn.datasets import load_breast_cancer
breast_cancer = load_breast_cancer()
data = breast_cancer.data
target = breast_cancer.target

# 데이터 분할
X_train, X_test, y_train ,y_test = train_test_split(data,
                                                    target,
                                                    test_size = 0.2,
                                                    random_state = 2205,
                                                    stratify = target)

# 모형객체 생성
ann_bin = MLPClassifier(alpha = 0.5,
                        max_iter = 500,
                        random_state = 2022)

# 모델학습
model_ann_bin = ann_bin.fit(X_train, y_train)

"""
breast_cancer 데이터셋을 8대 2의 비율로 학습 데이터와 평가 데이터로 분할한 후 MLP 모형 객체를 생성한 후 모형을 학습하였다.
"""

# ROC
from sklearn.metrics import roc_curve, auc
y_score = model_ann_bin.predict_proba(X_test)[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_score)

# AUC
AUC = auc(fpr, tpr) # roc_curve()에서 반환된 fpr을 x축, tpr을 y축
print(AUC)

"""
 - AUC를 계산한 결과 0.9997로 매우 높게 나타났다.
 - 이 결과는 무조건 높다고 해서 좋은 모형은 아니며, 분석 분야에 따라 다양한 지표들을 활용하여 분석 모형을 선택할 수 있음을 참고하자.
"""

"""
Q. 사이킷런 패키지 내 iris 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 MLPClassifier()을 통해
다지분류 모형객체를 생성하고 학습한 후 평가 데이터로 목푯값을 예측하고 성능을 측정하는 코드를 작성해 보자.
(단, 학습과 평가 데이터의 비율은 8대 2로 하고, target의 비율을 반영하고 평가지표는 macro f1-score를 사용해보자.)
"""

# 패키지로부터 클래스, 함수를 호출
from sklearn.neural_network import MLPClassifier
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
ann_multi = MLPClassifier(random_state = 2022, max_iter = 600)

# 모델학습
model_ann_multi = ann_multi.fit(X_train, y_train)

"""
iris 데이터셋을 8대 2의 비율로 학습 데이터와 평가 데이터로 분할한 후 MLP 모형객체를 생성한 후 모형을 학습하였다.
"""

# macro f1-score
from sklearn.metrics import f1_score
y_pred = model_ann_multi.predict(X_test)

macro_f1 = f1_score(y_test, y_pred, average = "macro")
print(macro_f1)

"""
 - macro f1-score를 계산한 결과 1.0로 매우 높게 나타났다.
 - 이 결과는 무조건 높다고 해서 좋은 모형은 아니며, 분석 분야에 따라 다양한 지표들을 활용하여 분석 모형을 선택할 수 있음을 참고하자.

 sklearn.neural_network.MLPRegressor(hidden_laer_sizes = (100, ),
 activation = 'relu', solver = 'adam', alpha = 0.0001,
 batch_size = 'auto', learning_rate_init = 0.001, max_iter = 200, ...)
"""

"""
Q. 사이킷런 패키지 내 diabetes 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 MLPClassifier()를 통해 연속형 예측 모형객체를
생성하고 학습한 후 평가 데이터로 목푯값을 예측하고 성능을 측정하는 코드를 작성해보자.
(단, 학습과 평가 데이터의 비율은 8대 2로 하고 평가 지표는 RMSE를 사용해보자.)
"""

# 패키지로부터 클래스, 함수를 호출
from sklearn.neural_network import MLPRegressor
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
ann_conti = MLPRegressor(alpha = 0.5, 
                         max_iter = 10000,
                         random_state = 2022)

# 모델학습
model_ann_conti = ann_conti.fit(X_train, y_train)

""" 
diabetes 데이터셋을 8대 2의 비율로 학습 데이터와 평가 데이터로 분할한 후 MLP 모형객체를 생성한 후 모형을 학습하였다.
"""

# RMSE
from sklearn.metrics import mean_squared_error
y_pred = model_ann_conti.predict(X_test)
# rmse = mean_quared_error(y_test, y_pred, squared = False)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
print(rmse)

"""
RMSE를 계산한 결과 60.2169로 나타났다.
"""