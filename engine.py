from strategy import Strategy
from datetime import *
import yfinance as yf
import pandas as pd

class Engine:
    strat: Strategy = None
    startingBalance: float
    balance: float
    startDate: datetime
    endDate: datetime
    timePeriod: timedelta
    currentTime: datetime
    dat = yf.Ticker("AAPL")

    def __init__(self, cash: float = 100000) -> None:
        self.balance = cash
        self.startingBalance = self.balance

    def addStrategy(self, strategy: Strategy) -> None:
        self.strat = strategy
    
    def setTimes(self, start: datetime, end: datetime, period: timedelta) -> None:
        self.startDate = start
        self.endDate = end
        self.timePeriod = period
        self.currentTime = self.startDate

    def getData(self, symbol: yf.Ticker, time: datetime, period: timedelta) -> pd.DataFrame:
        end_time = time + period
        data = symbol.history(start=time, end=end_time, interval=self.timeDeltaToInterval(period))
        return data

    def timeDeltaToInterval(self, period: timedelta) -> str:
        seconds = period.total_seconds()
        if seconds >= 86400:
            return '1d'
        elif seconds >= 3600:
            return '1h'
        else:
            return '1m'
        
    def run(self) -> None:
        while self.currentTime <= self.endDate:
            # Check if day is not weekend
            if self.currentTime.weekday() < 5:
                # Get data for time
                data: pd.DataFrame = self.getData(self.dat, self.currentTime, self.timePeriod)

                # Run strategy
                try:
                    self.strat.onBar(data)
                except:
                    pass

            # Move to next day
            # DO NOT PUT LOOP CODE AFTER THIS
            self.currentTime += self.timePeriod
