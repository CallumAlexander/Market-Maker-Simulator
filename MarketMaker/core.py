import logging
import random
from GME.core import *


class MarketMaker:
    def __init__(self, equity):
        self.equity = equity
        self.price = equity.price
        self.volatility = 0.2  # Fixed
        self.profit = 0
        self.bid = self.price - 1
        self.ask = self.price + 1

    def simulate(self, days):
        self.equity.simulate(days)

    def chart_history(self):
        self.equity.chart_history()

    def trade(self, side, quantity):
        if side == "buy":
            if quantity <= self.equity.price - self.ask:
                self.price = self.price + 1
                self.profit += (self.price - self.equity.price) * quantity
                return quantity
            else:
                return 0
        elif side == "sell":
            if quantity <= self.price - self.bid:
                self.price = self.price - 1
                self.profit += (self.equity.price - self.price) * quantity
                return quantity
            else:
                return 0


def main():
    e = Equity(50, 0.2)
    market_maker = MarketMaker(e)
    for i in range(30):
        market_maker.simulate(1)
        side = random.choice(["buy", "sell"])
        quantity = random.randint(1, 10)
        traded_quantity = market_maker.trade(side, quantity)
        print(traded_quantity)
    market_maker.chart_history()
    print(market_maker.profit)

if __name__ == "__main__":
    main()
