import numpy as np
import matplotlib   .pyplot as plt


def rectangle_circumference(a, b):
    return 2*a + 2*b
def rectangle_area(a, b):
    return a*b


def task():
    value_count = 20

    # initializing vectors of 20 random values scaled from 0 to 1
    random_sides_a = np.random.rand(value_count)
    random_sides_b = np.random.rand(value_count)

    # scaling and shifting the vectors to range from 1 to 10
    random_sides_a = (random_sides_a * 9) + 1
    random_sides_b = (random_sides_b * 9) + 1

    # initializing empty lists
    circumferences = []
    areas = []

    for i in range(value_count):
        # appending values to lists
        circumferences.append(rectangle_circumference(random_sides_a[i], random_sides_b[i]))
        areas.append(rectangle_area(random_sides_a[i], random_sides_b[i]))

    # utilizing zip to iterate over several collections at the same time
    for a, b, circ, area in zip(random_sides_a, random_sides_b, circumferences, areas):
        print(f'sides {a} and {b}, circumference {circ}, area {area}')

    # printing newline to separate output logs
    print('\n')
    # obtaining order of indices by ascending value
    order = np.argsort(areas)

    # utilizing enumerate() to get a helper variable for iteration number
    for iteration_no, index in enumerate(order):
        print(f'{iteration_no} place, rectangle #{index}, area {areas[index]}')

    plt.plot(sorted(areas))
    plt.title('distribution of areas of rectangles')
    plt.xlabel('sample #')
    plt.ylabel('area [units^2]')
    plt.grid()
    plt.show()
    plt.plot(sorted(circumferences))
    plt.title('distribution of circumferences of rectangles')
    plt.xlabel('sample #')
    plt.ylabel('circumference [units^2]')
    plt.grid()
    plt.show()