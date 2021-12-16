#201123

class Fixedqueue:
    class Full(Exception):
        pass
    class Empty(Exception):
        pass

    #annotation : 주석, 매개변수, 함수반환값
    #매개변수 : expression 반환값 -> 자료형
    def __init__(self,capacity:int)->None: # ':' 가운데에 쓰지 않기
        self.no=0 #원소의 개수
        self.front=0 #전위 포인터
        self.rear=0 #후위포인터
        self.capacity=capacity #큐의 크기
        self.que=[None]*capacity #큐 본체


        def is_empty(self)->bool:
            return self.no<=0
        def is_full(self)->bool:
            return self.no>=self.capacity

    def __len__(self):
        return self.no

    #enque, deque
    def enque(self,value):
        if self.is_full():
            raise Fixedqueue.Full
        self.que[self.rear]=value
        self.rear=self.rear+1
        self.no=self.no+1
        if self.rear==self.capacity:
            self.rear=0
    def deque(self)->int:
        if self.is_empty():
            raise Fixedqueue.Empty
        x=self.que[self.front]
        self.front=self.front+1
        self.no=self.no-1
        if self.front==self.capacity:
            self.front=0
            return x

#*****큐의 동작*****
from enum import Enum
Menu=Enum('Menu',['Enque','Deque','Exit'])

def select_menu():
    #se=['({m.value}){m.name}'.format(m) for m in Menu)]
    se=['({0}){1}'.format(m.value,m.name) for m in Menu]

    while True:
        print(*se, sep='   ',end='')
        n=int(input(": "))
        if 1<=n<=len(Menu):
            return Menu(n)
        #큐의 시작
q1313=Fixedqueue(13) #큐 클래스 선언
while True:
    print('Queue1313 Start :{0} / {1}'.format(len(q1313),q1313.capacity))

    menu=select_menu()
    if menu==Menu.Enque:
        x=int(input("Enter Data:"))
        try:
            q1313.enque(x)
        except Fixedqueue.Full:
            print("Queue Full!!!")
    elif menu==Menu.Deque:
        try:
            y=q1313.deque()
            print("Data deque {0}".format(y))
        except Fixedqueue.Empty:
            print("Queue Empty")
    else:
        break

