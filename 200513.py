#200513 1313 박진성

#while

a=[1,2,3,4]
while a: #while 조건문 : 조건 => a가 존재할때
    print(a.pop()) #4를 반환하고 삭제 => a=[1,2,3] 3을 반환하고 삭제
    #=> a=[1.2]
#while 반복문은 조건이 True일때 실행문을 실행. == 조건이 False일때까지 반복문을 실행

treeHit=0 #변수의 선언
while treeHit < 10:
	treeHit=treeHit+1 #****while문에서 조건을 변화시키는 구문은 반드시 있어야함.
	print('나무를 %d번 찍었습니다.' % treeHit)
	if treeHit==10:
         print('나무가 쓰러집니다.')

#반복해서 메뉴를 출력
'''promt="""
    1. ADD
    2. DEL
    3. LIST
    4. QUIT
    """
number=0
while number!=4: #조건 number가 4가 아닐때까지
    print(promt)
    number=int(input("Enter Number:"))

#in연산자와 조건부표현식
k='python'
print('k' in k) #False
#print('k' in K) #Error 대소문자를 구분

score=85
msg="합격" if score>=80 else "불합격" #조건이 True일때 if 조건문 else 조건이 False일때
print(msg)
msg="'합격' if score>=80 else '불합격'" #"문자열"
print(msg)

coffee=10 #전역변수 vs 지역변수
while True: #while 조건 : 조건 => True
    money=int(input('Enter Money: ')) #input() 사용자입력 내장함수 int()
    if money == 300:
        print("커피가 나옵니다.")
        coffee=coffee-1
    elif money > 300:
        print("거스롬돈 %d를 반환하고 커피가 나옵니다." % (money-300))
        coffee=coffee-1
    else:
        print("돈을 반환합니다. 커피는 나오지 않습니다.")
        print("남은 커피는 %d개 입니다." %coffee)
    if coffee==0:
        print("커피가 모두 소진되었습니다. 판매를 중지합니다.")
        break #반복을 중단하는 break문 : 무한반복 중단구문

#continue : 현재반복을 중단하고 반복 처음으로
a=0
while a<10: #a<10작을때
    a=a+1 #조건변화
    if a % 2 ==0: continue #짝수일때는 반복을 처음으로\
    print(a)
    '''
'''
과제1. 다음은 A학급 학생의 점수를 나타내는 리스트이다.
다음 리스트에서 아래의 요구사항을 화면에 출력하여 주세요.
a) 응시학생의 숫자를 출력하세요.
b) 전체평균을 구하세요.
c) 40점 이하의 과락 학생의 수를 구하세요.
d) 70점 이상의 점수만 더한 합을 구하세요.
A=[14,60,82,94,87,74,88,90,64,24,45,79,90,85,74,53,99,35,75,67,33]
'''
'''
A=[14,60,82,94,87,74,88,90,64,24,45,79,90,85,74,53,99,35,75,67,33]
#a) 응시학생의 숫자를 출력하세요.
print('응시학생수 :',len(A),"명")
#b) 전체평균을 구하세요.
#c) 40점 이하의 과락 학생의 수를 구하세요
print(sum(A)/len(A))
std=len(A)
sum=0
count=0
sum2=0
while A: #리스트A에 요소가 없을때까지
    mark=A.pop() #pop()내장함수  : 리스트의 맨 마지막 값을 반환하고 삭제
    if mark<=40: #점수가 40점 이하라면
        count=count+1
    if mark>=70: #점수가 70점 이상이라면
        sum2+=mark
    sum+=mark
print("전체평균은",sum/std,"점")
print("40점 이하 학생은",count,'명')
print("70점 이상 학생만 더한 총합은",sum2,'점')
'''

'''과제2. 다음과 같이 입력되는 사용자로부터 입력받은 숫자의 합과 평균을 구하는 프로그램을 작성하시오.
숫자를 입력하세요 : ex) 54,54,34,45,32,13
'''
number_str=input("숫자를 입력하시오 :")
number=number_str.split(',')
sum = 0
cnt=0
while number:
    user=int(number.pop())
    sum+=user
    cnt+=1
print (sum)
print(sum/cnt)






