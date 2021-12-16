t1=(1,2,3)
print(t1)
t1.index(2)
print(t1)
a=[]
print(bool(a))
b={'a':1,'b':2}
print(bool(b))
if bool(a) or bool(b):
    print(True)
c1=""
c2='Python'

if 'p' in c2:
    pass
elif 'P' in c2:
    print("True c2 elif")
else:
    print('Else')

#삼항연산자
score=90
msg='PASS' if score>=80 else 'FAIL' #?:
print(msg)

a2=(1,2,3,4)
for i in a2:
    print(i*2)
print(a2)
print()