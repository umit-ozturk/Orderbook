import pandas as pd


class Order:
    """
    Order class is taking order correctly
    """
    def __init__(self, timestamp, order_id, action, ticker=None, side=None,
                 price=None, size=None):
        self.action = action
        self.timestamp = pd.Timestamp(timestamp)
        self.order_id = order_id
        self.ticker = ticker
        self.side = side
        self.price = price
        self.size = size

    def __str__(self):
        return self.order_id
