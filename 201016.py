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
print(ch1313.info()) #결측값 확인 , 데이터 형태

#value_counts() vs Unique() 차이점
print(ch1313['item_name'].value_counts()) #중복값을 제거한 데이터범주 + 개수
print(type(ch1313['item_name'].value_counts())) #Series
print(ch1313['item_name'].unique()) #중복값 제거한 데이터범주
print(type(ch1313['item_name'].unique())) #ndarray

#Series
p1=pd.Series([1,2,3])
print(p1)
print(p1.index.tolist())
print(p1.values.tolist())

ch1313['order_id']=ch1313['order_id'].astype(str) #수치데이터
ch1313['item_price']=ch1313['item_price'].apply(lambda x: float(x[1:]))
#주문당 평균금액 출력
print(list(ch1313.groupby('order_id')['item_price']))
print(ch1313.groupby('order_id')['item_price'].sum())
print(ch1313.groupby('order_id')['item_price'].sum().mean())

#한 주문에 10달러 이상 지불한 주문번호 출력
orderid_group=ch1313.groupby('order_id').sum()
print(orderid_group)
result=orderid_group[orderid_group.item_price>=10] #
print(result[:10])
print(type(result))
print(result.index.values)

#각 메뉴의 가격 구하기 #50개 메뉴
item_one=ch1313[ch1313.quantity==1]
price_per_item=item_one.groupby('item_name').min()
print(price_per_item.sort_values(by='item_name',ascending=False))

#시각화
item_name_list=price_per_item.index.tolist()
x_pos=np.arange(len(item_name_list))
item_price=price_per_item['item_price'].tolist()
plt.bar(x_pos,item_price,align='center')
plt.ylabel('item_price($)')
plt.title('Distribution of item price')
plt.show()

plt.hist(item_price)
plt.ylabel('count')
plt.title('Histogram of item')
plt.show()

#막대그래프에서 x축과 y축을 바꾸어서 가로로 변경하여 출력
item_name_list=price_per_item.index.tolist()
x_pos=np.arange(len(item_name_list))
item_price=price_per_item['item_price'].tolist()
plt.barh(x_pos,item_price,align='center')
plt.xlabel('item_price($)')
plt.title('Distribution of item price')
plt.show()
