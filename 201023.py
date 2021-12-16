#201023

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

wp1313=pd.read_csv('http://jhserver.dimigo.hs.kr/drinks.csv')


#1. 다음 데이터 셋에서 결측값이 존재하는 컬럼이 무엇이며 결측값은 몇개입니까?
#int, float
#2. 다음 데이터 셋에서 기초통계량을 산출할 때 통계량이 산출되는 컬럼은 몇개입니까?



print(wp1313.info())
print(wp1313.describe())