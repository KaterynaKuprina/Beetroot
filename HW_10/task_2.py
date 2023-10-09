def operation():

    try:
        a = float(input("The first number is: "))
        b = float(input("The second number is: "))
        result = (a**2)/b
        return result
    except ValueError as v:
        print(f"Error is defined {v}")
    except ZeroDivisionError as z:
        print(f"Error is defined {z}")


print(operation())




