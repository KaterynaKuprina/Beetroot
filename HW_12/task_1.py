def our_func():
    a = 0
    b = 1
    print(locals())
    x = locals()
    return len(x)

print(our_func())