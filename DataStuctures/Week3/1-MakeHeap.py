# python3
import math

def Parent(index):
    return math. floor((index-1)/2)

def LeftChild(index):
    return 2*index + 1

def RightChild(index):
    return 2*index + 2

def SiftDown(index, data, swaps):
    minindex = index
    l = LeftChild(index)
    r = RightChild(index)
    size = len(data)
    if l < size and data[l] < data[minindex]:
        minindex = l

    if r < size and data[r] < data[minindex]:
        minindex = r
    if index != minindex:
        swaps.append((index, minindex))
        data[index], data[minindex] = data[minindex], data[index]
        SiftDown(minindex, data, swaps)

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    swaps =[]
    size = len(data)
    for i in range (size//2, -1, -1):
        SiftDown(i, data, swaps)
    return swaps



def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data, )

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
