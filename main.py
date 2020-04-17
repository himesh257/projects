__author__ = "Himesh Buch"
__copyright__ = "Copyright 2020, TradingBot Project"

import intradayData
from config import *
from datetime import datetime
from threading import Timer

x = datetime.today()
y = x.replace(day=x.day + 1, hour=17, minute=0, second=0, microsecond=0)
delta_t = y - x

secs = delta_t.seconds + 1

d = intradayData
# print(d.pretty_data(d.get_data()))
stockData = d.name_and_changed()
changed = d.top_changed(stockData)
print(d.pretty_data(changed))


def yesterday_data():
    yesterday_changed = d.top_changed(stockData)
    print(d.pretty_data(yesterday_changed))


t = Timer(secs, yesterday_data)
t.start()

"""
    the idea here is not to spend all wealth, and so we will only spend
    3/4th of initial money. It will get updated everyday after market closes.
    Dividing it by the number of stock will equally devide the money for all stocks.
    It shouldn't be like this and will be modified towards the end because we would 
    like to spend more money over the stocks that have changed more than others
"""
wealth_per_stock = ((INIT_WEALTH * 3) / 4) / len(changed)
print("Amount invested in each stock: %f" % wealth_per_stock)


def invest():
    pass
