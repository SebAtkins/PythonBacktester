import pandas as pd
from tqdm import tqdm

class Engine():
    def __init__(self, startingBalance=100000):
        self.strategy = None
        self.cash = startingBalance
        self.data = None
        self.currentIdx = None
    
    def addData(self, data: pd.DataFrame):
        self.data = data

    def addStrategy(self, strategy):
        self.strategy = strategy
    
    def run(self):
        self.strategy.data = self.data

        for idx in tqdm(self.data.index):
            self.currentIdx = idx
            self.strategy.currentIdx = self.currentIdx

            self.fillOrders()

            self.strategy.onBar()
            print(idx)
    
    def fillOrders(self):
        for order in self.strategy.orders:
            canFill = False

            #  Check if the order can be made
            if order.side == "buy" and self.cash >= self.data.loc[self.currentIdx]["Open"] * order.size:
                canFill = True
            elif order.side == "sell" and self.strategy.positionSize >= order.size:
                canFill = True
            
            # Make order
            if canFill:
                t = Trade(
                    ticker = order.ticker,
                    side = order.side,
                    price = self.data.loc[self.currentIdx]["Open"],
                    size = order.size,
                    type = order.type,
                    idx = self.currentIdx
                )

                self.strategy.trades.append(t)
                print(f'Added trade {t}')
                self.cash -= t.price * t.size
        self.strategy.orders = []

class Strategy():
    def __init__(self):
        self.currentIdx = None
        self.data = None
        self.orders = []
        self.trades = []
    
    def buy(self, ticker, size=1):
        self.orders.append(
            Order(
                ticker = ticker,
                side = "buy",
                size = size,
                idx = self.currentIdx
            )
        )
    
    def sell(self, ticker, size=1):
        self.orders.append(
            Order(
                ticker = ticker,
                side = "sell",
                size = -size,
                idx = self.currentIdx
            )
        )
    
    @property
    def positionSize(self):
        return sum([t.size for t in self.trades])
    
    def onBar(self):
        pass

class Trade():
    def __init__(self, ticker, side, size, price, type, idx):
        self.ticker = ticker
        self.side = side
        self.price = price
        self.size = size
        self.type = type
        self.idx = idx
    
    def __repr__(self):
        return f'<Trade: {self.idx} {self.ticker} {self.size}@{self.price}>'

class Order():
    def __init__(self, ticker, size, side, idx):
        self.ticker = ticker
        self.side = side
        self.size = size
        self.type = "market"
        self.idx = idx
