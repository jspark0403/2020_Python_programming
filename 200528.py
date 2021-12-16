#200528 1313

#함수 : 실행할 문장들의 모음.

def add(a,b): #a,b는 매개변수
    return a+b

x=1
y=3
add(x,y) #함수의 호출(실행)
print(add(x,y)) #x,y 인수

#입력값이 없는 함수 = 매개변수(인수)가 없는 함수
def say():
    return 'Hello'
print("함수의 호출1")
say()
print("함수의 호출2")
print(say())

#결과값(반환값)이 없는 함수 = return 없다.
def add1(a,b):
    print("%d %d의 합은 %d" %(a,b,a+b))
print("add1-1")
add1(1,3)
print("add1-2")
print(add1(1,3))
#입력값도 반환값도 없는 함수 매개변수(인수)와 return이 없는 함수
def say1():
    print("Hi 1-3")

say1()

#여러개의 입력을 받는 함수
def add_many(*args):
    result=0
    print(type(args)) #
    for i in args:
        result=result+i
    return result #print=>결과값이 없는 함수

print(add_many(1,2,3,4,5))

def add_mul(choice, *args):
    if choice=="add":
        result = 0
        for i in args:
            result=result+i
    elif choice=="mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add',1,2,3,4,5)
print(result)
result = add_mul('mul',1,2,3,4,5)
print(result)

#키워드파라미터
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)
