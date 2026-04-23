# set.py

"""
집합형: 수학에서 다루는 집합.
리스트와 달리 순서가 없고, 중복을 허용하지 않으며, 불변한 객체 타입이므로 인덱싱이 불가, iterable한 객체
중괄호"{,}" 형태로 저장
set() 함수를 통해 빈 집합(공집합) 생성과 집합으로 데이터 타입을 변환 가능
집합형에서 가능한 연산은 교집합, 합집합, 차집합 등과 같은 집합 연산
"""

set_1 = {1,2,3,4}
set_2 = {'E', 'd', 'u'}
"""
집합 타입의 메소드(내장함수)
.add(ele) 집합객체에서 하나의 원소를 추가
.update(ele) 집합객체에서 여러 개의 원소를 추가
.union(set2) 집합객체1과 집합객페2의 합집합, 기호 "|"로도 가능
.intersection(set2) 집합객체1과 집합객체2의 교집합, 기호 "&"로도 가능
difference(set2) 집합객체1과 집합객체2의 차집합, 기호"-"로도 가능
"""

set_3 = {2,4,6,8,10}
set_4 = {4,8}

set_3.add(12)
print(set_3)

set_4.update({12,16})
print(set_4)

set_3.union(set_4)
print(set_3.union(set_4))

set_3.intersection(set_4)
print(set_3.intersection(set_4))

set_3.difference(set_4)
print(set_3.difference(set_4))