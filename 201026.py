#201026

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns',10)
wp1313=pd.read_csv('http://jhserver.dimigo.hs.kr/drinks.csv')
print(wp1313.info())
print(wp1313.describe())

#상관계수(단일상관분석 / 다중상관분석)
corr1=wp1313[['beer_servings','wine_servings']].corr(method='pearson')
print(corr1)

cols=['beer_servings','spirit_servings','wine_servings','total_litres_of_pure_alcohol']
corr2=wp1313[cols].corr(method='pearson')
print(corr2)
#그래프 heatmap vs pairplot 자잘한 것 시험 X
cols_view=['beer_servings','spirit_servings','wine_servings','total_litres_of_pure_alcohol']
sns.set(font_scale=1.5)
hm = sns.heatmap(corr2.values,cbar = True,annot = True,square = True, fmt = '.2f',annot_kws = {'size' : 15},yticklabels=cols_view,xticklabels=cols_view)

plt.tight_layout()
plt.show()

#pairplot() 산점도 그래프
sns.set(style='whitegrid',context='notebook')
sns.pairplot(wp1313[['beer_servings','spirit_servings','wine_servings','total_litres_of_pure_alcohol']],height=2.5)
plt.show()

p1313=sns.load_dataset('penguins')
sns.pairplot(p1313,hue='species',palette='prism')
#hue:구분자
plt.show()