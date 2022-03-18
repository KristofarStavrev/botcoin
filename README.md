# BotCoin

## Project Description
BotCoin is a simple algorithmic cryptocurrency [trading bot](https://www.investopedia.com/articles/active-trading/101014/basics-algorithmic-trading-concepts-and-examples.asp) developed on Python. The main purpose of the program is to automate the execution of different trading strategies while also removing the risks of manual errors when placing trades and the possibility of mistakes based on emotional and psychological factors. The data collection process is done by using an API connection to a cryptocurrency market exchange ([Poloniex](https://poloniex.com/)).

**Note: The current version serves the purpose only as a simulation and does not support the opening of real trade positions.**

## Main features
- The bot supports the functionality for both real-time live trading simulation and historical backtesting with built in basic trading strategies using indicators for technical analysis.
- Algo-trading can be backtested using available historical and real-time data to see if it is a viable trading strategy.
- Simultaneous automated checks on multiple market conditions.
- Trades are timed correctly and instantly to avoid significant price changes.
- Trade order placement is instant and accurate (there is a high chance of execution at the desired levels).

## Future development oppurtunities
- Add more available exchanges and different sources for data collection.
- Expand the range of trading stategies by also adding additional techical indicators.
- Make it possible to have multiple open trade positions simultaniously.
- Explore for other [DeFi](https://www.investopedia.com/decentralized-finance-defi-5113835) opportunities that can be incorporated in functionality of the trading bot.

## To run the program
1. Clone the repository `git clone https://github.com/KrythonS/botcoin.git`.
2. Create a virtual environment and install dependencies `pip install poloniex` (library used for the API connection).
3. Run the script `BotCoin.py`.

## Visual examples of the program

### Image 1: Main Menu
![alt text](https://i.ibb.co/xC14TYC/image1.png)

### Image 2: Live Trading Mode Initializing
![alt text](https://i.ibb.co/yPSB9nM/image2.png)

### Image 3: Live Trading Mode Active
![alt text](https://i.ibb.co/Tm75LVF/image3.png)

### Image 4: Historical Backtesting
![alt text](https://i.ibb.co/pjzccqg/image4.png)

### Image 5: Historical Backtesting Results
![alt text](https://i.ibb.co/2v7Vjn2/image5.png)
