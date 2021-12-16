

class Cookie:
    print("TEST CLASS")
    r1=0

A=Cookie()

r1=0
r2=0
def add(num1):
    global r1
    r1+=num1
    return r1
def add2(num2):
    global r2
    r2+=num2
    return r2
print(add(3))
print(add(4))
print(add2(3))
print(add2(4))


class Cal:
    #result=0
    def __init__(self):
        self.result=0
    def add(self,num): #정의
        self.result+=num
        return self.result

A1=Cal()
print(A1.add(3))
A2=Cal()
print(A2.add(4))
print(A1.add(3))