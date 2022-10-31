
# Python File
1. WorldCarbone.py
   1. WorldCarbornEmission.csv 파일을 가져와서 데이터프레임으로 만들었다
   2. 필요한 특성인 년도와 전세계 탄소 배출량만 가져와서 새롭게 데이터프레임으로 만들었다
   3. typoonOfYear.csv 파일을 가져와서 데이터프레임으로 만든다
   4. 위의 2,3 에서 만들어진 데이터프레임을 concat한다
   5. 필요없는 열은 drop으로 제거한다
   6. 열 이름을 잘 알 수 있게 이름 변경
      - .rename(columns = {'World':'World Carbone Emission'}, inplace=True)
   7. CarboneTypoon.csv 파일 생성 (index = False)
   8. dataframe 변형되었을 때 .reset_index(drop=True) 사용

2. data analysis01.py
   1. CarboneTypoon.csv 파일 불러오기
   2. matplotlib.pyplot 사용하여 x = 년도 y = 탄소배출량으로 그래프 생성
   3. 생성한 그래프 savefig로 저장
      1. 저장할 때 show() 뒤에 하면 그래프가 꺼진 다음 저장되서 빈 화면만 저장됨

3. data analysis02.py
   1. CarboneTypoon.csv 파일 사용
   2. 두 개의 특성을 같은 그래프에 놓을 때 단위가 다르므로 정규화 필요
   3. 사이킷런 패키지를 사용해서 간단하게 Min-Max Normalization 사용
   4. World Carbone Emission 과 Named Storms 특성을 같이 그래프에 그리고 저장
   5. subplot 으로  4구역을 나누어서 Named Storms / Hurricanes / Cat. 3+ Hurricanes /World Carbone Emission 그래프를 한번에 그리고 저장


# Folder

## csv Folder
존재하는 csv 파일을 모아놓은 폴더
1. CarboneTypoon.csv
2. typoonOfYear.csv
3. WorldCarbornEmission.csv

## graph Folder
그래프 사진을 모아놓은 폴더
1. Carbone Emission and Named storm.png
2. carbone emission of year
3. 4parameters.png