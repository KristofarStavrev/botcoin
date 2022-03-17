# Imports
from livetrading import LiveTrade
from historicalbacktesting import HistoricalBacktest


# Introduction
version = "alpha"
intro = '''Botcoin is a cryptocurrency trading, lending(To do) and information gathering(To do) bot, written on Python 3.5.3/3.6.0
Currently works only on the Poloniex exchange.
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
'''.format(version)
print(intro)
print("")


# Making the user choose between live trading and historical_backtesting
trading_mode = input("""Select trading mode:
[1] for Live trading
[2] for Historical backtesting
Mode: """)

if trading_mode == "1" and __name__ == "__main__":
    type = LiveTrade()
    type.live_trading()
elif trading_mode == "2" and __name__ == "__main__":
    type = HistoricalBacktest()
    type.historical_backtesting()
else:
    print("Invalid input")
