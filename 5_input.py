# task 1
import random
user_number = int(input("Give me a number: "))
comp_number = random.randint(1,10)
if user_number == comp_number and user_number in range(1, 10):
    print("U r lucky man!")
elif user_number != comp_number and user_number in range(1, 10):
    print("U own me 1000$")
else:
    print("Realy? Is it number in range 1 and 10? Read the rules!")


# task 2
user_name = input("Give me your name: ")
user_age = int(input("Give me your birthday: "))
user_next_age = str(user_age + 1)
print("Hello " + user_name + ", on your next birthday you’ll be " + user_next_age + "years")

#task 3
import random
while True:
    user_word = str(input("Write your word or 'exit' to quit: ").lower())
    if user_word == 'exit':
        print('Bye')
        break
    else:
        user_list = list(user_word)
        for _ in range(5):
            random.shuffle(user_list)
            print(''.join(user_list))