def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1



