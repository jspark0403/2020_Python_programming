# 200921 1313

# 1.Pandas 2.Seaborn 3.xlrd

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

'''
sns.distplot(np.random.normal(size=1000), hist=False)
plt.show()
'''

import pandas as pd
data1 = [1, 2, 3, 4, 5]
p1 = pd.Series(data1)
print(p1)
p1.plot()
plt.show()

# DataFrame
data2 = {
    'year': [2018, 2019, 2020],
    'persons': [5000, 5500, 6000],
    'p_rate': [10.0, 20.0, 30.0],
}
p2 = pd.DataFrame(data2)
print(p2)
p2.plot(kind="bar")
plt.show()

print(p2['year'] >= 2019)  # 불라인 인덱싱
print(p2.head(3))  # 상위 컬럼
print(p2.loc[:, 'persons':'p_rate'])
# loc : 컬럼명 슬라이싱
print(p2.iloc[:, 0:2])  # 인덱스 슬라이싱
print(p2.describe())  # 기본 통계값 계산

# 엑셀에서 데이터 불러오기 또는 쓰기
# 3반만 DATA만 추출해보세요.
df1313 = pd.read_excel('http://jhserver.dimigo.hs.kr/class2020.xlsx')
print(df1313)
df1313_new = df1313.iloc[:, 9:12]
df1313_new.to_csv('w1313.csv')

#where : 인덱스
n1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
n1 = n1+10
print(n1)
n1_new = np.where(n1 % 2 == 0)
print(n1_new)
n2 = n1.reshape(3, 3)
print(n2)
n2_new = np.where(n2 >= 4)
print(n2_new)
