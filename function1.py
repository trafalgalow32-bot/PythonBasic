# function1.py

# 제어자 반환타입 메서드 이름(매개변수)

# 파이썬 함수 - def 함수이름(매개변수):

def hi():
    print("안녕")

# 함수 실행 - 호출
# 함수이름() - () 소괄호에 매개변수가 있다면 넣어주기
hi()


def intro(name):
    print( name, "님 로그인 하셨습니다.")

name = "김유신"
if type(name) == str: # isinstance (name, str)
    intro(name)

intro("김현규")
intro("하늘소")
intro(1000)

def dataInput(a,b,c):
    print( a + b + c)

dataInput(1, 20 , 30)
# 함수를 만들 때(정의) 어떤 기능을 가진 함수를 만들 것인가
# 해당 기능이 작동되기 위해서 필요한 것이 무엇인가
# 필요한 것들이 함수 안에서 만들 수 있는 것인가 아니면 외부에서 받아야 하는 것인가

# 함수의 반환값 return - 함수가 호출된 위치로 값을 돌려보내는 작업

def add(num1, num2):
    return "계산 결과 ", num1 + num2

comment, res = add( 10, 20 )
print(comment, res)

# 변수의 범위 - 지역 변수, 전역 변수
number = 1000 # 전역 변수(함수 외부에서 선언한!), 따라서 어느 곳에서든 사용 가능!

def totalPrice( price ):
    total = 0 # 지역 변수 이므로 함수 내부에서만 사용 가능!!
    for money in price:
        total += money
    global number # 전역변수의 수정은 안된다! 함수 내에서! 앞에 global을 붙여줘야!
    number = total 

totalPrice ( [ 1,2,3,4,5] )
print( number )

# 문제1. 간단한 함수 만들기
# 사각형의 너비와 높이를 받아서 넓이를 출력하는 함수를 만들어 호줄해 보세요. 
def square(width, height):
    # return "사각형의 넓이 : 너비 X  높이 =", width * height
    res = width * height
    print("넓이는 : ", res)

# result = square(10, 20)
# print(result)
square(20, 5)

# 문제2. 아래 코드를 보고 함수를 만드세요. 
# 로그인 체크 함수 만들기
def login_check(id, pw):
    if id=="admin" and pw=="1234":
        return True
    else: return False

id = input("아이디를 입력하세요")
pw = input("비밀번호를 입력하세요")

if id=="admin" and pw=="1234": # 여기 부분을 함수로 처리될 수 있게!
    print("로그인 성공하였습니다.")
else: 
    print("아이디 또는 비밀번호를 잘못 입력했습니다.")

# 문제3. 상품의 재고를 확인하여 재고 충분, 재고 부족, 품절이라고 출력할 수 잇는 함수 만들기
# 재고 부족 기준은 현재 재고량이 8이하인 경우

item_stock = 12

def stockcheck(stock):
    if stock > 8:
        return "재고 충분"
    elif stock > 0:
        return "재고 부족"
    else:
        return "품절"

# 위 코드를 print( 함수 호출 ) 이렇게 실행하면 동작할 수 있게 함수를 만드시오! 
# print(stockcheck) # 이렇게 하면 주소값 보내줌
print(stockcheck(item_stock))

# 문제4. 회원가입을 한다. 아이디 중복체크 함수를 만드세요. 

id_list=["kim", "lee", "sky", "gold", "war123", "qwer12", "eeee14"]
# id_list는 현재 가입된 회원드르이 아이디만 저장된 리스트이다. 
# 아이디 중복체크 함수를 통해 사용가능, 불가능을 출력하세요. 
def id_check( id ):
    # if id == id_list:
    #     return "사용 불가능"
    # else:
    #     return "사용 가능"

    if id in id_list:
        return "사용 불가능"
    else: 
        return "사용 가능"
print( id_check("park"))

