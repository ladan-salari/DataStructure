from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    price_unit = []
    for i in range (len(weights)):
        price_unit.append(values[i]/weights[i])
    while capacity > 0:
        item = price_unit.index(max(price_unit))
        amount = min (capacity, weights[item])
        value = value + amount * price_unit[item]
        capacity = capacity - amount
        del weights[item]
        del values[item]
        del price_unit[item]
        if price_unit==[]:
            return value

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
