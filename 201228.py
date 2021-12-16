class Node:
    #연결리스트 노드 클래스
    def __init__(self, data, next): #매개변수 data, next <= 클래스 선언시 매개변수
        self.data=data #데이터
        self.next=next #뒤쪽 포인터

class LinkedList:
    #연결 리스트 클래스
    def __init__(self):
        self.no=0 #노드의 갯수
        self.head=None #Head Node
        self.current=None #Current Node

    def __len__(self):
        return self.no

    def add_first(self, data):
        #Head 부분에 노드를 삽입
        ptr=self.head #넣기 전에 Head부분
        self.head=self.current=Node(data,ptr)
        self.no=self.no+1

    def add_last(self,data):
        #맨 마지막에 노드를 추가
        if self.head is None: #리스트가 비어있을때
            self.add_first(data)
        else:
            ptr=self.head #ptr : 임시 포인터
            while ptr.next is not None: #ptr의 꼬리노드를 검색
                ptr=ptr.next

            ptr.next=self.current=Node(data, None)
            self.no=self.no+1

    def remove_first(self):
        #맨 처음 노드 삭제
        if self.head is None:
            print("No Node")
        else:
            self.head=sel

    ############################
    def print(self):
        ptr=self.head
        while ptr is not None:
            print(ptr.data)
            ptr=ptr.next


#연결리스트 구현
from enum import Enum
Menu=Enum('Menu',['InsertHead','InsertTail','DeleteHead','DeleteTail','NodePrint','Exit'])
def select_Menu():
    sel=[f'({m.value}){m.name}'for m in Menu]
    while True:
        print(*sel, sep='    ',end='')
        n=int(input(":  "))
        if 1<=n<=len(Menu):
            return Menu(n)

lst1313=LinkedList() #객체선언
while True:
    menu=select_Menu()

    if menu==Menu.InsertHead:
        lst1313.add_first(int(input("Enter Data =>")))
    elif menu==Menu.InsertTail:
        lst1313.add_last(int(input("Enter Data =>")))
    elif menu==Menu.DeleteHead:
        lst1313.remove_first()
    elif menu==Menu.DeleteTail:
        lst1313.remove_last()
    elif menu==Menu.NodePrint:
        lst1313.print()
    else:
        break