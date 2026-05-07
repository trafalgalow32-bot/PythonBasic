# dataSplit01.py

"""
Part 4. 머신 러닝
1장. 지도 학습 모형
1절. 데이터 분할
1. 홀드아웃

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
2. K-fold

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

"""
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
