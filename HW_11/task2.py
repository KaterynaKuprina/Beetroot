import os
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("data_path", help="Phonebook file path")
args = parser.parse_args()

current_dir = os.path.dirname(os.path.realpath(file))

PHONEBOOK = {}

datafile_path = os.path.join(current_dir, "data", (args.data_path + ".json"))


def create_phonebook():
    first_name = input("Write your first name pls: ")
    second_name = input("Write your second name pls: ")
    full_name = first_name + " " + second_name
    phone_number = input("Write your phone number pls: ")
    city = input("Write your city pls: ")

    if phone_number:
        PHONEBOOK[phone_number] = {
            "first_name": first_name,
            "second_name": second_name,
            "full_name": full_name,
            "phone_number": phone_number,
            "city": city
        }


if os.path.exists(datafile_path):
    with open(datafile_path, "r") as file:
        PHONEBOOK = json.load(file)

create_phonebook()

with open(datafile_path, "w") as file:
    json.dump(PHONEBOOK, file, indent=4)

input()