a1='Pythont'
b=a1.count('p') #문자열 내에 포함되어 있는 개수
print(b)
c=a1.find('t') #문자열 내에 문자의 위치
print(c)
#printf(a1.index('p'))
print(b+c)

#join & split

a2=",".join(a1)
print(a2,type(a2))
a3=a2.split(",")
print(a3,type(a3))
a4="".join(a3)
print(a4,type(a4))

c1=[1,2,3,4,5]#int
c2=['1','2','3','4','5']#문자열
print(c1[1],c2[1],type(c1[1]),type(c2[1]))
c1.append(6)
c2.append(6)
print(c1,c2)
#print(c1[5]+c2[4]) Err int + str
c1.insert(2,9) #인덱스,값
c1.sort()
print(c1)#1,2,3,4,5,6,9
c1.pop()#1,2,3,4,5,6
print(c1.pop())#1,2,3,4,5 => 6
c1.pop()#1,2,3,4
c1.pop()#1,2,3
print(a1[c1.pop()]) #a1='Pythont'

d1={'a':1,'b':2,'c':3}
print(d1.get('d'))
print(d1['c'])
