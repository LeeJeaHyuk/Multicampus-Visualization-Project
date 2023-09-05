# analysis

멀티캠퍼스에서 한 첫 번째 프로젝트(시각화 프로젝트)에 대한 python을 사용한 분석 코드 모음 입니다.



---

## 분석 파일 

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
4. data analysis03.py
   1. World Carbone Emission 특성과 Cat. 3+ Hurricanes 특성을 년도별로 seaborn 사용하여 lineplot으로 그리기 
   2. 하나의 파이썬 파일 내에 여러 개의 savfig를 사용하기(여러 개 그래프를 저장하기)
   3. 상관계수 확인하기 .corr('pearson')
   4. 선형회귀 그래프 그려보기

5. data analysis03-1.py
   1. ['Named Storms','Hurricanes','Cat. 3+ Hurricanes'] 특성과 World Carbone Emission 특성의 상관관계 구하기
   2. 구한 상관관계를 sns.seaborn heatmap을 사용해서 시각적으로 확인하기

6. data analysis04.py
   1. 공유받은 데이터와 기존 데이터 합치기 pd.concat([df01,df_shared['Total_Emission']], axis=1)
   2. 열이름 변경하기
   3. 새로 받은 데이터와 상관계수 계산해보기
   4. **데이터를 잘라서 상관계수가 가장 높은 년도의 데이터를 추출해보기**
      1. 데이터프레임에 빈 열 추가하기
      2. 빈 열에 상관계수 삽입하기 (for문 사용)
   5. 상관계수가 비교적 높은 년도의 데이터를 추출해서 csv로 만들기 : CarboneTypoon03.csv 생성
      1. 2015년 이후 데이터로 사용
7. data analysis04-ex1.py
   1. 데이터프레임에 빈 열 추가 CarboneTypoon02.assign(Named_corr="", Hurricanes_corr="",Hurricanes_cat3_corr="")
   2. 빈 열에 for문을 이용해서 상관계수 삽입 
      1. 두 데이터가 교차하는 지점의 데이터만 가져오기tmp.loc['Named Storms', 'World Carbone Emission']

   3. 구한 상관게수 빈 열에 집어넣기
   4. 그래프 그리기 위해 빈 값 제거(1로 채워줌) CarboneTypoon02.replace(np.nan,1) 
   5. 년도별 상관계수 lineplot,heatmap으로 그리기
   6. 2016년 이후 데이터만 CarboneTypoon03.cvs에 저장

8. data analysis05.py
   1. 데이터 정규화 하기
      1. 기존보다 코드가 더 간단하게 바뀜

   2. 선형 관계를 다시 그려보기
      1. World Carbone Emission02 데이터를 선택하여 다시 그리기
      2. 2015년 이후부터는 탄소배출량이 증가하면 태풍의 수도 증가한다는 결과를 찾아냄
9. data analysis06.py
   1. 온실가스 배출량과 평균기온 2015 이후 데이터만 사용하여 lineplot으로 그려보기

10. data analysis07.py
    1. CarboneTypoon data Transpose 사용



----


# Folder

존재하는 csv 파일을 모아놓은 폴더

   1. **Shared folder**
         1. World-Carbon-Emission.csv 
               1. 심현아님으로부터 공유받은 세계 탄소 배출량 파일
   2. CarboneTypoon.csv
         1. 세계 탄소 배출량 + 세계 태풍 발생 파일
         2. WorldCarbone.py에서 생성
   3. CarboneTypoon03.csv
         1. 세계 탄소 배출량 + 공유밭은 세계 탄소 배출량 + 세계 태풍 발생 + 년도별 상관계수 파일
         2. data analysis04.py에서 생성
   4. typoonOfYear.csv
         1. 세계 태풍 발생 파일
         2. ../crawling/typoon.py에서 생성
   5. WorldCarbornEmission.csv
         1. 세계 탄소 배출량 파일


## graph Folder
그래프 사진을 모아놓은 폴더
1. Carbone Emission and Named storm.png
2. carbone emission of year
3. 4parameters.png
