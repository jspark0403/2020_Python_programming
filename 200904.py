#200904

#예외처리
# try, except, finally
try:
    4/0
except:
    print("ERROR Zerodivision")

try:
    4/0
except ZeroDivisionError as e:
    print(e)

try:
    a=[1,2,3]
    print(a[4])
except  IndexError as e:
    print(e)

f=open("test.txt",'w')
try:
    pass
finally: #에러 또는 오류의 발생에 무관하게 무조건 실행
    f.close()

#쓰레드
import threading #쓰레드 사용

import time
def t1313_task():
    for i in range(5):
        time.sleep(1)
        print("working:%d" %i)
'''
print("F start.")
t1=time.time()
for i in range(5):
    t1313_task()
t2=time.time()
print("F end",t2-t1)
'''
#스레드의 생성
threads=[]
for i in range(5):
    t=threading.Thread(target=t1313_task)
    threads.append(t)
tt1=time.time()
print("T start!")
for t in threads:
    t.start() #쓰레드 실행
for t in threads:
    t.join() #쓰레드의 종료까지 기다림.
tt2=time.time()
print("T end!",tt2-tt1)