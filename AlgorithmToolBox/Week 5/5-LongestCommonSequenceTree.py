def lcs3(first_sequence, second_sequence, third_sequence):
    if len(first_sequence) == 0 or len(second_sequence) == 0 or len(third_sequence)==0:
        return 0
    L = [[[0 for i in range(len(third_sequence) + 1)] for j in range(len(second_sequence) + 1)] for k in range(len(first_sequence) + 1)]

    for i in range(1, len(first_sequence) + 1):
        for j in range(1, len(second_sequence) + 1):
            for k in range(1, len(third_sequence)+1):
                if first_sequence[i - 1] == second_sequence[j - 1] and first_sequence[i-1] == third_sequence[k-1]:
                    L[i][j][k] = L[i - 1][j - 1][k - 1] + 1
                else:
                    L[i][j][k] = max(max(L[i - 1][j][k],L[i][j - 1][k]),
                        L[i][j][k - 1])

    return L[len(first_sequence)][len(second_sequence)][len(third_sequence)]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
