def GCD(a, b):
    if b ==0:
        return a
    else:
        new_number = a % b
        return GCD(b, new_number)

def LCM(a,b):
    if b == 0:
        return 0
    else:
        return a*b/GCD(a,b)

if __name__=='__main__':
    a, b = map(int, input().split())
    print(int(LCM(a,b)))