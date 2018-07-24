""" Design and Implement Special Stack Data Structure """

from Stack import NewStack

class Operations:

    ActualStack = NewStack()
    AuxillaryStack = NewStack()

    def pushItem(self, item):
        if Operations.ActualStack.isempty() is True:
            Operations.ActualStack.push(item)
            Operations.AuxillaryStack.push(item)
        else:
            Operations.ActualStack.push(item)
            popped = Operations.AuxillaryStack.pop()
            Operations.AuxillaryStack.push(popped)
            if popped > item:
                Operations.AuxillaryStack.push(item)
            else:
                Operations.AuxillaryStack.push(popped)

    def getMin(self):
        print "minimum item:", Operations.AuxillaryStack.pop()


oper = Operations()
oper.pushItem(3)
oper.pushItem(5)
oper.pushItem(6)
oper.pushItem(4)
oper.pushItem(2)


print "Actual Stack:",Operations.ActualStack.printstack()
print "Auxillary Stack:",Operations.AuxillaryStack.printstack()
oper.getMin()

