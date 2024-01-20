####   Dekoratory   ####

def my_decorator(func):
    def wrapper():
        print("Before func.")
        func()
        print("After func.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()