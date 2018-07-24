# Python program to print next greater element using stack
# Stack is import from the Stack.py file

from Stack import NewStack


def nextgreaterelement(array):

    mystack = NewStack()
    item = 0
    mystack.push(array[0])

    for i in range(1,len(array)):
        item = array[i]
        if mystack.isempty() is False:
            popped = mystack.pop()
            while popped < item:
                print popped, "-->", item
                if mystack.isempty() is True:
                    break
                popped = mystack.pop()
            if popped > item:
                mystack.push(popped)
        mystack.push(item)

    while mystack.isempty() is False:
        popped = mystack.pop()
        item = -1
        print popped,"-->", item


print(nextgreaterelement([11, 12, 21, 3]))


