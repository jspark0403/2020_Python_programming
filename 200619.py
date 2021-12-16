#200619

#삼각수
#1-> 1
#2-> 1+2 3
#3-> 1+2+3 6
#...
def isprime(a): #약수의 개수 반환하는 함수 만들기
    cnt=0
    for i in range(1,a+1):
        if a%i==0:
            cnt=cnt+1
    return cnt

sum=1
n=1 #수열의 위치
su=500 #약수의 개수를 의미
while (sum>=1):
    max=isprime(sum) #함수isprime=>약수의 개수를 반환
    answer=sum
    print(max,answer)
    if max>=su:
        print(max,answer)
        break
    n+=1
    sum=int((n*(n+1))/2) #!!

