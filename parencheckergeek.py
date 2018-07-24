from Stack import NewStack

def parenchecker(paren_string):

    index = 0
    balanced = True
    mystack = NewStack()

    while index < len(paren_string) and balanced:
        symbol = paren_string[index]
        if symbol == '(' or symbol == '[' or symbol == '{':
            mystack.push(symbol)
        else:
            if symbol == ')' or symbol == ']' or symbol == '}':
                item = mystack.pop()
                if item == '(' or item == ']' or item == '}':
                    balanced = True
                balanced = False
        return balanced
        index += 1


print(parenchecker('{{([][])}()}'))
