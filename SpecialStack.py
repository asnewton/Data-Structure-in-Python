class StackNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            print("Empty Stack")
        else:
            print("Not Empty")

    def push(self, item):
        new_node = StackNode(item)
        new_node.next = self.head
        self.head = new_node
        print "pushed to stack :" ,new_node.data

    def pop(self):
        if self.head is None:
            return
        temp = self.head
        self.head = self.head.next
        popped = temp.data
        print "popped item :", popped

    def peek(self):
        print "peeked item :",self.head.data

    def getMidNode(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr != None and fast_ptr.next != None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        print "deleted item :", slow_ptr.data
        slow_ptr.next = slow_ptr.next.next

    def printStack(self):
        temp = self.head
        stack = []
        while temp:
            stack.append(temp.data)
            temp = temp.next
        print(stack)

myS = Stack()
myS.push(1)
myS.push(2)
myS.push(3)
myS.push(4)
myS.push(5)
myS.printStack()
print(myS.getMidNode())
myS.printStack()