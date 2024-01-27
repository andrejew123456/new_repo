####   Dekoratory   ####

def my_decorator(func):
    def wrapper():
        print("Before func.")
        func()
        print("After func.")
    return wrapper


def say_hello():
    print("Hello!")

roll = my_decorator(say_hello)
roll()