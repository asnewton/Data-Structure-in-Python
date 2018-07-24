from Stack import NewStack

def to_postfix(infix):
    precednce = {}
    precednce["*"] = 3
    precednce["/"] = 3
    precednce["+"] = 2
    precednce["-"] = 2
    precednce["("] = 1

    op_stack = NewStack()
    postfix_list =[]
    token_list = infix.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top = op_stack.pop()

            while top != "(":
                postfix_list.append(top)
                top = op_stack.pop()
        else:
            while (not op_stack.isempty()) and (precednce[op_stack.peek()] >= precednce[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.isempty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)


print(to_postfix("A * B + C * D"))
print(to_postfix("( A + B ) * ( C + D )"))