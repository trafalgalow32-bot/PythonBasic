#conditional.py
# if ( i > 5 ) { # 자바, 자바스크립트 방법

# } else {

# }
# if 조건식:
#       실행할 코드

num = 10
if num > 5:
    print("크다")
    print("10이 크다")
elif num < 5:
    print("작다")
    print("5보다 작다")

# 변수 apple의 갑이 10이상이라면 1봉지 라고 출력
# apple  값이 10개 미만이라면 개당 2000원 출력
apple = 11
if apple >= 10:
    print("1봉지")
# elif apple < 10:
else:
    print("개당 2000원")