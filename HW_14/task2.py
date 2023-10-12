def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            our_str = func(*args, **kwargs)
            for word in words:
                our_str = our_str.replace(word, "*")
            return our_str

        return wrapper

    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW !"


print(create_slogan("Dima"))


