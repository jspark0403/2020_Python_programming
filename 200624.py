#1313_박진성

#대칭수
'''
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를
대칭수(palindrome)라고 부릅니다.
두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 
9009 (= 91 × 99) 입니다.
세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?
출력하는 프로그램을 작성해보자.
'''
def get_pd(num1,num2): #곱한 수 !!!
    max_pd=0
    num2_org=num2
    while num1>(num1/10):
        while num2>(num2/10):
            m_num=num1*num2
            if is_pd(m_num) and (max_pd<m_num):
                max_pd=m_num
            num2-=1
        num1-=1
        num2=num2_org
    return max_pd
def is_pd(num): #대칭수 확인 함수
    if str(num)==str(num)[::-1]:
        return True
    else:
        return False

print(get_pd(999,999))


# Check
n1=99
n2=99
while n1>(n1/10):
    n3=n2
    while n2>(n2/10):
        print(n1,n2)
        n2-=1
    n1-=1
    n2=n3

