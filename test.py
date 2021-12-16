#주석

#1부터 100까지 더하는 프로그램을 만드세요!

sum_t=0 #변수
for i in range(1,100+1):
    if i%2==0: #짝수만
        sum_t=sum_t+i
print(sum_t)