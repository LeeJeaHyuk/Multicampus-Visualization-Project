# 기사 크롤링 후, 빈도수를 wordcloud로

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt

## 크롤링 기사 불러오기 (jupyter)

# 1. 원인은 이미지

# 2. 원인으로 인한 결과 -> 자연재해로 이어짐.

# 더나은미래
df_f = pd.read_csv("C:/Users/tnqls/Documents/바탕 화면/Multicampus-2210-ProjectGroup4/ParkSooBin/data/더나은미래.csv", sep='\t')

# 이투데이
df_e = pd.read_csv("C:/Users/tnqls/Documents/바탕 화면/Multicampus-2210-ProjectGroup4/ParkSooBin/data/이투데이.csv", sep='\t')

# 매일경제
df_m = pd.read_csv("C:/Users/tnqls/Documents/바탕 화면/Multicampus-2210-ProjectGroup4/ParkSooBin/data/매일경제.csv", sep='\t')

# 원인으로 인해 결과가 자연재해로 이어지는 기사들의 wordcloud
frequency_word = {
        '탄소': 27,
        '배출': 15,
        '배출량': 3,
        '홍수': 13,
        '발생': 3,
        '강수량': 16,
        '증가': 7,
        '극한': 8,
        '예측': 2,
        '재난': 5,
        '기후': 53,
        '변화': 22,
        '재앙': 2,
        '전염병': 1,
        '기온': 3,
        '예방': 1,
        '폭염': 8,
        '태풍': 16,
        '위기': 7,
        '위협': 1,
        '집중': 4,
        '피해': 6,
}
wc = WordCloud(width=800, height=800, background_color="white", random_state=0, font_path='C:/Users/tnqls/Downloads/nanum-gothic/NanumGothic.ttf')
plt.imshow(wc.generate_from_frequencies(frequency_word))
plt.axis("off")
plt.show()

# 3. 해결방안

# 경북매일
df_k = pd.read_csv("C:/Users/tnqls/Documents/바탕 화면/Multicampus-2210-ProjectGroup4/ParkSooBin/data/경북매일.csv", sep='\t')

# 동아일보
df_d = pd.read_csv("C:/Users/tnqls/Documents/바탕 화면/Multicampus-2210-ProjectGroup4/ParkSooBin/data/동아일보.csv", sep='\t')

# 헤드라인제주
df_h = pd.read_csv("C:/Users/tnqls/Documents/바탕 화면/Multicampus-2210-ProjectGroup4/ParkSooBin/data/헤드라인제주.csv", sep='\t')

# 해결방안을 담은 기사들의 wordcloud
frequency_word = {
        '탄소': 33,
        '발자국': 6,
        '이산화탄소': 2,
        '배출': 14,
        '일회용품': 5,
        '제한': 3,
        '확대': 2,
        '온실가스': 11,
        '저감': 5,
        '효과': 6,
        '순환': 3,
        '생태': 2,
        '폐기물': 1,
        '자원': 4,
        '배출량': 4,
        '연결': 1,
        '원료': 8,
        '중립': 13,
        '실천': 12,
        '포인트': 7,
        '환경': 6,
        '필요': 2
}
wc = WordCloud(width=800, height=800, background_color="white", random_state=0, font_path='C:/Users/tnqls/Downloads/nanum-gothic/NanumGothic.ttf')
plt.imshow(wc.generate_from_frequencies(frequency_word))
plt.axis("off")
plt.show()