import pandas as pd

#검색량 간의 상관 관계
탄소배출 = pd.read_csv('data/datalab_탄소배출.csv')
기후위기 = pd.read_csv('data/datalab_기후위기.csv')
온실가스 = pd.read_csv('data/datalab_온실가스.csv')
이상기후 = pd.read_csv('data/datalab_이상기후.csv')

#탄소배출, 기후위기
carbonclimate=탄소배출['data'].corr(기후위기['data'], method = 'pearson')
#print(carbonclimate)
#0.8651425867768688 -> 매우 강한 상관관계

#탄소배출, 이상기후
carbonabnormal=탄소배출['data'].corr(이상기후['data'], method = 'pearson')
#print(carbonabnormal)
#0.6964117754525839 -> 강한 상관관계

#온실가스, 기후위기
gasclimate=온실가스['data'].corr(기후위기['data'], method = 'pearson')
#print(gasclimate)
#0.4988051864174031 -> 상관관계

#온실가스, 이상기후
gasabnormal = 온실가스['data'].corr(이상기후['data'], method = 'pearson')
#print(gasabnormal)
#0.5035435589849869 -> 상관관계






#장마일수와 산업 온실가스 배출 파일 불러오기
rainseason = pd.read_csv('data/rainseason_yearmean.csv')
gastotal = pd.read_csv('data/gastotal.csv')
raintotal=pd.read_csv('data/raintotal.csv')
emission=pd.read_csv('data/kor_emission.csv')
heat=pd.read_csv('data/heat.csv')
gasmax=pd.read_csv('data/year_gasmax.csv')
rain1990=pd.read_csv('data/rain1990_mean.csv')
rain1990_total=pd.read_csv('data/rain1990_total.csv')
yeargassum=pd.read_csv('data/gassum_fin.csv')
rain2016=pd.read_csv('data/rain2016sum.csv')


#폭염일수와 탄소 배출 상관관계
emissionheat = heat['year.sum'].corr(emission['total_ems'], method = 'pearson')
#print(emissionheat)
#0.26253294942572464 -> 약한 상관관계


#평균 장마일수와 탄소 배출 상관관계
raingasmax= rain1990['rainseason'].corr(emission['total_ems'], method='pearson')
#print(raingasmax)
#0.05481970735862907 : 상관 없다

#합계 강수량과 탄소 배출 상관관계
rain1990_total= rain1990_total['rain_total'].corr(emission['total_ems'], method='pearson')
#print(rain1990_total)
#-0.01609438998087995 : 상관 없다


#장마일수 평균과 산업 온실가스 최대 배출량 상관 관계
rainbusgasmax = rainseason['rainseason'].corr(gasmax['GHG_EMS'], method='pearson')
print(rainbusgasmax)
#0.7272548801350748 -> 강한 상관 관계

#장마일수 평균과 산업 온실가스 총합 상관 관계
yeargassumrain = rainseason['rainseason'].corr(yeargassum['GHG_EMS'], method='pearson')
print(yeargassumrain)
#0.36992849735726446 -> 약한 상관 관계

#합계 강수량과 산업 온실가스 최대 배출량 상관 관계
rainsumgas=rain2016['total'].corr(gasmax['GHG_EMS'], method='pearson')
print(rainsumgas)
#0.7616279925340889 -> 강한 상관관계

#합계 강수량과 산업 온실가스 총합 상관 관계
rainsumgassum=rain2016['total'].corr(yeargassum['GHG_EMS'],method='pearson')
print(rainsumgassum)
#-0.011620222695820723 : 상관 없음


#폭염 일수와 산업 온실가스 최대 배출량 상관 관계
gasheat = heat['year.sum'].corr(gasmax['GHG_EMS'], method = 'pearson')
print(gasheat)
#0.1484269837567242 : 상관 거의 없다


#폭염 일수와 산업 온실가스 총합 상관 관계
gassumheat = heat['year.sum'].corr(yeargassum['GHG_EMS'], method='pearson')
print(gassumheat)
#-0.6528451577216 : 상관 없다



#강한 상관 관계에 있는 것만 그래프 그리기
import seaborn as sns
import matplotlib.pyplot as plt

fig = plt.figure()
ax01 = fig.add_subplot(1, 2, 1)
ax02 = fig.add_subplot(2, 2, 2)
ax03 = fig.add_subplot(2, 2, 4)

graph_rain_gas=pd.read_csv('data/graph_rain_gas.csv')


#합계 강수량과 산업 온실가스 최대 배출량 상관 관계
sns.regplot(data=graph_rain_gas, x='GHG_EMS', y='rain_sum', ax=ax01)
#장마일수 평균과 산업 온실가스 최대 배출량 상관 관계
sns.regplot(data=gasmax, x='GHG_EMS', y='rainseason',ax=ax02)
#폭염일수와 탄소 배출 상관관계
sns.regplot(data=heat, x='year.sum', y='total_ems',ax=ax03)

plt.show()

