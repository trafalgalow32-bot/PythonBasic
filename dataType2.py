# #dataType2.py

# # 딕셔너리
# # 딕셔너리는 데이터를 key와 value로 저장하는 자료형

# info = {"name" : "이순신"}
# print( info["name"]) # index 대신 key를 사용!

# """# list에서 데이터 추출
# m = ["이순신", 34, "군인"] 
# print(m[0])
# print(m[1])
# """ # m[0] -> 이름인지, 나이인지, 직업인지 알 수 없다.

# info = {"name" : "이순신" , "age" : 20, "job" : "군인"}
# print(info["job"])

# # 딕셔너리는 언제 사용하는가?
# # 로그인 회원이나, 상품정보, 단일게시글 정보, 설정값
# # JSON 데이터, API 응답데이터용
# mem = dict()

# print(info.get("city")) # 존재하지 않는 키 입력 시 결과값 "none" 표출

# info["city"] = "대전" # 딕셔너리에 키와 값 추가

# print(info)

# city = info.pop("city") # 딕셔너리 삭제
# print(city)
# print(info)
# del info["age"]

# if "city" in info: # 딕셔너리에서 키 존재 여부 확인
#     print("도시 정보 있다.")
# else:
#     print("도시 정보 없다.")

# if "김유신" in info.values(): # 딕셔너리에서 값 존재 여부 확인
#     print("우리 멤버야!")
# else:
#     print("그런 사람 없어!")

# k, v = info.items()

# print(type(k), type(v)) #  tuple 타입으로 나옴!
# print(k, v)

# # 딕셔너리에 key로 사용가능한 것
# # 문자열, 정수, 실수, 튜플

# info = {
#     "id" : 1004,
#     "email" : "hahaha@naver.com",
#     "name" : "이순신",
#     "address" : "대전 광역시 중구 선화동 방산빌딩 2층 203호"
# }

# # 이름이 이순신이냐?
# if "name" in info:
#     if info["name"] == "이순신":
#         print("이순신이다.")
#     else:
#         print("이순신이 아니다")
# else: 
#     print("이름 정보가 없습니다.")

# # 이메일의 도메인은 무엇인가?
# if "email" in info:
#     email = info["email"] # 딕셔너리에서 email키의 값 가져오기
#     # domain = email.split("@")[1]
#     # print(domain)

#     domain = email[email.index("@")+1 : ]
#     print(domain)

# # 주소가 잘못 저장되었다. 선화동 아니고 대흥동이다. 수정하시오!
# if "address" in info:
#     addr = info["address"]
#     addr = addr.replace("선화동","대흥동")
#     print(addr)
#     info["address"] = addr

# print(info)

# nums = []
# for i in range(1,5,1):
#     nums.append(i*2)
# print(nums)

# #컴프리헨션(comprehenion)
# # [표현식  for 변수 in 반복대상]
# nums2 = [i*2 for i in range(1,5,1)]
# print(nums2)

# # 1 ~ 15까지 숫자중에서 3의 배수만 리스트에 저장하겠다. 
# # nums3 = [i*3 for i in range(1,6,1)] i에 3을 곱하는 방식으로도!
# nums3 = [i for i in range(1,16,1) if i % 3 == 0]
# print(nums3)

# cost = [4500, 6700, 3100, 5800, 2700, 4900]
# # cost 리스트에는 상품의 가격이 저장 되어 있다. 
# # 5000 이하만 저가형, 5000 초과는 고가형

# # for v in cost:
# #     if v <= 5000:
# #         print("저가형")
# #     else:
# #         print("고가형")
# result = ["저가형" if p <= 5000 else "고가형" for p in cost ]
# print(result)

# # 학생 성적 관리 프로그램 만들기, 과목: 국어, 수학, 영어
# std1 = [89, 56, 73]
# std2 = [45, 87, 35]
# std3 = [81, 85, 94]
# std4 = [90, 34, 61]
# std5 = [59, 63, 70]
# stdName = ["이순신", "임꺽정", "한석봉", "정약용", "김춘추"]

# """{
#     "이순신": {"국어": 89, "수학": 56, "영어":73},
#     "임꺽정"
#  } 이와 같이 하면 일일이 다 입력해야 하니 번거로움! 반복문을 이용합시당!""" 

# std = std1, std2, std3, std4, std5
# print(type(std))
# score = dict()

# #과목명 튜플
# subject = ("국어", "수학", "영어")

# for i, name in enumerate(stdName):
#     temp = dict()
#     for k, s in enumerate(std[i]):
#         temp[subject[k]] = s
#     score[name] = temp

# # 한석봉 학생의 성적을 출력하시오
# print(score["한석봉"])
# for k, v in score["한석봉"].items():
#     print(k, v)

# print(score)

# # 문제 1. 딕셔너리를 만드세요

# snackName=["새우깡","칙촉","마가렛","짱구","포카칩","초코하임"]
# price = [2000, 3200, 4500, 3000, 2800, 4200]

# # for i, name in enumerate(snackName):
# #     print(f"{name}: {price[i]}원")

# snack = dict()
# for i, k in enumerate(snackName):
#     snack[k] = price[i]
# print(snack)

# snack2 = { k:price[i] for i,k in enumerate(snackName)}
# print(snack2)

# # 문제 2. 딕셔너리를 만들고 다음 조건으로 조회하세요.

# item = ["선풍기", "냉장고", "에어컨", "TV", "컴퓨터", "노트북", "청소기"]
# brand = ["LG", "삼성", "LG", "삼성", "HP", "DELL", "다이슨"]
# price = [80000, 1250000, 850000, 1540900, 2300000, 1570000, 534000]

# # item, brand, price의 각 인덱스 매칭이다. 
# # 선풍기는 LG이고 금액은 80000원이다.
# # 딕셔너리의 키는 제품명, value는 브랜드와 금액
# # 삼성 브랜드의 제품명과 금액을 출력하세요. 
# """for name in item:
#     print(name) 이렇게가 그냥 나열"""

# # bandp = dict(brand) # 우선 빈 딕셔너리를 설정해야! 
# # bandp = {}

# # for i, k in enumerate(item):
    
# # print(bandp)

# # for i in range(len(item)):
# #     bandp[item[i]] = [brand[i], price[i]]
# # # print(bandp)

# # print("--- 삼성 제품 목록 ---")
# # for name, info in bandp.items():
# #     # info[0]은 브랜드, info[1]은 가격입니다.
# #     if info[0] == "삼성":
# #         print(f"제품명: {name}, 가격: {info[1]}원")

# # 강사님 풀이
# product = dict()
# for i, k in enumerate(item):
#     product[k] = {"brand":brand[i], "price":price[i]}

# product = { k:{"brand":brand[i], "price":price[i]}
#            for i, k in enumerate(item)}
# print(product)

# for k , v in product.items():
#     if v["brand"] == "삼성":
#         print(k , v["price"])

# # set - 중복 허용하지 않고, 순서가 없는 자료형 (중복된 값을 넣어도 덮어쓰기 되어 한 번만 출력!)
# # 데이터 정리, 검색

# data = {1,2,3,4,5,3,4,5,3,4,5} # 키 없이 값만!!
# print(data)
# set1 = set() # 비어있는 set 만들기

# list = ["이순신", "김춘추", "장영실", "이순신", "장영실"]
# set2 = set(list)
# print(set2)
# # print(set2[1]) # *인덱스 접근 불가*(순서가 없으므로!)

# set2.add("한석봉") # set에 값 추가
# print(set2)

# set2.update(["정약용", "문익점", "이성계"]) # 여러 개 추가
# print(set2)

# set2.remove("한석봉") # 삭제 (단, 존재하는 데이터를 삭제해줘야!)
# print(set2)

# set2.discard("한석보") # 삭제 (존재하지 않는 데이터 삭제해도 오류 안뜸!!)
# print(set2) 

# # set 안에 값이 존재하냐 -> in

# # 교집합, 합집합, 차집합
# a = {"복숭아", "배", "메론", "체리", "포도"} # 도헌
# b = {"사과", "배", "딸기", "바나나"} # 찬용
# c = {"바나나", "참외", "사과", "귤", "포도", "딸기", "토마토"} # 현규

# print( a & b ) # 교집합
# print( a | c ) # 합집합 
# print( b - c ) # 차집합
# print( a ^ c ) # 대칭차집합(합집합에서 공통요소를 빼버린!)

# for fruit in c:
#     print(fruit)

# """
#     list - 다수의 데이터 저장용으로 많이 사용, 중복 허용, 추가 / 수정 / 삭제 가능
#     tuple - 다수의 데이터 저장 기능, 중복 허용, 추가 / 수정/ 삭제 불가능
#     dict - key : value 구조, key는 중복 안됨
#     set - 중복허용하지 않음, 순서 없음, 검색, 그룹(집합)에 사용
# """
# #↑ 여기까지 잠시 주석 처리(과일 관리 프로그램 때문에!)

# 과일 가게 재고 관리 프로그램
# 과일 데이터
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
        keyword = input("검색어 입력 : ").strip()

        result = [ fruit for fruit in fruits if keyword in fruit["name"] ]

        if result :
            for f in result:
                print(f["name"], f["price"], "원 / 재고 ", f["stock"], "개")
        else:
            print("검색 결과가 없습니다.")
            
    elif menu == "3":
        print("판매")
    elif menu == "4":
        print("재고")
    elif menu == "5":
        print("추천")
    elif menu == "6":
        print("기록")
    elif menu == "0":
        print("종료")
        break
    else:
        print("잘못된 메뉴입니다.")
