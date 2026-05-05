# textdata.py

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
df = pd.read_csv('data/예제/University_text_after.csv', encoding = 'CP949')
# print(df)

print("시리즈객체.str[]")
# 시리즈객체.str[] : 단순하게 인덱싱과 슬라이싱 가능
addr = df['주소'].str[0:5]
print(addr)

print("\n str.startswith(pat)")
# sts.startswith(pat) : pat(문자열)로 시작한다면 True, 아니면 False 반환
addr_seoul_bool = df['주소'].str.startswith("서울")
print(addr_seoul_bool)

print("\n 주소가 '서울'로 시작하는 데이터셋 추출")
addr_seoul = df[df['주소'].str.startswith("서울")]
print(addr_seoul)

print("\n 주소가 '서울'로 시작하지 않는 데이터셋 추출")
addr_notseoul = df[~df['주소'].str.startswith("서울")] # ~는 부정!
print(addr_notseoul)

print("\n str.endswith(pat)")
# sts.endswith(pat) : pat(문자열)로 끝난다면 True, 아니면 False 반환
addr_univ_bool = df['대학이름'].str.endswith("대학교")
print(addr_univ_bool)

print("\n 대학이름이 '대학교'로 끝나는 데이터셋 추출")
addr_univ = df[df['대학이름'].str.endswith("대학교")]
print(addr_univ)

print("\n 대학이름이 '대학교'로 끝나지 않는 데이터셋 추출")
addr_univNot = df[~df['대학이름'].str.endswith("대학교")]
print(addr_univNot)

# str.contains(pat) : pat(문자열 또는 정규식)이 포함되면 True, 아니면 False 반환
print("\n str.contains(pat)")
addr_matro_bool = df['주소'].str.contains('광역시')
print(addr_matro_bool)

print("\n 주소에 '광역시'를 포함하는 데이터셋 추출")
addr_metro = df[df['주소'].str.contains('광역시')]
print(addr_metro)

# str.split(pat=None) : pat을 기준으로 문자열을 분할
print("\n str.split(pat=None)")
addr_splitBlank = df['주소'].str.split() # 공백을 기준으로 분리
print(addr_splitBlank)

# str.find(sub, start=0, end=None) : sub가 있는 위치를 start에서부터 end까지에서 찾아 위치값을 반환
print("\n str.find(sub, start=0, end=None)")
addr_district_idx = df['주소'].str.find('구') # '구'가 있는 위치 인덱스
print(addr_district_idx)

# str.rfind(sub, start=0, end=None)
# sub가 있는 위치를 start에서부터 end까지에서 찾아 가장 높은 위치값을 반환
print("\n str.rfind(sub, start=0, end=None)")
addr_behind = df['주소'].str.rfind(sub = ' ') # 가장 뒤에 있는 공백 위치
print(addr_behind)

# str.findall(pat) : 모든 pat(문자열 또는 정규식) 항목을 반환
print("\n str.findall(pat)")
addr_end = df['주소'].str.findall('\w+구') # 구로 끝나는 단어들을 모두 반환
print(addr_end)

# str.replace(pat, repl) : pat를 repl로 대치함
print("\n str.replace(pat, repl)")
addr_replace = df['주소'].str.replace(" ", "_") # 공백을 '_'로 대치함
print(addr_replace)