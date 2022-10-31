import urllib.request
import requests
from bs4 import BeautifulSoup

url = "https://databank.worldbank.org/reports.aspx?source=2&series=EN.ATM.CO2E.PC&country="
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
