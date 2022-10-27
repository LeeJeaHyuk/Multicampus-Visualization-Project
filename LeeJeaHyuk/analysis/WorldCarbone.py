import pandas as pd
import csv


file = 'WorldCarbornEmission.csv'
f = open(file,'rt',encoding='UTF8')
reader = csv.reader(f)

csv_list = []
for i in reader:
    csv_list.append(i)
f.close()

# 년도와 world(전체 탄소 배출량 데이터) 만 가져온다
# csv_list[0] 에 null값이 있어서 data와 개수가 다르다고 나오는 듯
# 먼저 null값을 없애고 다시 만들기
# df = pd.DataFrame(data=csv_list[1:], columns=csv_list[0])

df = pd.DataFrame(data=csv_list)
df_World = df[df[0]=='World']
df_index = df[df[0]=='Country Name']
print(type(df[df[0]=='World']))

# 각각의 데이터들을 합친다
# typoon데이터와 같이 사용하기 위해서 transpose해준다
df_carbone=pd.concat([df_index,df_World])
df_carbone = df_carbone.transpose()
# print(df_test[1:])
header = df_carbone.iloc[0]
df_carbone = df_carbone[1:]

df_carbone.rename(columns=header, inplace=True)
# print(df_test)


# typoon data확인
df_typoon = pd.read_csv('typoonOfYear.csv')
# print(df_typoon)
# 1981년부터 2021년까지 존재한다

# corbone 데이터에서 1981~ 2021데이터만 따로 빼낸다
# print(df_carbone)
# print(df_carbone[24:66])
df_carbone01 = df_carbone[24:66]

# df_tyAndCb =  