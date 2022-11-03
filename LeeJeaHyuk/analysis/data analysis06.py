import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

# 온실가스 배출량 과 평균기온 (박수빈님 데이터)

global_green_gas = pd.read_csv('csv file/Shared folder/global green gas.csv')
Kor_avg_temp = pd.read_csv('csv file/Shared folder/kor avg temp.csv')

# print(global_green_gas.columns)
# 'Year', 'energy', 'industrial process', 'agriculture', 'LULUCF',
# 'waste', 'Total emissions per GDP', 'Total Emissions Per Person'

# print(Kor_avg_temp.columns)
# 'Year', 'avg temp', 'low temp', 'high temp'

# 상관계수가 높게 나오지 않는 문제 년도를 15년도이후 데이터를 사용해서 해결

concat = pd.concat([global_green_gas,Kor_avg_temp], axis=1)
# print(concat)

concat01 = concat[3:]
# print(concat01)

concat02 = concat01[['avg temp','low temp', 'high temp', 'Total emissions per GDP']]
print(concat02.corr('pearson')['Total emissions per GDP'])

# 모든 년도 사용 
# avg temp                  -0.430820
# low temp                  -0.091340
# high temp                 -0.512814
# Total emissions per GDP    1.000000

# 2015년부터 사용
# avg temp                   0.542129
# low temp                   0.511704
# high temp                  0.766592
# Total emissions per GDP    1.000000

# 특히 최고 온도가 연관성이 깊은 것을 볼 수 있다

fig01 = plt.figure()

ax01 = fig01.add_subplot(2,1,1)
ax02 = fig01.add_subplot(2,1,2)

sns.lineplot( x=concat01['Total emissions per GDP'], y=concat01['avg temp'], ax=ax01)
sns.lineplot( x=concat01['Total emissions per GDP'], y=concat01['high temp'], ax=ax02)
plt.show()

# 그래프를 보면 데이터 양이 적어서 정확한 정보라고는 할 수 없을 것 같다