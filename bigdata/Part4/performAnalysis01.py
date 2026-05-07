# performAnalysis.py

"""
Part 4. 머신 러닝
1장. 지도 학습 모형
2절. 성과분석

1. 분류지표
가. 혼동 행렬을 이용한 평가 지표

Q. 임의의 리스트 y_true와 y_pred를 생성한 후, 함수 confusion_matrix()를 통하여 이진분류와 다진분류인 경우 혼동행렬을 구하는 코드를 작성해보자.
"""

# 함수 confusion_matrix() 호출
from sklearn.metrics import confusion_matrix

# 이진 분류
y_true = [0,0,0,1,1,1]
y_pred = [0,1,0,1,1,1]

print(confusion_matrix(y_true, y_pred)) # 혼동 행렬

# array([[2,1],
#        [0,3]], dtype=int64)

# 이진 분류(레이블로 되어 있는 경우)
y_true = ['A','A','A','B','B','B']
y_pred = ['A','B','A','B','B','B']

print(confusion_matrix(y_true, y_pred, labels= ['A', 'B'])) # 혼동 행렬(레이블 구분)

# 다지 분류(레이블: 0,1,2)
y_true = [0,0,0,1,1,2,2,2,2]
y_pred = [0,1,1,1,0,0,1,2,2]

print(confusion_matrix(y_true, y_pred)) # 혼동 행렬

"""
Q. 임의의 리스트 y_true와 y_pred를 생성한 후, 이진분류에 대하여 Accuarcy, Recall, Precision, F1-score를 구하는 코드를 작성해 보자.
"""

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

# 이진 분류
y_true = [0,0,0,1,1,1]
y_pred = [0,1,0,1,1,1]

# 정분류율(Accuracy)
print("\n 정분류율(Accuracy)")
accuracy = accuracy_score(y_true, y_pred)
print(accuracy)

# 재현율(Recall)
print("재현율(Recall)")
recall = recall_score(y_true, y_pred)
print(recall)

# 정밀도(Precision)
print("정밀도(Precision)")
precision = precision_score(y_true, y_pred)
print(precision)

# f1-score
print("f1-score")
f1 = f1_score(y_true, y_pred)
print(f1)

"""
나. AUC

Q. 임의의 리스트 y_true와 y_score를 생성한 후, 이진분류에 대하여 AUC를 구하는 코드를 작성해보자.
"""

from sklearn.metrics import roc_curve, auc

# 이진분류
y_true = [0,0,0,1,1,1]
y_score = [0.1, 0.75, 0.35, 0.92, 0.81, 0.68]

# ROC : 함수 roc_curve()는 fpr, tpr, thresholds 세 가지를 반환함
fpr, tpr, thresholds = roc_curve(y_true, y_score)

# AUC 
print("AUC")
AUC = auc(fpr, tpr) # roc_curve()에서 반환된 fpr을 x축, tpr을 y축
print(AUC)

"""
2. 예측 지표

Q. 임의 리스트 y_true와 y_pred를 생성한 후, 목푯값이 연속형인 모델의 평가 지표 MSE, MAE, MAPE를 구하는 코드를 작성해 보자. 
"""

from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error

# 연속형 데이터, 균일 분포(0,1)에서 임의의 난수 생성
import numpy as np
np.random.seed(123) # 난수 고정

y_true = np.random.random_sample(5) # 균일분포 (0,1)에서 5개 랜덤 추출
print(y_true)

y_pred = np.random.random_sample(5) # 균일분포 (0,1)에서 5개 랜덤 추출
print(y_pred)

#MSE
print("MSE")
mse = mean_squared_error(y_true, y_pred)
print(mse)

#MAE
print("MAE")
mae = mean_absolute_error(y_true, y_pred)
print(mae)

#MAPE
print("MAPE")
mape = mean_absolute_percentage_error(y_true, y_pred)
print(mape)