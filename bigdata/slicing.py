# slicing.py

"""
슬라이싱 : 시퀀스형 데이터의 일부를 잘라내는 것(추출하는 것)
"""
# 시컨스형(문자열, 리스트, 튜플, range) 슬라이싱
# 문자열 슬라이싱
String = 'DataEdu, Python!'
# 0번과 7번 사이의 객체를 추출!
print(String[0:7])
print(String[:7])

# 9번과 16번 사이의 객체를 추출함
print(String[9:])
print(String[9:16])

# 4번과 7번 사이의 객체를 추출함
print(String[4:7])

# List 슬라이싱
List = [0,1,2,3,4,5,6,7,8,9]
# 0번과 2번 사이의 객체를 추출함
print(List[0:2])
print(List[:2])
# 6번과 10번 사이의 객체를 추출함
print(List[6:])
print(List[6:10])
# 3번과 7번 사이의 객체를 추출함
print(List[3:7])

# Tuple 슬라이싱
Tuple = (0,1,2,3,4,5,6,7,8,9)
#0번과 2번 사이의 객체를 추출함
print(Tuple[0:2])
print(Tuple[:2])
#6번과 10번 사이의 객체를 추출함
print(Tuple[6:])
print(Tuple[6:10])
#3번과 7번 사이의 객체를 추출함
print(Tuple[3:7])

# range 슬라이싱
Range = range(0,10,1)
# 0번과 2번 사이의 객체를 추출함
print(Range[0:2])
print(Range[:2])
# 6번과 10번 사이의 객체를 추출함
print(Range[6:10])
print(Range[6:])
# 3번과 7번 사이의 객체를 추출함
print(Range[3:7])

"""
연결:여러 개의 시퀀스형을 연결. "+" 연산자를 이용하여 연결 가능하지만, range는 불가! 
반복:시퀀스형을 원하는 횟수만큼 반복하는 것을 의미하며 "*" 연산자를 이용하여 가능. range는 불가!
길이 정보:내장 함수인 len()을 통해 시퀀스형의 길이 정보 확인 가능
"""