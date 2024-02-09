def fibonacci_last_digit(n):
        fibo = list(range(n + 1))
        if n == 0:
            return fibo[0]
        if n == 1:
            return fibo[1]
        if n > 1:
            for i in range(2, n + 1):
                fibo[i] = (fibo[i - 1] + fibo[i - 2])%10
            return fibo[n]


if __name__ == '__main__':
    number = int(input())
    print(fibonacci_last_digit(number)%10)