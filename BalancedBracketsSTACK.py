class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        if(self.isEmpty()):
            return False
        return self.stack[-1]

    def pop(self):
        self.stack.pop()

    def getLen(self):
        return len(self.stack)

    def isEmpty(self):
        return self.stack == []


def isBalanced(s):
    stack = Stack()
    for i in s:
        if(i == "{" or i == "[" or i == "("):
            stack.push(i)
        elif(i == "}"):
            if(stack.peek() == "{"):
                stack.pop()
            else:
                return "NO"

        elif(i == "]"):
            if(stack.peek() == "["):
                stack.pop()
            else:
                return "NO"

        elif(i == ")"):
            if(stack.peek() == "("):
                stack.pop()
            else:
                return "NO"
    if(stack.getLen()):
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        s = input()  # [({})]  [{(]}]
        print(isBalanced(s))
