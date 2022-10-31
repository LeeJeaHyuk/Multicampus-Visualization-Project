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
CarboneTypoon02 = CarboneTypoon02.assign(cat3_corr01="", cat3_corr02="")

# 빈 열에 년도별 상관계수를 삽입
for i in range(0,len(CarboneTypoon02)):
    tmp=CarboneTypoon02[i:].corr('pearson')
    comtmp01 = tmp.loc['Cat. 3+ Hurricanes', 'World Carbone Emission02']
    comtmp02 = tmp.loc['Cat. 3+ Hurricanes', 'World Carbone Emission']
    CarboneTypoon02.loc[i, 'cat3_corr01'] = comtmp01
    CarboneTypoon02.loc[i, 'cat3_corr02'] = comtmp02

# print(CarboneTypoon02)

# 구한 년도별 상관계수를 그려보자
# fig = plt.figure(constrained_layout=True)
# ax01 = fig.add_subplot(2,1,1)
# ax02 = fig.add_subplot(2,1,2)
#
#
# sns.lineplot(x=CarboneTypoon02['Year'], y=CarboneTypoon02['cat3_corr01'], ax=ax01)
# sns.lineplot(x=CarboneTypoon02['Year'], y=CarboneTypoon02['cat3_corr02'], ax=ax02)
#
# plt.savefig('./graph file/analysis04_cat.3_corr.png')
# plt.show()

# 상관계수가 비교적 높아지기 시작한 2004년도 이후의 데이터를 추출
CarboneTypoon03 = CarboneTypoon02[26:]
print(CarboneTypoon03)

# csv파일로 저장
CarboneTypoon03.to_csv('./csv file/CarboneTypoon03.csv', index=False)
