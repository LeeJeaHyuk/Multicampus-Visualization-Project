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

# 2-1. 'Named Storms', 'World Carbone Emission' 의 연관성 구하기

#sns.lineplot(crawling=df02_scaled, x=df_Year,y=df02_scaled['Named Storms'], ax=ax01)
fig = plt.figure(constrained_layout=True)
ax01 = fig.add_subplot(2,1,1)
ax02 = fig.add_subplot(2,1,2)


sns.lineplot(x=df01['Year'], y=df01['World Carbone Emission'], ax=ax01)
sns.lineplot(x=df01['Year'], y=df01['Cat. 3+ Hurricanes'], ax=ax02)
# 탄소는 연간 상승률이 뚜렷하지만 태풍은 그렇지 않아 보이는 모습
plt.savefig('./graph file/analysis03_cat3AndCarbonOfYear.png')


fig01 = plt.figure()
ax03 = fig01.add_subplot(2,2,1)
ax04 = fig01.add_subplot(2,2,2)
ax05 = fig01.add_subplot(2,2,3)

## 정규화 한 데이터로 두 특성 비교
sns.regplot(x=df02_scaled['World Carbone Emission'], y=df02_scaled['Named Storms'], ax=ax03)
sns.regplot(x=df02_scaled['World Carbone Emission'], y=df02_scaled['Hurricanes'], ax=ax04)
sns.regplot(x=df02_scaled['World Carbone Emission'], y=df02_scaled['Cat. 3+ Hurricanes'], ax=ax05)

## 그냥 두 특성을 비교했을 때에는 큰 연관성이 보이지 않는 것 같다

plt.tight_layout()
plt.savefig('./graph file/analysis03_HurricaneOfCarbon.png')

plt.show()

## 상관계수 확인해보기
df02_scaled_corr = df02_scaled.corr("pearson")

# pd.set_option('display.max_rows',None)
# pd.set_option('display.max_columns',None)
print(df02_scaled_corr['World Carbone Emission'])
# Cat. 3+ Hurricanes 특성이 0.057734 로 그나마 높지만 선형관련성이 거의 없다

## 선형회귀 그래프 그려보기
fig02 = plt.figure()
ax06 = fig02.add_subplot(2,1,1)
sns.regplot(data = df02_scaled , x=df02_scaled['World Carbone Emission'], y=df02_scaled['Hurricanes'], ax=ax06)
plt.savefig('./graph file/analysis03_carbone_huricane_regplot.png')
# 상관관계가 거의 없었음으로 회귀 그래프 또한 상관관계가 없다고 나온다


plt.show()

# 가설1 : 탄소배출량의 증가는 태풍의 개수 증가와 관련성이 거의 없다
# 가설2 : 데이터에서의 문제점