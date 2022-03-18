# Botcoin

## Project Description
Botcoin is a simple algorithmic cryptocurrency [trading bot](https://www.investopedia.com/articles/active-trading/101014/basics-algorithmic-trading-concepts-and-examples.asp) developed on Python. The main purpose of the program is to automate the execution of different trading strategies while also removing the risks of manual errors when placing trades and the possibility of mistakes based on emotional and psychological factors. The data collection process is done by using an API connection to a cryptocurrency market exchange ([Poloniex](https://poloniex.com/)).

## Main features
- The bot supports the functionality for both live trading and historical backtesting with built in basic trading strategies using indicators for technical analysis
- Algo-trading can be backtested using available historical and real-time data to see if it is a viable trading strategy
- Simultaneous automated checks on multiple market conditions
- Trades are timed correctly and instantly to avoid significant price changes
- Trade order placement is instant and accurate (there is a high chance of execution at the desired levels)

## Future development oppurtunities
lending(To do) and information gathering(To do) bo
Currently works only on the Poloniex exchange


Botcoin version: {0}
Main functions:
[IN PROGRESS] Real time cryptocurrency trading:
    [DONE] Working simple trading strategy
    [X] Making multiple trades and having multiple open positions at the same time
    [X] More advanced profitable trading strategy:
        [X] Using precentages in different calculations for better optimization
        [X] Creating more indicators (RSI, MACD, Volume, Bollinger Bands, Support and Resistance and others)
    [IN PROGRESS] Testing, bug polishing and optimization
    [IN PROGRESS] Separating Botcoin into multiple files using OOP, classes and imports
    [X] Adding the finishing touches from the API (initializing the trading)
[DONE] Checking Historical data and backtesting:
    [DONE] Epoch & Unix timestamp converter
[X] Automatic lending
[?] Information gathering

(SMA, EMA, MACD)
