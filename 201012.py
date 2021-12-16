#1313 박진성

#데이터 분석
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#데이터 읽고 확인하기
ch1313=pd.read_csv('http://jhserver.dimigo.hs.kr/chipotle.tsv',sep='\t')
#tsv : 구분자 tap / csv : 구분자 ,
pd.set_option('display.max_columns',10)
print(ch1313)
print(ch1313.shape) #shape vs reshape() 속성 vs 메소드
print(ch1313.info()) #

df1313=pd.read_excel('http://jhserver.dimigo.hs.kr/class2020.xlsx')
df1313_tmp=df1313.iloc[:,8:12]
print(df1313_tmp)
df1313_tmp.to_csv('w1313a.csv') #csv comma tsv tab

#데이터분석, 행, 열, 기초통계량
print(ch1313.head(3)) # 행 3개 출력
#DB vs Pandas
#rows(행) * columns(열)
#record(레코드) * field(열)
#피쳐(데이터) 와 인사이트(분석값)
print(ch1313.columns)
print(ch1313.index)

ch1313['order_id']=ch1313['order_id'].astype(str) #수치데이터
#str(10)
c1=[1,2,3]
print(str(c1[2]))
print('------------------------------------')
print(type(ch1313['order_id'])) #!!!
print(ch1313)
print(ch1313.describe()) #기초통계량 수치데이터
#객체 = 속성+메소드

#가장 많이 주문한 메뉴 Top 10개
#Pandas 자료구조: Series(1차원), DataFrame(2차원), Panel(3차원)
item_count=ch1313['item_name'].value_counts()[:10]
print(item_count)
for idx,(val,cnt) in enumerate(item_count.iteritems(),1):
    print('Top',idx,":",val,cnt)

#Second Time
#중복데이터 제거 unique()
print(len(ch1313['order_id'].unique()))
print(len(ch1313['item_name'].unique()))

#메뉴 주문 개수와 중량
order_count=ch1313.groupby('item_name')['order_id'].count()
print(order_count[:10])
item_quantity=ch1313.groupby('item_name')['quantity'].sum()
print(item_quantity[:10])

print('-----------------------------------groupby')
print(list(ch1313.groupby('item_name')['order_id']))

#시각화 : 메뉴별 주문의 총량을 막대그래프로.

item_name_list=item_quantity.index.tolist()
x_pos=np.arange(len(item_name_list)) #메뉴이름이 너무 길어서 표현이 불가
print(x_pos)
#x_pos=item_name_list
order_cnt=item_quantity.values.tolist()

plt.bar(x_pos,order_cnt,align='center')
plt.ylabel('ordered_item_count')
plt.title("Distribution of All ordered item")

plt.show()

print(ch1313.describe()) #기초통계량 수치데이터
#print(ch1313)
ch1313['item_price']=ch1313['item_price'].apply(lambda x: float(x[1:]))
#각 피쳐(가격 데이터에 '$' 문자를 제거
print(ch1313.info())
print(ch1313.describe()) #기초통계량 수치데이터
print(ch1313.info()) #데이터그룹의 기본정보 출력

#Homework
#value_counts() vs unique() 차이점을 간략히 기술한 후 제출하세요!!!
'''
unique를 이용하면 유일한 값을 찾을 수 있고
value_counts를 사용하면 유일한 값별 개수를 셀 수있다.'''
#직접 작성하시면 됩니다.
#dimigo.biz > submit > 1-3