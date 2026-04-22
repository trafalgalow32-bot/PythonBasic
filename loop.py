# loop.py

# 아래 내용을 for 문으로 깔끔하게!!
# print("숫자 : 1")
# print("숫자 : 2")
# print("숫자 : 3")
# print("숫자 : 4")
# print("숫자 : 5")

"""for (int i=1; i<=5; i++)
    print("숫자" + i) <= 이렇게 자바식으로 하면 오류떠!"""

# 5번 반복하는 반복문
for i in range(5, 1, -1): 
    print("숫자 : " + str(i+1))

print("===========================")

for ch in "hello":
    print(ch)

print("===========================")

for name in ["차도헌", "박지연", "이성찬", "김진숙", "이동렬", "김현규"]:
    if name.startswith("이"):
        print(name)
print("==============문제 1=============")
# #문제1. 1부터 10까지의 총합을 구하세요. 반복문을 사용해서
sum = 0
for i in range(1, 11):
    sum = sum + i
print("총합 : " + str(sum))

print("==============문제 2=============")
# #문제2. ["15,000", "13,000", "8,700", "9,000", "25,000"]
# #배열에 출금 금액들이 저장되어 있다. 만원 이상 금액들에 대해 출력하세요.
"""고민만 한 현장 ㅋㅋ
money = ["15,000", "13,000", "8,700", "9,000", "25,000"]

# soulution : 우선 금액들이 전부 문자열이니, 숫자로 변환해 주어야! 또한 ,를 없애줘야!
change = int(money.replace(",",""))
print(change)"""

for money in ["15,000", "13,000", "8,700", "9,000", "25,000"]:
    if int(money.replace(",","")) >= 10000:
        print(money)

# 다른 풀이
for i in range( len(money) ):
    print("금액 : ", i , money[i])

for i, v in enumerate(money): # enumerate : 열거하다
    print(i, v )

print("==============문제 3=============")
# 문제 3. [89, 56, 78, 92, 61, 96, 83, 74]
# 203호 학생들의 성적이다. 성적의 총합과 평균을 출력하세요.
# 80점 이상인 학생들의 위치(인덱스)도 출력하세요.
sum = 0
avg = 0
score = [89, 56, 78, 92, 61, 96, 83, 74]
for v in score:
# 여기부터 Solution : 일단 점수들은 출력되어 나옴! 그렇다면 여기서 총합과 평균을 구해야만 한다!
    # print(scores)
    # sum = sum + int(scores)
    # print(sum(scores))

    #타입 체크
    # print(type(scores))
    sum = sum + v
    avg = sum / 8
print("총점 : " + str(sum) + ", 평균 : " + str(round(avg,2))) # round(n, 2) 소수점 둘째자리까지 반올림

# 인덱스 찾기!
score = [89, 56, 78, 92, 61, 96, 83, 74]
for i in range(len(score)):
    if score[i] >= 80:
        print(i)
    
for i, v in enumerate(score): # i = index, v = value 또한 range(len(score)) 보다는 enumerate를 더 널리 쓴다!
    if v >= 80:
        print(i)

# 반복문 while : 반복 횟수가 정해져 있지 X 
# 조건식이 참인 경우에 동작하기 때문에 쉽게 무한루프에 들어갈 수 있다. 
# 하여 while문 사용시 중단시킬 수 있는 break를 같이 사용하는 게 좋다.

# while 조건:
#     실행코드

# num = 5
# while num > 2:
#     print("2보다 크다")
#     break

while True: # 원하는 조건에 도달 시 break가 작동하도록 if문으로 조건을! 
    num += 1 # num = num + 1
    if num == 7: continue # 건너뛰기(for 문에서도 사용 가능!)
    print(num)
    if num == 10: break

print("===================================")
while True:
    cmd = input("명령어 입력 : ").strip().lower()
    if cmd == "history":
        print("모든 기록 출력")
    elif cmd == "mkdir":
        print("새로운 폴더 만들기")
    elif cmd == "remove":
        print("파일 삭제")
    elif cmd == "exit":
        print("종료")
        break
    else:
        print("존재하지 않는 명령어입니다.")

print("===================================")
# 동전 앞면 뒷면 맞추기 게임 만들기
import random

""" 수업 때 내가 이상하게 만든 것
coin = random.randint(1,2)
user = int(input("1. 앞면, 2. 뒷면 : "))
print(num)
while True:
    if coin == 0:
        print("뒷면입니다.")
    elif coin == 1:
        print("앞면입니다.")
        break
if coin == user:
    print("정답!")
else:
    print("땡!")"""

# 수업 후 복습
import random

while True:    
    coin = random.randint(1,2)
    user = int(input("1. 앞면, 2. 뒷면 : "))
    print("동전 면 : " + str(coin) + " 내가 지목한 면 : "+ str(user))
    if coin == user:
        print("정답")
        break
    else:
        print("오답 혹은 이상한 값 입력")

# n = random.randrange(1,3) # 1-9

# 가위바위보 게임 5판 진행
# 5번째 게임이 끝나면 몇승 몇패 몇무인지 출력
""" 내가 이상하게 적은!
while True:
    user = input("가위 바위 보 입력 : ")
    game = ["가위", "바위", "보"]
    n = random.choice(game)
    if user != game:
        print("가위 바위 보 똑바로!")
    elif user == n:
        print("무승부")
        break
    elif (user == "가위" and game == "바위") and (user == "바위" and game == "보") and (user =="보" and game == "가위"):
        print("당신의 패배입니다.")
        break
    else:
        print("당신의 승리입니다.")
        break"""

def compare(a,b):
    if a>b: return 1
    elif a<b: return -1
    else: return 0

game = ["가위", "바위", "보"]

win = lose = draw = 0
for i in range(5):
    com = random.choice(game)
    user = input("가위 바위 보 : ").strip()

    print("컴퓨터 : ", com , "나 : ", user )
    # 승 패 무 판단
    # game.index("가위")
    # 사전적 순서 비교 방법은 비교 연산자
    cidx = game.index(com)
    uidx = game.index(user)

    comp = cidx - uidx # 유저와 컴의 가위바위보 값 비교
    # 가위-0, 바위-1, 보-2 => 유저가 0 컴이 1이라면 컴의 승
    # 즉, comp에 1이 있다면 컴의 승

    if com == user: 
        print("무승부")
        draw+=1
    elif comp== -1 or comp== 2:
        print("나의 승!")
        win+=1
    else:
        print("나의 패!")
        lose+=1
print("승 : ", win, " 패 : ", lose, " 무 : ", draw)