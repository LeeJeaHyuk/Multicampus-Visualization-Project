import pandas as pd

# kor_tem : 우리나라평균기온변화
kor_tem = pd.read_excel('C:/Users/tnqls/Documents/바탕 화면/Multicampus-2210-ProjectGroup4/ParkSooBin/data/우리나라평균기온변화.xlsx')

# all_gas : 국가온실가스배출량
all_gas = pd.read_excel('C:/Users/tnqls/Documents/바탕 화면/Multicampus-2210-ProjectGroup4/ParkSooBin/data/국가온실가스배출량.xlsx')


print("1. 에너지")
# 에너지에서의 온실가스배출량에 따른 평균기온 변화의 상관관계
energy_mean = round((all_gas['에너지'].corr(kor_tem['평균기온'], method = 'pearson')), 3)
print("평균기온 :", energy_mean)

# 에너지에서의 온실가스배출량에 따른 최저기온 변화의 상관관계
energy_min = round((all_gas['에너지'].corr(kor_tem['최저기온'], method = 'pearson')), 3)
print(energy_min)

# 에너지에서의 온실가스배출량에 따른 최고기온 변화의 상관관계
energy_max = round((all_gas['에너지'].corr(kor_tem['최고기온'], method = 'pearson')), 3)
print(energy_max)


print("2. 산업공정")
# 산업공정에서의 온실가스배출량에 따른 평균기온 변화의 상관관계
industry_mean = round((all_gas['산업공정'].corr(kor_tem['평균기온'], method = 'pearson')), 3)
print(industry_mean)

# 산업공정에서의 온실가스배출량에 따른 최저기온 변화의 상관관계
industry_min = round((all_gas['산업공정'].corr(kor_tem['최저기온'], method = 'pearson')), 3)
print(industry_min)

# 산업공정에서의 온실가스배출량에 따른 최고기온 변화의 상관관계
industry_max = round((all_gas['산업공정'].corr(kor_tem['최고기온'], method = 'pearson')), 3)
print(industry_max)


print("3. 농업")
# 농업분야에서의 온실가스배출량에 따른 평균기온 변화의 상관관계
agriculture_mean = round((all_gas['농업'].corr(kor_tem['평균기온'], method = 'pearson')), 3) 
print(agriculture_mean)

# 농업분야에서의 온실가스배출량에 따른 최저기온 변화의 상관관계
agriculture_min = round((all_gas['농업'].corr(kor_tem['최저기온'], method = 'pearson')), 3)
print(agriculture_min)

# 농업분야에서의 온실가스배출량에 따른 최고기온 변화의 상관관계
agriculture_max = round((all_gas['농업'].corr(kor_tem['최고기온'], method = 'pearson')), 3)
print(agriculture_max)


print("4. LULUCF")
# lULUCF분야에서의 온실가스배출량에 따른 평균기온 변화의 상관관계
lulucf_mean = round((all_gas['LULUCF'].corr(kor_tem['평균기온'], method = 'pearson')), 3)
print(lulucf_mean)

# lULUCF분야에서의 온실가스배출량에 따른 최저기온 변화의 상관관계
lulucf_min = round((all_gas['LULUCF'].corr(kor_tem['최저기온'], method = 'pearson')), 3)
print(lulucf_min)

# lULUCF분야에서의 온실가스배출량에 따른 최고기온 변화의 상관관계
lulucf_max = round((all_gas['LULUCF'].corr(kor_tem['최고기온'], method = 'pearson')), 3)
print(lulucf_max)


print("5. 폐기물")
# 폐기물에서의 온실가스배출량에 따른 평균기온 변화의 상관관계
waste_mean = round((all_gas['폐기물'].corr(kor_tem['평균기온'], method = 'pearson')), 3)
print(waste_mean)

# 폐기물에서의 온실가스배출량에 따른 최저기온 변화의 상관관계
waste_min = round((all_gas['폐기물'].corr(kor_tem['최저기온'], method = 'pearson')), 3)
print(waste_min)

# 폐기물에서의 온실가스배출량에 따른 최고기온 변화의 상관관계
waste_max = round((all_gas['폐기물'].corr(kor_tem['최고기온'], method = 'pearson')), 3)
print(waste_max)