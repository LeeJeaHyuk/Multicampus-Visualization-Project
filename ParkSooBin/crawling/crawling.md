# news_crawling file

### 경북매일.py, 더나은미래.py, 동아일보.py, 매일경제.py, 이투데이.py, 헤드라인제주.py

1. AttributeError: module 'collections' has no attribute 'Callable'라는 오류 발생.
   - django-pydenticon 내에서 사용되는 collections.Callable 참조가 파이썬 3.10부터 collections.abc.Callable로 이동하여, 제거된 Attribute라서 발생하는 오류 메시지임을 찾음.
   - import collections
							    
     if not hasattr(collections, 'Callable'):
        
        collections.Callable = collections.abc.Callable 를 사용하여 해결.

2. selector를 사용하여 크롤링 하기 위하여 .select 함수 사용

3. 제목, 내용을 데이터 프레임 형식으로 저장하기 위하여 pd.DataFrame(columns=제목, data=내용)의 함수 사용.


4. csv 파일로 저장하기 위하여 .to_csv("경로/파일이름") 을 지정해 줌.


---

### data file

1. 크롤링 완성 후, decompose()로 태그 삭제 성공한 파일과 그렇지 않은 파일을 모아둠.

---

### img file
1. 주제 발표에 앞서 사용할 1.5도와 2도의 차이, 기후변화로 인한 경제적 피해 이미지 파일을 모아둠.
