def lcs2(first_sequence, second_sequence):
    if len(first_sequence) == 0 or len(second_sequence)==0:
        return 0

    L = [[0 for col in range(len(second_sequence) + 1)] for row in range(len(first_sequence) + 1)]
    for i in range(1,len(first_sequence) + 1):
        for j in range(1,len(second_sequence) + 1):
            if first_sequence[i-1] == second_sequence[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[len(first_sequence)][len(second_sequence)]

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
