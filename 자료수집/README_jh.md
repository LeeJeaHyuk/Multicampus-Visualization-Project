# 4조 이재혁 자료조사



## 탄소 배출량 데이터 

1. [yearbook.enerdata.co.kr](https://yearbook.enerdata.co.kr/co2/emissions-co2-data-from-fuel-combustion.html)
   1. 전 세계적인 탄소 배출량 정보를 csv 파일로 공유해주고 있습니다
   2. 위 사이트에서는 csv파일을 받을 수 있음
2. [Data on CO2 and Greenhouse Gas Emissions by *Our World in Data*](https://github.com/owid/co2-data)
   1. 전 세계적인 탄소 배출량 정보를 csv 파일로 공유해주고 있습니다 1보다 조금 더 상세합니다
   2. [full codebook](https://github.com/owid/co2-data/blob/master/owid-co2-codebook.csv) :csv파일의 description입니다
3. [data.worldbank.org](https://data.worldbank.org/indicator/EN.ATM.CO2E.PC)
   1. golbal carbone emissions 
      1. cvs 파일 다운로드 가능
      2. [DataBank](https://databank.worldbank.org/reports.aspx?source=2&series=EN.ATM.CO2E.PC&country=)에서 개발자도구를 사용해서 봤을 때 충분히 크롤링 가능할 것으로 보임
4. [www.unep.org](https://www.unep.org/explore-topics/climate-action/what-we-do/climate-action-note/state-of-climate.html?gclid=Cj0KCQjwqc6aBhC4ARIsAN06NmOz-UYHOdBuiA1ItYjTO7ly3f7nDeIrs1OMWp86ayvfuwA4KnYZYrYaAmBuEALw_wcB)
   1. 아래로 내리다보면 See how the GHG emissions for each country have changed since 1970 데이터가 있는데 크롤링으로 가져오기 쉬워 보인다
   2. COUNTRY : EMISSION 으로 json파일로 만든 다음에 csv로 바꿔서 사용하면 될 듯



## 자연 재해 관련 데이터

1. 자연재해에 관한 리포트
   1. [2021 Global Natural Disaster Assessment Report](https://reliefweb.int/report/world/2021-global-natural-disaster-assessment-report)
      1. 91~21사이의 자연재해는 늘었지만 사망자는 감소했다는 리포트
   2. [https://public.wmo.int/](https://public.wmo.int/en/media/press-release/weather-related-disasters-increase-over-past-50-years-causing-more-damage-fewer)
      1. 50년동안 자연재해는 늘었지만 사망자는 줄었다는 뉴스 
2. 어떤 것을 자연재해로 규정짓는가?
   1. [www.statista.com](https://www.statista.com/statistics/510959/number-of-natural-disasters-events-globally/)
   2. 위 사이트에서는 아래 조건이 만족되었을 때 자연재해라고 한다 : 개인의 생각 또는 시대에 따라 자연재해의 정의가 다를 수 있음
      1. at least one of the criteria must be met: economic loss of 50 million U.S. dollars;
      2.  insured loss of 25 million U.S. dollars;
      3.  ten fatalities;
      4.  50 injured;
      5.  or 2,000 homes or structures damaged.
3. 매년 태풍발생 현환
   1. [기상청 날씨누리](https://www.weather.go.kr/w/typhoon/typ-stat.do)
      1. 우리나라의 태풍 발생 현황(51~21년)
   2. ★[tropical.atmos.colostate.ed](http://tropical.atmos.colostate.edu/Realtime/index.php?arch&loc=global)
     1. 전세계적인 현황 
   


=======
      1. 전세계적인 현황 
>>>>>>> .merge_file_bO9qKw



