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

news_url = 'https://futurechosun.com/archives/65649'

resp = requests.get(news_url)
soup = BeautifulSoup(resp.text, "html.parser")

title = soup.select("body > div.elementor.elementor-47574.elementor-location-single.post-65649.post.type-post.status-publish.format-standard.has-post-thumbnail.hentry.category-10738.tag-14947.tag-7533 > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-49b9b9b.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div.elementor-column.elementor-col-33.elementor-top-column.elementor-element.elementor-element-266e0d9 > div > div > div.elementor-element.elementor-element-15733db3.elementor-widget.elementor-widget-theme-post-title.elementor-page-title.elementor-widget-heading > div > div")

contents = soup.select("body > div.elementor.elementor-47574.elementor-location-single.post-65649.post.type-post.status-publish.format-standard.has-post-thumbnail.hentry.category-10738.tag-14947.tag-7533 > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-a09503a.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div > div > div.elementor-column.elementor-col-20.elementor-top-column.elementor-element.elementor-element-35e899e > div > div > div.elementor-element.elementor-element-24e82692.elementor-widget__width-initial.newstext.elementor-widget.elementor-widget-theme-post-content > div")

news_con = []
for news in contents:
    title = title
    contents = contents
   
    news_con.append(title)
    news_con.append(contents)

    print(news_con)

test = pd.DataFrame(columns = title, data=news_con)
print(test)
test.to_csv("./더나은미래.csv")