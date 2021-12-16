#201019.py #1313 박진성

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

#데이터 읽고 확인하기
ch1313=pd.read_csv('http://jhserver.dimigo.hs.kr/chipotle.tsv',sep='\t')
#tsv : 구분자 tap / csv : 구분자 ,
pd.set_option('display.max_columns',10)
print(ch1313.info()) #결측값 확인 , 데이터 형태

ch1313['order_id']=ch1313['order_id'].astype(str) #수치데이터
ch1313['item_price']=ch1313['item_price'].apply(lambda x: float(x[1:]))

#가장 비싼 주문에서 메뉴를 몇개 주문했는가?
print(ch1313.groupby('order_id').sum().sort_values(by='item_price',ascending=False)[:10]) #false = 기본값이 오름차순 이라서
#특정 메뉴가 몇번 주문 되었는지 확인하기!
print(ch1313['item_name'].unique())
ch1313_select=ch1313[ch1313['item_name']=='Chicken Salad']
ch1313_select=ch1313_select.drop_duplicates(['item_name','order_id'])
print(len(ch1313_select))
print(ch1313_select.head(10))


#특정 메뉴가 2번 이상 주문한 주문 횟수 구하기!
ch1313_select2=ch1313[ch1313['item_name']=='Chicken Salad']
ch1313_select2_ordersum=ch1313_select2.groupby('order_id').sum()['quantity']
ch1313_select2_result=ch1313_select2_ordersum[ch1313_select2_ordersum>=2]
print(len(ch1313_select2_result))
print(ch1313_select2_ordersum.head(10))

