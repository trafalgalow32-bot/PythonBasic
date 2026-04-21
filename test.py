# print("wow")
# num = 10
# num2 = 30
# result = num + num2
# print(result)
# # 파이썬의 자료형
# # 문자열, 정수, 실수, Boolean 
# # 문자열 입력시 '' 작은 따옴표는 고유 명사! 
# name = "KIM"
# print( name )
# job = "none"
# print( name + job + " 이다")
# print("I'm hungry " * 5)
# radius = 5 # 변수명 한글로도 가능!
# print (radius)
# pi = 3.14
# print(radius * 2 * pi)
# is_student = True #boolean (True / False 첫글자 반드시 대문자로!)
# is_food = False
# print(is_student)
# print(type(pi))
# # Python에서 키보드 통해 입력 받기(Java의 Scanner 역할)
# num = input("정수입력 : ")
# num = int(num) # 문자열을 정수로 형변환! str () 문자열로 변환! bool () boolean으로 변환! 
# print( num + 10 )
# """여러줄 주석 걸기 """

# # 문제. 너비와 높이를 입력받아 사각형의 넓이를 출력하세요. 
# w = input("너비") 
# # w = int(input("너비: ")) // 다른 풀이 : 변수 선언과 동시에 형변환
# w = int(w)
# h = input("높이") 
# # h = int(input("높이: ")) // 다른 풀이 : 변수 선언과 동시에 형변환
# h = int(h)
# # s = w * h 
# # print(s)
# print(w * h) # 다른 풀이

# 연산자 - 비교, 논리, 증감, 대입, 산술
# 산술연산자 / 나누기, 곱하기, 거듭제곱
print(10 / 3) 
print(10 // 3) # 몫
print(10 % 3) # 나머지
print( 2 * 3 )
print ( 2 ** 3 ) # 거듭제곱 **

# 논리연산자
num = 10
print( num > 5 and 110 > 50 ) # 기호(&&)로 쓰지 않고, 영어로 쓴다!
print( not num > 5 )

# 복합 대입 연산자 : a = a + 5 -> a += 5
# 조건연산자 ( 삼항 연산자 )
# 조건식 ? 참일 경우 : 거짓일 경우 < = 파이썬에는 없다!!!
# 파이썬에는 조건 연사자가 없다. 조건문으로!
