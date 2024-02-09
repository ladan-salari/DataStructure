def change(money):
    # write your code here
    minNumCoins = [None]*(money+1)

    minNumCoins[0] = 0
    coins = [1, 3, 4]
    for m in range(1, money+1):
        minNumCoins[m] = float('inf')
        for i in range(len(coins)):
            if m >=coins[i]:
                NumCoins = minNumCoins[m-coins[i]] + 1
                if NumCoins < minNumCoins[m]:
                    minNumCoins[m] = NumCoins
    return minNumCoins[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))

