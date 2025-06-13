import BacktestEngine as be

class BuyAndSellSwitch(be.Strategy):
    def onBar(self):
        if self.positionSize == 0:
            self.buy("AAPL", 1)
            print(self.currentIdx, "buy")
        else:
            self.sell("AAPL", 1)
            print(self.currentIdx, "sell")
        
