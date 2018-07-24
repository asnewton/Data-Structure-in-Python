""" Linked List implementation of Stack """

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

if __name__=='__main__':
    my_stack = Stack()
    my_stack.isEmpty()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)
    my_stack.isEmpty()
    my_stack.pop()
    my_stack.peek()