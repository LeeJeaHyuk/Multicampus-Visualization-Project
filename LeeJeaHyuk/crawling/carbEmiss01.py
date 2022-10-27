from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests
from bs4 import BeautifulSoup

url = "https://databank.worldbank.org/reports.aspx?source=2&series=EN.ATM.CO2E.PC&country="

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')

driver.get(url)

# 스크롤을 맨 밑까지 내려야함


divClass = driver.find_element(By.CLASS_NAME,"dxgvCSD")
print(divClass)
last_height = driver.execute_script("return document.body.scrollHeight",divClass)
print(last_height)

while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);",divClass)

    # 1초 대기
    sleep(5)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight",divClass)
    if new_height == last_height:
        break
    last_height = new_height



# webData = driver.page_source
# print(webData)

carbons = soup.select("tr#grdTableView_DXDataRow265 > td")
print(carbons)



