#sequencemethod.py

# 시퀀스형 데이터 타입의 주요 메소드 : sequenceobj.index(element), sequenceobj.count(element)

Str = 'dbbac'
List = [5,1,3,3,9]
Tuple = (6,10,3,4,10)
Range = range(2,13,3)

# 메소드.index(요소), 시퀀스 객체 내 해당 요소의 위치 인덱스 번호
Str.index('a')
print(Str.index('a'))

List.index(1)
print(List.index(1))

Tuple.index(3)
print(Tuple.index(3))

Range.index(11)
print(Range.index(11))

# 메소드 .count(요소), 시퀀스 객체 내 해당 요소의 빈도
Str.count('b')
print(Str.count('b'))

List.count(3)
print(List.count(3))

Tuple.count(10)
print(Tuple.count(10))

Range.count(11)
print(Range.count(11))
