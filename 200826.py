#20200826

#클래스 변수
class a1313:
    c_name=""
a=a1313()
a.c_name="박"
b=a1313()
b.c_name="성"
a=a1313() #클래스변수는 동일한 변수를 가르키고 있다,
b=a1313()
print(id(a.c_name))
print(id(b.c_name))
#모듈
# 사용방법 first
import mod1313 #파일(스크립트) mod1313
#import mod1313.py (X) !!!!!!
print(mod1313.add(13,13))
print(mod1313.sub(13,13))

#사용방법 second
from mod1313 import * #mod1313 파일내의 함수를 가져와 사용
print(add(13,13))
print(sub(13,13))

print(mod1313.PI) #모듈의 변수
c1313=mod1313.Math() #모듈에 정의된 클래스도 사용
print(c1313.solv(2)) #원의 넓이를 구함.

#내장함수
#print() len() type() str() int() list() tuple()

#all() : 구성요소 중에 False값이 없을때 vs any()
print(all([1,2,3,4,5])) #True
print(all([0,1,2,3,4,5])) #False
print(all(['a','b','','c'])) #False
print(any([1,2,3,4,5])) #True
print(any([0,1,2,3,4,5])) #True


#chr() vs ord() :  아스키코드
print(chr(99))
print(ord('A'))

#enumerate : 인덱스값 출력
for i, name in enumerate(['eb','dc','wp','hd']):
    print(i,name)

#eval : eval(expression) 수식
print(eval('1+2'))
print(eval('"aaa+bbb"'))
print(eval('chr(97)'))

#map : map(f,data) : 함수를 실행
def t_times(x):
    return x*2
print(list(map(t_times,[1,2,3,4])))

print(list(map(lambda b:b*2, [1,2,3,4])))