def arg_rules(type_: type, max_length: int, contains: list):
    def decoraror(func):
        def wrapper(*args, **kwargs):
            my_string = func(*args, **kwargs)
            print(my_string)
            for item in args:
                if isinstance(item, type_) and len(item) <= max_length and not contains in args:
                    return my_string
                else:
                    return False

        return wrapper

    return decoraror


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan1(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


create_slogan1('johndoe05@gmail.com')

assert create_slogan1('johndoe05@gmail.com') is False

assert create_slogan1('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'