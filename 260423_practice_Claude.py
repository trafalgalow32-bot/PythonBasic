#260423_practice_Claude.py
"""문제A. "월요일,화요일,수요일,목요일,금요일"
위 문자열을 나누어 각 요일을 출력하세요."""

print("==================문제A==================")
day = ["월요일" ,"화요일","수요일","목요일","금요일"]
for item in day:
    print(item)

"""day = "월요일,화요일,수요일,목요일,금요일"
for item in day.split(","):
    print(item)"""

"""문제B.커피숍 메뉴 주문 시스템입니다.
주문 가능한 메뉴는 아래 4가지뿐입니다.
아메리카노, 카페라떼, 카푸치노, 에스프레소
input으로 메뉴를 입력받아 주문 가능 여부를 출력하세요. """

print("==================문제B==================")
menu = ["아메리카노", "카페라떼", "카푸치노", "에스프레소"]

# for pick in menu:
    # pick = input()
    # if( pick == menu):
    #     print("주문 하신 음료 나왔습니다.")
    # else:
    #     print("그런 메뉴 없습니다")

while True:
    print("음료를 주문해주세요 : 아메리카노, 카페라떼, 카푸치노, 에스프레소")
    pick = input()
    if pick not in menu:
        print("그런 음료 없습니다!")
    else:
        print("주문하신 음료 나왔습니다.")
        break

print("==================문제C=================")
"""직원별 이번 달 성과급이 지급되었다. 총 지급액이 얼마인지 출력하시오.
kim = "1,250,000원"
lee = "870,500원"
park = "3,015,750원"
"""
salary = ["1,250,000원", "870,500원", "3,015,750원"]
total = sum(int(item.replace(",","").replace("원","")) for item in salary)
print(str(total) + "원")

"""문제D. 아래 문장에서 단어별로 나누고, 각 단어의 첫 글자만 모아서 출력하세요.
"Python is very fun and powerful"
출력 예시: P i v f a p"""
print("==================문제D=================")
sentence = "Python is very fun and powerful"
# print(sentence.split(" "))
words = sentence.split(" ")
for word in words:
    print(word[0], end=" \n") # print 시 옵션 부여: 맨 끝에 " " 공백 부여하여 한 줄로 출력!

print("==================문제E=================")
"""문제E. 숫자를 input으로 입력받아 짝수면 "짝수입니다", 홀수면 "홀수입니다" 출력하고, 
0을 입력하면 종료되는 프로그램을 만드세요. 단, 숫자가 아닌 값을 입력하면
"숫자만 입력하세요!" 를 출력하고 다시 입력받으세요."""
while True:
    print("===숫자를 입력하세요===")
    num = input()
    if num.isnumeric() and int(num) % 2 == 0:
        print("짝수입니다.")
        break
    elif num.isnumeric() and int(num) % 2 != 0:
        print("홀수입니다.")
        break
    else:
        print("숫자만 입력하세요!")    

# 다른 풀이 (try ~ except 예외처리)
"""while True:
    try:
        num = int(input("===숫자를 입력하세요==="))
        # 여기서부터 짝수/홀수/0 처리 하면 돼요!
    except ValueError:
        print("숫자만 입력하세요!")"""

"""문제F. 아래 직원 데이터에서 급여가 300만원 이상인 직원의 이름과 급여만 출력하세요.
employees = {
    "김철수": 2_800_000,
    "이영희": 3_500_000,
    "박민준": 4_100_000,
    "최지우": 2_450_000,
    "정하늘": 3_200_000
}

# 출력 예시
# 이영희 : 3,500,000원
# 박민준 : 4,100,000원
# 정하늘 : 3,200,000원 """
employees = {
    "김철수": 2_800_000,
    "이영희": 3_500_000,
    "박민준": 4_100_000,
    "최지우": 2_450_000,
    "정하늘": 3_200_000
}
for name, salary in employees.items(): # items 뒤에 괄호()
    if salary >= 3000000:
        # print(employees.items()) # 내 실수
        print(f"{name} : {salary} 원")

