# TradingBot

Making a trading bot efficient enough to trade automatically for the user

<h3>Things to know for coding:</h3>

1. The program needs to run for indefinite amount of time in the background (use something like "nohup" for that)
2. Get data from Yahoo Finance by simple webscraping (<u>NOTE:</u> if the website changes its format, meaning if any of the tags get changed in html, it will not return correct data. The solution for that will be to create a "watch dog" that checks for the changes and modifies the code accordingly)
    - It needs to fetch data every minute (subject to change), so that required trade can happen
3. Come up with a simple but effective trading strategy
    - Make sure that not more than certain amount of money is being used to trade
    - Keep looking at the changes in price to select when and which stock to buy or sell
    - Try to make it such that no loss ever occures
4. Use Robinhood's api to trade stocks!
