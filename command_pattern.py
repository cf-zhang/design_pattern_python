class Order:
    def execute(self):
        pass

class Stock:
    def __init__(self):
        self.name = "ABC"
        self.quantity = 10

    def buy(self):
        print("Stock name: "+self.name+", "+str(self.quantity) + " bought")

    def sell(self):
        print("Stock name: "+self.name+", "+str(self.quantity) + " sell")


class BuyStock(Order):
    def __init__(self, abc_stock):
        self.abc_stock = abc_stock

    def execute(self):
        self.abc_stock.buy()

class SellStock(Order):
    def __init__(self, abc_stock):
        self.abc_stock = abc_stock

    def execute(self):
        self.abc_stock.sell()

class Broker:
    def __init__(self):
        self.order_list = list()

    def take_order(self, order: 'Order'):
        self.order_list.append(order)

    def place_order(self):
        for order in self.order_list:
            order.execute()
        self.order_list.clear()

stock = Stock()
buy_stock_order = BuyStock(stock)
sell_stock_order = SellStock(stock)
broker = Broker()
broker.take_order(buy_stock_order)
broker.take_order(sell_stock_order)
broker.place_order()