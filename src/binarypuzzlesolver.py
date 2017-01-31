# Binary puzzle solver for manually (hard-coded) inserted puzzles using recursion
import numpy as np
from time import time

digits = [0, 1]
bp1 = np.array([[1, -1, 1, -1, -1, 1],      # 6x6 binary puzzle
               [-1, -1, -1, -1, 0, -1],
               [-1, 0, -1, -1, -1, -1],
               [-1, -1, -1, -1, 0, -1],
               [1, -1, -1, 1, -1, -1],
               [-1, -1, 0, -1, -1, -1]])

bp = np.array([                             # 8x8 binary puzzle
    [-1,0,-1,-1,1,-1,0,-1],
    [-1,-1,-1,-1,-1,-1,-1,1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,0,-1,-1,1,-1],
    [-1,-1,1,-1,1,-1,-1,0],
    [1,-1,-1,-1,1,-1,-1,-1],
    [1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,0,-1]
])

bp2 = np.array([                            # 14x14 binary puzzle
    [-1,-1,0,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1],
    [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,0,-1,1,-1,-1,-1,-1,-1],
    [-1,-1,-1,1,1,-1,-1,-1,-1,0,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1],
    [-1,-1,0,-1,-1,-1,0,-1,1,1,-1,-1,1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1],
    [-1,-1,0,0,-1,-1,1,-1,1,0,-1,-1,-1,0],
    [-1,-1,1,-1,-1,0,-1,1,1,-1,-1,-1,-1,-1],
    [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,0],
    [-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,-1,0],
    [1,-1,1,-1,-1,0,-1,-1,-1,1,0,-1,-1,-1],
    [1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,0],
    [-1,-1,1,-1,1,1,-1,1,-1,-1,0,-1,1,-1]
])

bp_size = bp[0].size


def get_free_spot():    # Re-implement to be more python like
    if bp[bp == -1].size == 0:
        return -1
    for i in range(0, bp_size):
        for j in range(0, bp_size):
            if bp[i, j] == -1:
                return [i, j]


def array_conflict(array, j, num):
    if array[array == num].size == bp_size/2:
        return True
    if j == 0 and array[j + 1] == array[j + 2] == num:
        return True
    elif j == bp_size - 1 and array[bp_size - 2] == array[bp_size - 3] == num:
        return True
    elif j != 0 and j != bp_size - 1 and array[j - 1] == array[j + 1] == num:
        return True
    elif j > 1 and array[j - 1] == array[j - 2] == num:
        return True
    elif j < bp_size - 2 and array[j + 1] == array[j + 2] == num:
        return True
    return False


def row_conflict(i, j, num):
    return array_conflict(bp[i], j, num)


def col_conflict(i, j, num):
    return array_conflict(bp[:,j], i, num)


def row_duplicate(array, i):
    row = array[i]
    if row[row == -1].size == 0:
        for x in range(0, bp_size):
            if x != i and np.array_equal(row, array[x]):
                return True
    return False


def col_duplicate(array, j):
    col = array[:,j]
    if col[col == -1].size == 0:
        for y in range(0, bp_size):
            if y != j and np.array_equal(col, array[:,y]):
                return True
    return False


def is_duplicate(i, j, num):
    array = np.copy(bp)
    array[i, j] = num
    return row_duplicate(array, i) or col_duplicate(array, j)


def gives_conflict(i, j, num):
    return row_conflict(i, j, num) or col_conflict(i, j, num) or is_duplicate(i, j, num)


def solve():
    if get_free_spot() != -1:
        index_spot = get_free_spot()
        row = index_spot[0]
        col = index_spot[1]

        for num in digits:
            if not gives_conflict(row, col, num):
                bp[row, col] = num
                solve()
                bp[row, col] = -1
    else:
        print(bp)


def run():
    print('The solver will now solve the binary puzzle: ')
    print(bp)
    print('\nThe solved puzzle is: ')
    begin = time()
    solve()
    print('\nSolving took %f seconds.' % (time() - begin))


run()
