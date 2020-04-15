# TradingBot

Making a trading bot efficient enough to trade for the user

# Requirement List

1> Get data from Yahoo Finance by simple webscraping (NOTE: if the website changes its format, meaning if any of the tags get changed, it will not give you right data. The solution for that will be to create a 'watch dog' that checks for the changes and modifies the code accordingly)</br>
  -- It needs to fetch data every minute (subject to change), so that required trade can happen
2> Come up with a simple but effective trading strategy
  -- Make sure that not more than certain amount of money is being used to trade
  -- Keep looking at the changes to select which stock to buy or sell
  -- Try to make it such that no loss ever occures
3> Use Robinhood to trade stocks!
