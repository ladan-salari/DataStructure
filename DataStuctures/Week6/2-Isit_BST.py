#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def inOrder(tree):
  i = 0
  result = []
  stack =[]
  while stack or i != -1:
    if i !=-1:
      root = tree[i]
      stack.append(root)
      i = root[1]
    else:
      root = stack.pop()
      result.append(root)
      i = root[2]
  return result



def IsBinarySearchTree(tree, n):
  nodes = inOrder(tree)
  for i in range(1,n):
    if nodes[i] <= nodes[i-1]:
      return False
  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if nodes ==0 or IsBinarySearchTree(tree, nodes):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
