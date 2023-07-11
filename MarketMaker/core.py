import random


class MarketMaker:
    def __init__(self, price):
        self.price = price
        self.bid = price - 1
        self.ask = price + 1
        self.quantity = 100

    def trade(self, side, quantity):
        if side == "buy":
            if quantity <= self.ask - self.price:
                self.price = self.price + 1
                return quantity
            else:
                return 0
        elif side == "sell":
            if quantity <= self.price - self.bid:
                self.price = self.price - 1
                return quantity
            else:
                return 0


def main():
    market_maker = MarketMaker(100)
    for i in range(100):
        side = random.choice(["buy", "sell"])
        quantity = random.randint(1, 100)
        traded_quantity = market_maker.trade(side, quantity)
        print(f"{side} {quantity} {traded_quantity}")


if __name__ == "__main__":
    main()
