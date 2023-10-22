import re
class Mail:
    def __init__(self, email: str):
        self.email = email
        self.validate()


    def validate(self):
        current_mail = r'^[a-zA-Z0-9_.+-]+[^_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        our_mail = self.email
        if not re.match(current_mail, our_mail):
            raise ValueError("Not correct mail")


mail_1 = Mail("abc-d@mail.com")
mail_2 = Mail("abc.def@mail.cc")
mail_3 = Mail("abc.def@mail.org")
mail_4 = Mail("aabc-@mail.com")
mail_5 = Mail("abc.def@mail#archive.com")

