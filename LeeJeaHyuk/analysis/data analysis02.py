import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('csv file/CarboneTypoon.csv')
# print(df.columns)
df01 = df.dropna()

#  df01.columns
# 'Year',
# 'Named Storms',
# 'Named Storm Days',
# 'Hurricanes',
# 'Hurricanes Days',
# 'Cat. 3+ Hurricanes',
# 'Cat. 3+ Hurricanes Days',
# 'Accumulated Cyclone Energy',
# 'World Carbone Emission'
    # - 년도별 탄소배출량 (ton)

# df = CarboneTypoon 데이터
# df01 = CarboneTypoon 에서 null값이 존재하는 행을 제거한 데이터
# df02 = Year 제거한 데이터
# df02_scaled = df02를 정규화한 데이터

## 0. year 데이터 나누기
df_Year = df01['Year']
# print(df01_Year)
df02 = df01.drop("Year", axis ='columns')
# print(df02)

## 2. 정규화
scaler = MinMaxScaler()
scaled_values = scaler.fit_transform(df02)
df02_scaled = df02
df02_scaled.loc[1:] = scaled_values
# print(df02_scaled)


# fig01, ax01 = plt.subplots()
#
# x = df_Year
# y01 = df02_scaled['World Carbone Emission']
# y02 = df02_scaled['Named Storms']
#
# ax01.plot(x,y01, color='r', label='carbone(ton)')
# ax01.plot(x,y02, color='r', label='Named storms')
#
# ax01.legend()
# ax01.set_title("carbone emission of year")
#
# plt.savefig('./graph file/Carbone Emission and Named storm.png')
# plt.show()


## 03 여러개 특성을 같이 보기
fig = plt.figure()
ax01 = fig.add_subplot(2,2,1)
ax02 = fig.add_subplot(2,2,2)
ax03 = fig.add_subplot(2,2,3)
ax04 = fig.add_subplot(2,2,4)

sns.lineplot(x=df_Year,y=df01['Named Storms'], ax=ax01)
sns.lineplot(x=df_Year,y=df01['Hurricanes'], ax=ax02)
sns.lineplot(x=df_Year,y=df01['Cat. 3+ Hurricanes'], ax=ax03)
sns.lineplot(x=df_Year,y=df01['World Carbone Emission'], ax=ax04)

plt.tight_layout()

plt.savefig('./graph file/analysis02_HurricanesOfYear.png')
## 그래프를 보았을 때 Cat. 3+ Hurricanes 데이터가 연간 탄소 배출량과 가장 비슷해보인다
plt.show()


