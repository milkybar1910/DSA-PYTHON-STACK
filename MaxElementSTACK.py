class Stack:

    def __init__(self):
        self.__STACK = []

    def push(self, item):
        if(self.__STACK):
            self.__STACK.append(max(self.peek(), item))
        else:
            self.__STACK.append(item)

    def pop(self):
        self.__STACK.pop()

    def peek(self):
        return self.__STACK[-1]

    def getMax(self):
        return self.peek()


if __name__ == '__main__':
    stack = Stack()
    Operations = int(input())
    for i in range(0, Operations):
        operationArray = list(map(int, input().strip().split()))
        if(operationArray[0] == 1):
            stack.push(operationArray[1])
        elif(operationArray[0] == 2):
            stack.pop()
        else:
            print(stack.getMax())
