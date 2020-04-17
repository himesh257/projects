__author__ = "Himesh Buch"

import requests
import itertools
from bs4 import BeautifulSoup
import json
from config import *

class IntradayData():

	def getData(self):
		data = {}
		allData = []

		# the variable URL comes from the config file
		page = requests.get(URL)
		soup = BeautifulSoup(page.content, 'html.parser')
		c = soup.findAll('table')[0].findAll('td')

		for x in c:
			if x.text:
				allData.append(x.text)

		for (p,q,r,s) in zip(allData[0::9], allData[1::9], allData[2::9], allData[3::9]):
			data[q]={'Ticker ': p, 'Change ': r, 'Change(%)': s}

		mainData = json.dumps(data, sort_keys=True, indent=4)

		return mainData
