# q5_timer_decorator.py
import time
import random

def timer(func):                 # decorator must be a function
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print("Time taken:", round(end - start, 4), "seconds")
        return result
    return wrapper

@timer
def do_work():
    duration = random.uniform(0.5, 1.5)
    print("Sleeping for ~", round(duration, 2), "seconds...")
    time.sleep(duration)

# run once
do_work()
