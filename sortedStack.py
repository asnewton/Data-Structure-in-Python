from Stack import NewStack

mystack1 = NewStack()
mystack2 = NewStack()
mystack1.push(3)
mystack1.push(5)
mystack1.push(2)
mystack1.push(9)
mystack1.push(6)
print("Unsorted Stack")
print(mystack1.printstack())
def sortstack():
    while not mystack1.isempty():
        popped = mystack1.pop()
        while not mystack2.isempty() and mystack2.peek() > popped:
            mystack1.push(mystack2.pop())
        mystack2.push(popped)


sortstack()
print(mystack2.printstack())




