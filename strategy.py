import pandas as pd

class Strategy:
    def __init__(self) -> None:
        pass

    def onBar(self, data: pd.DataFrame) -> None:
        print("Strategy onBar")
