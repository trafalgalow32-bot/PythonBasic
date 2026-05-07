# dictionary.py

"""
하나의 변수에 이름과 순서가 있는 여러 개의 자료를 동시에 저장하기 위한 데이터 타입.
키(key)와 값(value)의 쌍으로 구성되어 있으며(해시 구조 형태), iterable한 객체이다. 
"""

dic_1 = {'A':1, 'B':2, 'C':3}
print(dic_1)

dic_2 = {1:'A', 2:'B', 3:'C'}
print(dic_2)

dic_3 = dict(A = 1, B = 2, C = 3)
print(dic_3)

"""
키는 불변한 객체 타입만 허용되므로 리스트 등은 키가 될 수 없다. 
키는 중복될 수 없고 고유해야 하기 때문에 동일한 키를 추가할 경우 기존의 키의 값 대신에 새로운 값이 덮어쓰기 된다. 
"""

dic_1['D'] = 4
print(dic_1)

dic_2[4] = 'D'
print(dic_2)

dic_1['A'] = 7
print(dic_1)
"""
다른 시퀀스형(문자열, 리스트, 튜플)과 달리 인덱스가 아닌 키를 이용해 값을 조회할 수 있다. 
"""
dic = {'A':1, 'B':2, 'C':3}
print(dic['A'])
print(dic['C'])

"""
딕셔너리 타입의 주요 메서드(내장함수)
.keys() 딕셔너리객체의 키로 구성된 리스트를 반환
.values() 딕셔너러객체의 값으로 구성된 리스트를 반환
.items() 딕셔너리객체의 키, 값 쌍으로 구성된 리스트를 반환
.update({key:value}) 딕셔너리객체의 키, 값 쌍으로 수정하거나 추가함
"""
dic.keys()
# dict_keys(['B', 'C'])

dic.values()
# dict_values([2, 3])

dic.items()
# dict_items([('B', 2), ('C', 3)])

dic.update({'D':7})
print(dic)