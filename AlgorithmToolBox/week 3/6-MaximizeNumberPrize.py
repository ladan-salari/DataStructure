def optimal_summands(n):
    summands = []
    if n <= 2:
        summands = [n]
        return summands
    loc_n = n
    count = 0
    while loc_n > 0:
        count += 1
        if loc_n - count <= count:
            count = loc_n
        summands.append(count)
        loc_n -= count

    return summands








    # write your code here
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)