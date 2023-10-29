import os
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_path", help="Phonebook file path")
args = parser.parse_args()
current_dir = os.path.dirname(os.path.realpath(__file__))
datafile_path = os.path.join(current_dir, (args.data_path + ".json"))
PHONEBOOK = {}
if not os.path.exists(datafile_path):
    with open(datafile_path, "w") as file:
        json.dump(PHONEBOOK, file)


def create_phonebook():
    first_name = input("Write your first name pls: ")
    second_name = input("Write your second name pls: ")
    phone_number = input("Write your phone number pls: ")
    city = input("Write your city pls: ")
    if phone_number:
        PHONEBOOK[phone_number] = {
            "first_name": first_name,
            "second_name": second_name,
            "phone_number": phone_number,
            "city": city
        }
    with open(datafile_path, "a") as file_obj:
        json.dump(PHONEBOOK, file_obj, indent=4)


def update_phonebook():
    phone_number = input("Write your phone number for update: ")
    first_name = input("Write your first name for update: ")
    second_name = input("Write your second name for update: ")
    city = input("Write your city for update: ")
    new_phonebook = {}
    if phone_number:
        new_phonebook[phone_number] = {
            "first_name": first_name,
            "second_name": second_name,
            "phone_number": phone_number,
            "city": city
        }
        PHONEBOOK.update(new_phonebook)
        with open(datafile_path, "w") as file:
            json.dump(PHONEBOOK, file, indent=4)


def search_phonebook():
    phone_number = input("Write the phone number: ")
    if phone_number in PHONEBOOK:
        return PHONEBOOK[phone_number]
    return "This number is not defined"


def search_first_name():
    first_name = input("Write the first name: ")
    return {key: value for key, value in PHONEBOOK.items() if first_name in value["first_name"]}


def search_second_name():
    second_name = input("Write the second name: ")
    return {key: value for key, value in PHONEBOOK.items() if second_name in value["second_name"]}


def search_full_name():
    full_name = input("Write the full name: ")
    return {key: value for key, value in PHONEBOOK.items() if
            full_name in (value["first_name"] + " " + value["second_name"])}


def search_city():
    city = input("Write the city: ")
    return {key: value for key, value in PHONEBOOK.items() if city in value["city"]}


def delete_phonebook():
    phone_number = input("Say goodbye to your number: ")
    if phone_number in PHONEBOOK:
        del PHONEBOOK[phone_number]
        with open(datafile_path, "w") as file:
            json.dump(PHONEBOOK, file, indent=4)
        print(f"Phone number {phone_number} deleted.")
    else:
        print(f"Phone number {phone_number} not found in the phonebook.")


START_PHONEBOOK = """
Enter 1 if you want to add new contact
Enter 2 if you want to search by first name
Enter 3 if you want to search by second name
Enter 4 if you want to search by full name
Enter 5 if you want to search by city
Enter 6 if you want to search by phone number
Enter 7 if you want to update a contact
Enter 8 if you want to delete a contact
Enter 9 if you want to exit from the phonebook
"""
MENU_PHONEBOOK = {
    "1": create_phonebook,
    "2": search_first_name,
    "3": search_second_name,
    "4": search_full_name,
    "5": search_city,
    "6": search_phonebook,
    "7": update_phonebook,
    "8": delete_phonebook,
    "9": exit
}
ALLOWED_SYMBOLS = [str(item) for item in list(range(1, 10))]
while True:
    print(START_PHONEBOOK)
    user_input = input("Write your number: ")
    if user_input in ALLOWED_SYMBOLS:
        print(MENU_PHONEBOOK[user_input]())
