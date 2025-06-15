from strategy import Strategy
import pandas as pd

class SimpleStrategy(Strategy):
    def __init__(self) -> None:
        super().__init__()
    
    def onBar(self, data: pd.DataFrame) -> None:
        row: pd.Series = data.iloc[1]
        open: float = float(row['Open'])
        high: float = float(row['High'])
        low: float = float(row['Low'])
        close: float = float(row['Close'])
