from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    max_product = 0
    dot_product = 0

    first_list = sorted(first_sequence)
    second_list = sorted(second_sequence)

    for i in range(len(second_sequence)):
        dot_product += first_list[i] * second_list[i]
        max_product = max(max_product, dot_product)

    # for permutation in permutations(second_sequence):
    #     dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
    #     max_product = max(max_product, dot_product)
    return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))