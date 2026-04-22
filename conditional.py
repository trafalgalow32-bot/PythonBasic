#conditional.py
# if ( i > 5 ) { # 자바, 자바스크립트 방법

# } else {

# }
# if 조건식:
#       실행할 코드

# num = 10
# if num > 5:
#     print("크다")
#     print("10이 크다")
# elif num < 5:
#     print("작다")
#     print("5보다 작다")

# # 변수 apple의 갑이 10이상이라면 1봉지 라고 출력
# # apple  값이 10개 미만이라면 개당 2000원 출력
# apple = 11
# if apple >= 10:
#     print("1봉지")
# # elif apple < 10:
# else:
#     print("개당 2000원")

# #match case(자바, 자바스크립트의 switch문과 유사!) - 정수값만 표현 가능!
# res = 2
# match res:
#     case 1:
#         print("숫자 1이다")
#     case 2:
#         print("숫자 2이다")
#     case int():
#         print("정수이다")

# # like 좋아요 변수의 값이 100 이상이면 spot 등록 출력
# # 좋아요 변수의 값이 10 이하라면 관심 spot 출력
# like = int(input())
# if like >= 100:
#     print( "spot 등록")
# elif like <= 10:
#     print( "관심 spot")

# # 아이디와 비밀번호 입력 받아 일치하면 로그인 성공, 불일치하면 아이디 또는 비밀번호가 잘못되었습니다.  출력
# # 아이디는 진섭, 비밀번호는 babo
# id = input("ID 입력 :")
# pw = input("PW 입력 :")
# if id == '진섭' and pw == 'babo':
#     print( "로그인 성공")
# else:
#     print("아이디 또는 비밀번호가 잘못되었습니다.")

# 파이썬에서 문자열 포함여부 확인하는 방법
# word = "나는 김진섭입니다."
# if '김진섭' in word: # cf) word in '김진섭'으로 해도 없다를 출력함... 영어 어순에 유의!
#     print("있다")
# else:
#     print("없다")

# #Another example (문자열 포함 여부) - word 안에 동렬이라는 이름이 없다라는 것을 출력하세요
# word = "나는 진섭이가 짝꿍일 때 별로였다."
# if '동렬' in word:
#     print("있네!")
# else:
#     print("동렬이 없다!")

# startswith() 함수 시작 문자열 비교
# word = "차도헌님께서 입장하셨습니다."
# if word.startswith('이창호') :
#     print("신원 확인 ")
# else:
#     print("이창호님이 아닙니다.")

# 대소문자 변환
# word = "I like banana"
# print( word.upper()) # 대문자
# print( word.lower()) # 소문자
# print( word.title()) # 대문자 - 단어의 첫 글자만

# # 공백제거 - 개발시 필요필수 (이거 때문에 오류나면 골치아픔!)
# word = " banana "
# print ( word ) # 공백제거없이
# print (word.strip()) # 양쪽공백제거
# print (word.lstrip()) # 왼쪽공백제거
# print (word.rstrip()) # 오른쪽공백제거

# # 찾기
# word = "찬용이는 진섭이보다 지금이 좋다고 한다."
# # print (word.find("진섭")) # 있다면! 0번부터 시작되는 인덱스!
# # print (word.index("동렬")) # 인덱스 반환, 없으면 error

# # 문자열 바꾸기 .replace("현재 문자열에서 변경할 문자열", "교체할 문자열")
# word = word.replace("찬용이", "성현이")
# print(word)

# # 문자열 나누기 - 배열
# text = "도헌-지연-동렬-진섭"
# result = text.split("-")
# print(result)

# # 배열을 하나의 문자열로 합치기
# # text = result.join
# text = ",".join(result)
# print( text )

# # 숫자 여부!
# text = "12345"
# print (text.isdigit()) # 문자열을 숫자로 변환하기 전에 확인!

# # 문자 종류 확인
# text1 = "tomato"
# text2 = "banana  "
# text3 = "사월22"
# print(text3.isalpha()) # 문자만 있는지 여부 확인!
# print(text2.isspace()) # 공백만 있는지 여부 확인!
# print(text3.isalnum()) # 문자+숫자 여부 확인!

# # 문자열 정렬
# text = "15"
# print (text.zfill(6)) # 함수 () 안에 자릿수 넣기
# print (text.rjust(4)) 
# print (text.ljust(5))

# # 문제1. - 공백제거와 소문자 변환을 하려면? 
# # input으로 입력 받아서 공백제거와 소문자 변환을 하세요.
# senten = input()
# print(senten.replace(" ","").lower()) # 다른 풀이: result = text.strip().lower() // print (result)

# 문제2. "행복,우울,기쁨,슬픔,화남"
# 위 문자열을 나누어 보세요.
# feel = "행복,우울,기쁨,슬픔,화남"
# result = feel.split(",")
# print(result)

# 문제3. 회원가입시 이메일 입력 하는데 특정 주소만 가능하다. 
# naver.com, gmail.com, nate.com, daum.net <- 이렇게 4개만 가능하다. 
# input으로 메일을 입력받아서 가능인지 불가능인지 출력할 것!
# email = input("이메일 입력: ")
# domain = ("naver.com", "gmail.com", "nate.com", "daum.net") # 도메인 하나 하나(요소)를 괄호 안에....
# # if ('naver.com' or 'gmail.com' or 'nate.com' or 'daum.net') in email: # 복잡한 풀이(내가 한거!)
# #     print("쌉가능")
# # elif 'gmail.com' in email:
# #     print("쌉가능")
# # elif 'nate.com' in email:
# #     print("쌉가능")
# # elif 'daum.net' in email:
# #     print("쌉가능")
# if email.endswith(domain):  # 모범 답안 (깔끔하게!)
#     print("쌉가능")
# else:
#     print("올바른 이메일이 아님...")

# 문제4. 금액 계산하기
# 각 업체별로 입금이 되었다. 총액이 얼마인지 출력하시오. 
"""나의 못난이 풀이 ㅋㅋ
coupang = "135,900원"
naver = "540,000원"
FiveDrone = "2,340,090원" 
# solution : , 기준으로 숫자만 추출, "원" 문자 제거!
sum = int((coupang.replace(",","").replace("원",""))) + int((naver.replace(",","").replace("원",""))) + int ((FiveDrone.replace(",","").replace("원","")))
print(sum) """

# 좀 더 깔끔한 풀이 (배열에 넣는 방법, 그리고 각 항목들에 대해 , 원 제거한 변수를 따로 선언 후 죄다 더하기!)
coupang = "135,900원"
naver = "540,000원"
FiveDrone = "2,340,090원" 
data = ["135,900원", "540,000원", "2,340,090원"]
total = sum(int(item.replace(",","").replace("원","")) for item in data)
print(total) 