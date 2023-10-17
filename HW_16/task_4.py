class CustomException(Exception):
    def __init__(self, msg):
        self.my_msg(msg)

    def my_msg(self, msg):
        with open("logs.txt", "w") as file:
            file.write(msg)

raise CustomException("Wrong")