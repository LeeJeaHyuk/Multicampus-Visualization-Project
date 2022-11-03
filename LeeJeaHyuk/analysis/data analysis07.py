import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('csv file/CarboneTypoon.csv')

df_transpose = df.transpose()

print(df_transpose)

df_transpose.to_csv('./csv file/CarboneTypoon_transpose.csv')