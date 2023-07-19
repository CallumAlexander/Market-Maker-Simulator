from flask import Flask

from Market.core import Market, Equity
from MarketMaker.core import MarketMaker

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)

    stock = Equity(100, 0.2, "APPL")
    market = Market(stock, 100)
    market.simulate_market()

    maker = MarketMaker("APPL")
    for order in market.orders:
        print(maker.execute_order(order))
