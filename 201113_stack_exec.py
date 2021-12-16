#201112  Menu=Enum('Menu', ['PUSH', 'POP', 'PEEK', 'EXIT'])

from enum import Enum #python 3.4 이상
from 201113_stack import FixedStack1313

        Menu=Enum('Menu', ['PUSH', 'POP', 'PEEK', 'FIND', 'DUMP' 'EXIT'])
        def select_menu():
            s=["({0}){1}".format(m.value,m.name) for m in Menu] #문자열 포멧팅 + 리스트 내포
            while True:
                print(*s, sep='  ', end = ' ')
                n=int(input(':'))
                if 1<=n<=len(Menu):
                    return Menu(n)

            s1313=FixedStack1313(13) #사용자 입력 저장공간 13=capacity

        while True:
            print("Now Stack:{0}/{1}". format(len(s1313), s1313.capacity))
            menu=select_menu()

            if menu==Menu.PUSH:
                x=int(input("Enter Data:"))
                try:
                    s1313.push(x)
                except FixedStack1313.Full:
                    print("Stack Full!!!")

            elif menu==Menu.POP:
                try:
                    y=s1313.pop()
                    print(y, 'is POP!')
                except FixedStack1313.Empty:
                    print("Stack Empty!!!")

            elif menu==Menu.PEEK:
                try:
                    z = s1313.pop()
                    print('Peek Data:', z)
                except FixedStack1313.Empty:
                    print("Stack Empty!!!")

            elif menu == Menu.FIND:
                pass

            elif menu == Menu.DUMP:
                s1313.dump()

            else:
                break