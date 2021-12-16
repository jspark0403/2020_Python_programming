#201112a
#Stack with Python Class

class FixedStack1313:
    #고정길이 스택 클래스
    def is_empty(self):
        #스택이 비어있는가?
        return self.ptr<=0 #조건문 => 부울형 (True/False)
    def is_full(self):
        #스택이 가득 차있는가?
        return self.ptr>=self.capacity

    #파생클래스 예외처리 기법 : 강제로 예외처리를 발생시켜 스택프로그램 운용
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    #초기화
    def __init__(self,capacity=256):
        self.stk1313=[None]*capacity #스택 저장용량의 기본값 a=[1,2]
        self.capacity=capacity #사용자 입력 저장용량
        self.ptr=0 #스택포인터

    #PUSH,POP,PEEK
    def push(self,value):
        if self.is_full():
            raise FixedStack1313.Full
        self.stk1313[self.ptr]=value
        self.ptr+=1


    def pop(self):
        if self.is_empty():
            raise FixedStack1313.Empty
        self.ptr-=1
        return self.stk1313[self.ptr]

    def peek(self): #최상위 데이터 확인
        if self.is_empty():
            raise FixedStack1313.Empty
        return self.stk1313[self.ptr-1]

    def __len__(self): #오버로딩된 len
        return self.ptr #ptr 스택에 저장된 자료의 수

#스택의 동작
from enum import Enum #python 3.4이상
Menu=Enum('Menu',['PUSH','POP','PEEK','EXIT'])
def select_menu():
    s=["({0}){1}".format(m.value,m.name) for m in Menu] #문자열 포맷팅 + 리스트 내포
    while True:
        print(*s, sep='  ', end=' ')
        n=int(input(':'))
        if 1<=n<=len(Menu):
            return Menu(n)

s1313=FixedStack1313(13) #사용자 입력 저장공간 13=capacity

while True:
    print("Now Stack:{0}/{1}".format(len(s1313),s1313.capacity))
    menu=select_menu()

    if menu==Menu.PUSH:
        x=int(input("Enter Data:"))
        try:
            s1313.push(x)
        except FixedStack1313.Full:
            print("Stack Full!!!")
    elif menu==Menu.POP:
        try:
            y=s1313.pop()
            print(y,'is POP!')
        except FixedStack1313.Empty:
            print("Stack Empty!!!")

    elif menu==Menu.PEEK:
        try:
            z=s1313.peek()
            print("Peek Data:", z)
        except FixedStack1313.Empty:
            print("Stack Empty!!!")

    elif menu == Menu.EXIT:
        break