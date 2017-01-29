BOARD = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

PLAYER1_MARK = 'X'  #Goes first
PLAYER2_MARK = 'O'  #Goes second
HUMAN_PLAYER = ''
COMPUTER_PLAYER = ''


def show_board(board):
    print("""
    {0} | {1} | {2}
    ---------
    {3} | {4} | {5}
    ---------
    {6} | {7} | {8}
    """.format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))


def is_free(index):
    return BOARD[index] != PLAYER1_MARK and BOARD[index] != PLAYER2_MARK


def make_move(board, player_mark, index):
    board[index] = player_mark


def is_winner(board, player_mark):
    return board[0] == board[1] == board[2] == player_mark or \
           board[3] == board[4] == board[5] == player_mark or \
           board[6] == board[7] == board[8] == player_mark or \
           board[0] == board[3] == board[6] == player_mark or \
           board[1] == board[4] == board[7] == player_mark or \
           board[2] == board[5] == board[8] == player_mark or \
           board[0] == board[4] == board[8] == player_mark or \
           board[2] == board[4] == board[6] == player_mark


def gameEnd():
    return is_winner(BOARD, HUMAN_PLAYER) or is_winner(BOARD, COMPUTER_PLAYER)


def determine_player_mark():
    global HUMAN_PLAYER
    global COMPUTER_PLAYER
    line = ''
    while line != PLAYER1_MARK or line != PLAYER2_MARK:
        line = input().upper()
        print('LINE: ' + line)

    HUMAN_PLAYER = line

    if HUMAN_PLAYER == PLAYER1_MARK:
        COMPUTER_PLAYER = PLAYER2_MARK
    else:
        COMPUTER_PLAYER = PLAYER1_MARK


def input_player_move():
    print('Where would you like to place your mark?')
    line = ''
    while line not in [0,1,2,3,4,5,6,7,8] or not is_free(int(line)):
        line = input()
    make_move(BOARD, HUMAN_PLAYER, int(line))

def copy_board():
    board = BOARD[:]
    return board


def ai_decide_move(): #seperate for loops for now, can be made more efficient, however not needed due to scale (for now)
    move_index = -1
    for i in range(0,9): #make move if can win
        if is_free(i):
            print ( i + ' is free')
            _board = copy_board()
            make_move(_board, COMPUTER_PLAYER, i)
            if is_winner(_board, COMPUTER_PLAYER):
                return i

    for i in range(0,9): #make move if opponent otherwise can win
        if is_free(i):
            _board = copy_board()
            make_move(_board, HUMAN_PLAYER, i)
            if is_winner(_board, HUMAN_PLAYER):
                return i

    for i in range(0,9): #make move: pref middle, then corners then sides
        if is_free(i):
            if i == 4:
                move_index = i
            elif (i == 0 or i == 2 or i == 6 or i == 8) and move_index != 4:
                move_index = i
            else:
                if move_index != 4 or move_index != 0 or move_index != 2 or move_index != 6 or move_index != 8:
                    move_index = i
    return move_index


def ai():
    move_index = ai_decide_move()
    make_move(BOARD, COMPUTER_PLAYER, move_index)
    print('DEBUG: ai made move: ' + move_index)


def main():
    print('Welcome to the almighty TicTacToe game!')
    #Ask player mark
    print('Would you like to be first player (X) or second player (O)?')
    determine_player_mark()
    print(PLAYER1_MARK + " " + PLAYER2_MARK)
    #Ask move

    #make moves untill game ends


main()
