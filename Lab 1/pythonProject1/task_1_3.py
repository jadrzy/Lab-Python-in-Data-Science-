import random

def task():
    print("Running task_1_3: ")
    _loop_function(0.8)

def _loop_function(threshold):
    a = 0
    while random.random() < threshold:
        a += 1
    print(f"Number of iterations = {a}")

    lucky_ratio = pow(threshold, a)
    if lucky_ratio < 0.5:
        print("Lucky")
    else:
        print("Unlucky")
