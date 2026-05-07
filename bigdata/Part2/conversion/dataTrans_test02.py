# dataTrans_test02.py

import sklearn
import pandas as pd
import numpy as np
"""
Part2. 데이터 핸들링
3장 데이터 변환
2절 데이터 인코딩
 사이킷런의 머신러닝 알고리즘은 입력 데이터에 문자열 값을 허용하지 않아 문자열을 숫자형으로 변환하는 과정이 필요하다. 
 주로 카테고리형인 문자형은 인코딩을 통해 코드 값인 숫자로 변환할 수 있다.

1. 라벨 인코딩(Label Encoding)
 단순히 문자열 값을 숫자형 카테고리 값으로 일대일로 변환
 변환된 숫자가 대소의 의미를 가지게 되어 큰 숫자로 변환된 카테고리를 더 중요하게 인식할 수 있으므로 가급적 트리 계열과 
 머신러닝 알고리즘에서만 사용 권장!
 파이썬에서는 preprocessing 모듈의 Label Encoder 클래스를 사용
"""

print("사이킷런 내의 preprocessing 모듈 내 LabelEncoder 클래스 호출")
from sklearn.preprocessing import LabelEncoder

print("\n 데이터프레임 생성")
obj = {'Class' : ['A', 'B', 'A', 'C', 'E', 'D', 'D', 'A', 'F']}
df = pd.DataFrame(obj)
print(df)

print("\n 라벨 인코딩")
encoder = LabelEncoder() # 라벨 인코더객체 생성
encoder.fit(df.Class) # 적합
labels = encoder.transform(df.Class) # 변환
print("인코딩 결과, 변환된 숫자 카테고리 값")
print(labels)
print("숫자 값에 대응되는 원본 레이블")
print(encoder.classes_)
print("\n 디코딩 : 다시 원본 문자열로 되돌리는 방법. inverse_transform()")
print(encoder.inverse_transform(labels))

print("\n numpy의 select() 함수와 pandas 시리즈 객체의 메소드 map 이용")
"""
numpy.select(condlist, choicelist, ...)
"""
print("numpy.select()를 이용해 라벨 인코딩과 동일한 결과를 만드는 방법")
# 조건 목록 생성
conditionList = [(df['Class'] == 'A'),
                 (df['Class'] == 'B'),
                 (df['Class'] == 'C'),
                 (df['Class'] == 'D'),
                 (df['Class'] == 'E'),
                 (df['Class'] == 'F')]
# 조건과 매칭할 선택 목록 생성(0~5)
choicelist = list(range(6))
# 결과
np.select(condlist = conditionList, choicelist = choicelist)
print(np.select(condlist = conditionList, choicelist = choicelist))

print("\n 시리즈객체.map(arg, ...)")
# 시리즈객체.map()을 이용해 라벨 인코딩과 동일한 결과를 만드는 방법
df['Class'].map(arg = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5})
print(df['Class'].map(arg = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5}))

"""
2. 원-핫 인코딩(One-Hot Encoding) : 행 형태로 되어있는 값들을 열 형태로 차원을 변환한 뒤, 각 값에 해당하는 
 컬럼에만 1을 표시하고 나머지 컬럼에는 0을 표시하는 방법
 파이썬에서는 OneHotEncoder 클래스를 사용해 변환 가능
"""

print("\n 원-핫 인코딩(One-Hot Encoding)")
# 사이킷런 내의 preprocessing 모듈 내 LabelEncoder, OneHotEncoder 클래스 호출
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# 데이터프레임 생성
obj = {'Class' : ['A', 'B', 'A', 'C', 'E', 'D', 'D', 'A', 'F']}
df = pd.DataFrame(obj)
# print(df)

# 라벨 인코딩 먼저 수행
encoder = LabelEncoder()
encoder.fit(df['Class'])

# 2차원 레이블 변환
labels = encoder.transform(df['Class']).reshape(-1,1)

# 원-핫 인코딩
# sparse = False 옵션은 결과를 보통의 array 형태로 반환하기 위함
oh_encoder = OneHotEncoder(sparse_output = False) # sklearn 최신버전에서는 sparse를 sparse_output으로 적어줘야!
oh_encoder.fit(labels)
oh_labels = oh_encoder.transform(labels)

print("\n 원-핫 인코딩 결과")
print(oh_labels)

"""
원-핫 인코딩의 더미변수(Dummy Variable) : 범주형 변수를 0 또는 1의 값으로 어떤 특징에 해당하는지 여부를 표현하는 변수
판다스에서는 pandas.get_dummies() 함수 사용
"""
print("\n 판다스 get_dummies() 함수")
obj = {'Class' : ['A', 'B', 'A', 'C', 'E', 'D', 'D', 'A', 'F']}
df = pd.DataFrame(obj)
pd.get_dummies(df)
print(pd.get_dummies(df, dtype=int))

print("\n 첫 번째 고유 특징을 제거해 k-1개의 변수를 생성")
pd.get_dummies(df, drop_first = True)
print(pd.get_dummies(df, drop_first = True, dtype=int))

print("\n numpy.where를 이용해 라벨 인코딩과 동일한 결과를 만드는 방법")
df['Class_B'] = np.where(df['Class'] == 'B', 1, 0)
df['Class_C'] = np.where(df['Class'] == 'C', 1, 0)
df['Class_D'] = np.where(df['Class'] == 'D', 1, 0)
df['Class_E'] = np.where(df['Class'] == 'E', 1, 0)
df['Class_F'] = np.where(df['Class'] == 'F', 1, 0)
print(df)

print("\n loc 인덱서와 부울 인덱싱을 이용한 방법")
obj = {'Class' : ['A', 'B', 'A', 'C', 'E', 'D', 'D', 'A', 'F']}
df = pd.DataFrame(obj)

#df의 Class열이 B이면, Class_B 열에 1을 추가
df.loc[df['Class'] == 'B', 'Class_B'] = 1
#df의 Class열이 B가 아니면, Class_B 열에 0을 추가
df.loc[df['Class'] != 'B', 'Class_B'] = 0

#df의 Class열이 C이면, Class_C 열에 1을 추가
df.loc[df['Class'] == 'C', 'Class_C'] = 1
#df의 Class열이 B가 아니면, Class_B 열에 0을 추가
df.loc[df['Class'] != 'C', 'Class_C'] = 0

#df의 Class열이 D이면, Class_D 열에 1을 추가
df.loc[df['Class'] == 'D', 'Class_D'] = 1
#df의 Class열이 D가 아니면, Class_D 열에 0을 추가
df.loc[df['Class'] != 'D', 'Class_D'] = 0

#df의 Class열이 E이면, Class_E 열에 1을 추가
df.loc[df['Class'] == 'E', 'Class_E'] = 1

#df의 Class열이 F가 아니면, Class_F 열에 0을 추가
df.loc[df['Class'] != 'F', 'Class_F'] = 0
print(df)

print("\n 예제")
"""
학생의 id(s1, s2, s3, s4, s5, s6)를 담은 'student_id' 컬럼과 시험점수(55, 90, 85, 71, 63, 99)를 담은 'score' 컬럼으로 구성된
데이터프레임을 생성하자. 그 후 시험점수가 90점 이상이면 '수', 80점 이상 90점 미만이면 '우', 70점 이상 80점 미만이면 '미', 60점 이상
70점 미만이면 '양', 60점 미만이면 '가'로 분류하는 'grade'라는 컬럼을 새롭게 생성하고 생성한 'grade' 컬럼에 대하여 라벨 인코딩과
원-핫 인코딩을 시행해보자.
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
print("학생 데이터 프레임")
obj = {'student_id' : ['s1', 's2', 's3', 's4', 's5', 's6'],
       'score' : [55, 90, 85, 71, 63, 99]}
df = pd.DataFrame(obj)
print(df)

print("\n 구간화한 파생변수 grade 열 생성")
df['grade'] = pd.cut(df['score'],
                bins = [0, 60, 69, 79, 89, 100],               
                labels = ['가', '양', '미', '우', '수'],
                right=False)
print(df)

print("\n sklearn을 활용한 라벨 인코딩")
lb_encoder = LabelEncoder()
lb_encoder.fit(df['grade'])
lb_labels = lb_encoder.transform(df['grade'])
print(lb_labels)
print("숫자 값에 대응되는 원본 레이블")
print(lb_encoder.classes_)

print("\n sklearn을 활용한 원-핫 인코딩")
lb_labels_2d = lb_labels.reshape(-1,1) # 2d 라벨

oh_encoder = OneHotEncoder(sparse_output= False)
oh_encoder.fit(lb_labels_2d)

oh_labels = oh_encoder.transform(lb_labels_2d)
print(oh_labels)