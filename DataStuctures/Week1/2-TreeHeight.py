# python3

import sys
import threading
from collections import deque

def findDepth(parent, i, depth):
    if depth[i] != 0:
        return
    if parent[i] ==-1:
        depth[i] = 1
        return

    if depth[parent[i]] == 0:
        findDepth(parent, parent[i], depth)
    depth[i] = depth[parent[i]] + 1

def maxHeight(n, parent):
    depth = [0 for i in range(n)]
    for i in range(n):
        findDepth(parent, i, depth)
    max_height = 0
    for i in range(n):
        max_height = max(max_height, depth[i])

    return max_height

        # maxHeight = 0
        # for vertex in range(self.n):
        #     height = 0
        #     i = vertex
        #     while i != -1:
        #         height += 1
        #         i = self.parent[i]
        #     maxHeight = max(maxHeight, height);
        # return maxHeight;


def main():
    n =int(sys.stdin.readline())
    parent = list(map(int, sys.stdin.readline().split()))
    print(maxHeight(n, parent))

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
threading.Thread(target=main).start()



