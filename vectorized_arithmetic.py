import numpy as np
import copy


def array_add(l, addend):
    l_copy = copy.deepcopy(l)
    num_rows = len(l)
    num_cols = len(l[0])
    for i in range(num_rows):
        for j in range(num_cols):
            l_copy[i][j] += addend
    return l_copy


if __name__ == '__main__':
    l = [[y + i * 5 for y in range(5)] for i in range(4)]
    print(l)

    print(array_add(l, 10))

    a = np.arange(20).reshape(5, 4)
    print(a)
    print(a + 10)

