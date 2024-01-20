import time
def measuretime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time needed: {end - start} seconds")
    return wrapper
@measuretime
def wastetime():
    sum([i**2 for i in range(1000000)])

@measuretime
def suma(a, b):
    return a + b

@measuretime
def sleep(sec):
    time.sleep(sec)

wastetime()

sleep(20)