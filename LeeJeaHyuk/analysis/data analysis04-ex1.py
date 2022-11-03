import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('csv file/CarboneTypoon.csv')
# print(df.columns)
df01 = df.dropna()

df_shared = pd.read_csv('csv file/Shared folder/World-Carbon-Emission.csv')

# print(df01)
# print(df_shared)

# 공유받은 전세계 탄소 배출량 데이터와 기존 데이터 합치기
df01=df01.reset_index(drop=True)
CarboneTypoon02 = pd.concat([df01,df_shared['Total_Emission']], axis=1)

# 열이름 변경
CarboneTypoon02.rename( columns = { 'Total_Emission':'World Carbone Emission02'}, inplace=True)

# 상관계수 계산
corr02 = CarboneTypoon02.corr('pearson')

corr03 = pd.DataFrame(data = corr02, columns = ['World Carbone Emission','World Carbone Emission02'])

# print(corr03)

'''                            World Carbone Emission  World Carbone Emission02
Year                                      0.907531                  0.979975
Named Storms                             -0.070750                 -0.014149
Named Storm Days                         -0.303960                 -0.276543
Hurricanes                               -0.280653                 -0.256968
Hurricanes Days                          -0.437466                 -0.415491
Cat. 3+ Hurricanes                        0.057734                  0.131226
Cat. 3+ Hurricanes Days                  -0.202366                 -0.163056
Accumulated Cyclone Energy               -0.296581                 -0.263207
World Carbone Emission                    1.000000                  0.971089
World Carbone Emission02                  0.971089                  1.000000
두 번째 데이터도 상관계수가 비슷한 것을 볼 수 있다
-> 적어도 이 데이터에서는 관련이 없음을 알 수 있다
'''

# World Carbone Emission이 1981년도에서는 별 관계가 없다가 다시 생겼다는 가정
# 점점 연관성이 생긴다는 가정 하에 년도마다 상관계수를 보자

# 데이터프레임의 빈 열 추가.assign(cat3_corr01="", cat3_corr02="")
CarboneTypoon02 = CarboneTypoon02.assign(Named_corr="", Hurricanes_corr="",Hurricanes_cat3_corr="")

# 빈 열에 년도별 상관계수를 삽입
for i in range(0,len(CarboneTypoon02)):
    tmp=CarboneTypoon02[i:].corr('pearson')
    comtmp_Named = tmp.loc['Named Storms', 'World Carbone Emission']
    comtmp_Hurricanes = tmp.loc['Hurricanes', 'World Carbone Emission']
    comtmp_cat3 = tmp.loc['Cat. 3+ Hurricanes', 'World Carbone Emission']
    CarboneTypoon02.loc[i, 'Named_corr'] = comtmp_Named
    CarboneTypoon02.loc[i, 'Hurricanes_corr'] = comtmp_Hurricanes
    CarboneTypoon02.loc[i, 'Hurricanes_cat3_corr'] = comtmp_cat3

# nan값때문에 heatmap이 안그려짐 -> replace
CarboneTypoon02=CarboneTypoon02.replace(np.nan,1)

# # # print(CarboneTypoon02[['Year','Named_corr','Hurricanes_corr','Hurricanes_cat3_corr']].tail(15))
df_heatmap = CarboneTypoon02.set_index('Year')
df_heatmap = df_heatmap[['Named_corr','Hurricanes_corr','Hurricanes_cat3_corr']]
# # print(df_heatmap)
# 구한 년도별 상관계수를 그려보자
fig = plt.figure(constrained_layout=True)
ax01 = fig.add_subplot(3,1,1)
ax02 = fig.add_subplot(3,1,2)
ax03 = fig.add_subplot(3,1,3)


sns.lineplot(x=CarboneTypoon02['Year'], y=CarboneTypoon02['Named_corr'], ax=ax01)
sns.lineplot(x=CarboneTypoon02['Year'], y=CarboneTypoon02['Hurricanes_corr'], ax=ax02)
sns.lineplot(x=CarboneTypoon02['Year'], y=CarboneTypoon02['Hurricanes_cat3_corr'], ax=ax03)
plt.show()
# # x축 돌려서 가로로 만들기
# plt.xticks(rotation = 0)
# sns.heatmap(df_heatmap,
#             cmap='Blues',
#             annot=True,)
# plt.show()

# 상관계수가 비교적 높아지기 시작한 2004년도 이후의 데이터를 추출
CarboneTypoon03 = CarboneTypoon02[26:]
print(CarboneTypoon03)

# csv파일로 저장
