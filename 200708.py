k1=input("Enter ClassNum:")

def test1_func(s):
    rtn=0
    for i in s:
        rtn += int(i)
    rtn=int(rtn)
    print(rtn)
    if int(s)%2==0:
        print("%o" %rtn)
    else:
        print("%x" %rtn)

test1_func(k1)