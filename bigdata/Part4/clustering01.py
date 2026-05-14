# clustering01.py

"""
Part 4. 머신 러닝
2장. 군집 모형
 - 파이썬에서 사이킷런의 서브패키지 cluster로부터 여러 클래스를 이용하면 군집 모형객체를 생성할 수 있다.
 - 군집 모형의 경우 지도 학습 모형과 유사한 방식으로 sklearn.서브패키지명.클래스명을 통해 모형 객체를 생성한 후, 모형객체의 메소드 fit_predict9)을 통해
 모형에 적합한 후 군집을 형성한다.
 - 본 장에서는 가장 대표적인 군집분석인 계층적 군집분석(Hierarchical Clustering)과 비계층적 군집분석의 k-means 군집분석을 파이썬에서 수행하는 방법에
 대해 배우고자 한다.
 - sklearn.metrics.cluster에서 제공하는 군집 평가에 대한 지표를 알아보고, 이를 사용하는 방법에 대해서도 알아보자.
1절. 군집 평가
 - 군집 평가란 군집 모형을 통해 형성된 군집이 얼마나 제대로 형성되었는지 평가하는 것을 말한다.
 - 정답 또는 타겟 레이블을 모르는 경우는 주로 실루엣(Silhoutte) 계수, 아는 경우에는 랜드지수(RI: Rand Index)와 조정 랜드지수(ARI; Adjusted RI) 
 등을 지표로 사용한다.

 1. 실루엣계수
 - 실루엣계수는 사이킷런의 서브패키지 metrics 내의 함수 silhouette_score()과 silhouette_samples()를 통해 계산할 수 있다.
 - silhouette_score()는 전체 개체에 대한 실루엣계수의 평균을 계산하고, silhouette_sample()은 각 개체에 대한 개별 실루엣계수를 계산하는 함수로 사용법은
 아래와 같다.

sklearn.metrics.silhouette_score(X, y, ...)

sklearn.metrics.silhouette_sample(X, y, ...)

 - 보통의 경우 두 함수를 이용하여 실루엣계수를 계산하고 이를 시각화로 표현하여 군집 평가를 진행하지만, 현재 시험 환경에서 시각화를 지원하지 않기 때문에
 시각화 없이 군집 평가를 수행하는 방법에 대해 알아보고자 한다.(이에 대한 자세한 방법은 다음 절에서 다루고자 한다.)

 2. RI와 ARI
 - 랜드지수와 조정 랜드지수는 각각 사이킷런의 서브패키지 metrics.cluster 내의 함수 rand_score(), adjusted_rand_score()를 통해 계산할 수 있다.
 
Q. 임의의 리스트 labels_true와 labels_pred를 생성한 후, 함수 rand_score(), adjust_rand_score()를 통하여 RI와 ARI를 계산하는 파이썬 코드를
작성해보자.
"""

# 임의의 리스트 작성
labels_true = [0,0,0,1,1,1,1,2,2]
labels_pred = [0,0,1,1,1,1,2,2,2]

# 함수 호출
from sklearn.metrics.cluster import rand_score, adjusted_rand_score

# RI(랜드지수)
ri = rand_score(labels_true, labels_pred)
print(ri)

# ARI(조정 랜드지수)
ari = adjusted_rand_score(labels_true, labels_pred)
print(ari)