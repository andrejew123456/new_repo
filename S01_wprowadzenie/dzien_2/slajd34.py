####   Dekoratory   ####
import datetime
import time


def my_decorator(func):
    def wrapper():
        print("Before func.")
        print(datetime.datetime.now())
        func()
        time.sleep(2)
        print("After func.")
        print(datetime.datetime.now())
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")


say_hello()
# my_decorator(say_hello)()
