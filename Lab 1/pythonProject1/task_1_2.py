import random

def task():
    print("Running task_1_2: ")
    _loop_function()

def _loop_function():
    a = 0
    while random.random() < 0.8:
       a += 1
    print(f"Number of iterations = {a}")

    lucky_ratio = pow(0.8, a)
    if lucky_ratio < 0.5:
        print("Lucky")
    else:
        print("Unlucky")