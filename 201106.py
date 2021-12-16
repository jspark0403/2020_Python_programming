#20201106 1313 박진성

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns',10)
wp1313=pd.read_csv('http://jhserver.dimigo.hs.kr/drinks.csv')
wp1313['continent']=wp1313['continent'].fillna('EXT') #fillna('대체값') : 결측값 보정

#시각화2 - 그래프꾸미기
#대륙별 total_litres_of_pure
total_mean=wp1313.total_litres_of_pure_alcohol.mean()
total_mean1=wp1313['total_litres_of_pure_alcohol'].mean()
print(type(total_mean), type(total_mean1)) #!!!!!! type(total_mean) vs type(total_mean1) 둘 다 class
conti_mean=wp1313.groupby('continent')['total_litres_of_pure_alcohol'].mean()
#groupby가 들어가면 series 아니면 class

continents = conti_mean.index.tolist()
print(continents)
continents.append('mean') #str 'mean'
print(continents)
x_pos = np.arange(len(continents))
alcohol = conti_mean.tolist()
print(alcohol)
alcohol.append(total_mean)
bar_list = plt.bar(x_pos, alcohol, align='center', alpha=0.6)
bar_list[len(continents) - 1].set_color('g')
plt.plot([0., 6], [total_mean, total_mean], "k--")
plt.xticks(x_pos, continents)
plt.ylabel('total_litres_of_pure_alcohol')
plt.title('total_litres_of_pure_alcohol by Continent')
plt.show()

beer_group = wp1313.groupby('continent')['beer_servings'].sum()
continents = beer_group.index.tolist()
y_pos = np.arange(len(continents))
alcohol = beer_group.tolist()
print(alcohol)
bar_list = plt.bar(y_pos, alcohol, align='center', alpha=0.5)
bar_list[continents.index("EU")].set_color('r') #색으로 강조
plt.plot([3., 5], [3345, 3345], "k--")
plt.xticks(y_pos, continents)
plt.ylabel('beer_servings')
plt.title('beer_servings by Continent')
plt.show()

#한국의 알코올 소비량의 순위
#새로운 컬럼의 생성 / 순위정보 만들기
wp1313['total_serving']=wp1313['beer_servings']+wp1313['spirit_servings']+wp1313['wine_servings']
wp1313['alcohol_rate']=wp1313['total_litres_of_pure_alcohol']/wp1313['total_serving']
print(wp1313.info())
wp1313['alcohol_rate']=wp1313['alcohol_rate'].fillna(0) #결측값 보정
#순위정보만들기
c_with_rank=wp1313[['country','alcohol_rate']]
print(type(c_with_rank))
c_with_rank=c_with_rank.sort_values(by=['alcohol_rate'],ascending=False)
c_with_rank.to_csv('wp1313_rank.csv')

#시각화
country_list = c_with_rank.country.tolist()
x_pos = np.arange(len(country_list))
rank = c_with_rank.alcohol_rate.tolist()
bar_list = plt.bar(x_pos, rank)
bar_list[country_list.index("South Korea")].set_color('r')
plt.ylabel('alcohol rate')
plt.title('liquor drink rank by contry')
plt.axis([0, 200, 0, 0.3])
korea_rank = country_list.index("South Korea")
korea_alc_rate = c_with_rank[c_with_rank['country'] == 'South Korea']['alcohol_rate'].values[0]
plt.annotate('South Korea : ' + str(korea_rank + 1), xy=(korea_rank, korea_alc_rate), xytext=(korea_rank + 10, korea_alc_rate + 0.05),arrowprops=dict(facecolor='red', shrink=0.05))
plt.show()



