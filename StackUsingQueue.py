class NewQueue:

    def __init__(self):
        self.Queue = []

    def isEmpty(self):
        return self.Queue == []

    def enqueue(self, item):
        self.Queue.insert(0, item)

    def dequeue(self):
        return self.Queue.pop()

    def size(self):
        return len(self.Queue)

    def __iter__(self):
        for item in self.Queue:
            print(item)

class Stack:

    myQ1 = NewQueue()
    myQ2 = NewQueue()

    def push(self, item):
        Stack.myQ1.enqueue(item)

    def pop(self):
        if Stack.myQ1.isEmpty() is True:
            return
        else:
            while Stack.myQ1.size() != 1:
                Stack.myQ2.enqueue(Stack.myQ1.dequeue())
            print " popped item :", Stack.myQ1.dequeue()




myS = Stack()
myS.push(1)
myS.push(2)
myS.push(3)
myS.pop()
print(myS.myQ1.__iter__())





