import matplotlib.pyplot as plt
import pandas as pd


fig, ax = plt.subplots()


gastotal = pd.read_csv('data/gastotal.csv')
year_max=gastotal.groupby('TRGT_YEAR')['GHG_EMS'].max()
year_max=year_max.reset_index()

ax.plot(year_max['TRGT_YEAR'], year_max['GHG_EMS'],color='b')

plt.show()
