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

news_url = 'https://www.mk.co.kr/news/society/view/2022/10/911138/'

resp = requests.get(news_url)

soup = BeautifulSoup(resp.text, "html.parser")

title = soup.select("#top_header > div > div > h1")
contents = soup.select("#article_body > div")

news_con = []
for news in contents:
    title = title
    contents = contents
   
    news_con.append(title)
    news_con.append(contents)

test = pd.DataFrame(columns = title, data=news_con)
print(test)
test.to_csv("./매일경제.csv")