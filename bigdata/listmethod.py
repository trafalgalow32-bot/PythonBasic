# listmethod.py

# 리스트객체에서만 사용되는 주요 메서드(*다른 시퀀스형에는 사용 불가!)
"""
.append(ele) 리스트객체의 맨 뒤에 요소를 추가
.insert(idx ,ele) 리스트객체의 특정 인덱스에 요소 추가
.remove(ele) 리스트 객체에서 처음으로 나오는 요소를 제거
.pop() 리스트 객체의 마지막 요소 삭제 후 마지막 요소 반환
.sort(reverse=False) 리스트 객체의 요소를 오름차순으로 정렬 => reverse=False는 오름차순, 생략 가능1 
                                                         reverse=True는 내림차순
.reverse() 리스트 객체의 요소 순서를 역순으로 대치
.copy() 리스트 객체를 복사
"""

List = [5, -1, 6, 7, 1, 3]

List.append(2)
print(List)

List.insert(3,8)
print(List)

List.remove(8)
print(List)

List_2 = List.pop()
print(List)
print(List_2)

List.sort()
print(List)

List.sort(reverse=True)
print(List)

List = [5, -1, 6, 7, 1, 3]
List.reverse()
print(List)