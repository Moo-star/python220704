# function3.py

# 교집합 함수
from re import X


def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

# 호출
print(intersect("HAM", "SPAM"))

# 지역변수와 전역변수
x = 1
def func1(a):
    return a+x

# 호출
print(func1(1))

def func2(a):
    x = 2
    return a+x

# 호출
print(func2(1))



print("---불변형식---")

a = 1.2
print(id(a))
a = 2.3
print(id(a))

print("---가변형식---")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))


# 객체는 참조를 통해 복사(입력+출력)
wordlist = ["J", "A", "M"]

# 함수정의
def change(x):
    # 내부에서 객체의 복사본 생성(deep copy)
    x1 = x[:]
    x2 = x

    x1[0] = "H"
    x2[0] = "K"

# 호출
change(wordlist)
print("함수 호출 후:", wordlist)

# 기본값
def times(a=10, b=12):
    return a*b
# 호출
print(times())
print(times(5))
print(times(5,6))

# 키워드 인자
def connectURI(server, port):
    strURL = "http://"+server+":"+port
    return strURL

# 호출
print(connectURI("ycampus.com", "80"))
print(connectURI(port="80", server="ycampus.com"))
