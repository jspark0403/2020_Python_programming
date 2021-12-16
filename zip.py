str_tmp=input()
tmp_t=""
cnt=0
result=""
for c in str_tmp:
    if tmp_t != c:
        tmp_t =c
        if cnt:
            result+=str(cnt)
        result +=c
        cnt=1
    else:
        cnt+=1
result+=str(cnt)

print(result)
