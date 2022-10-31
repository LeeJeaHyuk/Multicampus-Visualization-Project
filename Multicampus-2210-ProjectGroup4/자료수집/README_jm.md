# 탄소배출과 기후위기 
1. 서론
   - 한국 온실가스 배출량 순위 확인
   - 탄소와 기후위기(이상기후) 기사 언급량 증가를 토대로 연관성 확인
   - 기사 타이틀 크롤링을 통해 최근 1년간 나타난 이상기후 관측
2. 기후 : 국내 이상기후(폭염, 태풍, 홍수 등)가 얼마나 증가했나
   - 국내에서 비가 내린 횟수가 최근 얼마나 증가했는지
   - 태풍, 폭염 정보 확인
3. 탄소 : 최근 얼마나 탄소배출량이 증가했는지
   - 국내 온실가스 배출 현황
   - 국내 산업별 온실가스 배출량
   - 광역시도별 온실가스 배출량
   - 발전소 온실가스 배출량
4. 최근 5년간 탄소 배출량 증가여부, 이상기후 증가여부 확인하여 연관성 검증
+) 탄소 발자국 요인들 검증

## 서론 및 가정
- 뉴스 기사 타이틀 크롤링을 통해 최근 1년간 얼마나 많은 "기후 위기", "이상 기후"와 "탄소" 관련 키워드 뉴스가 언급 됐는지 조사
  + [기사 타이틀 크롤링 방법](https://everyday-tech.tistory.com/entry/%EC%89%BD%EA%B2%8C-%EB%94%B0%EB%9D%BC%ED%95%98%EB%8A%94-%EB%84%A4%EC%9D%B4%EB%B2%84-%EB%89%B4%EC%8A%A4-%ED%81%AC%EB%A1%A4%EB%A7%81python-2%ED%83%84)
  
  + [기후위기 관련 키워드 크롤링(탄소 중립 함께 검색 가장 많음)](https://blackkiwi.net/service/keyword-analysis?keyword=%EA%B8%B0%ED%9B%84%EC%9C%84%EA%B8%B0&platform=naver)
  - [한국의 온실가스 배출량 글로벌 순위](http://www.greenpostkorea.co.kr/news/articleView.html?idxno=131273)
  - [참고 기사](https://www.newspenguin.com/news/articleView.html?idxno=12518)
  - [참고 기사](https://www.pressian.com/pages/articles/2022052014435720546)


## 데이터 취합
### 기후 관련
- [공공데이터포털 : 기상청 지상기상관측자료 조회 서비스](https://www.data.go.kr/data/15057084/openapi.do?recommendDataYn=Y)
- [공공데이터포털 : 기후변화 관련 지표 정보](https://www.data.go.kr/data/15047213/fileData.do#tab-layer-openapi)
- [기상청_태풍정보 조회서비스](https://www.data.go.kr/data/15043565/openapi.do?recommendDataYn=Y)
- [태풍 데이터셋](https://data.kma.go.kr/data/weatherIssue/typList.do?pgmNo=724)
- [기상청_폭염정보 조회](https://www.data.go.kr/data/15075950/fileData.do)
- [웨더아이_지난 강수 횟수를 활용해 최근 5년간 얼마나 더 자주 비가 내렸는지 확인](https://www.weatheri.co.kr/bygone/bygone04.php)


### 탄소 배출 관련
- [국내 온실가스 배출 현황](https://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1464)
- [세계 온실가스 배출량](https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_2KAAF02&conn_path=I2)
- [국내 산업부문 온실가스 배출량 보고](https://netis.kemco.or.kr/netis/hp/hp3_21)
- [광역시도별 온실가스 배출량](https://data.gg.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OYUMJUDK201TN8I8CM9Y31515663&infSeq=1&order=&loc=)
- [공공데이터포털 : 대기오염 물질 배출량](https://www.data.go.kr/data/15106362/openapi.do)
- [공공데이터포털 : 월별, 지사별 온실가스 배출량](https://www.data.go.kr/data/15002810/openapi.do)
- [공공데이터포털 : 한국동서발전 대기오염 배출량](https://www.data.go.kr/data/3071438/openapi.do)
- [공공데이터포털 : 한국서부발전 온실가스 배출량](https://www.data.go.kr/data/15003832/openapi.do)
- [온실가스 배출량, 에너지사용량](https://www.bigdata-environment.kr/user/data_market/detail.do?id=56f03d80-f36a-11eb-b976-6966248a20b9)

  
### 탄소발자국, 탄소배출지(참고만)
- 음식물 : https://www.greenpeace.org/korea/update/16149/blog-ce-carbon-water-footprint-veryvezy/
  - + 음식배출량 api https://www.data.go.kr/data/15096609/openapi.do 
- [탄소발자국 검색량 증가](https://blackkiwi.net/service/keyword-analysis?keyword=%ED%83%84%EC%86%8C%EB%B0%9C%EC%9E%90%EA%B5%AD&platform=naver)