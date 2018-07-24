from Stack import NewStack


def postfix_eval(postfix_expr):
    op_stack = NewStack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token in "0123456789":
            op_stack.push(token)
        else:
            op2 = op_stack.pop()
            op1 = op_stack.pop()
            result = do_math(token, op1, op2)
            op_stack.push(int(result))
    return op_stack.pop()


def do_math(operator, op1, op2)
    if operator == "*":
        return op1 * op2

    elif operator == "/":
        return op1 / op2

    elif operator == "+":
        return op1 + op2

    else:
        return op1 - op2

print(postfix_eval('7 8 + 3 2 + /'))
