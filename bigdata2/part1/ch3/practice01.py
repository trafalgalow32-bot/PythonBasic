# practice01.py

"""
01. 필터링, 최솟값, 중앙값

'f5' 컬럼이 0이 아닌 데이터(행)를 구하시오. 
앞에서 구한 데이터에 'views' 컬럼 결측치를 'views'컬럼의 최솟값으로 채워주세요.
그리고 'views' 컬럼의 중앙값을 계산해 정수로 구하시오.
"""
print("Q1")
import pandas as pd
exam1 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv') # csv 파일 경로 bigdata2/part1/ch3/
# print(exam1)

# 0 제외
f5 = exam1['f5']!=0
print(exam1[f5])

# 결측치 최소값으로 채우기
min = exam1['views'].min()
# print(min)
exam1 = exam1['views'].fillna(min)
print(exam1)

# 중앙값
mid = exam1.median()
print(int(mid)) # 출력값 5924

"""
02. 카테고리, 인덱스, 문자열 슬라이싱

'subscribed' 컬럼에서 가장 빈도수가 많은 날짜를 구하시오.
앞에서 구한 날짜의 일(day) 값을 정수로 구하시오.
"""
print("\n Q2")
import pandas as pd
exam2 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# 종류가 가장 많은 날짜 구하기
exam2 = exam2['subscribed'].value_counts()
# print(exam2)

# 일(day) 값을 찾고, 정수형으로 변경
day = int(exam2.index[0][-2:])
print(day) # 출력값 17

"""
03. 파생변수, 정렬, 인덱싱

결측치가 있는 데이터(행)를 제거하시오.
'views' 컬럼을 'f1' 컬럼으로 나눈 값을 새로운 컬럼으로 추가하시오.
새로운 컬럼 값 중 가장 큰 값을 가진 행의 age를 정수로 구하시오.
"""
print("\n Q3")
import pandas as pd
exam3 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# 결측치 제거
exam3 = exam3.dropna()
# print(exam3)

# 새로운 컬럼 계산
exam3['new'] = exam3['views'] / exam3['f1']
# print(exam3)

# 내림차순 정렬
exam3 = exam3.sort_values('new', ascending=False).reset_index(drop=True)
# print(exam3)

# age값만 찾아서 출력
age = exam3.loc[0, 'age'] # age = exam3.loc[exam3.index[0], 'age']
# age = exam3.iloc[0,1]
print(int(age)) # 출력값 22

"""
04. 값 변경, 정렬, 합계
'views' 컬럼의 결측 데이터를 0으로 대체하시오.
'views' 컬럼에서 상위 10번째 값을 구하시오.
'views' 컬럼에서 상위 10개의 값을 상위 10번째 값으로 대체하시오.
'views' 컬럼의 전체 합을 정수로 구하시오.
"""
print("\n Q4")
import pandas as pd
exam4 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# 결측치 0으로 대체
exam4['views'] = exam4['views'].fillna(0)
# print(len(exam4[exam4.isna()==True])) # 결측치 대체 여부 확인

# 내림차순 정렬
exam4 = exam4.sort_values('views', ascending=False) # .reset_index(drop=True)
# print(exam4)

# views 상위 10개 데이터 값 구하기
# top10 = exam4['views'][:9]
# print(top10)
min = exam4.iloc[:10]['views'].min()
exam4.iloc[:10, -1] = min
# print(min)

# views 컬럼의 합
print(int(exam4['views'].sum())) # 출력값 652812