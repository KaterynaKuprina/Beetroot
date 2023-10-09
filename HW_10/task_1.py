# Task_1.1
new_list = [1, 2, 3, 4]


def oops(i):
    print(new_list[i])


def oops_again(i):
    try:
        oops(i)
    except IndexError:
        print("Oops, i did it again")


oops_again(6)

# Task_1.2
my_dict = {'1': 'one', '2': 'two'}


def oops(i):
    print(my_dict[i])


def oops_again(i):
    try:
        oops(i)
    except IndexError:
        print("Oops, i did it again")


oops_again(6)