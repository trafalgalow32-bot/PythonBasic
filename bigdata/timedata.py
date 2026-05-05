# timedata.py

"""
6장. 텍스트와 날짜 시간 데이터
2절. 날짜시간 데이터 다루기
1. 데이터 타입
 -  날짜 데이터는 파이썬(판다스 포함)에서 datetime형을 가진다. datetime형은 날짜와 시간에 대한 문자열로, 
 데이터에서 문자형인 object형으로 인식되는 경우가 많으므로 변환이 필요하다. 
 - datetime형으로 변환하는 방법은 판다스에서 제공하는 to_datetime() 등이 있다. 함수 to_datetime()는 날짜를 
 나타내는 문자열을 정해진 format을 바탕으로 datetime형으로 변환하는 역할을 수행한다. 
 pandas.to_datetime(arg, format=None, ...)
"""

import pandas as pd

# 데이터프레임 불러오기
df = pd.read_csv('data/예제/University_date.csv', encoding = 'CP949')
foundation = df['창립일']
print(foundation)

# pandas.to_datetime() : 문자열 -> datetime형
print("\n pandas.to_datetime()")
foundation_datetime = pd.to_datetime(df['창립일']) # 구문 분석 자동
print(foundation_datetime)

# 문자열 -> datetime형
print("\n 문자열 -> datetime형")
foundation_ymd = pd.to_datetime(df['창립일'], format = '%Y-%m-%d') # '네자리연도-월-일'로 구문
print(foundation_ymd)

# 기존의 창립일 열을 datetime형으로 변환
df['창립일'] = pd.to_datetime(df['창립일'])

# 시계열 생성 : 2000년 1월 1일부터 2000년 1월 10일까지 1일 단위로 생성
print("\n 시계열 생성")
datetimeidx = pd.date_range("2000-01-01", "2000-01-10")
print(datetimeidx)

# 2000년 1월 1일부터 1일씩 증가(3번 반복)
print("\n 1일씩 세번 반복")
datetimeTriple = pd.date_range("2000-01-01", periods = 3)
print(datetimeTriple)

# 2000년 1월부터 1달씩 증가(5번 반복)
print("\n 1달씩 5번 반복")
datetimeMonth = pd.date_range("2000-01-01", periods = 5, freq = "m")
print(datetimeMonth)