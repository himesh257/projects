__author__ = "Himesh Buch"

import requests
from bs4 import BeautifulSoup
import json
from config import *


def get_data():
    data = {}
    all_data = []
    # the variable URL comes from the config file
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    c = soup.findAll('table')[0].findAll('td')
    for x in c:
        if x.text:
            all_data.append(x.text)
    for (p, q, r, s, t) in zip(all_data[0::9], all_data[1::9], all_data[2::9], all_data[3::9], all_data[4::9]):
        data[q] = {'Ticker ': p, 'Price ': r, 'Change': s, 'Change(%)': t}

    return data


def name_and_changed():
    data_name_change = {}
    all_data = []
    # the variable URL comes from the config file
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    c = soup.findAll('table')[0].findAll('td')
    for x in c:
        if x.text:
            all_data.append(x.text)
    for (q, t) in zip(all_data[1::9], all_data[4::9]):
        data_name_change[q] = t

    return data_name_change


# comeup with a better sorting algorithm
def top_changed(stock_data):
    arr1 = []
    limited_d = {}
    for x in list(stock_data.values()):
        arr1.append(float(x[1:-1]))
    sorted(arr1, reverse=True)
    for x in stock_data:
        val_float = float(stock_data[x][1:-1])
        for p in range(0, len(arr1)):
            if arr1[p] > TOPNUM:
                if val_float == arr1[p]:
                    limited_d[x] = arr1[p]
                else:
                    continue
            else:
                break

    return limited_d


def pretty_data(data1):
    return json.dumps(data1, indent=4)
