#mod1313.py 모듈활용

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

PI=3.141592
class Math:
    def solv(self,r):
        return PI*(r**2)
def mul(a,b):
    return a*b

if __name__ == "__main__":
    #스크립트 실행파일의 계층(위치)를 의미
    print(add(1,3))
    print(sub(1,3))