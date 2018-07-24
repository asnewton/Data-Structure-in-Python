# Reverse a stack using recursion

from Stack import NewStack

mystack = NewStack()
def reverse():
    if not mystack.isempty():
        temp = mystack.pop()
        reverse()
        insertatbottom(temp)



def insertatbottom(item):
    if mystack.isempty():
        mystack.push(item)
    else:
        temp = mystack.pop()
        insertatbottom(item)
        mystack.push(temp)


insertatbottom(1)
insertatbottom(2)
insertatbottom(3)
print(mystack.printstack())
reverse()
print("after reverse")
print(mystack.printstack())