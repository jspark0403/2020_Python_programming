#201112

#데이터분석
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns',10)
wp1313=pd.read_csv('http://jhserver.dimigo.hs.kr/drinks.csv')
wp1313['continent']=wp1313['continent'].fillna('EXT') #fillna('대체값') : 결측값 보정

#새로운 컬럼의 생성 / 순위정보 만들기
wp1313['total_serving']=wp1313['beer_servings']+wp1313['spirit_servings']+wp1313['wine_servings']
wp1313['alcohol_rate']=wp1313['total_litres_of_pure_alcohol']/wp1313['total_serving']
wp1313['alcohol_rate']=wp1313['alcohol_rate'].fillna(0) #결측값 보정

#loc() vs isin()

#전체평균보다 적은 알코올을 섭취하는 대륙 중에서 spirit을 가장 많이 마시는 국가를 찾으세요.
total_avg=wp1313.total_litres_of_pure_alcohol.mean()
con_mean=wp1313.groupby('continent')['total_litres_of_pure_alcohol'].mean()
con_under_mean=con_mean[con_mean<=total_avg].index.tolist()
print(con_under_mean) #con_under_mean => 리스트자료형
#loc() : 행전체를 가져옴.
print(wp1313.continent.isin(con_under_mean)) #'AF', 'AS' ,'OC'
df_con_under_mean=wp1313.loc[wp1313.continent.isin(con_under_mean)]
#isin() : 리스트요소가 포함되어 있는지 확인하는 메소드
most_spirit_over_mean=df_con_under_mean.loc[df_con_under_mean['spirit_servings'].idxmax()]
print(most_spirit_over_mean)


#데이터가져오기 -> info() -> fillna() -> DF[] > Series

#자료구조
#배열, 스택, 큐, 리스트, 트리, 그래프
#선형구조 : 배열, 스택, 큐, 리스트
#비선형구조 : 트리, 그래프
#파이썬 : 자료형 숫자형, 문자형, 리스트형(=배열), 튜플형, 딕셔너리형, 집합형, 부울형
#list()=[] / numpy:ndarray

#Stack 구현 list() 자료형이용
#1. 스택저장소 2. 스택포인터 3. 스택 용량 4. 입출력 5. 오버플로/언더플로

stk1313=[] #리스트형 list() 저장소
ptr=0 #스택포인터
c1313=13 #저장용량

menu="1.PUSH 2.POP 3.PEEK 4.EXIT"
print("Stack Start!!!")

while True:
    print(menu)
    print('Stack now:',ptr,'/',c1313)
    k=int(input("Select Num :")) #input() : 기본자료형 문자형
    if k==1: #PUSH 데이터 넣기
        x=int(input("Enter Number"))
        if ptr>1313:
            print("Stack Full!!!") #오버플로
        else:
            stk1313.append(x)
            print(x,"Push Complete!!!")
            ptr=ptr+1
    elif k==2: #POP 데이터 꺼내기
        if ptr<=0:
            print("Stack Empty!!!") #언더플로
        else:
            y=stk1313.pop()
            print(y,"is POP!")
            ptr=ptr-1
    elif k==3: #PEEK 최상위 데이터 찾기
        if ptr <=0:
            print("Stack Empty!!!") # 언더플로
        else:
            print("Peek Data:",stk1313[ptr-1])
    elif k==4:
        print(stk1313)
    else: #종료
        break


#스택 내에 모든 원소를 확인하는 코드를 작성하여 추가해주세요.
#menu="1.PUSH 2.POP 3.PEEK 4.DUMP 5.EXIT"
#dump 기능을 추가해주세요.
print(stk1313)
