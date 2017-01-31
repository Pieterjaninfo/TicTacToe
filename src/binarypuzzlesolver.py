# Binary puzzle solver for manually (hard-coded) inserted puzzles using recursion
import numpy as np

DMAX = [0, 1]
bp_size = 6
bp = np.array([[1, -1, 1, -1, -1, 1],
               [-1, -1, -1, -1, 0, -1],
               [-1, 0, -1, -1, -1, -1],
               [-1, -1, -1, -1, 0, -1],
               [1, -1, -1, 1, -1, -1],
               [-1, -1, 0, -1, -1, -1]])


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
    return False


def row_conflict(i, j, num):
    return array_conflict(bp[i], j, num)


def col_conflict(i, j, num):
    return array_conflict(bp[:,j], i, num)


def gives_conflict(i, j, num):
    return row_conflict(i, j, num) or col_conflict(i, j, num)


def solve():
    if get_free_spot() != -1:
        index_spot = get_free_spot()
        row = index_spot[0]
        col = index_spot[1]

        for num in DMAX:
            if not gives_conflict(row, col, num):
                bp[row, col] = num
                solve()
                bp[row, col] = -1
    else:
        print(bp)
        exit(0)


print(bp)
print('')
solve()

# a=bp[1]
# b=bp[:,1]
#
# print(a)
# print('')
# print(b)
#
# print(b[b == 1].size)