#1313 박진성

#실습 2 임의의 정수를 입력 받아 약수를 구하는 프로그램을 작성하시오.

num=int(input("Enter Num=>"))
count=0

for i in range(1,num+1): #1,2,3,4....
    if num % i == 0: # 12 / 1,2,3,4...
        print(i, end=",") # end=","/end=" " 매개변수 이어쓰기
        count=count+1

print('약수의 개수:',count,'개')

#실습3 임의의 정수를 입력 받아 그 안에 포함된 소수의 개수와 합을 구하는 프로그램을 작성하시오
print("{0:#^100}".format("소수구하기 1313"))
num2=int(input("Enter Num=>"))

count1=0 #개수변수
sum1=0 # 합 변수
for i in range(2,num2+1): #2~12 2,3,4,... i
    chk=True #소수인지 판별하는 자료형
    for j in range(2,i): #j 2~i
        if i % j == 0:
            chk=False
            break
    if chk: #True 소수이면...
        count1=count1+1
        sum1=sum1+i
        print(i,end=" ")

print(' ')
print('소수개수:',count1,'개, 소수합:',sum1)

#어떤 정수의 모든 약수 중 자신을 제외한 약수를 모두 합하
#면 자신과 같아지는 수가 있다. 예를 들어 6의 약수 1,2,3,6중
#6을 제외한 1,2,3을 더하면 6이 되어 자신과 같아진다. 1부터
#1000까지의 정수 중 이러한 약수를 갖는 수를 찾아 출력하
#고 또한 그 개수를 구하여 출력하는 프로그램을 만드세요.
#완전수 구하기

print("{0:#^100}".format("완전수 구하기 1313"))
num3=int(input("Enter Num3=>"))
p=[] #빈 리스트

for i in range(1,num3+1):
    sum2=0 #초기화
    for j in range(1,i): #
        if i % j == 0: #6 % 1, 2, 3, 4, 5
            sum2 = sum2+j # 약수만 더해지는

    if i==sum2: # 합과 자기자신이 같다면
        p.append(i) #리스트에 추가

print(p)
print('갯수:',len(p))

#a,b=b,a
#a,b
#tmp=a
#a=b
#b=tmp

A=3
B=5

A=A^B #XOR 같으면 0 다르면 1
B=A^B
A=A^B

print(A,B)