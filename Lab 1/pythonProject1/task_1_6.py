import numpy as np

def task():
    print("Running task_1_6: ")
    values1 = np.random.rand(20)
    values2 = np.random.rand(20)
    list_l = []
    list_m = []
    _separate(values1, list_l, list_m)
    _separate(values2, list_l, list_m)
    print(f"\nList of values less than 0.5: {list_l}")
    print(f"List of values more or equal 0.5: {list_m}")

    print(f"\nLength of list_l = {len(list_l)}")
    print(f"Length of list_m = {len(list_m)}")

def _separate(list_input, list_less, list_more):
    for i in range(len(list_input)):
        if list_input[i] < 0.5:
            list_less.append(list_input[i])
        else:
            list_more.append(list_input[i])
