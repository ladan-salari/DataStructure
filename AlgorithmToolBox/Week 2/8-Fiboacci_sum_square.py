def fibonacci_sum_squares(n):
    if n <= 1:
        return n
    number = n%60
    fibo = [0,1]
    for i in range(2, number+1):
        fibo.append((fibo[i - 1] + fibo[i - 2])%60)
    return fibo[number]


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n)*fibonacci_sum_squares(n+1)%10)