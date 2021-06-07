from order import Order


class OrderBook:
    """
    OrderBook class
    """
    def __init__(self):
        self.orders = []

    def get_order(self, order_id):
        """
        Get correct order from order book with order_id.
        :param order_id: Order id
        :return: String of order
        """
        for i, order in enumerate(self.orders):
            if order_id in order:
                return self.orders[i]

    def process_order(self, order):
        """
        :param order: Order id to process the related order.
        """
        if not isinstance(list, order):
            raise Exception("Order should be list.")
        action = order[2]
        if action == "a":
            self.add_order(order)
        if action == "u":
            self.update_order(order)
        if action == "c":
            self.cancel_order(order)

    def add_order(self, order):
        """
        Add order to the orderbook.
        :param order:
        :return:
        """
        self.orders.append(Order(*order))

    def update_order(self, order):
        """
        Note: order coming from outside, _order is coming from self.orders.
        :param order: Order coming from outside to update the order
        :return: Updated orders
        """
        for i, _order in enumerate(self.orders):
            if order[1] in _order:
                self.orders[i].size = order[3]  # Size for updater
        return self.orders

    def cancel_order(self, order):
        """
        Cancel order (remove from orderbook)
        :param order: Order object.
        :return:
        """
        for i, _order in enumerate(self.orders):
            if order[1] in _order:
                self.orders.remove(order[1])
        return self.orders
