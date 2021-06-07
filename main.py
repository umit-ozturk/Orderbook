from order_book import OrderBook
import json


def main():
    with open("example.txt", "r") as orders_file:
        orders = orders_file.readlines()
        orders = json.dumps(orders)

    ord_book = OrderBook()
    for i in orders:

        a = ord_book.process_order(orders)
        print(a)


if __name__ == "__main__":
    main()
