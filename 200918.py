#200918

#연산
import numpy as np #alias : 재명명

w1313a=np.array([[1,2,3],[7,8,9]])#2D
w1313b=np.array([4,5,6])#1D
w1313c=np.array([[1,3],[1,8]])
w1313d=np.array([13,18])

#배열의 사칙연신, 차원이 다른 배열의 사칙연산 가능
print(w1313a+w1313b)
print(w1313a-w1313b)
print(w1313a*w1313b)
print(w1313a/w1313b)
print(np.dot(w1313c,w1313d)) #!!!행렬의 내적

#arange(시작, 끝) 시작부터 끝-1 까지 구성된 배열 생성
w1=np.arange(1,1313)
print(w1)
w2=np.arange(1,13,dtype=float)
print(w2)
w3=np.random.rand(3,3) #2D 9개 요소
print(w3)
w4=np.random.randint(10,size=(3,3))
print(w4)
w5=np.random.randn(10) #1D 10개 요소
print(w5)
w6=np.arange(1,25)
w7=w6.reshape(4,6) #재구성
print(w7)
print(w7.sum())
print(w7.sum(axis=0)) #열의 합
print(w7.mean())
print(w7.mean(axis=1)) #행의 평균
print(w7.max(),w7.min)

w8=np.zeros(10,dtype=int) #10개의 요소가 모두 0인 1-D int 배열생성
w9=np.ones((3,5),dtype=float) #요소가 모두 1인 3*5 float 배열 생성
print(w8,w9)

#matplotlib
import matplotlib
import matplotlib.pyplot as plt
w10=np.random.randn(1000)
w11=np.random.normal(0,1,1000)
print(w10)
plt.grid()
plt.hist(w10)
plt.show()
#randn vs rand va normal
#randn==normal 평균이 0 편차가 1인 정규분포
#rand 0<r<1 난수

#pandas / matplotlib / seaborn