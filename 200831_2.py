#200831_2

#HW  난수(random)을 이용하여 난수 1~100사이의 수 를 생성한 후
#어떤 숫자인지 맟추는 프로그램을 만드세요.
#입력한 숫자가 난수보다 크면 UP, 작으면 Down으로 알려주고 계속 추측하여 난수값을
#만드는 프로그램을 작성

import random

rn = random.randrange(1, 101, 1)
num = -1

print("start!")

while ( rn != num ):

    num = int(input("1-100 사이의 숫자를 입력 : "))

    if (num > rn):
        print("Down!")
    elif (num < rn):
        print("Up!")

print("Correct!")