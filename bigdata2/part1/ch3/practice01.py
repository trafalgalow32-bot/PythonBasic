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

"""
05. 문자열 슬라이싱, 파생변수, 평균값
(이전 단계의 결과를 사용!)
'f4' 컬럼에 'FJ'가 포함된 데이터를 찾으시오.
찾은 데이터 중에서 'f2'컬럼의 평균값을 구하시오.(반올림 후 소수 둘째 자리까지 계산)
"""
print("\n Q5")
import pandas as pd
exam5 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# f4 컬럼에서 뒤에 2개 값 슬라이싱
# print(exam5)
exam5['new'] = exam5['f4'].str[2:4]

# FJ인 데이터 찾기
cond = exam5['new'] == 'FJ'
exam5 = exam5[cond]

# f2 평균 구하기
print(round(exam5['f2'].mean(),2)) # 출력값 0.61

"""
06. 필터링, 분산
(이전 단계의 결과를 사용!)
'f3' 컬럼이 gold이면서 'f2'컬럼이 2인 데이터를 찾으시오.
찾은 데이터에서 'f1' 컬럼의 분산을 구하시오. (반올림 후 소수 둘째 자리까지 계산)
"""
print("\n Q6")
import pandas as pd
exam6 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')
# print(exam6)
cond = exam6[(exam6['f3']=='gold')&(exam6['f2']==2)] 
# 다른 풀이 : cond1 = exam6['f3']=='gold', cond2 = exam6['f2']==2, exam6 = exam6[cond1 & cond2]
# print(exam6[cond])
# print(exam6[(exam6['f3']=='gold')&(exam6['f2']==2)])
f1_var = cond['f1'].var()
f1_var = round(f1_var,2)
print(f1_var) # 출력값 235.43

"""
07. 값 변경(연산), 필터링 절댓값
(이전 단계의 결과를 사용!)
모든 나이(age)에 1을 더하시오.
20대의 'views' 평균과 30대의 'views' 평균의 차이의 절댓값을 구하시오. (반올림 후 소수 둘째자리까지 계산)
"""
print("\n Q7")
import pandas as pd
exam7 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

exam7['age'] = exam7['age'] + 1

# 20대, 30대 조건
cond1 = (exam7['age'] >= 20) & (exam7['age'] < 30)
cond2 = (exam7['age'] >= 30) & (exam7['age'] < 40)

# 30대 views
result = abs(exam7[cond1]['views'].mean() - exam7[cond2]['views'].mean())
print(round(result,2)) # 출력값 263.13

"""
08. 값 변경(연산), 필터링 절댓값
(이전 단계의 결과를 사용!)
'subscribed' 컬럼이 2024년 2월인 데이터를 찾으시오.
위에서 찾은 데티어 중 'f3' 컬럼이 gold인 데이터의 개수를 구하시오.
"""
print("\n Q8")
import pandas as pd
exam8 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# 자료형 변환
exam8['subscribed'] = pd.to_datetime(exam8['subscribed'])

# 파생변수 생성(연, 월)
exam8['year'] = exam8['subscribed'].dt.year
exam8['month'] = exam8['subscribed'].dt.month

# 2024년 2월이고, 'f3'이 gold인 데이터
cond1 = exam8['year'] == 2024
cond2 = exam8['month'] == 2
cond3 = exam8['f3'] == 'gold'
exam8 = exam8[cond1 & cond2 & cond3]

# 데이터 개수
print(len(exam8)) # 출력값 5

"""
09. 필터링, 카테고리, 최빈값
'views' 컬럼 값이 1000이하인 데이터(결측치 제외)를 찾잇오.
앞에서 구한 데이터 중 'f4' 컬럼의 최빈값을 구하시오.
"""
print("\n Q9")
import pandas as pd
exam9 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# # 풀이1, 근데 풀이2가 더 낫다!
# # views 수가 1000 이하
# cond = exam9['views'] <= 1000
# exam9 = exam9[cond]
# # print(len(exam9))

# # f4 컬럼 종류별 개수
# exam9 = exam9['f4'].value_counts()
# # print(exam9)

# # f4 컬럼 최빈값
# print(exam9.index[0])

# 풀이2. 이걸로 가자!
cond = exam9['views'] <= 1000

exam9 = exam9[cond]

print(exam9['f4'].mode()[0])

"""
10. 그룹핑, 최댓값, 정렬
결측치가 있는 행을 삭제하시오.
결측치가 삭제된 데이터를 사용하여 지역별(city) 평균을 계산하시오.
앞에서 계산한 지역별 평균 데이터에서 'f2' 컬럼 값이 가장 큰 지역을 구하시오.
"""
print("\n Q10")
import pandas as pd
exam10 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# 결측치 있는 행 삭제
exam10 = exam10.dropna()

# 지역별 평균 계산
exam10 = exam10.groupby(['city']).mean(numeric_only=True)

# f2 컬럼이 가장 큰 지역 출력
print(exam10['f2'].idxmax())

"""
11. 슬라이싱, 사분위수, 결측치 제거
데이터에서 결측치가 있는 데이터(행)를 모두 제거하시오.
결측치가 제거된 데이터를 사용하여 앞에서부터 70% 데이터를 구하시오. 
(단, 데이터 70% 지점의 index 가 소수점으로 계산될 경우 소수점 이하는 버림)
앞에서 구한 70% 데이터 중 'views' 컬럼의 3사분위수에서 1사분위수를 뺀 값을 소수점 이하를 버리고 정수 부분만 구하시오.
"""
print("\n Q11")
import pandas as pd
exam11 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# 결측치 있는 데이터 제거
exam11 = exam11.dropna()
# print(len(exam11.isna()))

# 70% 지점
end = int(len(exam11) * 0.7)

# 70% 데이터 슬라이싱
exam11 = exam11.iloc[:end]

# 3사분위수, 1사분위수
q3 = exam11['views'].quantile(.75)
q1 = exam11['views'].quantile(.25)

print(int(q3 - q1)) # 출력값 2771

"""
12. 결측치 처리, 최빈값, 데이터 개수
결측치가 가장 많은 두 컬럼을 찾으시오.
첫 번째로 결측치가 많은 컬럼에서 결측치가 있는 데이터(행)를 삭제하시오.
두 번째로 결측치가 많은 컬럼을 최빈값으로 대체하시오.
'f3' 컬럼의 'gold' 값을 가진 데이터의 수를 정수형으로 구하시오.
"""
print("\n Q12")
import pandas as pd
exam12 = pd.read_csv('bigdata2/part1/ch3/type1_data1.csv')

# print(exam12.isnull().sum()) # f1, f3 컬럼

# 특정 컬럼에 결측치가 있을 경우 해당 행 제거
exam12 = exam12.dropna(subset=['f1'])

# 두 번째로 결측치가 많은 컬럼 최빈값 대체
freq = exam12['f3'].mode()[0]
exam12['f3'] = exam12['f3'].fillna(freq)

# f3 컬럼이 gold인 데이터의 수
print(sum(exam12['f3'] == 'gold')) # 출력값 63