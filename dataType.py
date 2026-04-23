# #dataType.py
# # List, Tuple
# # List - 여러 데이터를 저장 관리하기 위한 파이썬 자료 구조이다.
# # Tuple도 List와 유사하지만, List와 달리 수정이 불가능하다. 
# """ArrayList a = (Java)
# a.add(100)
# a.add(200)
# a.add(300)
# ...
# """
# # List - 순서 유지, 인덱스를 통해 접근. 추가 & 수정 & 삭제 가능
# # 다른 자료형도 저장 가능
# number = [10, 20, 30, 40, 50]
# empty  = [] # 비어 있는 List
# name = list() # 비어 있는 List

# print(number[0])
# print(number[-2])

# # List 자르기
# num = number[2:4]
# print(num)
# num2 = number[:3] # 0번 index부터 3번 index 전까지!
# print(num2)
# num3 = number[2:]
# print(num3)

# # List 값 수정
# number[2] = 100
# print(number)

# # List 값 추가
# """number[5] = 60
# print(number) # 이렇게 하면 오류남 ㅋㅋ"""

# number.append(60) # 새로운 값 추가하는!
# print(number)

# number.insert(2, 500) # (index, value)
# print(number)

# # List 값 삭제
# number.remove(100) # 삭제할 값 , *index 아님!!!!*
# print(number)
# number.pop(1) # List에서 삭제할 데이터의 index
# print(number)
# del number[2] # index 삭제!
# print(number)

# # List 크기 (길이)
# print(len(number))

# for num in number:
#     print(num)

# for i , num in enumerate(number): # index와 값 둘다 표현!
#     print(i, num)

# # List 검색
# print(40 in number) # 값의 존재 여부 True, False
# print(number.index(50)) # 50이라는 값을 가진 index를 가졌는지 여부! 
# # index를 통해 index를 찾기 전에 in으로 존재여부 먼저 확인하기!

# # List 정렬
# number.sort() # 기본값은 오름차순!
# print(number)
# number.sort(reverse=True)
# print(number)

# # List는 일반적으로 많이 사용되는 자료구조이다. 
# # Java에서 List (ArrayList)를 많이 사용한다면, Python에서는 List이다. 
# # 정렬, 검색도 되고 그래서 사용하기 좋은 녀석이다!! 

# # List 문제
# # 문제1. 5명의 이름이 저장되어 있는 List 만들기
# student = ["홍길동", "김현규", "차도헌", "이동렬", "박찬용"]
# # 5명의 이름 출력하는 반복문 만들기 
# for i, v in enumerate(student):
#     print(i, v)

# # 문제2. 정도전 이름 추가 후 출력
# student.append("정도전") # 원하는 위치 추가는 insert(index, value)
# print(student)

# # 문제3. List에 김유신이 있는지 확인하는 코드 작성
# # print("김유신" in student)
# # if 활용
# if "김유신" in student:
#     print("우리 멤버임")
# else:
#     print("등록된 이름 아님")

# # 문제4. 이름 List를 내림차순으로 정렬 후 출력
# student.sort(reverse=True)
# print(student)

# # 문제5. 과일의 이름이 두 글자인 과일만 출력하세요.
# fruits = ["사과", "바나나", "파인애플", "딸기", "오렌지", "포도", "배"]
# # print(fruits) # 전체 출력
# for item in fruits:
#     if len(item) == 2:
#         print(item)

# # 문제6. 과일 검색 프로그램 (input 이용)
# # 입력한 과일이 리스트에 있다면 판매중, 없다면 품절

# while True:
#     fsearch = input("==input fruits==").strip()
#     if fsearch in fruits:
#         print("On Sale")
#         break    
#     else:
#         print("Sold-Out")

# # fsearch = input("과일 입력 : ").strip()
# # for fruit in fruits:
# #     if fsearch == fruit:
# #         print("On Sale")
# #     else:
# #         print("Sold-Out")

# # 문제7. 구매 하고자 하는 과일을 입력하면 총 지불금액 얼마인지 출력
# # 단, 과일은 1개를 구매할 수도 있고 여러 개 구매할 수도 있어야 한다. 

# fruits.sort() # 딸기, 바나나, 배, 사과, 오렌지, 파인애플, 포도
# price = [5000, 8000, 12000, 9500, 15500, 20400, 9000]

# # fname = input("구매할 과일 :").strip()
# # famount = input("구매할 개수 : ")
# # # index 를 활용? fruits.sort() // price의 index를 서로 어떻게... ?? price[i] * famount
# # if fname in fruits.sort():

# fname = input("구매할 과일 :").split()
# total = 0
# for f in fname:
#     if f in fruits:
#         idx = fruits.index(f)
#         total += price[idx]
# print("총 금액 : ", total)

# # Tuple - List처럼 여러 데이터를 저장할 수 있는 자료형.
# # List와 달리 데이터 수정 불가! 목적은 데이터 보호! 데이터 추가(append, insert), 삭제(remove)도 안됨!!
# # 속도와 메모리 효율성
# # Dictionary의 key로 사용 (key는 바꿀 수 없고, value 값을 바꾸므로!)
# # 여러 개의 값을 반환(return) 시킬 때

# Tuple 만들기
number = (10, 20, 30, 40)
print(number)
print(type((1,2,3,4)))
print(type((10,))) # 값이 하나인 경우, 맨 끝에 "," 입력해야 Tuple로 인식!

print(number[1]) # index 0부터 시작
# number[0] = 100 <= 수정 안됨! 얘 실행하면 오류뜸!

# Tuple 슬라이싱 (자르기)
print(number[1:3] )

# Tuple 검색
print(10 in number)
print(number.index(20))

print(number.count(20)) # 특정값 갯수 구하기
data = 10, 20, 30 , 40 , 50 # 패킹: 여러값을 하나로 묶기 / 괄호 없이도 Tuple로 제작 가능
print(type(data)) # class tuple로 뜸!

a, b, c, d, e = data # 언패킹 - 묶여 있는 값을 여러 개로 나누기
print (a, b, c, d, e)

red = 20
blue = 10

red , blue = blue, red
print(red, blue)

# 함수 반환 여러 개
def get():
    return 10, 20, 30, 40

# list <--> tuple
info = ("다음주", "금요일", "빨간날", "그래서", "우리는", "5월6일에","봐요")
info_list = list(info)
info_list[0]="이번주"
print(info_list)

info = tuple(info_list)
print(info)