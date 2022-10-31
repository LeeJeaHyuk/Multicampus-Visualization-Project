# mycrawling 환경에서 진행

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv file/CarboneTypoon.csv')
print(df.columns)

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


## 1. World Carbone Emission값이 없는 년도 제거하고 분석 == df01
df01 = df.dropna()
# print(df01)

## 탄소 배출량 그래프
fig01, ax01 = plt.subplots()

x = df01['Year']
y01 = df01['World Carbone Emission']

ax01.plot(x,y01, color='r', label='carbone(ton)')

ax01.legend()
ax01.set_title("carbone emission of year")

## show 이후에 저장하면 닫힌 다음 빈 화면 출력된다
plt.savefig('./graph file/carbone emission of year.png', dpi=300)
plt.show()


