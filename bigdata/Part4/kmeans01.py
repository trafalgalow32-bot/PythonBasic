# kmeans01.py

"""
Part 4. 머신 러닝
2장. 군집 모형
 - 파이썬에서 사이킷런의 서브패키지 cluster로부터 여러 클래스를 이용하면 군집 모형객체를 생성할 수 있다.
 - 군집 모형의 경우 지도 학습 모형과 유사한 방식으로 sklearn.서브패키지명.클래스명을 통해 모형 객체를 생성한 후, 모형객체의 메소드 fit_predict9)을 통해
 모형에 적합한 후 군집을 형성한다.
 - 본 장에서는 가장 대표적인 군집분석인 계층적 군집분석(Hierarchical Clustering)과 비계층적 군집분석의 k-means 군집분석을 파이썬에서 수행하는 방법에
 대해 배우고자 한다.
 - sklearn.metrics.cluster에서 제공하는 군집 평가에 대한 지표를 알아보고, 이를 사용하는 방법에 대해서도 알아보자.
3절. k-means 군집분석
 - k-means 군집모형은 사이킷런의 cluster 내 클래스 KMeans()을 통해 모형객체를 생성할 수 있다.
 - 이를 통해 생성된 모형객체의 메소드 fit_predict()를 통해 군집을 형성한다.

 sklearn.cluster.KMeans(n_clusters = 8)

Q. 사이킷런 패키지 내 iris 데이터를 호출한 후 군집의 수(k)가 2 ~ 4개일 때 k-mean 모형에 대하여 전체, 레이블별 실루엣계수의 평균을 계산하는 코드를 
작성해보자.
"""

# 패키지로부터 클래스, 함수를 호출
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples

# iris 데이터셋 호출
from sklearn.datasets import load_iris
iris = load_iris()
data = iris.data

# k=2일 때 k-means 군집모형 군집 형성
kmeas_k2 = KMeans(n_clusters = 2, random_state = 2022)
labels_pred_k2 = kmeas_k2.fit_predict(data)

# k=3일 때 k-means 군집모형 군집 형성
kmeas_k3 = KMeans(n_clusters = 3, random_state = 2022)
labels_pred_k3 = kmeas_k3.fit_predict(data)

# k=4일 때 k-means 군집모형 군집 형성
kmeas_k4 = KMeans(n_clusters = 4, random_state = 2022)
labels_pred_k4 = kmeas_k4.fit_predict(data)

# 계체별로 연결법에 따른 실루엣계수를 계산
import pandas as pd # 데이터프레임 생성 필요

print("k=2일때")
# k=2일 때
sil_k2 = silhouette_samples(data, labels_pred_k2) # 개체별 실루엣 계수

# 계체별 예측 레이블과 실루엣계수를 각각 컬럼으로 가지는 데이터프레임 생성
df_k2 = pd.DataFrame({'labels' : labels_pred_k2, 'silhouette' : sil_k2})

# 레이블별 실루엣계수의 평균
print(df_k2.groupby('labels')['silhouette'].mean())

# 전체 실루엣계수 평균
print(silhouette_score(data, labels_pred_k2))

print("\n k=3일때")
# k=3일 때
sil_k3 = silhouette_samples(data, labels_pred_k3) # 개체별 실루엣 계수

# 계체별 예측 레이블과 실루엣계수를 각각 컬럼으로 가지는 데이터프레임 생성
df_k3 = pd.DataFrame({'labels' : labels_pred_k3, 'silhouette' : sil_k3})

# 레이블별 실루엣계수의 평균
print(df_k3.groupby('labels')['silhouette'].mean())

# 전체 실루엣계수 평균
print(silhouette_score(data, labels_pred_k3))

print("\n k=4일때")
# k=4일 때
sil_k4 = silhouette_samples(data, labels_pred_k4) # 개체별 실루엣 계수

# 계체별 예측 레이블과 실루엣계수를 각각 컬럼으로 가지는 데이터프레임 생성
df_k4 = pd.DataFrame({'labels' : labels_pred_k4, 'silhouette' : sil_k4})

# 레이블별 실루엣계수의 평균
print(df_k4.groupby('labels')['silhouette'].mean())

# 전체 실루엣계수 평균
print(silhouette_score(data, labels_pred_k4))

"""
 - 실루엣계수로 군집의 수를 결정하기 위해서는 전체 실루엣계수의 평균이 1에 가까우면서 레이블별 실루엣계수의 평균의 편차가 적은 지를 살펴보아야 한다.
 - k = 2인 경우가 전체 실루엣계수의 평균이 0.6810으로 가장 크고 군집(레이블) 간 실루엣계수의 편차가 적으므로 2로 선택하는 것이 바람직해 보인다.
"""