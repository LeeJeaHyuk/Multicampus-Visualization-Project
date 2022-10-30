import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('csv file/CarboneTypoon.csv')
# print(df.columns)
df01 = df.dropna()

# 각 특성의 선형성 확인해보기
