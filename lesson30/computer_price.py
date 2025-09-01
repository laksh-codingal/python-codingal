
class computer:

    def __init__(self):
        self.__maxprice = 700

    def sell(self):
        print("selling price is:- ", self.__maxprice)

    def setmaxprice(self,price):
        self.__maxprice = price

a = computer()
a.sell()

a.__maxprice=1000
a.sell()

a.setmaxprice(1000)

a.sell()
