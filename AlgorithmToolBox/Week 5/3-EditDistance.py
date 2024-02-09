def edit_distance(first_string, second_string):
    if len(first_string) ==0:
        return len(second_string)
    if len(second_string) ==0:
        return len(first_string)

    D = [[0 for col in range(len(second_string)+1)] for row in range(len(first_string)+1)]
    for i in range(len(first_string)+1):
        D[i][0] = i
    for j in range (len(second_string)+1):
        D[0][j] = j
    for j in range(1, len(second_string)+1):
        for i in range(1, len(first_string)+1):
            inseration = D[i][j-1] +1
            deletion = D[i-1][j] +1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1] +1
            if first_string[i-1]==second_string[j-1]:
                D[i][j] = min(inseration, deletion, match)
            else:
                D[i][j] =min(inseration, deletion, mismatch)

    return int(D[len(first_string)][len(second_string)])


if __name__ == "__main__":
    print(edit_distance(input(), input()))
