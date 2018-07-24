from Stack import NewStack

my_stack = NewStack()

def to_str(input_num, base):
    convert_string = "0123456789ABCDEF"

    while input_num > 0:
        if input_num < base:
            my_stack.push(convert_string[input_num])

        else:
            my_stack.push(convert_string[input_num % base])

        input_num = input_num // base

    result = " "

    while not my_stack.isempty():
        result = result + str(my_stack.pop())

    return result

print(to_str(10, 2))



