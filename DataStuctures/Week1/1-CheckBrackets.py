# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    opening_list = ['(','[', '{']
    closing_list = [')', ']', '}']
    for i, next in enumerate(text):
        if next in opening_list:
            opening_brackets_stack.append([i,next])
            # print(opening_brackets_stack)
            # Process opening bracket, write your code here
        else:
            if next in closing_list:
                if len(opening_brackets_stack) == 0:
                    return i +1
                top = opening_brackets_stack.pop()
                if (top[1] =='[' and next !=']') or (top[1]=='{' and next !='}') or (top[1] =='(' and next !=')'):
                    return i+1



    # print(len(opening_brackets_stack))
    if len(opening_brackets_stack) ==0:
        return "Success"
    else:
        return opening_brackets_stack[-1][0] + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    print (mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()