import matplotlib.pyplot as plt
import pandas as pd

#연도별 폭염일수 총합 변화(1990~2022)
heat = pd.read_csv('data/heat.csv')

fig, ax = plt.subplots()
ax.plot(heat['year'], heat['year.sum'],color='r', label="폭염")


plt.show()