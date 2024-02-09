def fibonacci_sum(n):
    if n <= 1:
        return n
    number = n%60
    fibo = [0,1]
    sum = 1
    for i in range(2, number+2):
        fibo.append((fibo[i - 1] + fibo[i - 2]))
        sum += fibo[i-1]%10
    return (sum-1)%10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))


# the last digit start to repeat at n=60 so you need to calculate the first 60 numbers
### Also sum of fibonacci n is F(n+2)-1