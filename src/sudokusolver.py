import numpy as np
import itertools

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
amount_solutions = 0

sp = np.array([                 # World's hardest sudoku puzzle
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
])

sp_size = sp[0].size


def get_free_spot():
    if sp[sp == 0].size > 0:
        for i, j in itertools.product(range(0, sp_size), range(0, sp_size)):
            if sp[i, j] == 0:
                return [i, j]
    return -1


def row_conflict(i, d):
    row = sp[i]
    return row[row == d].size > 0


def col_conflict(j, d):
    col = sp[:, j]
    return col[col == d].size > 0


def box_conflict(i, j, d):
    row_index = i // 3 * 3
    col_index = j // 3 * 3
    for x, y in itertools.product(range(row_index, row_index + 3), range(col_index, col_index + 3)):
        if sp[x, y] == d:
            return True
    return False


def gives_conflict(i, j, d):
    return row_conflict(i, d) or col_conflict(j, d) or box_conflict(i, j, d)


def solve():
    global amount_solutions
    if get_free_spot() != -1:
        spot_index = get_free_spot()
        row = spot_index[0]
        col = spot_index[1]

        for d in digits:
            if not gives_conflict(row, col, d):
                sp[row, col] = d
                solve()
                sp[row, col] = 0
    else:
        amount_solutions += 1
        print(sp)       # Print the soltion with empty line
        print()


def run():
    print('The given sudoku will now be solved.')
    print(sp)
    print('\n The solutions:')
    solve()
    print('\nThe puzzle has %d solutions.' % amount_solutions)


run()
