#201130


#collections.deque 스택 + 큐를 동시에 구현

#append() extend() appendleft() extendleft()
#append() : 원소 입력 s ㄷㅌㅅ둥() : rorcpdml dlqfur

#pop() popleft() remove() reverse() rotate()
from collections import deque

w1313=deque([1,3,1,3])
w1313_s=deque(['1','3','1','3'])

w1313.append(13) #오른쪽
w1313.appendleft(14) #왼쪽
print(w1313)

w1313.extend([15]) #'15'로 하면 문자열 처리 '1', '5' ajs
w1313.extendleft([15]) #문자열 처리시 덧샘연산 불가 int+str
print(w1313)


w1313_s.append('wp')
w1313_s.extend('wp')
print(w1313_s)
#deque은 원소수정이 가능함. vs 문자열, 튜플
w1313_s[6]='wpwp'
print(w1313_s)
t_str='wpwp1313'
#t_str[1]='h' #Error 중간 문자열은 교체 불가

w1313_s.pop()
print(w1313_s.popleft()) #반환값이 존재
w1313_s.remove('3')
print(w1313_s.remove('w')) #반환값이 없음 => None
print(w1313_s)

print(w1313)
w1313.reverse() #역순정렬
print(w1313)
w1313.rotate(2) #지정된 숫자만큼 순환
print(w1313)

#deque는 원형큐의 기능을 갖고 있음, maxlen가 지정되었을 경우


#Stack with collections.deque

class Stack1313:
    def __init__(self,maxlen=13):
        self.capacity=maxlen
        self.stk1313=deque([],maxlen) #deque의 초기선언
        #deque([1,2,3]) vs [None]*capacity

    def __len__(self): #연산자 오버로딩
        return len(self.stk1313)
    def is_empty(self)->bool:
        return not self.stk1313
    def is_full(self):
        return len(self.stk1313)==self.stk1313.maxlen

    #push.pop
    def push(self,value):
        if self.is_full():
            print("Stack is Full!!!")
        else:
            self.stk1313.append(value)

    def pop(self):
        return self.stk1313.pop()

    def dump(self):
        print(list(self.stk1313))


    #Peek, find, count
    def peek(self):
        return self.stk1313[-1] #파이썬 리스트의 특징

    def find(self,value):
        try:
            return self.stk1313.index(value) #찾을 값의 인덱스 반환 : 순차 검색하여 앞의 원소의 인덱스
        except ValueError:
            return -1

    def count(self,value): #찾는 값의 중복된 갯수
        return self.stk1313.count(value)

    def __contains__(self, value): #in 연산자의 오버로딩
        return self.count(value)

#스택의 구현
from enum import Enum
Menu=Enum('Menu',['Push','Pop','Dump','Peek','Find','Exit'])

def select_menu():
    sel=[f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*sel,sep='   ',end=' ')
        n=int(input(":  "))
        if 1<=n<=len(Menu):
            return Menu(n)

w1313_stk=Stack1313(13)
while True:
    print('Stack with Deque {0}/{1}'.format((len(w1313_stk)),w1313_stk.capacity))

    menu=select_menu()

    if menu==Menu.Push:
        try:
            x=int(input("Enter Data:"))
            w1313_stk.push(x)
        except IndexError: # maxlen : 13 / 14 번째 참조
            print("Stack Full!!!")

    elif menu==Menu.Pop:
        try:
            y=w1313_stk.pop()
            print('Pop Data is',y)
        except IndexError:
            print("Stack empty")
    elif menu==Menu.Dump:
        w1313_stk.dump()

    elif menu==Menu.Peek:
        try:
            z=w1313_stk.peek()
            print("Peek Data",z)
        except IndexError:
            print("Stack Empty")

    elif menu==Menu.Find:
        tmp=int(input("Find Data:"))
        if tmp in w1313_stk:
            print("{0}번째 위치에 있고 {1}개 있음.".format(w1313_stk.find(tmp),w1313_stk.count(tmp)))
        else:
            print("No find")

    else:
        break