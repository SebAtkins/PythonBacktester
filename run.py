import BacktestEngine as be
import yfinance as yf
import strategies as strats

data = yf.Ticker("AAPL").history(start="2020-01-01", end="2022-12-31", interval="1d")
e = be.Engine()
e.addData(data)
e.addStrategy(strats.BuyAndSellSwitch())
e.run()

print(e.strategy.trades)
