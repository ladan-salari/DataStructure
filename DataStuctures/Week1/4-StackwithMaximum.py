#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max_numbers = []

    def Push(self, a):
        if not self.max_numbers:
            self.max_numbers.append(a)
        if a >= self.max_numbers[-1]:
            self.max_numbers.append(a)
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.top = self.__stack.pop()
        if self.top == self.max_numbers[-1]:
            self.max_numbers.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.max_numbers[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
