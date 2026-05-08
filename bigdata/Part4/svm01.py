# svm01.py

"""
Part 4. 머신 러닝
1장. 지도 학습 모형
4절. 서포트벡터머신

Q. 사이킷런 패키지 내 breast_cancer 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 SVC()을 통해 이진분류
모형체계를 생성하고 학습한 후 평가 데이터로 목푯값을 예측하고 성능을 측정하는 코드를 작성해보자.
(단, 학습과 평가 데이터의 비율은 8대 2로하고, target의 비율을 반영하고 평가지표는 AUC를 사용해 보자.)
"""

# 패키지로부터 클래스, 함수를 호출
from sklearn.svm import SVC
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
# 메소드 .predict_proba()의 사용을 위해서 probability=True 입력 필요
svm_bin = SVC(kernel = 'linear', C = 0.5, probability = True)

# 모델학습
model_svm_bin = svm_bin.fit(X_train, y_train)

"""
breast_cancer 데이터셋을
"""

# ROC
from sklearn.metrics import roc_curve, auc
y_score = model_svm_bin.predict_proba(X_test)[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_score)

# AUC
AUC = auc(fpr, tpr) # roc_curve()에서 반환된 fpr을 x축, tpr을 y축
print(AUC)

"""
Q. 사이킷런 패키지 내 iris 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 Linear 
SVC()을 통해 다지분류 모형객체를 생성하고 학습한 후 평가 데이터로 목푯값을 예측하고 성능을 측정하는
코드를 작성해보자. 
(단, 학습과 평가 데이터의 비율은 8대 2로하고, target의 비율을 반영하고 평가지표는 
macro f1-score를 사용해보자.)
"""

# 패키지로부터 클래스, 함수를 호출
from sklearn.svm import LinearSVC
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
svm_multi = LinearSVC(C = 0.1)

# 모델학습
model_svm_multi = svm_multi.fit(X_train, y_train)

"""
iris 데이터셋을 8대 2의 비율로
"""

# macro f1-score
from sklearn.metrics import f1_score
y_pred = model_svm_multi.predict(X_test)

macro_f1 = f1_score(y_test, y_pred, average = "macro")
print(macro_f1)

"""
Q. 사이킷런 패키지 내 diabetes 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 SVR()과 
LinearSVR()을 통해 연속형 예측 모형객체를 생성하고 학습한 후 평가 데이터로 목표값을 예측하고 성능을 측정하는
코드를 작성해보자. 
(단, 학습과 평가데이터의 비율은 8대 2로 하고 평가지표는 RMSE를 사용해보자.)
"""

# 패키지로부터 클래스, 함수를 호출
from sklearn.svm import SVR, LinearSVR
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

# 모델객체 생성
svm_conti_1 = SVR(C = 0.1, epsilon = 0.01)
svm_conti_2 = LinearSVR(C = 0.1, loss = 'squared_epsilon_insensitive')

# 모델학습
model_svm_conti_1 = svm_conti_1.fit(X_train, y_train)
model_svm_conti_2 = svm_conti_2.fit(X_train, y_train)

# RMSE
from sklearn.metrics import mean_squared_error
y_pred_1 = model_svm_conti_1.predict(X_test)
rmse_1 = mean_squared_error(y_test, y_pred_1, squared = False)
print(rmse_1)

y_pred_2 = model_svm_conti_2.predict(X_test)
rmse_2 = mean_squared_error(y_test, y_pred_2, squared = False)
print(rmse_2)