def calculate_il(p1, p2, p3, p4):
    initial_price = p2 / p1
    future_price = p4 / p3
    price_increase = abs(future_price - initial_price) / initial_price
    il = abs((2 * (price_increase ** 0.5) / (1 + price_increase)) - 1)
    return il


if __name__ == '__main__':
    print(calculate_il(1, 100, 1, 110))
