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


#장마일수와 산업 온실가스 배출 상관관계
rainseason = pd.read_csv('data/rainseason_yearmean.csv')
gastotal = pd.read_csv('data/gastotal.csv')
raintotal=pd.read_csv('data/raintotal.csv')



#평균장마일수와 최대온실가스 배출 상관관계
raingasmax = rainseason['rainseason'].corr(gastotal[int('GHG_EMS')], method = 'pearson')
print(raingasmax)
