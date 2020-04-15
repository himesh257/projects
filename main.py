import requests
import itertools
from bs4 import BeautifulSoup
import json

data = {}
allData = []

URL = 'https://finance.yahoo.com/gainers'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
c = soup.findAll('table')[0].findAll('td')

for x in c:
	if x.text:
		allData.append(x.text)

for (p,q,r,s) in zip(allData[0::9], allData[1::9], allData[2::9], allData[3::9]):
	data[q]={'Ticker ': q, 'Change ': r, 'Change(%)': s}

mainData = json.dumps(data, sort_keys=True, indent=4)
print(mainData)
