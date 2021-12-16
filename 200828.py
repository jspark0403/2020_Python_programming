#200828

import mod200828
print("200828.py exec:",__name__)

print(mod200828.PI)
m1313=mod200828.Math() #m1313 객체는 mod200828,Math 클래스의 인스턴스입니다.
print(m1313.solv(3))
#반지름이 5인 원의 둘레를 구하세요
print(m1313.rx2(5))

#isinstance
#객체와 인스턴스
print(isinstance(m1313,mod200828.Math))
#round: 반올림
print(round(3.141592,2)) #자리수
print(round(3.141592)) #기본값

#divmod : 몫과 나머지를 반환(튜플)
print(divmod(8,3))

#sorted: 정렬
print(sorted([1,5,4,2]))
print(sorted('agcf'))

#***eval eval(expression) 수식
print(eval('1'+'2'))
aaabbb="박진성"
print(eval('aaa'+'bbb'))
#print(eval(chr(65)))