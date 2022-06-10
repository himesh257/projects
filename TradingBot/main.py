__author__ = "Himesh Buch"
__copyright__ = "Copyright 2020, TradingBot Project"

import os
from datetime import datetime
import time
import intradayData
from config import *

logfile = os.path.join(os.environ['HOME'], "Desktop", "logFile.txt")

d = intradayData

bought_dict = {}
now = datetime.now()
amount_left = INIT_WEALTH


def invest(total_spent=0):
    all_data = d.get_data()
    stock_data = d.name_and_changed()
    buy = d.changed_buy(stock_data)
    global bought_dict
    if buy:
        for name in buy:
            if name not in bought_dict:
                try:
                    bought_dict.update(d.make_dict(name, d.get_change_from_name(all_data, name)))
                    price = d.get_price_from_name(all_data, name)
                    total_spent += float(price)
                    global amount_left
                    print(amount_left)
                    amount_left = amount_left - float(price)
                    # if total_spent >= INIT_WEALTH or amount_left < 0:
                    if amount_left > 0:
                        s_val = "{date: " + now.strftime("%B %d, %Y %H:%M:%S") + ", status: bought, name: " + \
                                name + ", price: " + price + ", total_left: " + str(amount_left) + "}\n"
                        with open(logfile, "a") as o1:
                            o1.write(s_val)
                        # sell(amount_left, name)
                except KeyError as k:
                    continue
            else:
                continue
    else:
        invest()


def sell(total_left, b_arr):
    all_data = d.get_data()
    bought = []
    for bought_name in b_arr:
        try:
            if float(d.get_change_from_name(all_data, bought_name)[1:-1]) > float(b_arr[bought_name] + 2):
                bought.append(bought_name)
                price_top = d.get_price_from_name(all_data, bought_name)
                total_left = float(total_left) + float(price_top)
                sold_val = "{date: " + now.strftime("%B %d, %Y %H:%M:%S") + ", status: sold, name: " + bought_name + \
                           ", price: " + str(price_top) + ", total_left: " + str(total_left) + "}\n"
                with open(logfile, "a") as o2:
                    o2.write(sold_val)
            else:
                continue
        except KeyError as e:
            continue

    delete_from_dict(bought, b_arr)
    global amount_left
    amount_left = total_left


def sell_dummy(total_left, b_arr):
    all_data = d.get_data()
    bought = []
    global amount_left
    for bought_name in b_arr:
        try:
            bought.append(bought_name)
            price_top = d.get_price_from_name(all_data, bought_name)
            total_left = float(total_left) + float(price_top)
            # amount_left = amount_left + total_left
            sold_val = "{date: " + now.strftime("%B %d, %Y %H:%M:%S") + ", status: sold, name: " + bought_name + \
                       ", price: " + str(price_top) + ", total_left: " + str(total_left) + "}\n"
            with open(logfile, "a") as o2:
                o2.write(sold_val)
        except KeyError as e:
            continue

    delete_from_dict(bought, b_arr)
    global amount_left
    amount_left = total_left


def delete_from_dict(deleted, original):
    for x in deleted:
        try:
            del original[x]
        except Exception as e:
            continue

    global bought_dict
    bought_dict = original


if __name__ == '__main__':
    count = 0
    while True:
        print(count)
        count = count + 1
        invest()
        current_time = time.strftime("%H:%M", time.localtime())
        time.sleep(30)
        # sell_dummy(amount_left, bought_dict)
        sell(amount_left, bought_dict)
        if current_time == "16:31":
            with open(logfile, "a") as o:
                o.write("End of day total amount spent/gained: %f\n=============================\n" %
                        (float(INIT_WEALTH) - float(amount_left)))
        # if count == 2:
        #     break
        time.sleep(60)
