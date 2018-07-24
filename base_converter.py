from Stack import NewStack

def base_converter(decimal_number, base):
    myStack = NewStack()
    myNumber = "0123456789ABCDEF"

    while decimal_number > 0:
        remainder = decimal_number % base
        myStack.push(remainder)
        decimal_number = decimal_number // base

    myString = ""

    while not myStack.isempty():
        myString = myString + myNumber[myStack.pop()]

    return myString

print(base_converter(10, 2))

