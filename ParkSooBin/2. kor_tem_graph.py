# 년도별 기온변화를 그래프로 -> 한 화면에 전부

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "gulim"
plt.rcParams["font.size"] = 10

# kor_tem : 우리나라평균기온변화
kor_tem = pd.read_excel('C:/Users/tnqls/Documents/바탕 화면/Multicampus-2210-ProjectGroup4/ParkSooBin/data/우리나라평균기온변화.xlsx')


# 년도별 평균기온, 최고기온, 최저기온을 그래프로
year_mean = kor_tem.groupby('구분')['평균기온'].mean().reset_index()
print(year_mean)

year_min = kor_tem.groupby('구분')['최저기온'].mean().reset_index()
print(year_min)

year_max = kor_tem.groupby('구분')['최고기온'].mean().reset_index()
print(year_max)

fig = plt.figure()
ax01 = fig.add_subplot(1, 2, 1)
ax02 = fig.add_subplot(2, 2, 2)
ax03 = fig.add_subplot(2, 2, 4)

sns.lineplot(x = year_mean['구분'], y = year_mean['평균기온'], ax=ax01)
sns.lineplot(x = year_max['구분'], y = year_max['최고기온'], ax=ax02)
sns.lineplot(x = year_min['구분'], y = year_min['최저기온'], ax=ax03)

plt.tight_layout()
plt.show()