# crwaling - wordcloud.py

1. csv 파일을 불러오기 위해 pd.read_csv 사용.

2. 기사에서 많이 사용되는 단어들을 이용하여 wordcloud 작성
   - 뉴스 기사를 크롤링 하면 여러 태그들이 많이 붙어서 크롤링이 되기 때문에 wordcloud 제작에 어려움이 있음. 
   - decompose() 함수를 사용하여 태그 삭제를 시도 했지만, 원하는 것처럼 태그 삭제가 잘 되지 않는 것도 있어 전문적으로 단어의 형태소를 전부 분석해주는 사이트 이용.(사이트 주소를 기록해뒀는데 잘못 누르고 삭제하여 그 이후로 찾지 못하고 있음.)

3. generate_from_frequencies를 사용하면 미리 정의된 단어의 빈도수를 이용하여 워드 클라우드를 그릴 수 있음.

4. img
   - 주제에 맞는 뉴스 기사를 크롤링 후, 내용을 토대로 wordcloud 생성. (원인으로 인한 결과WC, 해결방안WC)  
  
---

# kor_tem_graph.py

1. 우리나라의 평균기온 변화(kor_tem) 파일을 .xlsx로 불러옴. (pd.read_excel)

2. 년도별 평균기온, 최고기온, 최저기온을 그래프로 한번에 나타냄.
   - 년도(구분)와 기온들을 합치기 위해 groupby 함수 사용.

3. seaborn 사용해서 꺾은선 그래프를 그릴 때는 sns.lineplot 함수 사용. 

4. .style.hide_index()를 사용하면 jupyter notebook에서 칼럼 숨기기 가능. (특정 칼럼 지정해서 숨기기도 가능)
   ex) .style.hide_columns([''])

5. plt.tight_layout()
    - subplot들이 겹치지 않도록 자동으로 여백 조절.
  
6. img
   - 년도별 기온 변화를 한 눈에 보기 위해 그래프로 작성. (년도별 기온변화 그래프)

---  

# all_gas_graph.py

1. 국가 온실가스 배출량(all_gas) 파일을 .xlsx로 불러옴. (pd.read_excel)

2. 년도별 에너지, 산업공정, 농업, LULUCF, 폐기물 분야에서의 온실가스 배출량을 그래프로 한번에 나타냄.
   - 년도(구분)와 기온들을 합치기 위해 groupby 함수 사용.

3. seaborn 사용해서 꺾은선 그래프를 그릴 때는 sns.lineplot 함수 사용. 

4. plt.tight_layout()
    - subplot들이 겹치지 않도록 자동으로 여백 조절.

5. img
   - 2번에서 실시한 그래프들을 배출량 1~5로 나타냄. (배출량1 ~ 5)

---  

# correlation.py  

1. 국가 온실가스 배출량(all_gas)과 우리나라 평균기온 변화(kor_tem) 파일을 .xlsx로 불러옴. (pd.read_excel)

2. 에너지, 산업공정, 농업, LULUCF, 폐기물의 다섯 가지 분야에서의 온실가스 배출량으로 인한, 우리나라의 평균기온, 최저기온, 최고기온의 변화에 상관관계가 있는지 확인하려고 함.
    ex) all_gas['에너지'].corr(kor_tem['평균기온'], method = 'pearson'))
    - pearson 상관계수를 구하기 위해 <b>method</b>를 반드시 지정해주어야 함.