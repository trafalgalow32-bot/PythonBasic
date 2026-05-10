# dataSplit01.py

"""
Part 4. 머신 러닝
1장. 지도 학습 모형
 - 사이킷런 패키지는 기계학습을 위한 패키지인만큼 많은 종류의 모형을 통일된 형식으로 사용할 수 있도록 구성되어 있다.
 - 사이킷런 패키지에서 사용할 수 있는 지도 학습 모형의 종류는 아래의 그림과 같이 정리할 수 있으며(그림은 생략! 혹은 나중에 별도 기술
 을 동원하여 본 페이지에 삽입!), 이들은 sklearn.서비패키지명.클래스명을 통해 모형객체를 생성한 후, 모형객체의 메소드 fit()을 통해
 모델을 학습하고, 메소드 predict()나 predict_proba() 등을 통해 결과를 예측한다.
 - 본 장에서는 파이썬으로 데이터를 분할하고 학습(훈련) 데이터를 통해 모형객체를 생성하고 학습한 후 학습된 모형에 평가 데이터를 활용해
 예측하는 방법에 대해 배우고자 한다.
 - 또한 sklearn.metrics에서 제공하는 성과지표를 알아보고, 이를 사용하는 방법에 대해서도 알아보고자 한다.
 
 from sklearn.서브패키지 import 클래스
 - 지도 학습 모형은 예측할 값의 형태에 따라 분류(이진/다지), 회귀로 구분할수 있으며, 이진 분류는 이진형(0 또는 1) 데이터,
 다지분류는 이산형(0, 1, ...) 데이터, 회귀는 연속형 데이터인 경우를 말한다.

1절. 데이터 분할 : 지도학습 모형의 모형객체를 생성하는 방법을 배우기 전, 먼저 파이썬에서 데이터를 분할하는 방법에 대해 알아보자.
1. 홀드아웃 : 파이썬에서 홀드아웃을 수행하는 방법은 사이킷 런의 model_selection 서브패키지 내 train_test_split()으로 편리하게
사용할 수 있다. 함수 사용법은 아래와 같다. 

sklearn.model_selection.train_test_split(arrays, test_size = 0.25, shuffle = True, statify = None, ...)

Q. 사이킷런 패키지 내 breast_cancer 데이터를 호출한 후 학습 데이터와 평가 데이터로 분할해보자. 
(단, 분할 시 breast_cancer 내의 data에 대하여 셔플을 진행하고 학습, 평가 데이터는 각각 X_train, y_train에 할당하고
target에 대해서는 y_train, y_test에 할당하고 학습 데이터와 평가 데이터의 비율은 7:3으로 가정한다.)
"""
print("홀드아웃")
from sklearn.datasets import load_breast_cancer
breast_cancer = load_breast_cancer()
data = breast_cancer.data
target = breast_cancer.target

# train_test_split 함수 호출
from sklearn.model_selection import train_test_split

# arrays에 아래와 같이 data와 target을 둘 다 넣을 경우,
# X와 y에 대해 train과 test가 분할된 데이터셋들을 반환함
# cf) data만 입력하면 X에 대한 train, test를 분할해서 반환함
# random_state를 특정 숫자로 입력할 경우, 계속해서 동일한 데이터셋으로 분할됨
X_train, X_test, y_train, y_test = train_test_split(data,
                                                    target,
                                                    test_size = 0.3, # 7:3
                                                    random_state = 2022)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# statify = target은 원래의 target 컬럼의 0과 1의 비율을 반영하여 데이터를 분할
X_train, X_test, y_train, y_test = train_test_split(data,
                                                    target,
                                                    test_size = 0.3, # 7:3
                                                    random_state = 2022,
                                                    stratify = target)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

"""
2. K-fold : 파이썬에 K-fold를 수행하는 방법은 먼저, 사이킷런의 model_selection 서브패키지 내 클래스 KFold()를 사용해 객체를
생성한다. 다음으로 메소드 split()을 통해 학습 데이터와 평가 데이터를 분할하기 위한 인덱스 번호를 생성하는 방법으로 진행한다.

sklearn.model_selection.KFold(n_splits = 5, shuffle = False, ...)

Q. 길이가 10인 임의의 넘파이 배열을 생성한 후, 클래스 KFold()를 통하여 k=5인 k-fold 시행 시 데이터셋이 어떻게 분할되는지 알아보자. 
"""
print("\n K-fold")
import numpy as np
X = np.arange(10)
# print(X)

# KFold 클래스 호출
from sklearn.model_selection import KFold
kfold = KFold(n_splits = 5) # k=5
# print(kfold)

# 메소드 .split은 학습, 평가 데이터의 인덱스를 생성해줌
for train_idx, test_idx in kfold.split(X) :
    print("학습 : ", train_idx, "평가 :", test_idx) # 인덱스 번호

# 파이썬에서 클래스 KFold()를 사용해 5-fold를 실행한 결과를 그림으로 표현하면 아래와 같다. 그림에서 Te는 평가 데이터(test data),
# Tr은 학습 데이터(train data)를 의미한다.

"""
홀드아웃에서와 같이 라벨의 비율에 맞게 K-fold를 수행하고자 할 경우, 사이킷런의 model_selection 서브패키지 내 클래스 StatifiedKFold()를 사용해 객체를
생성하고 메소드 split()을 통해 학습 데이터와 평가 데이터를 분할하기 위한 인덱스 번호를 생성하면 된다.

sklearn.model_selection.StartifiedKFold(n_splits = 5, shuffle = False, ...)

Q. 길이가 15인 임의의 넘파이 배열 X와 0, 1, 2의 비율이 각각 2:1:2인 리스트 y를 생성한 후, 클래스 StratifiedKFold()를 통하여 y의 비율을 반영하여
k=3인 k-fold 시행 시 데이터셋이 어떻게 분할되는지 알아보자.
"""
print("\n 다른 K-fold 예시")
X = np.arange(15)
y = [0] * 6 + [1] * 3 + [2] * 6 # 리스트 생성, y = [0,0,0,0,0,0,1,1,1,2,2,2,2,2,2]

# StratifiedKFold 클래스 호출
from sklearn.model_selection import StratifiedKFold
kfold = StratifiedKFold(n_splits = 3) # k = 3

# 메소드 .split은 학습, 평가 데이터의 인덱스를 생성해 줌
# 동시에 y의 0,1,2도 함께 고려함
for train_idx, test_idx in kfold.split(X, y) :
    print("학습 : ", train_idx, "평가 : ", test_idx) # 인덱스 번호

"""
파이썬에서 클래스 StratifiedKFold()를 사용해 3-fold를 실행한 결과를 그림으로 표현하면 아래와 같다. 그림에서
Te는 평가 데이터(test data), Tr은 학습 데이터(train data)를 의미한다.
"""