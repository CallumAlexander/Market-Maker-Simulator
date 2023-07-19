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

        self.inventory = 0
        self.cash = 10000

        # The bid price represents the maximum price the market maker is willing to pay to buy the security
        self.bid = self.price - 1
        # the ask price represents the minimum price at which they are willing to sell it.
        self.ask = self.price + 1

    def simulate(self, days):
        self.equity.simulate(days)

    def chart_history(self):
        self.equity.chart_history()

    def execute_order(self, order):
        if order.side == "buy":
            if order.price >= self.ask:
                cost = order.quantity * self.ask
                if self.cash >= cost:
                    # Buy the securities at the ask price
                    self.inventory += order.quantity
                    self.cash -= cost
                    self.profit -= cost
                    return True
                else:
                    # Insufficient cash to execute the order
                    return False
            else:
                # Order not executed
                return False
        elif order.side == "sell":
            if order.price <= self.bid:
                if order.quantity <= self.inventory:
                    # Sell the securities from the inventory at the bid price
                    revenue = order.quantity * self.bid
                    self.inventory -= order.quantity
                    self.cash += revenue
                    self.profit += revenue
                    return True
                else:
                    # Not enough securities in inventory to execute the order
                    return False
            else:
                # Order not executed
                return False


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
