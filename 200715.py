#def vs lambda

def addt(x,y): #여러줄 정의
    return x+y

addt1=lambda x,y: x+y #여러줄에 있는 것은 정의할 수 없다. 문법상 매개변수에 괄호가 없다. return이 없다.

print(addt(1,3))
print(addt1(1,3))

a=[1,2,3]
d2={'a':1,'b':2}

if a.sort() == d2.get('c'): #키값을 찾을 수 없는 경우 반환값 None
    z=abs(-1) #절댓값 함수
    print(z)
    print(z,z)
    print("W","P")
    print("W" "P")
    print('W'+'P')

f=open("test.txt",'w')
for x in range(1,5):
    f.write(str(x))
f.close()