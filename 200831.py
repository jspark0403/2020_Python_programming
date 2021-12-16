#200831

#내장함수
#all() vs any()
#all(반복가능한자료형 : True or False / 모두 True일때 True
#any(반복가능한자료형 : True or False / 모두 False일때 False
print(all([1,2,3,4])) #True
print(all([1,2,0,3,4])) #False
print(any([1,2,3,4])) #True
print(any([0,1,2,3,4])) #True
print(any([])) #False
print(any([''])) #False
print(any([' '])) #True
if any([' ']): #!!!
    print("Hello")
if any([0,0,0]):
    print("Jinseong Park")

#chr() vs ord()
#아스키코드 관련
print(chr(65)) #A
print(ord('a')) #97

#enumerate : 인덱스 출력
for i, name in enumerate(['EB','DC','WP','HD']):
    print(i,name)

#filter
def positive(x):
    result=[]
    for i in x:
        if i>0:
            result.append(i)
    return result
print(positive([1,2,-4,0,3,-5,6]))

def positive1(x):
    return x>0
print(list(filter(positive1,[1,2,-4,0,3,-5,6])))

print(list(filter(lambda x:x>0,[1,2,-4,0,3,-5,6])))

#외장함수 : 모듈
import time
print(time.time())
print(time.ctime())
print(time.asctime(time.localtime(time.time())))
#print(time.strftime('%x',time.localtime(time.time)))
#print(time.strftime('%c',time.localtime(time.time)))

for i in range(10,0,-1):
    print(i,end=" ")
    #time.sleep(1) #!!!

#calendar
import calendar
print(calendar.calendar(2020))
print(calendar.prmonth(2020,8))

#random
import random
print(random.random())
result=[]
for i in range(1,6):
    result.append(random.randint(1,10))
print(result)
data=[1,2,3,4,5,6,7,8,9,0]
random.shuffle(data)
print(data)
print(random.sample(data,3))

mylist=['apple','banana','pear']
print(random.choices(mylist,weights=[5,1,1],k=10))

re2=[]
for i in range(1,100):
    re2.append(random.randrange(1,100,3))
print(re2)