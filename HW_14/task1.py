def logger(func):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        return func(*args, **kwargs)

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

print(add(5, 6))
print(square_all(4, 10))

