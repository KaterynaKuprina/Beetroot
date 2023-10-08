def first_func():
    def second_func(y, z):
        return y + z

    return second_func


print(first_func()(3, 4))