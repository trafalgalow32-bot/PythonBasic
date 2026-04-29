# dataTrans_test01.py

import sklearn
"""
3장 데이터 변환
1절 파생변수 생성
 파생변수: 사용자가 특정 의미를 부여하여 만든 변수로서 다양한 함수와 조건문 등을 활용하여 생성할 수 있다. 
 주관적일 수 있으므로 논리적 타당성을 갖추어 개발해야 하며, 특정 상황에서만 유의미하지 않도록 대표성을 나타낼 수 있도록
 생성해야 한다.
1. 컬럼 추가 : 데이터프레임['컬럼명'] = 추가할 컬럼의 객체
"""

# print("예시")
from sklearn.datasets import load_iris
iris = load_iris()
# print(iris)

print("pandas 호출")
import pandas as pd
data = pd.DataFrame(iris.data, columns= iris.feature_names)
print(data)

print("\ n 150개 개체들의 고유 번호에 해당하는 'ID'컬럼 새로 생성")
data['ID'] = range(150)
print(data.head()) # 상위 5개 행 출력

print("\n insert 메소드")
# 데이터프레임객체.insert(loc, column, value, ...)
data = pd.DataFrame(iris.data, columns= iris.feature_names) # 다시 생성
data.insert(0, column= 'ID', value = range(150))
print(data.head())

print("\n ===================================================")
"""
2. 컬럼 삭제 : 데이터프레임객체.drop(labels, axis=0, inplace = False, ...)
"""
print(".drop() 메소드를 통한 컬럼 삭제")
data2 = data.drop('ID', axis=1) # 위에서 생성한 ID 컬럼을 삭제!
print(data2.head() )

print("\n ===================================================")
"""
3. 구간화(비닝; binning) : 특정 컬럼에 대해 수치형(연속형) 값들을 이산형 또는 범주형으로 변환하는 것.
판다스에서 제공하는 cut() 함수와 qcut() 함수를 통해 수행 가능
pandas.cut(x, bins, labels=None, right=True, ...)
pandas.qcut(x, q, labels=None, right=True, ...)
"""
print("3. 구간화(비닝;binning)")
print(".cut")
print("5개 구간으로 분할")
print(pd.cut(data['sepal length (cm)'], bins= 5))

print("\n 구간 (4, 5], (5, 6], (6, 7], (7, 8]으로 분할")
print(pd.cut(data['sepal length (cm)'], bins = [4,5,6,7,8]))

print("\n 컬럼 'sepal length' (cm)의 요약 통계량에 대한 정보")
print("\n .qcut() : 4분위수마다 분할")
print(pd.qcut(data['sepal length (cm)'], q = 4))

print("\n 4분위수 확인")
print(data['sepal length (cm)'].quantile([.25, .5, .75]))

print("\n 10분위수마다 분할")
print(pd.qcut(data['sepal length (cm)'], q=10))

print("\n 10분위수 확인")
print(data['sepal length (cm)'].quantile([.0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1]))