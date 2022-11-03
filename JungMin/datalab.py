import matplotlib.pyplot as plt
import pandas as pd

#2016~2022 검색량 추이
fig, ax = plt.subplots()

탄소배출 = pd.read_csv('data/datalab_탄소배출.csv')
기후위기 = pd.read_csv('data/datalab_기후위기.csv')
온실가스 = pd.read_csv('data/datalab_온실가스.csv')
이상기후 = pd.read_csv('data/datalab_이상기후.csv')


ax.plot(탄소배출['month'], 탄소배출['data'],color='blue', label="carbon emissions")
ax.plot(탄소배출['month'], 기후위기['data'],color='red', label="climate crisis")
ax.plot(탄소배출['month'], 온실가스['data'],color='green', label="green gas")
ax.plot(탄소배출['month'], 이상기후['data'],color='orange', label="abnormal climate")

ax.legend()

plt.show()

