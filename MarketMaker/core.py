import logging
import random

import numpy as np

from Market.core import *


class MarketMaker:
    def __init__(self, equity):
        self.equity = equity
        self.price = equity.price
        self.volatility = 0.2  # Fixed
        self.profit = 0
        self.profit_history = np.empty(0)

        # The bid price represents the maximum price the market maker is willing to pay to buy the security
        self.bid = self.price - 1
        # the ask price represents the minimum price at which they are willing to sell it.
        self.ask = self.price + 1

    def simulate(self, days):
        self.equity.simulate(days)

    def chart_history(self):
        self.equity.chart_history()

    def trade(self, side, quantity):
        if side not in ["buy", "sell"]:
            raise ValueError("Invalid side. Choose 'buy' or 'sell'.")

        if side == "buy":
            if quantity <= self.equity.price - self.ask:
                self.price += 1
                self.profit += (self.ask - self.bid) * quantity
                self.profit_history = np.append(self.profit_history, self.profit)
                return quantity
            else:
                return 0

        elif side == "sell":
            if quantity <= self.price - self.bid:
                self.price -= 1
                self.profit += (self.ask - self.bid) * quantity
                self.profit_history = np.append(self.profit_history, self.profit)
                return quantity
            else:
                return 0


def main():
    e = Equity(50, 0.2, "gme")
    market_maker = MarketMaker(e)
    for i in range(30):
        market_maker.simulate(1)
        side = random.choice(["buy", "sell"])
        quantity = random.randint(1, 10)
        traded_quantity = market_maker.trade(side, quantity)
        print(market_maker.profit)
    market_maker.chart_history()
    print(market_maker.profit)

if __name__ == "__main__":
    main()
