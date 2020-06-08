URL = "https://finance.yahoo.com/gainers"  # url for yahoo finance's website
TOPNUM = 2  # if the change amount is up by what it was + TOPNUM then we sell the stock
TOPNUM_CHANGE = 10  # this is only used in top_changed() method, to get the stocks who have chnaged >=TOPNUM_CHANGED
INIT_WEALTH = 1000  # the amount you start off with
LOWBUY1 = 12  # if TWOCHECKS is true then we will buy the stocks that have changed between LOWBUY1 and LOWBUY2
LOWBUY2 = 40  # if TWOCHECKS is true then we will buy the stocks that have changed between LOWBUY1 and LOWBUY2
TWO_CHECKS = False  # determine whether to buy stocks that have changed amount in an interval or no
LOWBUY = 15  # if TWOCHECKS is set to false, then we will buy stocks that have changed amount >=LOWBUY
