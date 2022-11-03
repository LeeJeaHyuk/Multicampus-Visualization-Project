import pandas as pd
import numpy as np


### 세계 탄소 배출량 데이터 원하는 형태로 만들기 ###
## (* XLSX 파일 다운받음 *)




## 엑셀 파일 불러오기
xlsx = pd.read_excel("../CSV/(RAW1)World_Carbon_Emiss.xlsx")
## CSV 파일로 만들기
xlsx.to_csv("../CSV/(RAW)World_Carbon.csv")


## CSV파일 읽기
df = pd.read_csv("../CSV/(RAW)World_Carbon.csv")
df.info()


## 의미 없는 행인 첫 행 없애기
df_new = df.drop(0, axis = 0)


## Null값 0으로 채우기
df_fill = df_new.fillna(0)
df_fill["Year"] = df_fill.iloc[:,1]

## Null이 제거된 df를 CSV파일로 만들기
df_fill.to_csv("../CSV/(RAW3)Carbon_Year.csv")


df_carbon = pd.read_csv("../CSV/(RAW3)Carbon_Year.csv")
print(df_carbon)

df_Glo_Ems = df_carbon.set_index(keys = "Year")
# print(df_Glo_Ems.columns)
df_Ems = df_Glo_Ems.drop(["Territorial emissions in MtCO₂", "Unnamed: 0.1", "Unnamed: 0"], axis = 'columns')
# print(df_Ems)
df_Ems.loc[:, "Total_Emission"] = df_Ems.loc[:, 'Unnamed: 1':'Unnamed: 221'].sum(axis = 1)

print(df_Ems)

df_Ems.to_csv("../CSV/World-Carbon-Emission.csv")