# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    queue = deque()
    #create queue for the first m elements:
    for i in range(m):
        while queue and sequence[i] >= sequence[queue[-1]]:
            queue.pop()
        queue.append(i)
    maximums.append(sequence[queue[0]])
    
    for i in range(m, len(sequence)):
        while queue and queue[0] <= i-m:
            queue.popleft()
        while queue and sequence[i] >= sequence[queue[-1]]:
            queue.pop()
        queue.append(i)
        maximums.append(sequence[queue[0]])
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

