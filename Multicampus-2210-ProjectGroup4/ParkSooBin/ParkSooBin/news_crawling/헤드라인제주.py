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

news_url = "http://www.headlinejeju.co.kr/news/articleView.html?idxno=486653"

resp = requests.get(news_url)
soup = BeautifulSoup(resp.text, "html.parser")

title = soup.select("#user-container > div.float-center.max-width-1080 > header > div > div")
contents = soup.select("#article-view-content-div")

news_con = []
for news in contents:
    title = title
    contents = contents
   
    news_con.append(title)
    news_con.append(contents)

test = pd.DataFrame(columns = title, data=news_con)
print(test)
test.to_csv("./헤드라인제주.csv")