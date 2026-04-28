# typing(곧삭제).py

import random

fruits = [
    {"name":"사과", "price":3000, "stock":20},
    {"name":"바나나", "price":1500, "stock":30},
    {"name":"포도", "price":5000, "stock":11},
    {"name":"복숭아", "price":4000, "stock":8},
    {"name":"수박", "price":9900, "stock":34}
]

sales = [] # 판매 기록 용
admin = {"id":"admin", "pw":"1234"} # 관리자 로그인

print("\n============ 과일 재고 관리 프로그램 ============\n")

userId = input("아이디 : ").strip().lower()
userPw = input("비밀번호 : ").strip().lower()

if userId == admin["id"] and userPw == admin["pw"]:
    print("로그인 성공")
else:
    print("아이디 또는 비밀번호가 잘못되었습니다.")
    exit()

# 로그인 메뉴 실행
while True:
    print("\n==== 메뉴 ====")
    print("1. 과일 목록 보기")
    print("2. 과일 검색")
    print("3. 과일 판매")
    print("4. 재고 확인")
    print("5. 과일 추천")
    print("6. 판매 기록 보기")
    print("0. 종료")

    menu = input("메뉴 선택 : ").strip()

    if menu == "1":
        print("목록")
        for fruit in fruits:
            print(f"{fruit['name']} / 가격 : {fruit['price']}원 / 재고 : {fruit['stock']}개")
    elif menu == "2":
        print("검색")
        keyword = input("검색어 입럭 : ").strip()

        result = [ fruit for fruit in fruits if keyword in fruit["name"]]

        if result :
            for f in result:
                print(f["name"], f["price"], "원 / 재고 ", f["stock"], "개")
        else:
            print("검색 결과가 없습니다.")

# def sum3(*args): # *arguments의 줄임말, 받으면 튜플로 받아들인다.
#     return sum(args), type(args)
# sum3(1,2,3,4,5,6,7,8,9,10)

# print(sum3(1,2,3,4,5,6,7,8,9,10))

# def mean1(**kwargs): #kwargs : keyword argument의 줄임말
#     print(type(kwargs))
#     return sum(kwargs.values())
# mean1(a=1,b=2)
# print(mean1(a=1,b=2))