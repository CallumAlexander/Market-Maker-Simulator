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
            for day in range(t):
                return_ = random.normalvariate(0, self.volatility)
                if self.price * (1 + return_) <= 0:
                    # Adjust return to prevent price from going below zero
                    return_ = -self.price / self.price - 1
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


class Market:
    def __init__(self, equity, num_orders):
        self.equity = equity
        self.num_orders = num_orders
        self.orders = []

    def generate_orders(self):
        for _ in range(self.num_orders):

            # Randomly decide whether to simulate the equity or use the current price
            simulate_equity = random.choice([True, False])

            # Simulate the equity or use the current price for generating the order
            if simulate_equity:
                self.equity.simulate(1)

            side = random.choice(["buy", "sell"])
            quantity = random.randint(1, 100)
            price = random.uniform(0.9 * self.equity.price, 1.1 * self.equity.price)
            order = Order(self.equity, side, quantity, price)
            self.orders.append(order)

    def execute_orders(self):
        for order in self.orders:
            order.execute()

    def simulate_market(self):
        self.generate_orders()
        for order in self.orders:
            print(order.__str__())

def main():
    stock = Equity(100, 0.2, "APPL")
    # stock.simulate(30)
    # print(stock.history)
    # stock.chart_history()
    market = Market(stock, 100)
    market.simulate_market()


if __name__ == "__main__":
    main()
