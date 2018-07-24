from Stack import NewStack

def infixtopostfix(infix_exp):

    operator_stack = NewStack()
    postfix_output = []
    token_list = infix_exp.split()

    precedence = {'(' : 1,'+' : 2, '-' : 2, '*' : 3, '/' : 3}
    for token in token_list:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfix_output.append(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            top = operator_stack.pop()
            while top != '(':
                postfix_output.append(top)
                top = operator_stack.pop()
        else:
            while (not operator_stack.isempty()) and (precedence[operator_stack.peek()] >= precedence[token]):
                postfix_output.append(operator_stack.pop())
            operator_stack.push(token)

    while not operator_stack.isempty():
        postfix_output.append(operator_stack.pop())

    return " ".join(postfix_output)

print(infixtopostfix("A * B + C * D"))
