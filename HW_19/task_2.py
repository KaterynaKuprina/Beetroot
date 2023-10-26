def my_range(*args):
    start, stop, step = 0, None, 1

    if len(args) == 1:
        stop = args[0]
    elif len(args) == 2:
        start, stop = args
    elif len(args) == 3:
        start, stop, step = args
        if step < 0:
            start, stop = stop, start
    else:
        raise TypeError(f'my_range expected at most 3 arguments, got {len(args)}')

    current = start
    while (stop is None) or (current < stop if step > 0 else current > stop):
        yield current
        current += step