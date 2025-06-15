from strategy import Strategy

class Engine:
    strat: Strategy = None
    startingBalance: float
    balance: float

    def __init__(self, cash: float = 100000) -> None:
        self.balance = cash
        self.startingBalance = self.balance
