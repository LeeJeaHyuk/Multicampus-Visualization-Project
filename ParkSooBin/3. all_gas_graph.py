# 년도별 분야별 온실가스배출량을 그래프로 -> 한 화면에 전부

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "gulim"
plt.rcParams["font.size"] = 10


# all_gas : 국가온실가스배출량
all_gas = pd.read_excel('C:/Users/tnqls/Documents/바탕 화면/Multicampus-2210-ProjectGroup4/ParkSooBin/data/국가온실가스배출량.xlsx')


# 년도별 에너지에서의 온실가스배출량
year_energy = all_gas.groupby('구분')['에너지'].mean().reset_index()
print(year_energy)

# 년도별 산업공정에서의 온실가스배출량
year_industry = all_gas.groupby('구분')['산업공정'].mean().reset_index()
print(year_industry)

# 년도별 농업에서의 온실가스배출량
year_agriculture = all_gas.groupby('구분')['농업'].mean().reset_index()
print(year_agriculture)

# 년도별 LULUCF에서의 온실가스배출량
year_lulucf = all_gas.groupby('구분')['LULUCF'].mean().reset_index()
print(year_lulucf)

# 년도별 폐기물에서의 온실가스배출량
year_waste = all_gas.groupby('구분')['폐기물'].mean().reset_index()
print(year_waste)

# 사용하게 된다면 그래프 위치 조정해야 함.
fig = plt.figure()
ax01 = fig.add_subplot(1, 5, 1)
ax02 = fig.add_subplot(1, 5, 2)
ax03 = fig.add_subplot(1, 5, 3)
ax04 = fig.add_subplot(1, 5, 4)
ax05 = fig.add_subplot(1, 5, 5)

sns.lineplot(x = year_energy['구분'], y = year_energy['에너지'], ax=ax01)
sns.lineplot(x = year_industry['구분'], y = year_industry['산업공정'], ax=ax02)
sns.lineplot(x = year_agriculture['구분'], y = year_agriculture['농업'], ax=ax03)
sns.lineplot(x = year_lulucf['구분'], y = year_lulucf['LULUCF'], ax=ax04)
sns.lineplot(x = year_waste['구분'], y = year_waste['폐기물'], ax=ax05)

plt.tight_layout()
plt.show()