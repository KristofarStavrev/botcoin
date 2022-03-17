import sys
from colorama import init, AnsiToWin32, Fore, Back, Style


class MATest():

    # Attribute initialization
    price_list1 = []
    price_list2 = []
    ma1 = 0
    ma2 = 0
    bool_past = ""
    bool_present = ""
    ma_compare = ""
    open_trade = False
    type_of_trade = ""
    PorL = 0
    open_price = 0
    total_PorL = 0

    # Making colored text work on the CMD
    init(wrap=False)
    stream = AnsiToWin32(sys.stderr).stream

    def moving_average_strat(self, current_price, lenght_of_ma1, lenght_of_ma2):

        # List used to return the processed information
        lst = []

        # Appending information(price) into a list for later use(Simple Moving Averages)
        self.price_list1.append(current_price)
        self.price_list2.append(current_price)

        # Moving Average 1
        if len(self.price_list1) > lenght_of_ma1:
            self.price_list1.remove(self.price_list1[0])

        if len(self.price_list1) == lenght_of_ma1:
            self.ma1 = sum(self.price_list1) / len(self.price_list1)

        # Moving Average 2
        if len(self.price_list2) > lenght_of_ma2:
            self.price_list2.remove(self.price_list2[0])

        if len(self.price_list2) == lenght_of_ma2:
            self.ma2 = sum(self.price_list2) / len(self.price_list2)

        # Comparing the present states of both moving averages(setup for crossover comparison)
        if self.ma1 == 0 or self.ma2 == 0:
            pass
        elif self.ma1 > self.ma2:
            # Short MA above long MA
            self.bool_present = True
        elif self.ma1 < self.ma2:
            # Short MA below long MA
            self.bool_present = False

        # Comparing the short and the long moving average(looking for crossovers)
        if self.bool_present == "" or self.bool_past == "":
            pass
        elif self.bool_present == self.bool_past:
            self.ma_compare = "No crossover"
        elif self.bool_present != self.bool_past:
            self.ma_compare = "Crossover"

        # Comparing the past states of both moving averages(setup for crossover comparison)
        if self.ma1 == 0 or self.ma2 == 0:
            pass
        elif self.ma1 > self.ma2:
            # Short MA above long MA
            self.bool_past = True
        elif self.ma1 < self.ma2:
            # Short MA below long MA
            self.bool_past = False

        # Buy, Sell, Close signals
        if self.open_trade == False:
            if self.ma_compare == "Crossover" and self.ma1 > self.ma2:
                self.open_trade = True
                self.type_trade = "LONG"
                self.open_price = current_price
                print("")
                print("OPEN LONG POSITION")
                print("")
            elif self.ma_compare == "Crossover" and self.ma1 < self.ma2:
                self.open_trade = True
                self.type_trade = "SHORT"
                self.open_price = current_price
                print("")
                print("OPEN SHORT POSITION")
                print("")
        elif self.open_trade == True:
            if self.type_trade == "LONG":
                if self.ma1 < self.ma2:
                    self.open_trade = False
                    self.type_trade = ""
                    self.PorL = float(current_price) - float(self.open_price)
                    self.total_PorL = self.total_PorL + (self.PorL)
                    PorL_str = str(self.PorL)
                    print("")
                    print("CLOSING POSITION")
                    if self.PorL > 0:
                        print("P/L: ", Fore.GREEN + Style.BRIGHT + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                    elif self.PorL < 0:
                        print("P/L: ", Fore.RED + Style.BRIGHT + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                    else:
                        print("P/L: ", Fore.RESET + Style.RESET_ALL + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
            elif self.type_trade == "SHORT":
                if self.ma1 > self.ma2:
                    self.open_trade = False
                    self.type_trade = ""
                    self.PorL = float(self.open_price) - float(current_price)
                    self.total_PorL = self.total_PorL + (self.PorL)
                    PorL_str = str(self.PorL)
                    print("")
                    print("CLOSING POSITION")
                    if self.PorL > 0:
                        print("P/L: ", Fore.GREEN + Style.BRIGHT + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                    elif self.PorL < 0:
                        print("P/L: ", Fore.RED + Style.BRIGHT + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)
                    else:
                        print("P/L: ", Fore.RESET + Style.RESET_ALL + PorL_str, file=self.stream)
                        print(Fore.RESET + Style.RESET_ALL, file=self.stream)

        # Appending variables into a resettable list and returning them when the method is called
        lst.append(self.ma1)
        lst.append(self.ma2)
        lst.append(self.total_PorL)
        lst.append(self.price_list1)
        lst.append(self.price_list2)
        return lst
