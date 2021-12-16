#최대공약수 & 최소공배수

input1=int(input("Enter Num1:"))
input2=int(input("Enter Num2:"))

num1=input1
num2=input2

gcd=0
icm=0

while num1 !=num2: # !!!!
    if num1 < num2:
        num1,num2=num2,num1
    num1=num1-num2

"""
if num1<num2
    num1,num2=num2,num1
while num2!=0:
    num1,num2=num1%num2
"""

gcd=num1
lcm=int((input1*input2)/gcd)

print("GCD:",gcd,"LCM", lcm)
