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

news_url = 'https://www.donga.com/news/article/all/20221019/116022846/1?utm_source=kakao&utm_medium=share&utm_campaign=article_share_kt'

resp = requests.get(news_url)
soup = BeautifulSoup(resp.text, "html.parser")

title = soup.select("#container > div.article_title > h1")
contents = soup.select("#article_txt")

news_con = []
for news in contents:
    title = title
    contents = contents
   
    news_con.append(title)
    news_con.append(contents)

test = pd.DataFrame(columns = title, data=news_con)
print(test)
test.to_csv("./동아일보.csv")