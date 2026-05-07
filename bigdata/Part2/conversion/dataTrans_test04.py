# dataTrans_test04.py

"""
Part2. 데이터 핸들링
3장 데이터 변환
4절 데이터 축소 : 변수를 축소하고 데이터를 잘 설명할 수 있는 적절한 변수들만 선택하여 분석에 활용하는 방법으로, 주성분분석(PCA)가 대표적이다.
1. 주성분분석
 데이터에 여러 변수들이 있을 때 서로 상관성이 높은 변수들이 선형결합으로 이루어진 '주성분(Principal Component)'이라는 새로운 변수를 만들어
 변수들을 요약하고 축소하는 기법
 주성분 기여율이라는 지표를 사용하여 주성분이 데이터를 얼마나 잘 설명할 수 있는지 평가
 주성분 기여율: 원 변수의 총 변동(각 변수들의 분산값 총합) 분의 주성분 변수의 분산 => 총 변동에 대한 주성분의 설명력
 주성분의 분산이 전체 데이터의 흩어진 정도와 비슷하다면 해당 주성분은 적절하다고 판단. 1에 가까울 수록 적절하고 0에 가까울 수록 설명력이 떨어짐
 첫번째 주성분부터 차례대로 기여율을 합한 누적 기여율(cumulative proportion)이 85% 이상이 되면 해당 지점까지를 주성분의 수로 결정.
 파이썬의 주성분 분석: sklearn 내 decomposition 모듈의 PCA 클래스를 통해 수행. fit(), transform()
"""
print("주성분분석 : USArrests 데이터를 예시로. 1973년 미국 50개주 100,000명의 인구 당 체포된 세 가지 강력 범죄 수마다 도시에 거주하는 인구 비율")

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

print("\n 데이터 확인")
df = pd.read_csv("data/예제/USArrests_rownames.csv", index_col = 0)
print(df.head()) # 데이터 확인

# 주성분 분석 전 표준화
x = StandardScaler().fit_transform(df)

# PCA 객체 생성(주성분의 수를 전체 컬럼 수로)
pca = PCA(n_components = 4)

# 전환 후 변환(배열형태)
pca_arr = pca.fit_transform(x)

# 주성분에 따른 분산 기여율과 누적 기여율
result = {"분산 기여율 " : pca.explained_variance_ratio_, # 분산 기여율
            "누적 기여율 " : pca.explained_variance_ratio_.cumsum()} # 누적 기여율

# 결과를 데이터프레임 형태로 변환, 전치하여 컬럼명이 주성분이 되게 함
result = pd.DataFrame(result, 
                      index = ['PCA1', 'PCA2', 'PCA3', 'PCA4']).T
print(result)
print("주성분 분석 결과")
pca = PCA(n_components = 2) # PCA 객체 생성
pca_arr = pca.fit_transform(x) # 적합후 변환(배열형태)
df_pca = pd.DataFrame(pca_arr, columns = ['PCA1', 'PCA2']) # 데이터프레임으로 변환
print(df_pca.head())