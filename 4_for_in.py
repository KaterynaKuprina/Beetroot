#task 1
my_string = input("Your text: ")
result = my_string[:2] + my_string[-2:]
if len(result) > 2:
    print(my_string)
else:
    print("Empty string")
print(result)


# task 2
user_number = input("Enter phone number: ")
right_number = "Good job! Take a candy, sweetheart"
wrong_number = "Realy? Is it too hard for you?"
if user_number.isdigit() and len(user_number) <= 10:
    print(right_number)
else:
    print(wrong_number)


# task 3
user_answer = int(input("2+2= "))
print("Nerd" if user_answer == 4 else "Go to school")

# task 4

name = "Kateryna"
user_name = input("Spell my name: ")
print(name.lower() == user_name.lower())