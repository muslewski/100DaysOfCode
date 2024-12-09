import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()
        result = function()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{function.__name__} run speed: {elapsed_time}s")
        return result

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i