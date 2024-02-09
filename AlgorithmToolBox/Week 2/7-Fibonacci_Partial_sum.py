def fibonacci_partial_sum_naive(m,n):
    if n <= 1:
        return n

    fibo = [0,1]
    for i in range(58):
        fibo.append((fibo[- 1] + fibo[- 2])%10)
    left = m%60
    right = n%60
    #in case the remainder of n is smaller than m then we add a 60 period there to fix the issue 
    if left > right:
        right+= 60
    sum = 0
    for i in range(left,right +1):
        sum+=fibo[i%60]
    return (sum)%10


if __name__ == '__main__':
    m, n = map(int, input().split())
    print(fibonacci_partial_sum_naive(m, n))


# the last digit start to repeat at n=60 so you need to calculate the first 60 numbers
### Also sum of fibonacci n is F(n+2)-1
