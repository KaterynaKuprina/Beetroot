tuple_i = []
tuple_j = []
for i in range(1, 11):
    tuple_i.append(i)
    tuple_j.append(i ** 2)
our_list = [item1 for item2 in (tuple_i, tuple_j) for item1 in item2]
print(our_list)
