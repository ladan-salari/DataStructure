def max_pairwise_product(numbers):
    if len(numbers) == 2:
        return numbers[0]*numbers[1]
    else:
        index_1 = 0
        for i in range(len(numbers)):
            if numbers[i]> numbers[index_1]:
                index_1 = i

        index_2 = 0
        for i in range(len(numbers)):
            if numbers[i]>numbers[index_2] and i != index_1:
                index_2 = i
        return numbers[index_1]*numbers[index_2]

# def max_pairwise_product(numbers):
#     new_numbers = sorted(numbers)
#     return new_numbers[-1]*new_numbers[-2]

if __name__ == '__main__':
    # input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
