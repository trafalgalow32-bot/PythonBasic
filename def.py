# def.py

#사용자 정의 함수(간단 학습)

def fun3(x,y):
    print(x)
    print(y)
    def fun4(*fun3) :
        Sum = x + y
        print(x, "+", y, "=", Sum)
    fun4(x,y)
    
fun3(3,5)