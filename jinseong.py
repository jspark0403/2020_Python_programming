import pandas as pd
aaa=pd.read_csv('http://jhserver.dimigo.hs.kr/test13.csv')
print(aaa.info())
print(aaa.groupby('User').Total.sum().sort_values(ascending=False))
