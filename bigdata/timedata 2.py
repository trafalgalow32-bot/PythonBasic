# timedata2.py

"""
6장. 텍스트와 날짜 시간 데이터
2절. 날짜시간 데이터 다루기
2. 데이터 전처리
 - datetime형인 시리즈객체의 메소드 dt를 사용하여 여러 가지 날짜와 시간에 대한 정보를 확인할 수 있다.
 메소드 dt 또한 여러 하위 메소드를 가진다.
"""

import pandas as pd

# 데이터프레임 불러와 기존의 창립일 열을 datetime형으로 변환
df = pd.read_csv('data/예제/University_date.csv', encoding = 'CP949')
df['창립일'] = pd.to_datetime(df['창립일'])

# 메소드 dt의 하위 메소드를 통한 날짜와 시간에 대한 정보를 확인
# dt.date : 날짜정보(연월일)
print("dt.date : 날짜정보(연월일)")
foundation = df['창립일'].dt.date
print(foundation)

# dt.year : 연도
print("\n dt.year : 연도")
foundation_year = df['창립일'].dt.year
print(foundation_year)

# dt.month : 월
print("\n dt.month : 월")
foundation_month = df['창립일'].dt.month
print(foundation_month)

# dt.month_name() : 월 이름
print("\n dt.month_name() : 월 이름")
foundation_monthname = df['창립일'].dt.month_name()
print(foundation_monthname)

# dt.day : 일
print("\n dt.day : 일")
foundation_day = df['창립일'].dt.day
print(foundation_day)

# df.weekday : 요일번호
print("\n df.weekday : 요일번호")
foundation_weekday = df['창립일'].dt.weekday
print(foundation_weekday)

# df.day_name() : 요일이름
print("\n df.day_name() : 요일이름")
foundation_dayname = df['창립일'].dt.day_name()
print(foundation_dayname)

# dt.quarter : 분기
print("\n dt.quarter : 분기")
foundation_quarter = df['창립일'].dt.quarter
print(foundation_quarter)

# weekofyear : 연도기준 주
print("\n weekofyear : 연도기준 주")
foundation_weekofyaer = df['창립일'].dt.isocalendar().week # weekofyear 는 안써!
print(foundation_weekofyaer)

# dayofyear : 연도기준 일
print("\n dayofyear : 연도기준 일")
foundation_dayofyear = df['창립일'].dt.dayofyear
print(foundation_dayofyear)

# daysinmonth : 해당 월의 총 일수
print("\n daysinmonth : 해당 월의 총 일수")
foundation_daysinmonth = df['창립일'].dt.daysinmonth
print(foundation_daysinmonth)

# 2022-06-01 16:30:05부터 1초씩 증가(10번 반복)하는 시계열 생성
print("\n 2022-06-01 16:30:05부터 1초씩 증가(10번 반복)하는 시계열 생성")
sr = pd.Series(pd.date_range("2022-06-01 16:30:05", periods = 5, freq = "s"))
print(sr)

# dt.time : 시간정보(시분초)
print("\n dt.time : 시간정보(시분초)")
print(sr.dt.time)

# dt.hour : 시
print("\n dt.hour : 시")
print(sr.dt.hour)

# dt.minute : 분
print("\n dt.minute : 분")
print(sr.dt.minute)

# dt.second : 초
print("\n dt.second : 초")
print(sr.dt.second)




