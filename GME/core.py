import random
import numpy as np
import matplotlib.pyplot as plt


class Equity:

    def __init__(self, starting_price, volatility, symbol):
        self.symbol = symbol
        self.volatility = volatility
        self.price = starting_price
        self.history = np.empty(0)

    def simulate(self, t):
        for day in range(t):
            return_ = random.normalvariate(0, self.volatility)
            self.price *= (1 + return_)
            self.history = np.append(self.history, self.price)

        return

    def chart_history(self):
        plt.plot(self.history)
        plt.xlabel("Days")
        plt.ylabel("Price")
        plt.show()


class Order:
    def __init__(self, equity, side, quantity, price):
        self.equity = equity
        self.side = side
        self.quantity = quantity
        self.price = price

    def execute(self):
        if self.side == "buy":
            # Execute buying logic here
            pass
        elif self.side == "sell":
            # Execute selling logic here
            pass

    def __str__(self):
        return f"Order: {self.side} {self.quantity} {self.equity.symbol} at {self.price}"


def main():
    stock = Equity(100, 0.2)
    stock.simulate(30)
    print(stock.history)
    stock.chart_history()


if __name__ == "__main__":
    main()
