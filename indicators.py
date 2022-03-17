#from poloniex import Poloniex

class Macd():

    # Attribute initialization
    price_list1 = []
    price_list2 = []
    price_list3 = []
    sma1 = 0
    sma2 = 0
    sma3 = 0
    ema1 = 0
    ema2 = 0
    lenght_of_averages1 = 26
    lenght_of_averages2 = 12
    lenght_of_averages3 = 9
    multiplier1 = (2 / (lenght_of_averages1 + 1))
    multiplier2 = (2 / (lenght_of_averages2 + 1))
    multiplier3 = (2 / (lenght_of_averages3 + 1))
    once1 = False
    once2 = False
    once3 = False
    macd = ""
    signal_line = ""
    macd_histogram = ""

    def macd_indicator(self, current_price):

        # List used to return the processed information
        lst = []

        '''Creating the MACD indicator'''
        # Creating the first SMA
        self.price_list1.append(current_price)

        if len(self.price_list1) > self.lenght_of_averages1:
            self.price_list1.remove(self.price_list1[0])

        if len(self.price_list1) == self.lenght_of_averages1:
            self.sma1 = sum(self.price_list1) / len(self.price_list1)

        # Creating the first EMA
        if len(self.price_list1) == self.lenght_of_averages1 and self.sma1 != 0 and self.once1 == False:
            self.ema1 = self.sma1
            self.once1 = True

        if self.ema1 != 0:
            self.ema1 = (current_price - self.ema1) * self.multiplier1 + self.ema1

        # Creating the second SMA
        self.price_list2.append(current_price)

        if len(self.price_list2) > self.lenght_of_averages2:
            self.price_list2.remove(self.price_list2[0])

        if len(self.price_list2) == self.lenght_of_averages2:
            self.sma2 = sum(self.price_list2) / len(self.price_list2)

        # Creating the second EMA
        if len(self.price_list2) == self.lenght_of_averages2 and self.sma2 != 0 and self.once2 == False:
            self.ema2 = self.sma2
            self.once2 = True

        if self.ema2 != 0:
            self.ema2 = (current_price - self.ema2) * self.multiplier2 + self.ema2

        # Creating the MACD
        if self.ema1 != 0 and self.ema2 != 0:
            self.macd = self.ema2 - self.ema1

        # Creating the MACD Line(EMA/9/ of the MACD)
        if self.macd != "":

            #Creating the third SMA
            self.price_list3.append(self.macd)

            if len(self.price_list3) > self.lenght_of_averages3:
                self.price_list3.remove(self.price_list3[0])

            if len(self.price_list3) == self.lenght_of_averages3:
                self.sma3 = sum(self.price_list3) / len(self.price_list3)

            # Creating the third EMA(Signal Line)
            if len(self.price_list3) == self.lenght_of_averages3 and self.sma3 != 0 and self.once3 == False:
                self.signal_line = self.sma3
                self.once3 = True

            if self.signal_line != "":
                self.signal_line = (self.macd - self.signal_line) * self.multiplier3 + self.signal_line

            # Creating the MACD Histogram
            if self.macd != "" and self.signal_line != "":
                self.macd_histogram = self.macd - self.signal_line

        # Appending variables into a resettable list and returning them when the method is called
        lst.append(self.macd)
        lst.append(self.signal_line)
        lst.append(self.macd_histogram)
        # lst.append(self.price_list1)
        # lst.append(self.price_list2)
        # lst.append(self.price_list3)
        # lst.append(self.sma1)
        # lst.append(self.sma2)
        # lst.append(self.sma3)
        # lst.append(self.ema1)
        # lst.append(self.ema2)
        return lst


''' for MACD testing '''
# polo = Poloniex()
# call = Macd()
#
# while True:
#     dic_output = polo.returnTicker()["USDT_BTC"]
#     current_price = float(dic_output["last"])
#
#     calling = call.macd_indicator(current_price)
#
#     print("Current Price: {0}".format(current_price))
#     print("Sma1: {0}".format(calling[6]))
#     print("Sma2: {0}".format(calling[7]))
#     print("Sma3: {0}".format(calling[8]))
#     print("Ema1: {0}".format(calling[9]))
#     print("Ema2: {0}".format(calling[10]))
#     print("Price list 1: {0}".format(calling[3]))
#     print("Price list 2: {0}".format(calling[4]))
#     print("Price list 3: {0}".format(calling[5]))
#     print("MACD: {0}".format(calling[0]))
#     print("Signal Line: {0}".format(calling[1]))
#     print("MACD Histogram: {0}".format(calling[2]))
#     print("")
#     print("")
'''~~~~~~~~~~~~~~~~'''


class Sma():

    price_list = []
    sma = 0

    def sma_indicator(self, current_price, lenght_of_averages):

        # List used to return the processed information
        lst = []

        # Creating the SMA
        self.price_list.append(current_price)

        if len(self.price_list) > lenght_of_averages:
            self.price_list.remove(self.price_list[0])

        if len(self.price_list) == lenght_of_averages:
            self.sma = sum(self.price_list) / len(self.price_list)

        # Appending variables into a resettable list and returning them when the method is called
        lst.append(self.sma)
        #lst.append(self.price_list)
        return lst


'''For SMA testing'''
# polo = Poloniex()
# call = Sma()
# len_of_sma = 5
#
# while True:
#     dic_output = polo.returnTicker()["USDT_BTC"]
#     current_price = float(dic_output["last"])
#
#     calling = call.sma_indicator(current_price, len_of_sma)
#
#     print("Current price: {}".format(current_price))
#     print("Sma: {}".format(calling[0]))
#     print("Price list: {}".format(calling[1]))
'''~~~~~~~~~~~~~~~~'''


class Ema():

    price_list = []
    sma = 0
    ema = 0
    once = False

    def ema_indicator(self, current_price, lenght_of_averages):

        # List used to return the processed information
        lst = []

        # Creating the SMA
        self.price_list.append(current_price)

        if len(self.price_list) > lenght_of_averages:
            self.price_list.remove(self.price_list[0])

        if len(self.price_list) == lenght_of_averages:
            self.sma = sum(self.price_list) / len(self.price_list)

        # Creating the EMA
        if len(self.price_list) == lenght_of_averages and self.sma != 0 and self.once == False:
            self.ema = self.sma
            self.once = True

        multiplier = (2 / (lenght_of_averages + 1))

        if self.ema != 0:
            self.ema = (current_price - self.ema) * multiplier + self.ema

        lst.append(self.ema)
        #lst.append(self.sma)
        #lst.append(self.price_list)
        return lst


'''For EMA testing'''
# polo = Poloniex()
# call = Ema()
# len_of_ema = 5
#
# while True:
#     dic_output = polo.returnTicker()["USDT_BTC"]
#     current_price = float(dic_output["last"])
#
#     calling = call.ema_indicator(current_price, len_of_ema)
#
#     print("Current price: {}".format(current_price))
#     print("Ema: {}".format(calling[0]))
#     print("Sma: {}".format(calling[1]))
#     print("Price list: {}".format(calling[2]))
'''~~~~~~~~~~~~~~~~'''
