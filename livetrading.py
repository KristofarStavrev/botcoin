# Imports
import time
import datetime
from poloniex import Poloniex
from smastrat import MATest
from momostrat import MomoStrat


class LiveTrade():

    def live_trading(self):

        print("")
        print("")
        print("LIVE TRADING")

        # Variable initialization
        polo = Poloniex()
        is_margin_trading = input("""Select trading mode:
[1] Normal exchange trade
[2] Margin trading
Mode: """)

        if is_margin_trading == "1":
            is_margin_trading = False
            for_print = "Margin trading"

        elif is_margin_trading == "2":
            is_margin_trading = True
            for_print = "Normal exchange trading"

        else:
            print("Invalid input")

        percent_on_trade = float(input("Percentage of trading capital used in each trade: "))
        percent_on_trade = percent_on_trade / 100
        time_period = int(input("Time period in seconds: "))
        pair = input("Pair (ex: BTC_ETH): ")

        # Assigning the strat object with the strategy thats going to be used for trading
        desired_strategy = input('''Trading strategy thats going to be used:
        [1] 2 Moving averages (one short and one long) crossover strategy (simple, not very efficient)
        [2] 5-Minute "Momo" trading strategy
        : ''')

        if desired_strategy == "1":
            lenght_of_ma1 = int(input("Lenght of the first (short) Moving Average: "))
            lenght_of_ma2 = int(input("Lenght of the second (long) Moving Average: "))
            strat = MATest()

        if desired_strategy == "2":
            strat = MomoStrat()

        # Printing information to the UI
        print("")
        print("")
        print("Trading mode: {0}".format(for_print))
        print("Time period: {0}s".format(time_period))
        print("Pair: {0}".format(pair))

        print("")

        # Initializing the main loop
        while True:

            # Gathering and storing information from the exchange API
            dic_output = polo.returnTicker()[pair]
            current_price = float(dic_output["last"])

            # Calling the strategy method
            if desired_strategy == "1":
                strat_call = strat.moving_average_strat(current_price, lenght_of_ma1, lenght_of_ma2)

            if desired_strategy == "2":
                strat_call = strat.momo_trading_strat(current_price, is_margin_trading, percent_on_trade)

            # Setting up the current time
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Prints the UI in the command line
            print("")
            print("Current time: {0}".format(current_time))
            print("Current price: {0}".format(current_price))
            if desired_strategy == "1":
                print("Moving average({1}): {0}".format(strat_call[0], lenght_of_ma1))
                print("Moving average({1}): {0}".format(strat_call[1], lenght_of_ma2))
                #print("Price list 1 (all past prices)[FOR DEBUGGING ONLY]: {0}".format(strat_call[3]))
                #print("Price list 2 (all past prices)[FOR DEBUGGING ONLY]: {0}".format(strat_call[4]))
                print("Total profit or loss: {0}".format(strat_call[2]))
            elif desired_strategy == "2":
                print("MACD: {0}".format(strat_call[0]))
                print("Signal Line: {0}".format(strat_call[1]))
                print("MACD Histogram: {0}".format(strat_call[2]))
                print("EMA: {0}".format(strat_call[3]))
                print("Status: {0}".format(strat_call[4])) #FOR DEBUGGING ONLY
                print("Counter: {0}".format(strat_call[5])) #FOR DEBUGGING ONLY
                print("Total profit or loss for pair 1 (capital 1): {0}".format(strat_call[6]))
                print("Total profit or loss for pair 2 (capital 2): {0}".format(strat_call[7]))
                print("Total number of trades opened: {0}".format(strat_call[8]))
                print("Total number of trades closed: {0}".format(strat_call[9]))
                print("Total number of profitable trades: {0}".format(strat_call[10]))
                print("Total number of unprofitable trades: {0}".format(strat_call[11]))
                print("Total long trades opened: {0}".format(strat_call[12]))
                print("Total short trades opened: {0}".format(strat_call[13]))
                print("Total fees: {0}.".format(strat_call[14]))
                print("Pair 1 capital: {0}.".format(strat_call[15]))
                print("Pair 2 capital: {0}.".format(strat_call[16]))
                print("Pair 1 percent gain: {0}%.".format(strat_call[17]))
                print("Pair 2 percent gain: {0}%.".format(strat_call[18]))
                print("Current capital in open positions: {0}.".format(strat_call[19]))
            print()
            print("")

            # Sleep time between loops
            time.sleep(time_period)
