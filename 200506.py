#1313박진성 200506

#집합자료형
s1=set([1,2,3]) #리스트형으로 입력
s2=set("hello") #문자열 형태로 입력
s3=set() #빈 집합자료형

print(s1,s2,s3)
s4=list(s1) #집합자료형을 리스트 자료형으로 변환
print(s4[0])

#집합자료형의 연산
s5=set([1,2,3,4,5,6])
s6=set([4,5,6,7,8,9])

print(s5 & s6) # & : 교집합 intersection
print(s5.intersection(s6)) #내장함수 교집합

print(s5 | s6) #| : 합집합 union
print(s5.union(s6)) #내장함수 합집합

print(s5-s6) # - : 차집합 difference
print(s5.difference(s6)) #내장함수 차집합

#odd() update() remove()
print(s1)
s1.add(10) #요소 1개 추가
print(s1)
s1.update([21,22,23]) #요소 여러개 추가
print(s1)
s1.remove(2) #요소 제거
print(s1)

#리스트에서 중복 숫자를 제거하여 리스트 [1,2,3,4,5]를 출력해보세요
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a) #집합자료형으로 변환 => 중복을 제거
b=list(aSet) #리스트형태로 변환 / 대소문자 구분 aset != aSet
print(b)

#bool 자료형 : True와 False를 구별하는 변수
b1=True #True  != true 대소문자 구별
#값이 있으면 True 비어 있으면 False

print(type(b1))
b2=(1>5)
print(b2)

print(bool('python'))
print(bool([]))

print(bool(0))
print(bool(3))

################변수

a=[1,2,3]
b=a # '=' (대입) != '==' (비교)
print(id(a)) #id() 메모리 값을 출력하는 내장함수
print(id(b))

#****** 단순대입 : 변수의 갯수는 증가했지만 가르키고 있는 것은 같다.
b[1]=4 #인덱싱
print(a) #변수 a와 b가 가르키고 있는 값이 동일

#복사
#두가지 방법
#1. 슬라이싱 이용한 방법
c=a[:] #a리스트의 처음부터 끝까지 슬라이싱
print(c)
print(id(a))
print(id(c))

#2. 모듈을 이용한 방법
#from copy import copy
from copy import copy
d=copy(a)
print(id(a))
print(id(d))

#is 예약어
print(a is b) #is는 동일한 객체를 가르키고 있는지 확인
print(a is c) #메모리 값이 같으면 True 다르면 False
print(a is d)
print(c is d)

#변수를 만드는 방법
e,f=('ab','cd') #한꺼번에 선언이 가능
e=f='ab' #같은 값 넣기
(e,f)='ab','cd'

print(e,f)
e,f=f,e #변수의 값을 서로 바꿀때 Swap
print(e,f)

#응용 : '+'연산자를 이용한 이어붙이기는 서로 다른 값을 만들지만 extend는 변함없다.
test1=[1,2,3]
print(id(test1))
#test1+[4,5] '+'연산자 이어붙이기
test1=test1+[4,5] # test1+=[4,5] '+=' 대입연산자
print(test1)
print(id(test1))

#vs
test2=[1,2,3]
print(id(test2))
test2.extend([4,5]) #extend() 내장함수 이어붙이기
#test2=test2.extend([4,5])
print(test2)
print(id(test2))

#
a1=[1,2,3]
b1=[1,2,3]
print(a1 is b1)

a2=[1,2,3]
b2=a2
print(a2 is b2)

#문제:딕셔너리 a에서 B에 해당하는 값을 추출해보세요.
a={'A':90,'B':80,'C':70}
#리스트와 동일한 내장함수를 사용할 수 있다.
result=a.pop('B') # pop 내장함수
print(a) #{'A':90,'C':70}출력
print(result) #80출력

print(type(result))