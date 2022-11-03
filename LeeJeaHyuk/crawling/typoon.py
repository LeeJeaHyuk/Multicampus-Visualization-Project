import requests
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
import pandas as pd

# 태풍 데이터 추출
url = "http://tropical.atmos.colostate.edu/Realtime/index.php?arch&loc=global"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)

# table 내용 확인 및 추출
tytoonTable = soup.find('tbody')
# print(type(tytoonTable))
# print(tytoonTable)

# html_table_parser의 make2d를 사용하여 테이블을 리스트로 추출
tyTableText = parser.make2d(tytoonTable)
# print(tyTableText)

# table의 행이름 확인
tableNames = soup.select("th")
# tableNames = soup.select("div#content")
# print(tableNames)

# table의 행이름 추출하기
columnName =[]
for tableName in tableNames:
    columnName.append(tableName.get_text())
# print(columnName)

# 리스트를 dataframe으로 만들기
df = pd.DataFrame(data=tyTableText[1:], columns=columnName)
# print(df)

# dataframe을 cvs로 만들기
df.to_csv('../analysis/csv file/typoonOfYear.csv', index=False)