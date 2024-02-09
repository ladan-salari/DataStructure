def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def maximum_value(database):
    numbers = []
    operations = []
    for i in range(0, len(database), 2):
        numbers.append(int(database[i]))
    for j in range(1, len(database), 2):
        operations.append(database[j])
    m = [[0 for col in range(len(numbers)+1)] for row in range(len(numbers)+1)]
    M = [[0 for col in range(len(numbers)+1)] for row in range(len(numbers)+1)]

    for i in range(1, len(numbers)+1):
        m[i][i] = numbers[i-1]
        M[i][i] = numbers[i-1]
    for s in range(1, len(numbers)):
        for i in range(1, len(numbers) +1 -s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i,j, m, M, operations)
    return M[1][len(numbers)]



def MinAndMax(i, j, m, M, operations):
    min_fun = float('+inf')
    max_fun = float('-inf')
    for k in range (i, j):
        a = evaluate(M[i][k], M[k+1][j], operations[k-1])
        b = evaluate(M[i][k], m[k+1][j], operations[k-1])
        c = evaluate(m[i][k], M[k+1][j], operations[k-1])
        d = evaluate(m[i][k], m[k+1][j], operations[k-1])
        min_fun = min(min_fun, a, b, c, d)
        max_fun = max(max_fun, a, b, c, d)
    return min_fun, max_fun

    # write your code here



if __name__ == "__main__":

    print(maximum_value(input()))
