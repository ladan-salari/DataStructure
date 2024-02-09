def compute_operations(n):
    operation=  [0]*(n+1)
    operation[1] = 1
    for m in range(2, n+1):
        indices = [m-1]
        if m %2 ==0:
            indices.append(m//2)
        if m%3 ==0:
            indices.append(m//3)
        min_operation = min(operation[x] for x in indices)
        operation[m] = min_operation + 1
    ptr = n
    optimal_seq = [n]
    while ptr!=1:
        candidate =[ptr-1]
        if ptr%2==0:
            candidate.append(ptr//2)
        if ptr%3==0:
            candidate.append(ptr//3)

        ptr = min([(c, operation[c]) for c in candidate], key=lambda x:x[1])[0]
        optimal_seq.append(ptr)
    return optimal_seq[::-1]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)