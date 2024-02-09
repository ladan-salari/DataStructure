def GCD(a, b):
    if b ==0:
        return a
    else:
        new_number = a % b
        return GCD(b, new_number)


if __name__=='__main__':
    a, b =map(int, input().split())
    print(GCD(a,b))

