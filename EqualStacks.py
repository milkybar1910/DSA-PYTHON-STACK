#!/bin/python3
class Stack:

    def __init__(self):
        self.stack = []
        self.total = 0

    def push(self, item):
        if(self.isEmpty()):
            self.total = item
            self.stack.append(item)
        else:
            self.total += item
            self.stack.append(item)

    def isEmpty(self):
        return self.stack == []

    def pop(self):
        self.total -= self.stack.pop()


def equalStacks(h1, h2, h3):

    s1 = Stack()
    for i in h1[::-1]:
        s1.push(i)

    s2 = Stack()
    for i in h2[::-1]:
        s2.push(i)

    s3 = Stack()
    for i in h3[::-1]:
        s3.push(i)

    while((s1.total != s2.total) or (s1.total != s3.total) or (s2.total != s3.total)):
        if(s1.total > s2.total or s1.total > s3.total):
            s1.pop()
        elif(s2.total > s3.total):
            s2.pop()
        else:
            s3.pop()

    return s1.total


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n1 = int(first_multiple_input[0])
    n2 = int(first_multiple_input[1])
    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    print(equalStacks(h1, h2, h3))
