def fibonacci_huge_naive(n, m):
    if n<=1:
        return n
    else:
        fibo= [0, 1]

        for i in range(2, n + 1):
            new = fibo[i-1]%m
            fibo.append((fibo[i - 1] + fibo[i - 2]) % m)
            if new == 0 and fibo[i] ==1:
                index = n%(i-1)
                return fibo[index]
        return fibo[-1]

if __name__ == '__main__':
    number, m = map(int, input().split())
    print(fibonacci_huge_naive(number, m))


### Pisano Period:
### It is mentioning that the reminder of Fibonacci numbers by any number is reapeating after a certain orders. And the start of the repeat is always 0 1
#### 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368,
### reminder to 3 is:
####0, 1, 1, 2, 0, 2, 2, 1, 0, 1, 1, 2, 0, 2, 2, 1, 0, 1, 1, 2, 0, 2, 2, 1, 0, .
