# task 1
import random
random_number_list = list(random.randint(1, 20) for _ in range(10))
max_number = random_number_list[0]
i = 1
while i < len(random_number_list):
    if max_number < random_number_list[i]:
        max_number = random_number_list[i]
    i += 1
print(str(random_number_list) + 'The max number is ' +str(max_number))


# task 2
import random
first_list = []
second_list = []
i = 0
while i < 10:
    first_number = random.randint(1,10)
    second_number = random.randint(1,10)
    first_list.append(first_number)
    second_list.append(second_number)
    i += 1
print(list(set(first_list + second_list)))


# task 3
my_list = list(range(1, 100))
my_second_list = []
i = 1
while i < len(my_list):
    number = my_list[i]
    if number % 7 == 0 and number % 5 != 0:
        my_second_list.append(number)
    i += 1
print(my_second_list)