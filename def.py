# def.py

#사용자 정의 함수(간단 학습)
"""
def fun3(x,y):
    print(x)
    print(y)
    def fun4(*fun3) :
        Sum = x + y
        print(x, "+", y, "=", Sum)
    fun4(x,y)
    
fun3(3,5)"""
# 좀 더 깔끔한 버젼
def fun3(x, y):
    print(f"외부 입력: {x}, {y}")

    # 가변 인자 관례인 *args 사용, 외부 변수와 이름 중복 피하기
    def fun4(*args):
        # args는 (3, 5)와 같은 튜플 형태가 됨
        Sum = sum(args) 
        print(f"내부 계산: {' + '.join(map(str, args))} = {Sum}")

    fun4(x, y)

fun3(3, 5)