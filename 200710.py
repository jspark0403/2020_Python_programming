a1=[1,2,3,4]
while a1:
    print(a1.pop())
print(bool(a1))

a2=(1,2,3,4)
for i in a2:
    print(i*2)
print(a2)

for i in range(1,5):
    for j in range(1,5): #5까지 가지 않는다.
        print(i,j)
    print("")

for i in "Python":
    print(i,type(i) )

sum=0
for j in [1,2,'3',4,5]: #3번쨰 string
    print(j,type(j))
    #sum+=j string + int Error
    sum+=int(j)

'''
def add(a,b) 매개변수

add(3,4) 인수
'''

def add_many(*args):
    result=0
    for i in args:
        result=result+i
    print(type(args))
    return result, result+1

k=add_many(1,2,3,4,5) #함수안에 정의되어 있는 arg의 값이 무엇인가 자료형:tuple
k1,k2=add_many(1,2,3)
print(k,type(k)) #두개의 값을 동시에 반환하면 하나로 된 튜플로 반환한다.
print(k1,k2,type(k1),type(k2)) #*****중요*****

def kk1(**k_arg):
    return k_arg

tmp1=kk1(a=1,b=2) #####중요##### key:value !!!!!!!!!!
print(tmp1,type(tmp1))

d1={'a':1,'b':2}
print(d1)


v1=1
def vtest(a):
    global v1
    v1+=1 #v1 = 지역변수
vtest(1)#함수 실행이 안되면 v1이 그대로 나온다...
f1=vtest(1)
print(v1)
print(f1)
