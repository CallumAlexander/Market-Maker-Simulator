from Market.core import Equity, Market
from MarketMaker.core import MarketMaker

if __name__ == "__main__":
    stock = Equity(100, 0.2, "APPL")
    market = Market(stock, 100)
    market.simulate_market()

    maker = MarketMaker(stock)
    for order in market.orders:
        print(maker.execute_order(order))

    print("Profit: " + str(maker.profit))
