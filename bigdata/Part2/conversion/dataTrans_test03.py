# dataTrans_test03.py

"""
Part2. 데이터 핸들링
3장 데이터 변환
3절 데이터 스케일링 : 데이터들의 범위가 같아지도록 속성(변수)별로 값을 비례적으로 조정하는 과정. z-score 표준화와 min-man 정규화가 많이 사용.됨
변수들의 측정 단위나 값 범위가 다를 때 표준화 혹은 정규화를 적용하여 같은 기준으로 데이터를 파악 가능

1. 표준화(Standardlization)
 각 개체들이 평균을 기준으로 얼마나 떨어져 있는지를 나타내는 값으로 변환하는 과정으로, 표준화 후 특정 범위를 벗어난 데이터를 확인하여 이상치 판
 별에 활용 가능
 z-점수 표준화는 각 요소의 값에서 평균을 뺀 후 표준편차로 나누어 수행. 변환 후 데이터의 평균은 0, 표준편차는 1.
 파이썬: preprocessing 모듈 내 StandardScaler 클래스, fit() transform()
"""

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

iris = load_iris() # iris 데이터셋 호출
data = pd.DataFrame(iris.data, columns = iris.feature_names) # 데이터프레임 변환

std_scale = StandardScaler() # 표준 스케일러객체 생성

# 표준화 데이터로 변환
print("표준화 - iris 데이터셋으로 확인")
data_std = std_scale.fit_transform(data)
data_std = pd.DataFrame(data_std, columns = iris.feature_names) # 데이터프레임 변환
print(data_std.head()) 

print("\n 정규화")
"""
정규화(Normalization) : 데이터의 범위를 0과 1 사이로 변환하여 데이터의 분포를 조정하는 방법. 데이터 군 내에서 특정 개체가 가지는 위치를 파악하고
비교할 때 유용하게 활용
일반적으로 많이 사용되는 클래스는 MinMaxScaler
"""

from sklearn.preprocessing import MinMaxScaler

iris = load_iris()
data = pd.DataFrame(iris.data, columns = iris.feature_names)

# 최소최대 스케일러객체 생성
mm_scale = MinMaxScaler()

# 정규화 데이터로 변환
data_std = mm_scale.fit_transform(data)
data_std = pd.DataFrame(data_std, columns = iris.feature_names)
print(data_std.head())



