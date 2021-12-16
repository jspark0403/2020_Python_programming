#1313 _ 200914

#import numpy
#print(numpy.__version__)

import numpy as np #as np=> alias 이름 간소화 => numpy => np
print(np.__version__)

#list vs numpy array
w1313_a=np.array([1,2,3,4,5])
print(w1313_a)
print(w1313_a+100) #전체연산

w1313_b=[1,2,3,4,5]
print(w1313_b)
#print(w1313_b+100) #Error
w1313_c=[]
for i in w1313_b:
    w1313_c.append(i+100)
print(w1313_c)
#리스트내포
w1313_d=[num+100 for num in w1313_b]
print(w1313_d)
#자료형 확인
print(type(w1313_a),type(w1313_b),type(w1313_c),type(w1313_d))

#numpy.array()
a=np.array(13) #0D 원소1
b=np.array([1,2,3,4,5,6,7]) #1D 1차원
c=np.array([[1,2,3],[4,5,6]]) #2D 2차원
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]) #3D 3치원
#ndim 차원 - Dimension
print(a.ndim,b.ndim,c.ndim,d.ndim)
#인덱싱 / 슬라이싱
print(b[2]+b[4]) #8 인덱스는 0부터 시작
print(c[1,2]) # 2차원
print(d[1,1,2]) # 3차원

print(b[1:4])
print(c[1,1:3])
print(d[0,1,1:3])

print(c[0:1,1:3]) #1!!전체연산

#copy vs view
x=b.copy() #배열을 복사
x[0]=13
print("b",b) #원본배열
print("x",x) #복사배열 : 새로만든다.
print(x.base) #원본이 있나요? None->자기자신

y=b.view()
y[0]=1313
print("b",b)
print("y",y)
print(y.base) #원본이 따로

#shape : 배열의 각 차원과 요소수
print(c.shape)
print(d.shape)

#reshape
e=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_e=e.reshape(4,3)
print(new_e)
print(new_e.ndim)
new_e2=e.reshape(2,3,2)
print(new_e2)
print(new_e2.ndim)

#반복
print("1D")
for i in e:
    print(i,end=" ")
print("*****")
print("2D")
for i2 in new_e:
    for i3 in i2:
        print(i3,end=" ")
print("")
print("3D")
for j in new_e2:
    for j1 in j:
        for j2 in j1:
            print(j2,end=" ")

#nditter : n for loop 간소화
for x in np.nditer(new_e2):
    print(x)

from numpy.linalg import*
k1=np.array([[4,3],[3,2]])
k2=np.array([23,16])

print(np.dot(k1,k1)) #스칼라곱 내적
print(inv(k1)) #역행렬

print(solve(k1,k2))

#연산
k3=np.array([1,2,3,4,5,6,7,8,9])
k4=np.array(k3%2==0)
k5=np.array(k3>=5)
print(k4)
print(k5)