#20200824_1313
#클래스의 상속, 메소드 오버라이딩, 오버로딩

class cal1313: #클래스의 선언
    def __init__(self,first,second):
        #__init__ 예약어=>초기화=>객체 생성자
        #객체를 선언할 때 자동으로 실행하는 함수(=method)
        self.first=first #self => cal1313 => cal1313.first = first(13)
        self.second=second
    def add(self):#self =>cal1313
        result=self.first+self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
    def __add__(self, other):
        #연산자 오버로딩:
        #__add__ = '+'
        print("연산자 오버로딩 %d %d" %(self.first,other.first))

    def div(self):
        #함수(메소드) 재정의 = 메소드오버라이딩
        if self.second==0:
            return 0
        else:
            return self.first/self.second
class cal1313more(cal1313):
    #상속!!!class 하위클래스이름(상위클래스이름)
    def pow(self):
        result=self.first**self.second
        return result
    def addmul(self):
        #더하기연산과 곱하기연산을 동시에 수행하여
        #튜플로 반환하는 코드를 작성
        #(13,13) => (26,169)
        return (self.first + self.second, self.first * self.second)


#객체의 선언
a1313=cal1313(13,13) #__init__ 변수에 값을 저장
print(a1313.add())
print(a1313.sub())
b1313=cal1313more(13,13)
print(b1313.add())
print(b1313.pow())
print(b1313.div())
a1313=cal1313(13,0)
b1313=cal1313more(13,0)
print(a1313.div())
print(b1313.div())
a1313+b1313
