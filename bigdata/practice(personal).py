# 문제1. 아래 점수 리스트를 보고, 각 점수에 해당하는 등급을 출력하는 코드를 작성하세요.
scores = [92, 75, 60, 88, 45, 53, 70]

# 오답
# if scores >= 90:
#     print("A")
# elif scores >= 80:
#     print("B")
# elif scores >= 70:
#     print("C")
# elif scores >= 60:
#     print("D")    
# else:
#     print("F")

for score in scores:        # score에 하나씩 들어옴
    if score >= 90: # print(f"{score}점 → 등급") f-string 구문!
        print(f"{score}점 -> A")
    elif score >= 80:
        print(f"{score}점 -> B")
    elif score >= 70:
        print(f"{score}점 -> C")
    elif score >= 60:
        print(f"{score}점 -> D")
    else:
        print(f"{score}점 -> F")

#문제2. 아래 숫자 리스트에서 짝수만 골라 출력하고, 그 합계도 같이 출력하세요.
# numbers = [3, 8, 15, 22, 7, 14, 9, 6, 31, 20]
# 짝수: [8, 22, 14, 6, 20]
# 합계: 70

numbers = [3, 8, 15, 22, 7, 14, 9, 6, 31, 20]

even_numbers = []


for number in numbers: # Python에서 for는 괄호 불필요!
    if (number % 2 == 0): # 비교 연산자 쓸 것! Python에서는!
        even_numbers.append(number)

total = sum(even_numbers) # 파이썬에서는 들여쓰기에 따라 적용 범위가 정해짐! 
print("짝수: " + str(even_numbers))
print("합계: " + str(total))