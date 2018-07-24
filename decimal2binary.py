from Stack import NewStack

def divide_by_2(dec_num):
    myStack = NewStack()

    while dec_num > 0:
        remainder = dec_num % 2
        myStack.push(remainder)
        dec_num = dec_num // 2

    binary_string = ""
    while not myStack.isempty():
        binary_string = binary_string + str(myStack.pop())

    return binary_string

print(divide_by_2(10))
