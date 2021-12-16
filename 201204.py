#201204

#리스트 / 단일(연결)리스트

# python list with class

class Node:
    #연결리스트 노드 클래스
    def __init__(self,data,next): #매개변수 data, next <=클래스 선언시 매개변수
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
        ptr=self.head
        self.head=self.current=Node(data,ptr)
        self.no=self.no+1

    def add_last(self,data):
        #맨 마지막에 노드를 추가
        if self.head is None:
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
            self.head=self.current=self.head.next
            self.no=self.no-1


    def remove_last(self):
        # 맨 마지막 노드 삭제
        if self.head is not None: # 빈 연결리스트가 아닐때
            if self.head.next is None: #노드가 1개뿐일때
                self.remove_first() #Head 노드 삭제
            else:
                ptr=self.head #스캔 중 노드
                pre=self.head #스캔 중 노드의 앞쪽 노드
                while ptr.next is not None: #꼬리노드 찾기
                    pre=ptr #pre 꼬리노드의 바로 앞쪽
                    ptr=ptr.next
                pre.next=None #pre가 삭제뒤에 꼬리노드드
                self.current=pre
            self.no=self.no-1

    def remove(self,p):
        #중간 노드 p
        if self.head is not None:
            if p is self.head:
                self.remove_first()
            else:
                ptr=selef.head
                while ptr.next is not p:
                    ptr=ptr.next
                    if ptr is None:
                        return
                ptr.next=p.next
                self.current=ptr
                self.no=self.no-1


