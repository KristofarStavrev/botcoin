import sys
from colorama import init, AnsiToWin32, Fore, Back, Style
from poloniex import Poloniex
from indicators import Macd
from indicators import Ema


class MomoStrat():

    # Attribute initialization
    indicator1 = Macd()
    indicator2 = Ema()
    period_for_ema = 20
    status1 = ""
    macdh_list1 = []
    len_of_macdh_list1 = 6
    counter1 = 0
    counter_time1 = 5
    open_trade = False
    type_of_trade = ""
    open_price = 0
    stop_loss_price = 0
    take_profit_price = 0
    stop_loss_percentage = 98
    take_profit_percentage = 4
    PorL = 0
    total_PorL_pair1 = 0
    total_PorL_pair2 = 0
    total_trades_opened = 0
    total_trades_closed = 0
    total_profit_trades = 0
    total_loss_trades = 0
    total_longs = 0
    total_shorts = 0
    total_fees = 0
    trade_fee = 0.002
    pair1_capital = 6000
    pair1_capital_start = 6000
    pair2_capital = 1
    pair2_capital_start = 1
    bought_amount = 0
    pair1_initial_capital = 0
    pair2_initial_capital = 0

    # Making colored text work on the CMD
    init(wrap=False)
    stream = AnsiToWin32(sys.stderr).stream

    def momo_trading_strat(self, current_price, is_margin_trading, percent_on_trade):

        return_list = []

        # Calling the MACD and EMA indicators
        call1 = self.indicator1.macd_indicator(current_price)
        call2 = self.indicator2.ema_indicator(current_price, self.period_for_ema)

        # Creating a list containing exactly 5 past values of the MACD Histogram for later use
        if call1[2] != "":
            self.macdh_list1.append(call1[2])
            if len(self.macdh_list1) > self.len_of_macdh_list1:
                self.macdh_list1.remove(self.macdh_list1[0])

        self.counter1 -= 1
        if self.counter1 < 0:
            self.counter1 = 0

        '''GOING LONG'''
        if call2[0] != 0 and call1[2] != "" and self.counter1 == 0 and len(self.macdh_list1) == self.len_of_macdh_list1 and self.status1 != "watch short":
            if float(current_price) < float(call2[0]) and float(call1[2]) < 0:
                self.status1 = "watch long"
                self.counter1 = self.counter_time1
                print("watching for long trade")
                print("")
            else:
                self.status1 = ""

        if self.status1 == "watch long":
            if (float(current_price) > float(call2[0])) and float(call1[2]) > 0 and self.macdh_list1[0] < 0:
                if self.open_trade == False:
                    if is_margin_trading == True:
                        # Opens a long position
                        pass
                    elif is_margin_trading == False:
                        # Makes a normal buy order
                        self.bought_amount = (self.pair1_capital * percent_on_trade) / current_price
                        print(self.bought_amount)
                        self.pair1_initial_capital = self.pair1_capital * percent_on_trade
                        print(self.pair1_initial_capital)
                        self.pair1_capital = self.pair1_capital - (self.pair1_capital * percent_on_trade)
                        print(self.pair1_capital)
                        fees = self.bought_amount * self.trade_fee
                        print(fees)
                        self.total_fees =  self.total_fees + (fees * current_price)
                        print(self.total_fees)
                        self.bought_amount = self.bought_amount - fees
                        print(self.bought_amount)
                        self.open_trade = True
                        self.type_of_trade = "Long"
                        self.open_price = current_price
                        self.take_profit_price = self.open_price * ((self.take_profit_percentage / 100) + 1)
                        self.stop_loss_price = self.open_price * (self.stop_loss_percentage / 100)
                        self.total_trades_opened = self.total_trades_opened + 1
                        self.total_longs = self.total_longs + 1

                        print("")
                        print("BUY ORDER PLACED")
                        print("")

        '''CLOSING LONG'''
        # Stop loss closing
        if self.open_trade == True and self.type_of_trade == "Long":
            if current_price <= self.stop_loss_price:
                if is_margin_trading == True:
                    # Closes long position
                    pass
                elif is_margin_trading == False:
                    fees = (self.bought_amount * current_price) * self.trade_fee
                    print(fees)
                    self.total_fees = self.total_fees + fees
                    print(self.total_fees)
                    self.pair1_capital = (self.pair1_capital + (self.bought_amount * current_price)) - fees
                    print(self.pair1_capital)
                    self.open_trade = False
                    self.type_of_trade = ""
                    #self.PorL = self.bought_amount * (float(current_price) - float(self.open_price))
                    self.PorL = ((self.bought_amount * current_price) - self.pair1_initial_capital) - fees
                    self.bought_amount = 0
                    print(self.bought_amount)
                    self.open_price = 0
                    self.total_PorL_pair1 = self.total_PorL_pair1 + (self.PorL)

                    PorL_str = str(self.PorL)
                    print("")
                    print("CLOSING POSITION")
                    if self.PorL > 0:
                        print("P/L: ", Fore.GREEN + Style.BRIGHT + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                        self.total_trades_closed = self.total_trades_closed + 1
                        self.total_profit_trades = self.total_profit_trades + 1
                    elif self.PorL < 0:
                        print("P/L: ", Fore.RED + Style.BRIGHT + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                        self.total_trades_closed = self.total_trades_closed + 1
                        self.total_loss_trades = self.total_loss_trades + 1
                    else:
                        print("P/L: ", Fore.RESET + Style.RESET_ALL + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                        self.total_trades_closed = self.total_trades_closed + 1

            # Take profit closing
            if current_price >= self.take_profit_price:
                if is_margin_trading == True:
                    # Closes long position
                    pass
                elif is_margin_trading == False:
                    fees = (self.bought_amount * current_price) * self.trade_fee
                    print(fees)
                    self.total_fees =  self.total_fees + fees
                    print(self.total_fees)
                    self.pair1_capital = (self.pair1_capital + (self.bought_amount * current_price)) - fees
                    print(self.pair1_capital)
                    self.open_trade = False
                    self.type_of_trade = ""
                    #self.PorL = self.bought_amount * (float(current_price) - float(self.open_price))
                    self.PorL = ((self.bought_amount * current_price) - self.pair1_initial_capital) - fees
                    self.bought_amount = 0
                    print(self.bought_amount)
                    self.open_price = 0
                    self.total_PorL_pair1 = self.total_PorL_pair1 + (self.PorL)

                    PorL_str = str(self.PorL)
                    print("")
                    print("CLOSING POSITION")
                    if self.PorL > 0:
                        print("P/L: ", Fore.GREEN + Style.BRIGHT + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                        self.total_trades_closed = self.total_trades_closed + 1
                        self.total_profit_trades = self.total_profit_trades + 1
                    elif self.PorL < 0:
                        print("P/L: ", Fore.RED + Style.BRIGHT + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                        self.total_trades_closed = self.total_trades_closed + 1
                        self.total_loss_trades = self.total_loss_trades + 1
                    else:
                        print("P/L: ", Fore.RESET + Style.RESET_ALL + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                        self.total_trades_closed = self.total_trades_closed + 1

        '''GOING SHORT'''
        if call2[0] != 0 and call1[2] != "" and self.counter1 == 0 and len(self.macdh_list1) == self.len_of_macdh_list1 and self.status1 != "watch long":
            if float(current_price) > float(call2[0]) and float(call1[2]) > 0:
                self.status1 = "watch short"
                self.counter1 = self.counter_time1
                print("watching for short trade")
                print("")
            else:
                self.status1 = ""

        if self.status1 == "watch short":
            if (float(current_price) < float(call2[0])) and float(call1[2]) < 0 and self.macdh_list1[0] > 0:
                if self.open_trade == False:
                    if is_margin_trading == True:
                        # Opens a short position
                        pass
                    elif is_margin_trading == False:
                        self.bought_amount = (self.pair2_capital * percent_on_trade) * current_price
                        print(self.bought_amount)
                        self.pair2_initial_capital = self.pair2_capital * percent_on_trade
                        print(self.pair2_initial_capital)
                        self.pair2_capital = self.pair2_capital - (self.pair2_capital * percent_on_trade)
                        print(self.pair2_capital)
                        fees = self.bought_amount * self.trade_fee
                        print(fees)
                        self.total_fees =  self.total_fees + fees
                        print(self.total_fees)
                        self.bought_amount = self.bought_amount - fees
                        print(self.bought_amount)
                        self.open_trade = True
                        self.type_of_trade = "Short"
                        self.open_price = current_price
                        self.stop_loss_price = self.open_price * ((self.take_profit_percentage / 100) + 1)
                        self.take_profit_price = self.open_price * (self.stop_loss_percentage / 100)
                        self.total_trades_opened = self.total_trades_opened + 1
                        self.total_shorts = self.total_shorts + 1


                        print("")
                        print("SELL ORDER PLACED")
                        print("")

        '''CLOSING SHORT'''
        # Stop loss closing
        if self.open_trade == True and self.type_of_trade == "Short":
            if current_price >= self.stop_loss_price:
                if is_margin_trading == True:
                    # Closes short position
                    pass
                elif is_margin_trading == False:
                    fees = (self.bought_amount / current_price) * self.trade_fee
                    print(fees)
                    self.total_fees =  self.total_fees + (fees * current_price)
                    print(self.total_fees)
                    self.pair2_capital = (self.pair2_capital + (self.bought_amount / current_price)) - fees
                    print(self.pair2_capital)
                    self.open_trade = False
                    self.type_of_trade = ""
                    self.PorL = ((self.bought_amount / current_price) - self.pair2_initial_capital) - fees
                    self.bought_amount = 0
                    print(self.bought_amount)
                    self.open_price = 0
                    self.total_PorL_pair2 = self.total_PorL_pair2 + (self.PorL)

                    PorL_str = str(self.PorL)
                    print("")
                    print("CLOSING POSITION")
                    if self.PorL > 0:
                        print("P/L: ", Fore.GREEN + Style.BRIGHT + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                        self.total_trades_closed = self.total_trades_closed + 1
                        self.total_profit_trades = self.total_profit_trades + 1
                    elif self.PorL < 0:
                        print("P/L: ", Fore.RED + Style.BRIGHT + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                        self.total_trades_closed = self.total_trades_closed + 1
                        self.total_loss_trades = self.total_loss_trades + 1
                    else:
                        print("P/L: ", Fore.RESET + Style.RESET_ALL + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                        self.total_trades_closed = self.total_trades_closed + 1

            # Take profit closing
            if current_price <= self.take_profit_price:
                if is_margin_trading == True:
                    # Closes short position
                    pass
                elif is_margin_trading == False:
                    fees = (self.bought_amount / current_price) * self.trade_fee
                    print(fees)
                    self.total_fees =  self.total_fees + (fees * current_price)
                    print(self.total_fees)
                    self.pair2_capital = (self.pair2_capital + (self.bought_amount / current_price)) - fees
                    print(self.pair2_capital)
                    self.open_trade = False
                    self.type_of_trade = ""
                    self.PorL = ((self.bought_amount / current_price) - self.pair2_initial_capital) - fees
                    self.bought_amount = 0
                    print(self.bought_amount)
                    self.open_price = 0
                    self.total_PorL_pair2 = self.total_PorL_pair2 + (self.PorL)

                    PorL_str = str(self.PorL)
                    print("")
                    print("CLOSING POSITION")
                    if self.PorL > 0:
                        print("P/L: ", Fore.GREEN + Style.BRIGHT + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                        self.total_trades_closed = self.total_trades_closed + 1
                        self.total_profit_trades = self.total_profit_trades + 1
                    elif self.PorL < 0:
                        print("P/L: ", Fore.RED + Style.BRIGHT + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                        self.total_trades_closed = self.total_trades_closed + 1
                        self.total_loss_trades = self.total_loss_trades + 1
                    else:
                        print("P/L: ", Fore.RESET + Style.RESET_ALL + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                        self.total_trades_closed = self.total_trades_closed + 1

        percent_gain1 = ((self.pair1_capital - self.pair1_capital_start) / self.pair1_capital_start) * 100
        percent_gain2 = ((self.pair2_capital - self.pair2_capital_start) / self.pair2_capital_start) * 100

        # '''FOR TESTING'''
        # print("Current price: {0}".format(current_price))
        # print("EMA: {0}".format(call2[0]))
        # print("MACD Histogram: {0}".format(call1[2]))
        # #print("MACD Histogram list: {0}".format(self.macdh_list1))
        # print("Status1: {0}".format(self.status1))
        # print("Counter1: {0}".format(self.counter1))
        # print("")
        # '''FOR TESTING'''

        self.pair1_capital = round(self.pair1_capital, 8)
        self.pair2_capital = round(self.pair2_capital, 8)
        percent_gain1 = round(percent_gain1, 2)
        percent_gain2 = round(percent_gain2, 2)

        return_list.append(call1[0])
        return_list.append(call1[1])
        return_list.append(call1[2])
        return_list.append(call2[0])
        return_list.append(self.status1)
        return_list.append(self.counter1)
        return_list.append(self.total_PorL_pair1)
        return_list.append(self.total_PorL_pair2)
        return_list.append(self.total_trades_opened)
        return_list.append(self.total_trades_closed)
        return_list.append(self.total_profit_trades)
        return_list.append(self.total_loss_trades)
        return_list.append(self.total_longs)
        return_list.append(self.total_shorts)
        return_list.append(round(self.total_fees, 2))
        return_list.append(self.pair1_capital)
        return_list.append(self.pair2_capital)
        return_list.append(percent_gain1)
        return_list.append(percent_gain2)
        return_list.append(self.bought_amount)

        return return_list

# polo = Poloniex()
# sss = MomoStrat()
#
#     dic_output = polo.returnTicker()["USDT_BTC"]
# while True:
#     current_price = float(dic_output["last"])
#     sss.momo_trading_strat(current_price)
