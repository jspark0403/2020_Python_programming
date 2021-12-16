#200831_1

#쓰레드
import time
import threading
import os

def t_test():
    os.system('cls')
    print(time.time())
    print(time.ctime())
    test_h=threading.Timer(1,t_test)
    test_h.start()

t_test()
