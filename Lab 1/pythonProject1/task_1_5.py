import math

def task():
    print("Running task_1_5: ")
    _solve(3, -4, -2)

def _solve(a, b, c):
    delta = pow(b, 2) - (4 * a * c)
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"Root 1 = {root1}")
    print(f"Root 2 = {root2}")
