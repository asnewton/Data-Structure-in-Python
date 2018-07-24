""" Implement Queue using Stacks """

from Stack import NewStack

class Queue:

    myStack1 = NewStack()
    myStack2 = NewStack()

    def enQueue(self, item):
        Queue.myStack1.push(item)

    def deQueue(self):
        while Queue.myStack1.isempty() is not True:
            Queue.myStack2.push(Queue.myStack1.pop())
        print "deleted item :", Queue.myStack2.pop()

    def printQ(self):
        while Queue.myStack1.isempty() is not True:
            print(Queue.myStack1.pop())



myQ = Queue()
myQ.enQueue(1)
myQ.enQueue(2)
myQ.enQueue(3)
myQ.deQueue()
