import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('csv file/CarboneTypoon03.csv')

# print(df.columns)
# 'Year',
# 'Named Storms',
# 'Named Storm Days',
# 'Hurricanes',
# 'Hurricanes Days',
# 'Cat. 3+ Hurricanes',
# 'Cat. 3+ Hurricanes Days',
# 'Accumulated Cyclone Energy',
# 'World Carbone Emission',
# 'World Carbone Emission02',
# 'cat3_corr01',
# 'cat3_corr02'

# 0. year 데이터 나누기
# 년도값은 정규화 하지 않기 위해
df_unscaled = df['Year']

df02 = df.drop("Year", axis ='columns')


# # 1. 데이터 정규화
scaler = MinMaxScaler()
scaled_values = scaler.fit_transform(df02)
df02_scaled = pd.DataFrame(scaled_values, columns=df02.columns)
# print(df02_scaled)



# 선형 관계를 다시 그려보기
fig01 = plt.figure()
# ax01 = fig01.add_subplot(2,1,2)
ax02 = fig01.add_subplot(2,1,1)
# sns.regplot(data = df02_scaled , x=df02_scaled['World Carbone Emission'], y=df02_scaled['Cat. 3+ Hurricanes'], ax=ax01)
sns.regplot(data = df02_scaled , x=df02_scaled['World Carbone Emission02'], y=df02_scaled['Cat. 3+ Hurricanes'], ax=ax02)
plt.show()


fig02 = plt.figure()
ax03 = fig02.add_subplot(3,1,1)
# ax04 = fig02.add_subplot(3,1,2)
ax05 = fig02.add_subplot(3,1,3)
sns.lineplot(data = df02_scaled , x=df['Year'], y=df02_scaled['Cat. 3+ Hurricanes'], ax=ax03)
# sns.lineplot(data = df02_scaled , x=df['Year'], y=df02_scaled['World Carbone Emission'], ax=ax04)
sns.lineplot(data = df02_scaled , x=df['Year'], y=df02_scaled['World Carbone Emission02'], ax=ax05)
plt.show()

# 2015년 이후 데이터를 보면 cat.3 이상의 태풍이 세계 탄소 배출량과 어느정도 관련이 있는 모습이다
