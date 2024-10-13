import math

def task():
    print("Running task_1_4: ")
    _solve()

def _solve():
    delta = math.sqrt( (4 * 4) - (4 * (-2) * 3) )
    print(delta)
    root1 = (4 + delta) / (2 * 3)
    root2 = (4 - delta) / (2 * 3)

    print(f"Root 1 = {root1}")
    print(f"Root 2 = {root2}")
