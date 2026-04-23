#range.py
#range(start,end,step)

range_1 = range(0, 10)
print(list(range_1))
range_2 = range(10)
print(list(range_2))
range_3 = range(10, 0, -1)
print(list(range_3))
range_4 = range(0) # 빈 열
print(list(range_4))

# 예시1. 0에서 시작해 2 간격으로 증가하고 10을 포함하지 않는 숫자열(0,2,4,6,8 생성)

range_5 = range(0, 10, 2)
print(list(range_5))

# 예시2. 2에서 시작해 3 간격으로 증가하고 17을 포함하지 않는 숫자열(2,5,8,11,14 생성)
range_6 = range(2,17,3)
print(list(range_6))

# 예시3. 15에서 시작해 2 간격으로 감소하고 3을 포함하지 않는 숫자열(15,13,11,9,7,5 생성)
range_7 = range(15,3,-2)
print(list(range_7))
