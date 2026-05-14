# agglo01.py

"""
Part 4. 머신 러닝
2장. 군집 모형
 - 파이썬에서 사이킷런의 서브패키지 cluster로부터 여러 클래스를 이용하면 군집 모형객체를 생성할 수 있다.
 - 군집 모형의 경우 지도 학습 모형과 유사한 방식으로 sklearn.서브패키지명.클래스명을 통해 모형 객체를 생성한 후, 모형객체의 메소드 fit_predict9)을 통해
 모형에 적합한 후 군집을 형성한다.
 - 본 장에서는 가장 대표적인 군집분석인 계층적 군집분석(Hierarchical Clustering)과 비계층적 군집분석의 k-means 군집분석을 파이썬에서 수행하는 방법에
 대해 배우고자 한다.
 - sklearn.metrics.cluster에서 제공하는 군집 평가에 대한 지표를 알아보고, 이를 사용하는 방법에 대해서도 알아보자.
2절. 계층적 군집분석
 - 계층적 군집모형은 사이킷런의 cluster 내 클래스 AgglomerativeClustering()을 통해 모형객체를 생성할 수 있다.
 - 이를 통해 생성된 모형객체의 메소드 fit_predict()를 통해 군집을 형성한다.

 sklearn.cluster.AgglomeratvieClustering(n_clusters = 2, linkage = 'ward', ...)

Q. 사이킷런 패키지 내 iris 데이터를 호출한 후 클래스 AgglomerativeClustering()를 통해 네 종류의 연결법에 따른 모형객체를 생성하여 각각 군집을 형성
하여 예측된 레이블과 정답 레이블을 이용하여 RI와 ARI를 계산하는 코드를 작성해보자. (단, 군집은 세 가지를 형성할 것)
"""

# 패키지로부터 클래스, 함수를 호출
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import rand_score, adjusted_rand_score

# iris 데이터셋 호출
from sklearn.datasets import load_iris
iris = load_iris()
data = iris.data
labels_true = iris.target # 정답 레이블

# 와드연결법
agg_ward = AgglomerativeClustering(n_clusters = 3)
labels_pred_ward = agg_ward.fit_predict(data)

# 평균연결법
agg_avg = AgglomerativeClustering(n_clusters = 3, linkage = 'average')
labels_pred_avg = agg_avg.fit_predict(data)

# 최장연결법
agg_comp = AgglomerativeClustering(n_clusters = 3, linkage = 'complete')
labels_pred_comp = agg_comp.fit_predict(data)

# 최단연결법
agg_sing = AgglomerativeClustering(n_clusters = 3, linkage = 'single')
labels_pred_sing = agg_sing.fit_predict(data)

# RI 비교
print("RI 비교")
print("와드연결법")
print(rand_score(labels_true, labels_pred_ward)) # 와드연결법

print("평균연결법")
print(rand_score(labels_true, labels_pred_avg)) # 평균연결법

print("최장연결법")
print(rand_score(labels_true, labels_pred_comp)) # 최장연결법

print("최단연결법")
print(rand_score(labels_true, labels_pred_sing)) # 최단연결법

# ARI 비교
print("\n ARI 비교")
print("와드연결법")
print(adjusted_rand_score(labels_true, labels_pred_ward)) # 와드연결법

print("평균연결법")
print(adjusted_rand_score(labels_true, labels_pred_avg)) # 평균연결법

print("최장연결법")
print(adjusted_rand_score(labels_true, labels_pred_comp)) # 최장연결법

print("최단연결법")
print(adjusted_rand_score(labels_true, labels_pred_sing)) # 최단연결법

"""
 - 연결법에 따라 RI를 비교한 결과, 평균연결법이 0.8924로 가장 높고 ARI도 평균연결법이 0.7592로 가장 높다.
 - 군집분석의 경우 군집의 수에도 영향을 받기 때문에 이에 대한 결정이 필요한데 계층적 군집분석의 경우 대개 군집 수의 결정을 덴드로그램을 통해 결정하고 이는
 scipy 내의 cluster.hierarchy 서브 패키지의 dendrogram() 함수와 파이썬의 시각화 패키지인 matplotlib()을 통해 시각화하면 비교적 쉽게 가능하지만,
 본 수험서에서는 생략하고자 한다.
"""