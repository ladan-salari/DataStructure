from itertools import permutations
from functools import cmp_to_key


def largest_number_naive(numbers):
    numbers = list(map(int, numbers))
    largest = 0
    # numbers_sorted=sorted(numbers, reverse=True)
    # print(numbers_sorted)
    # for i in range (len(numbers_sorted)-1):
    #     if numbers_sorted[i]//10 !=0 and numbers_sorted[i+1]//10 ==0:
    #         if numbers_sorted[i]//10 <= numbers_sorted[i+1]:
    #             numbers_sorted[i+1], numbers_sorted[i] = numbers_sorted[i], numbers_sorted[i+1]
    #
    # numbers_sorted_str = list(map(str, numbers_sorted))
    # largest=max(largest, int("".join(numbers_sorted_str)))
    def compare(a, b):
        ab = int(str(a) + str(b))
        ba = int(str(b) + str(a))
        if ab > ba:
            return -1
        elif ab < ba:
            return 1
        else:
            return 0

    res = sorted(numbers, key=cmp_to_key(compare))
    numbers_sorted_str = list(map(str, res))
    largest = max(largest, int("".join(numbers_sorted_str)))

    # for permutation in permutations(numbers):
    #     largest = max(largest, int("".join(permutation)))

    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_naive(input_numbers))