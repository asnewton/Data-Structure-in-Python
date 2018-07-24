
class NewStack:

    stack = []

    """initialize satck"""
    def __init__(self):
        self.stack = []

    """check weather stack is empty or note"""
    def isempty(self):
        if self.stack == []:
            return True
        return False

    """insert an item into stack"""
    def push(self, item):
        self.stack.append(item)

    """delete last element and return it"""
    def pop(self):
        return self.stack.pop()

    """returns the last element"""
    def peek(self):
        return self.stack[len(self.stack) - 1]

    """returns the size of stack"""
    def size(self):
        return len(self.stack)

    """print the element of stack"""
    def printstack(self):
        return self.stack


stack_1 = NewStack()
stack_1.push('Ahmad')
stack_1.push(1998)
stack_1.push('Falak')
print(stack_1.size())
print(stack_1.isempty())
print(stack_1.size())
print(stack_1.printstack())
stack_1.push('Adaa')
stack_1.push('2000')
print(stack_1.printstack())
print(stack_1.pop())
print(stack_1.peek())
