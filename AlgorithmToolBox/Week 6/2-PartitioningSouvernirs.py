from sys import stdin


def partition3(values):
    if len(values) <= 2:
        return 0
    if len(values) == 3:
        if values[0] == values[1] and values[0] == values[2]:
            return 1
        else:
            return 0
    max_sum = sum(values)
    if max_sum % 3 != 0:
        return 0
    else:
        max_sum = max_sum // 3
    for partition in range (2):
        new_sum = maxNumbers(max_sum, values)
        if new_sum[len(values)][max_sum] != max_sum:
            return 0
        else:
            used_values = optimial(new_sum, max_sum, values)
            for i in used_values:
                values.pop(i)
    return 1

def maxNumbers(capacity, values):
    temp_numbers=[[0 for col in range(capacity + 1)] for row in range(len(values) + 1)]

    for i in range(1, len(values) + 1):
        for w in range(1, capacity+1):
            temp_numbers[i][w] = temp_numbers[i - 1][w]
            if values[i - 1] <= w:
                weight = temp_numbers[i - 1][w - values[i - 1]] + values[i - 1]
                if temp_numbers[i][w] < weight:
                    temp_numbers[i][w] = weight
    return temp_numbers


def optimial(new_sum, capacity, values):
    used_number =[]
    i = len(values)
    n = capacity
    while  i > 0 and n > 0:
        if new_sum[i][n] == new_sum[i-1][n]:
            i -= 1
        else:
            used_number.append(i-1)
            n -= values[i-1]
            i -= 1
    return used_number






if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))