class Stack():

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def getStack(self):
        return self.stack

     # @classmethod
    def isEmpty(self):
        return self.stack == []

    def peek(self):
        if(not self.isEmpty()):
            return self.stack[-1]


myStack = Stack()
myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")
myStack.pop()
print(myStack.peek())
print(myStack.peek())
