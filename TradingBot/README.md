# TradingBot

<h3>How it works:</h3>
We get the data by doing some web scraping on Yahoo Finance's website (intradayData.py). Once we have the data, we refresh it every minute and make the decisions to either buy or sell (main.py). At the moment, it is configured such that, if the stock price has changed >=15% then we buy it and we keep track of those stocks, and if the changed amount goes up by 2% then we sell it. All these values are configurable (see config.py). All the information regarding the configurable variables is included in the config.py file

<h3>How to run:</h3>
At the moment, use any linux os to run the code. Set a cronjob that runs everyday between 9:00am to 4:30pm (US stock market hours). It will create a logfile.txt log file under user's desktop directory which keeps track of all the buying and selling of stocks

<h3>Next steps:</h3> 

Next steps are to test it thoroughly and see how to make the algorithm even more efficient. Learn more about algorithmic trading. The final steps will be to set up an email server which will send out emails at the end of day each day with detailed summary of that day's trades. Graphical representation of trades along with complete summary will be included in the email
