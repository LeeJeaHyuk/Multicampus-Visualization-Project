import matplotlib.pyplot as plt
import pandas as pd

fig = plt.figure()

ax01 = fig.add_subplot(1, 2, 1)
ax02 = fig.add_subplot(1, 2, 2)

#연도별 평균 장마일수 변화 그래프
rainseason = pd.read_csv('data/rainseason_yearmean.csv')

fig, ax = plt.subplots()
ax01.plot(rainseason['year'], rainseason['rainseason'],color='b', label="rainyday")


#장마기간 동안 합계 강수량 변화
raintotal=pd.read_csv('data/raintotal.csv')
#print(raintotal)

#plt.figure()
#sns.barplot(data=raintotal, x='start', y='total')
ax02.plot(raintotal['start'], raintotal['total'],color='r', label="totalrain")

plt.show()


