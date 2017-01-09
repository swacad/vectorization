import numpy as np
import copy
import timeit
import matplotlib.pyplot as plt


def array_add_1d(l, addend):
    return [x + addend for x in l]


def array_add_2d(l, addend):
    l_copy = copy.deepcopy(l)
    num_rows = len(l)
    num_cols = len(l[0])
    for i in range(num_rows):
        for j in range(num_cols):
            l_copy[i][j] += addend
    return l_copy


if __name__ == '__main__':
    # l = [[y + i * 5 for y in range(5)] for i in range(4)]

    n = [x * 1000 for x in range(1, 11)]
    list_run_times = []
    array_run_times = []

    for i in range(len(n)):
        l = [x for x in range(n[i])]
        a = np.arange(n[i])
        list_run_times.append(timeit.timeit('array_add_1d(l, 10)', number=1000, globals=globals()))
        array_run_times.append(timeit.timeit('a + 10', number=1000, globals=globals()))

    print(list_run_times)
    print(array_run_times)

    plt.plot(n, list_run_times)
    plt.plot(n, array_run_times)
    plt.show()

