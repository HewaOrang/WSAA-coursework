# This program calculates the average price of books from the API.
# By: Hewa Orang

from bookapi import readbooks

def average_book_price():
    books = readbooks()

    prices = []
    for book in books:
        price = book.get("price")
        if isinstance(price, (int, float)):
            prices.append(price)

    if len(prices) == 0:
        return 0

    return sum(prices) / len(prices)

if __name__ == "__main__":
    avg = average_book_price()
    print("Average book price:", avg)