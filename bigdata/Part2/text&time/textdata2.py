# textdata2.py

"""
6장. 텍스트와 날짜시간 데이터
1절. 텍스트 데이터 다루기
1. 문자열 데이터 전처리
 - 데이터프레임의 값에 들어가 있는 문자열은 시리즈 객체의 str메소드를 사용하여 문자열을 처리할 수 있다.
 - str을 사용하면 인덱싱과 슬라이싱이 가능해지므로 간단한 위치 기반의 추출은 시리즈객체.str[]와 같은 형태를 통해 처리할 수 있다.
 - 이외의 문자열 처리는 str의 여러 하위 메소드를 사용해야 한다. 
"""

import pandas as pd

# 데이터프레임 불러오기
df = pd.read_csv('data/예제/University_text_before.csv', encoding = 'CP949')
addr = df['주소']
print(addr)

# str.strip(to_strip = None) : 선행 및 후행 문자를 제거
print("\n str.strip(to_strip = None)")
addr_strip = df['주소'].str.strip(to_strip = '_^!#? /%')
print(addr_strip)

# str.lstrip(to_strip = None) : 선행 문자를 제거
print("\n str.lstrip(to_strip = None)")
addr_lstrip = df['주소'].str.lstrip(to_strip = '_^!#? /%')
print(addr_lstrip)

# str.rstrip(to_strip = None) : 후행 문자를 제거
addr_rstrip = df['주소'].str.rstrip(to_strip = '_^!#? /%')
print(addr_rstrip)

"""
대소문자 변경
.str.lower() : 모두 소문자로 변경
.str.upper() : 모두 대문자로 변경
.str.swapcase() : 소문자는 대문자, 대문자는 소문자로 변경
"""