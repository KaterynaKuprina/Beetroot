import os

file_path = "myfile.txt"

with open(file_path, "w") as file:
    file.write("Hello file world!\n")

with open(file_path, "r") as file:
    print(file.read())