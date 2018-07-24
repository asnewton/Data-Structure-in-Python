from Stack import NewStack

def parenchecker(symbol_string):
    index = 0
    balanced = True
    myStack = NewStack()

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]

        if symbol == '{[(':
            myStack.push(symbol)
        else:
            if myStack.isempty():
                balanced = False
            else:
                top = myStack.pop()
                if not matchSymbol(top, symbol):
                    balanced = False

        index += 1

    if balanced and myStack.isempty():
        return True
    return False

def matchSymbol(open, close):
    openSymbol = '{[('
    closeSymbol = ')]}'
    return openSymbol.index(open) == closeSymbol.index(close)

print(parenchecker('{{([][])}()}'))
print(parenchecker('{[()]}'))