def make_operation(operator, *args):

    result = args[0]
    if operator == '+':
        for num in args[1:]:
            result += num
    elif operator == '-':
        for num in args[1:]:
            result -= num
    elif operator == '*':
        for num in args[1:]:
            result *= num
    elif operator not in ('+', '-', '*'):
                result ("Wrong way")

    return(f"Result is {result}")

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))