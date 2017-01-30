# Binary puzzle solver for manually (hard-coded) inserted puzzles
import numpy as np

bp_size = 6
bp = np.array([[1, -1, 1, -1, -1, 1],
               [-1, -1, -1, -1, 0, -1],
               [-1, 0, -1, -1, -1, -1],
               [-1, -1, -1, -1, 0, -1],
               [1, -1, -1, 1, -1, -1],
               [-1, -1, 0, -1, -1, -1]])


def copy_grid():
    array = bp[:]
    return array


def get_free_spot(): #re-implement to be more python like
    if bp[bp == -1].size == 0:
        return -1
    for i in range(0, bp_size):
        for j in range(0, bp_size):
            if bp[i, j] == -1:
                return [i, j]


def row_conflict(i, j, num):
    row = bp[i]
    if row[row == num].size >= bp_size/2:
        return True
    # if

def col_conflict(i, j, num):
    col = bp[:,j]


def gives_conflict(i, j, num):
    return row_conflict(i, j, num) and col_conflict(i, j, num)

# row_conflict(1,2,0)
# col_conflict(1,2,0)

index = get_free_spot()
print(str(index[0]) + ' ' + str(index[1]))

# a = np.array([[1,2,3], [4,5,6], [5,5,9]])
# print(a)
# print('')
# b = a
# print(b)

#
# def is_solved():
#     return bp[bp == -1].size == 0

# def check_opposite():
#     changes = True
#     while changes:
#         changes = False
#         for i in range(0, bp_size - 2):
#             for j in range(0, bp_size):
#                 if bp[i,j] != -1:
#                     if bp[i,j] == bp[i+2,j] and bp[i+1,j] == -1:
#                         bp[i+1,j] = get_inverse(bp[i,j])
#                         changes = True
#
#         for i in range(0, bp_size):
#             for j in range(0, bp_size - 2):
#                 if bp[i,j] != -1:
#                     if bp[i,j] == bp[i,j+2] and bp[i,j+1] == -1:
#                         bp[i,j+1] = get_inverse(bp[i,j])
#                         changes = True
#
#
# def get_inverse(num):
#     if num == 0:
#         return 1
#     elif num == 1:
#         return 0
#
            #
# def check_near():
#     print('hello')