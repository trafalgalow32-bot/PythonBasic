#indexing.py

# 시퀀스형(문자열, 리스트, 튜플, range) 연산
String = 'DataEdu, Python!'
List = [0,1,2,3,4,5,6,7,8,9]
Tuple = (0,1,2,3,4,5,6,7,8,9)
Range = range(0,10,1)

# 문자열 인덱싱
print(String[0])
print(String[-1]) # 뒤에서부터 시작, 제일 뒤에서 한 글자
print(String[10]) # 앞에서부터 시작 10번에서 한 글자
print(String[-6]) # 뒤에서부터 6번에서 한 글자

# 리스트 인덱싱
print(List[0])
print(List[-1]) # 뒤에서부터 시작, 제일 뒤에서 한 원소
print(List[7]) # 앞에서 부터 7번에서 한 원소
print(List[-2]) # 뒤에서부터 2번에서 한 원소

# 튜플 인덱싱
print(Tuple[0])
print(Tuple[-1]) # 뒤에서부터 시작, 제일 뒤에서 한 원소
print(Tuple[7]) # 앞에서부터 7번에서 한 원소
print(Tuple[-2]) # 뒤에서부터 2번에서 한 원소

# range 인덱싱
print(Range[0])
print(Range[-1]) # 뒤에서부터 시작, 제일 뒤에서 한 숫자
print(Range[7]) # 앞에서부터 7번에서 한 숫자
print(Range[-2]) # 뒤에서부터 2번에서 한 숫자

# 인덱싱을 통한 리스트의 특정 객체 수정
List = [0,1,2,3,4,5,6,7,8,9]
List[0] = -1
List[-1] = 100 # 맨 뒤의 값을 100으로 수정
print(List)

""" 불가한 케이스들!
# 인덱싱을 통한 문자열의 특정 객체 수정(불가!)
String = 'DataEdu, Python!'
String[0] = 'd'

# 인덱싱을 통한 튜플의 특정 객체 수정(불가!)
Tuple = (0,1,2,3,4,5,6,7,8,9)
Tuple[0] = -1

# 인덱싱을 통한 range의 특정 객체 수정(불가!)
Range = range(0,10,1)
Range[0] = -1"""