from Stack import NewStack

def parenchecker(new_string):
    index = 0
    balanced = True
    mystack = NewStack()

    while index < len(new_string) and balanced:
        symbol = new_string[index]

        if symbol == '(':
            mystack.push(symbol)
        else:
            if mystack.isempty():
                balanced = False
            else:
                mystack.pop()
        index += 1

    if balanced and mystack.isempty():
        return True
    return False

print(parenchecker()'))