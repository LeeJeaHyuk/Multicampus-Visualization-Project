from base64 import encode
import requests
from pandas import DataFrame
from bs4 import BeautifulSoup
import re
from datetime import datetime
import os
import csv
import pandas as pd
import collections
							    
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable

news_url = 'https://www.etoday.co.kr/news/view/2168177'

resp = requests.get(news_url)
soup = BeautifulSoup(resp.text, "html.parser")

title = soup.select("body > div.wrap > article.containerWrap > section.news_dtail_view_top_wrap > h1")
contents = soup.select("body > div.wrap > article.containerWrap > section.view_body_moduleWrap > div.l_content_module > div > div > div.view_contents")

news_con = []
for news in contents:
    title = title
    contents = contents
   
    news_con.append(title)
    news_con.append(contents)

test = pd.DataFrame(columns = title, data=news_con)
print(test)
test.to_csv("./이투데이2.csv")