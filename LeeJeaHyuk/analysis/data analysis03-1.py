import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('csv file/CarboneTypoon.csv')
# print(df.columns)
df01 = df.dropna()

# 0. year 데이터 나누기
# 년도값은 정규화 하지 않기 위해
df_Year = df01['Year']
# print(df01_Year)
df02 = df01.drop("Year", axis ='columns')

# 1. 데이터 정규화
scaler = MinMaxScaler()
scaled_values = scaler.fit_transform(df02)
df02_scaled = df02
df02_scaled.loc[1:] = scaled_values

# 2. 선형 회귀 분석
# 연간 탄소 배출량의 증가가 태풍과의 연관성이 있는가

# 'Year',
# 'Named Storms',
# 'Named Storm Days',
# 'Hurricanes',
# 'Hurricanes Days',
# 'Cat. 3+ Hurricanes',
# 'Cat. 3+ Hurricanes Days',
# 'Accumulated Cyclone Energy',
# 'World Carbone Emission'
#   - 년도별 탄소배출량 (ton)
df03 = df02_scaled[['Named Storms','Hurricanes','Cat. 3+ Hurricanes','World Carbone Emission']]
corr = df03.corr()
corr01 = corr[['World Carbone Emission']]
# LABELS = ['Named Storms','Hurricanes','Cat. 3+ Hurricanes','World Carbone Emission']
sns.heatmap(corr01,
            cmap='Blues',
            # xticklabels=LABELS,
            # yticklabels=LABELS,
            annot=True,)
plt.title('Corr Typoon and Carbone Emission')

plt.savefig('./graph file/analysis03-1 hurricane carbone corr heatmap.png')

plt.show()
