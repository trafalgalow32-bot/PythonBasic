# ensemble05.py

"""
Part 4. 머신 러닝
1장. 지도 학습 모형
9절. 앙상블
 - 사이킷런에서 지원하는 앙상블 모형은 배깅(Bagging), 랜덤포레스트(Random Forest), 에이다부스트(AdaBoost), 
 그래디언트부스팅(Gradient Boosting) 등이 있다. 본 절에서는 해당 모형들의 모형객체를 생성하는 방법
 을 다루고자 한다.
 - 추가적으로 사이킷런에서는 지원하지 않지만 별도의 패키지에서 사용 가능한 앙상블 모형인 XGBoost와 LightGBM의 모형객체를 생성하는 방법에
 대해서도 알아보자. 

 5. XGBoost : XGBoost는 xgboost 패키지를 설치한 후 해당 사이킷런 래퍼(Wrapper) 패키지 내 클래스 XGBClassifier, XGBRegressor 등을 통해
 모형객체를 생성한다. 클래스들의 사용법은 아래와 같으며 XGBClassifier는 이진분류와 다지분류, XGBRegressor는 연속형 타겟변수에 사용된다.
 
xgboost.XGBClassifier(max_depth=6, n_estimators = 100, nthread = None, min_child_weight = 1, gamma = 0, objective = reg:squarederror)

Q. 사이킷런 패키지 내 breast_cancer 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 XGBClassifier()를 통해 
이진분류 모형객체를 생성하고 학습한 후 평가 데이터로 목푯값을 예측하고 성능을 측정하는 코드를 작성해보자.
(단, 학습과 평가 데이터의 비율은 8대 2로하고, target의 비율을 반영하고 평가지표는 AUC를 사용해 보자.)
"""

# 패키지로부터 클래스, 함수를 호출
from xgboost import XGBClassifier
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
xgb_wrap_bin = XGBClassifier(max_depth = 8,
                            n_estimators = 500,
                            nthread = 5,
                            min_child_weight = 20,
                            gamma = 0.5,
                            objective = 'binary:logistic',
                            eval_metric = 'logloss', # eval_metric = 'mlogloss'를 'logloss'로 수정하여 여기로!
                            # use_label_encoder = False, # 이건 필요없음!
                            random_state = 2022)

# 모델학습
model_xgb_wrap_bin = xgb_wrap_bin.fit(X_train, y_train, ) # eval_metric = 'mlogloss' 여기서 제거!

"""
 - breast_cancer 데이터셋을 8대 2의 비율로 학습 데이터와 평가 데이터로 분할한 후 사이킷런 래핑 xgboost 모형객체를 생성한 후 모형을 학습하였다.
 - xgboost 모형은 자동으로 라벨인코딩이 수행(use_label_encoder의 default 값이 True)되는데 현재 데이터가 라벨인코딩이 되어있는 형태이므로 False
 옵션을 추가한다.
 - (참고) 모형객체의 메소드 fit() 내 eval_metric 인자는 학습 모형에 대한 검증시 사용되는 평가 지표로, default 값은 'rmse'(연속형), 'error'(이진분류)이다.
 - (참고) objective에 따라 사용할 수 있는 함수들이 다르고 eval_metric에 사용 가능한 함수는 'rmse', 'mse', 'logloss'(negative log-likelihood),
 'error'(binary classification error rate), 'merror', 'mlogloss'(multiclass logloss), 'auc' 등이 있다.
"""

# ROC
from sklearn.metrics import roc_curve, auc
y_score = model_xgb_wrap_bin.predict_proba(X_test)[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_score)

# AUC
AUC = auc(fpr, tpr) # roc_curve()에서 반환된 fpr을 x축, tpr을 y축
print(AUC)

"""
 - AUC를 계산한 결과 0.9952으로 매우 높게 나타났다.
 - 이 결과는 무조건 높다고 해서 좋은 모형은 아니며, 분석 분야에 따라 다양한 지표들을 활용하여  분석 모형을  선택할 수 있음을 참고하자.
"""

"""
Q. 사이킷런 패키지 내 iris 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 XGBClassifier()를 통해 다지분류 모형객체를 생성하고 
학습한 후 평가 데이터로 목푯값을 예측하고 성능을 측정하는 코드를 작성해보자.
(단, 학습과 평가 데이터의 비율은 8대 2로 하고, target의 비율을 반영하고 평가지표는 macro f1-score를 사용해 보자.)
"""

# 패키지로부터 클래스, 함수를 호출
from xgboost import XGBClassifier
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
xgb_wrap_multi = XGBClassifier(max_depth = 8,
                               n_estimators = 500,
                               nthread = 5,
                               min_child_weight = 10,
                               gamma = 0.5,
                               objective = 'multi:softmax',
                               eval_metric = 'logloss', # 아래 eval_metric = 'mlogloss'을 여기로 옮기고 logloss로 수정!
                            #    use_label_encoder = False, # 쓸모 없음!
                               random_state = 2022)

# 모델학습
model_xgb_wrap_multi = xgb_wrap_multi.fit(X_train, y_train) # eval_metric = 'mlogloss' 여기서 제거!
"""
iris 데이터셋을 8대 2의 비율로 학습 데이터와 평가 데이터로 분할한 후 xgboost 모형객체를 생성한 후 모형을 학습하였다.
"""

# macro f1-score
from sklearn.metrics import f1_score
y_pred = model_xgb_wrap_multi.predict(X_test)

macro_f1 = f1_score(y_test, y_pred, average = "macro")
print(macro_f1)

"""
 - macro f1-score를 계산한 결과 0.9666으로 매우 높게 나타났다.
 - 이 결과는 무조건 높다고 해서 좋은 모형은 아니며, 분석 분야에 따라 다양한 지표들을 활용하여 분석 모형을 선택할 수 있음을 참고하자.

 xgboost.XGBRegressor(max_depth = 6, n_estimators = 100, nthread = None, min_child_weight = 1, gamma = 0
 objective = reg:squarederror) 
"""

"""
Q. 사이킷런 패키지 내 diabetes 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할하고 클래스 XGBRegressor()를 통해 연속형 예측 모형객체를 
생성하고 학습한 후 평가 데이터로 목표값을 예측하고 성능을 측정하는 코드를 작성해보자.
(단, 학습과 평가 데이터의 비율은 8대 2로 하고 평가 지표는 RMSE를 사용해보자.)
"""

# 패키지로부터 클래스, 함수를 호출
from xgboost import XGBRegressor
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
xgb_wrap_conti = XGBRegressor(max_depth = 8,
                              n_estimators = 500, 
                              nthread = 5,
                              min_child_weight = 10,
                              gamma = 0.5,
                              objective = 'reg:squarederror',
                              eval_metric = 'rmse', # 아래에 있던 eval_metric = 'rmse' 여기로 이동
                            #   use_label_encoder = False,
                              random_state = 2022)

# 모델학습
model_xgb_wrap_conti = xgb_wrap_conti.fit(X_train, y_train) # eval_metric = 'rmse' 버전 이슈로 인한 제거 후 위로 이동

"""
diabetes 데이터셋을 8대 2의 비율로 학습 데이터와 평가 데이터로 분할한 후 배깅 모형객체를 생성한 후 모형을 학습하였다.
"""

# RMSE
from sklearn.metrics import mean_squared_error
y_pred = model_xgb_wrap_conti.predict(X_test)

# rmse = mean_squared_error(y_test, y_pred, squared = False) # squared=False 쓰지마셈!
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
print(rmse)

"""
RMSE를 계산한 결과 67.9309로 나타났다.
"""