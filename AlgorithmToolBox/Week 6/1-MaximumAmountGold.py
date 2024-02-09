from sys import stdin


def maximum_gold(capacity, weights):
    temp_weight=[[0 for col in range(capacity+1)] for row in range(len(weights)+1)]
    for i in range(1, len(weights)+1):
        for w in range(1, capacity+1):
            temp_weight[i][w] = temp_weight[i-1][w]
            if weights[i-1] <= w:
                weight = temp_weight[i-1][w-weights[i-1]] + weights[i-1]
                if temp_weight[i][w] < weight:
                    temp_weight[i][w] = weight
    return temp_weight[len(weights)][capacity]



if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))