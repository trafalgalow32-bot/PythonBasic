# pandas_test02.py

import numpy as np
import pandas as pd

"""
Part2. 데이터 핸들링
2장 Pandas를 활용한 데이터 다루기
1절. Series와 DataFrame
2. DataFrame(데이터프레임)
 - 직사각형 형태의 스프레드시트처럼 같은 크기의 열들을 모아 놓은 구조적 2차원 객체.
 - 열은 변수(variable); 컬럼명, 행은 개체(subject); 로우명
 - 2d-array 객체와 가장 큰 차이점은 각 변수들이 서로 다른 데이터 타입을 가질 수 있음 

가. 데이터프레임의 생성: 
 pandas.DataFrame(object, index, columns) 
 object: 객체, 주로 딕셔너리형과 2d-array 객체를 사용
 index: 행에 대한 인덱스를 별도 지정. 별도 지정하지 않을 경우 행 위치 인덱스로 자동 지정
 columns: 열에 대한 인덱스를 별도 지정. 별도 지정하지 않을 경우 열 위취 인덱스로 자동 지정됨
"""

# DataFrame 객체 생성
print("가. 데이터프레임의 생성 : pd.DataFrame(object, index, columns)")
# 1. object에 동일한 길이의 리스트를 값으로 가지는 딕셔너리 이용
print("1. object에 동일한 길이의 리스트를 값으로 가지는 딕셔너리 이용")
obj = {'이름' : ['이유리', '최민준', '김민지'],
        '전공' : ['경영학과', '컴퓨터공학과', '데이터과학과'],
        '성별' : ['여', '남', '여'],
        '나이' : [20, 22, 21]}
df_1 = pd.DataFrame(obj)
print(df_1)

print("\n 2. object에 2차원 배열 이용")
obj = np.array([['이유리', '경영학과', '여', 20],
                ['최민준', '컴퓨터공학과', '남', 22],
                ['김민지', '데이터과학과', '여', 21]])

df_2 = pd.DataFrame(obj)
print(df_2)

print("\n 원하는 인덱스 지정")
df_3 = pd.DataFrame(obj,
                    columns = ['Name', 'Major', 'Sex', 'Age'], # 열에 대한 인덱스
                    index = ['A', 'B', 'C']) # 행에 대한 인덱스
print(df_3)

print("\n 나. 데이터프레임의 정보 확인 메소드")
print("DaraFram 객체 생성")
obj = {'Name' : ['Olivia', 'Lucas', 'Sophia', 'Zoe', 'Ava', 'Elliot'],
       'Sex' : ['Female', 'Male', 'Female', 'Female', 'Female', 'Male'],
       'Age' : [22, 32, 27, 18, 38, 19]}
df = pd.DataFrame(obj)
print(df)

print("\n .values: 데이터프레임 내 값을 배열 형태로 반환")
print(df.values)

print("\n .index: 데이터프레임 내 행 인덱스를 레이블 배열 형태로 반환")
print(df.index)

print("\n .columns: 데이터프레임 내 열 인덱스를 레이블 배열 형태로 반환")
print(df.columns)

print("\n .dtypes: 데이터프레임 내 변수(컬럼)별 데이터 타입 확인")
print(df.dtypes)

print("\n .shape: 데이터프레임의 행, 열길이 확인")
print(df.shape)

print("\n .info(): 데이터프레임의 전반적인 요약 정보 확인. 로우명, 컬럼명, 행길이 ,열길이, 컬럼별 데이터 타입, 메모리 등 확인 가능")
print(df.info())

print("\n .head(n=5): 데이터프레임의 상위 행을 반환(n은 반환할 행의 수)")
print(df.head())
print("상위 1개의 행 반환")
print(df.head(1))
print("상위 (전체행-3)개의 행 반환")
print(df.head(-3))

print("\n .tail(n=5): 데이터프레임의 하위 행을 반환(n은 반환할 행의 수)")
print(df.tail())
print("하위 1개의 행 반환")
print(df.tail(1))
print("하위 (전체행-3)개의 행 반환")
print(df.tail(-3))

"""
다. 데이터프레임의 인덱싱과 슬라이싱
 - 판다스 객체인 시리즈와 달리 행과 열 그리고 각각의 위치 기반 인덱스 번호와 레이블 기반의 인덱스를 갖고 있음
 - 행에 대한 인덱싱과 슬라이싱을 위해 별도의 메소드(인덱서 indexer)를 사용해야 함
"""
print("\n 다. 데이터프레임의 인덱싱과 슬라이싱")
print("데이터프레임 생성")
obj = {'Name' : ['Olivia', 'Lucas', 'Sophia', 'Zoe', 'Ava', 'Elliot'],
       'Sex' : ['Female', 'Male', 'Female', 'Female', 'Female', 'Male'],
       'Age' : [22, 32, 27, 18, 38, 19]}
idx = list('abcdef')
df = pd.DataFrame(obj, index= idx)

print("Case1. 열만 참조, 데이터프레임명['컬럼명']")
print(df['Name'])

print("\n 여러 열을 추출 : 데이터프레임명[리스트]")
colnm = ['Name', 'Age']
print(df[colnm])

print("\n Case2. 행만 참조, iloc은 위치 기반으로, 데이터프레임명.iloc[행위치인덱스]")
#. 정수 위치 기반. Integer-based. 끝절 미포함!
print(df.iloc[1])
print("2~5번째 표 기준")
print(df.iloc[1:5])

print("\n 연속하지 않은 위치일 경우에도 리스트로 행을 참조")
idx = [1,3]
print(df.iloc[idx])

print("\n loc: 레이블 기반")
# loc은 레이블 기반이며, 데이터프레임명.loc[행레이블인덱스]. Label-based. 끝절 미포함
# 2번째(표 기준) 행의 값과 원래의 컬럼명을 레이블 인덱스로 가지는 시리즈
print(df.loc['b'])
print("\n 2~5번째(표기준) 행을 가지는 데이터프레임")
print(df.loc['b':'e'])

print("\n 대부분의 레이블 인덱스는 연속하지 않음")
rownm = ['b','d'] # 리스트로 행을 강조
print(df.loc[rownm])

print("\n Case3. 인덱서 없이 행과 열을 동시에 참조하는 방법")
print("i) 하나의 열에 대해 인덱싱")
df['Age'] # Age 열 참조
print(df['Age'])

print("ii) 행에 대해 인덱싱")
# 시리즈가 되기 때문에 가능해짐
df['Age']['a']
df['Age'][0]
print(df['Age']['a'])
print(df['Age'][0])

print("\n Case4. 여러 열에 대해, 행과 열을 동시에 참조하는 방법")
# i) iloc를 통한 방법: 2d-array와 동일
# 행: 위치 인덱스 번호가 1에서 4 사이
# 열: 위치 인덱스 번호가 1에서 행길이(마지막)
print("i) iloc를 통한 방법")
df.iloc[1:4,1:]
print(df.iloc[1:4,1:])

print("\n ii) loc를 통한 방법")
# ii) loc를 통한 방법: 2d-array에서의 방법에 숫자 대신 레이블을 이용
# 행 인덱스(로우명)이 b이고 열 인덱스(컬럼명)이 Name
df.loc['b', 'Name']
print(df.loc['b', 'Name'])

print("\n 대부분의 행과 열의 레이블 인덱스(특히 열)은 연속되지 않아 리스트 사용")
# 행 : b, d, e
# 열 : Name, Sex
rownm = ['b', 'd', 'e']
colnm = ['Name', 'Sex']
df.loc[rownm, colnm]
print(df.loc[rownm, colnm])

print("\n 라. 데이터프레임의 통계 메소드")
# 데이터프레임은 시리즈와 동일한 통계 메소드를 사용하여 컬럼별 요약 통계량을 확인할 수 있다.
# (단, 데이터프리엠의 경우 컬럼의 데이터타입이 float, int인 경웨 대해서만 사용 가능)
print("데이터프레임 생성")
obj = {'Name' : ['Olivia', 'Lucas', 'Sophia', 'Zoe', 'Ava', 'Elliot'],
       'Sex' : ['Female', 'Male', 'Female', 'Female', 'Female', 'Male'],
       'Age' : [22, 32, 27, 18, 38, 19],
       'Score' : [100, 95, 60, 77, 83, 84]
       }
df = pd.DataFrame(obj) # 데이터 프레임 생성
print(df.describe()) # 컬럼별 요약 통계량에 대한 정보(float, int인 경우만!)