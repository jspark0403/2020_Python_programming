#1313 박진성

import numpy as np #n차원 배열
import matplotlib # 그래프 그리기
import matplotlib.pyplot as plt #그래프 속성과 메소드
import pandas as pd #데이터 처리를 위한 자료구조와 메소드

plt.plot([1,2,3],[100,110,130]) #plot 선그리기
plt.show() #화면에 보이기

a=np.linspace(0,10,100) #100개로 균등분할
b=np.exp(a)
plt.plot(a,b)
plt.show()

#스타일 지정
plt.plot([10,20,30,40],[1,4,9,16],c="b",lw=5,ls='--',
         marker="o",ms=15,mec="r",mew=5,mfc="y")
plt.show()

#제목, 범례, x축, y축
plt.plot([1,2,3],[1,4,9])
plt.plot([2,3,4],[9,16,25]) #x축 이름
plt.xlabel('sequence') # y축 이름
plt.ylabel('Time(secs)') # 표 제목
plt.title('1313 Result') # 범례
plt.legend(['1-3','1-4'])
plt.show()

#pandas를 이용한 그래프 그리기
p1=pd.Series(np.random.rand(16), index=list("abcdefghijklmnop"))
#p1.plot(kind='bar')
p1.plot(kind='barh')
plt.show()

#산점도
a1=np.random.rand(100)
b1=np.random.rand(100)
plt.scatter(a1,b1) #산점도
plt.show()

#3D
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=fig.gca(projection='3d')
X=np.arange(-5,5,0.25)
Y=np.arange(-5,5,0.25)
X,Y=np.meshgrid(X,Y)
R=np.sqrt(X**2+Y**2)
Z=np.sin(R)
surf=ax.plot_surface(X,Y,Z,
rstride=1,cstride=1,cmap=matplotlib.cm.coolwarm)
plt.show()

#다중그래프 그리기
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)
ax1 = plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'yo-')
plt.title('A tale of 2 subplots')
plt.ylabel('Damped oscillation')
print(ax1)
ax2 = plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r.-')
plt.xlabel('time (s)')
plt.ylabel('Undamped')
print(ax2)
plt.tight_layout()
plt.show()

#다중그래프 그리기 2

fig, axes = plt.subplots(2, 2)
np.random.seed(0)
axes[0, 0].plot(np.random.rand(5))
axes[0, 0].set_title("axes 1")
axes[0, 1].plot(np.random.rand(5))
axes[0, 1].set_title("axes 2")
axes[1, 0].plot(np.random.rand(5))
axes[1, 0].set_title("axes 3")
axes[1, 1].plot(np.random.rand(5))
axes[1, 1].set_title("axes 4")
plt.tight_layout()
plt.show()

