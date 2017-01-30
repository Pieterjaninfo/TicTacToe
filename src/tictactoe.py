import random

BOARD = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

PLAYER1_MARK = 'X'  # Goes first
PLAYER2_MARK = 'O'  # Goes second
HUMAN_PLAYER = ''
COMPUTER_PLAYER = ''

# Statistics while running
games_played = 0
wins_human = 0
wins_bot = 0


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


def game_end(player1_mark, player2_mark):
    return is_winner(BOARD, player1_mark) or is_winner(BOARD, player2_mark) or is_board_full()


def is_board_full():
    for i in range(0, 9):
        if BOARD[i] != 'X' and BOARD[i] != 'O':
            return False
    return True


def determine_player_mark():
    global HUMAN_PLAYER, COMPUTER_PLAYER
    line = ''
    while line != PLAYER1_MARK and line != PLAYER2_MARK:
        line = input().upper()
    HUMAN_PLAYER = line

    if HUMAN_PLAYER == PLAYER1_MARK:
        COMPUTER_PLAYER = PLAYER2_MARK
    else:
        COMPUTER_PLAYER = PLAYER1_MARK


def input_player_move():
    print('Where would you like to place your mark?')
    line = ''
    while line not in "0 1 2 3 4 5 6 7 8".split(" ") or not is_free(int(line)):
        line = input()
    make_move(BOARD, HUMAN_PLAYER, int(line))


def copy_board():
    board = BOARD[:]
    return board


def ai_decide_move():   # Separate for loops for now, can be made more efficient
    move_index = -1
    for i in range(0,9):    # Make move if can win
        if is_free(i):
            _board = copy_board()
            make_move(_board, COMPUTER_PLAYER, i)
            if is_winner(_board, COMPUTER_PLAYER):
                return i

    for i in range(0,9):    # Make move if opponent otherwise can win
        if is_free(i):
            _board = copy_board()
            make_move(_board, HUMAN_PLAYER, i)
            if is_winner(_board, HUMAN_PLAYER):
                return i

    for i in range(0,9):    # Make move: pref middle, then corners, then sides
        if is_free(i):
            if i == 4:
                move_index = i
            elif (i == 0 or i == 2 or i == 6 or i == 8) and move_index != 4:
                move_index = i
            else:
                if move_index != 4 or move_index != 0 or move_index != 2 or move_index != 6 or move_index != 8:
                    move_index = i
    return move_index


def ai_decide_move_random():    # R
    move_index = -1
    while move_index == -1 or not is_free(move_index):
        move_index = random.randint(0, 8)
    return move_index


def ai_pro(ai_mark):
    move_index = ai_decide_move()
    make_move(BOARD, ai_mark, move_index)


def ai_beginner(ai_mark):
    move_index = ai_decide_move_random()
    make_move(BOARD, ai_mark, move_index)


def ai(ai_type, ai_mark):
    if ai_type == 0:
        ai_pro(ai_mark)
    elif ai_type == 1:
        ai_beginner(ai_mark)


def play_again():
    print('Do you want to play again? y/n: ')
    line = ''
    while line != 'y' and line != 'n':
        line = input().lower()
    return line == 'y'


def reset_board():
    global BOARD
    BOARD = [0,1,2,3,4,5,6,7,8]


def play_game_manual():
    global wins_bot, wins_human, games_played

    print('Welcome to the almighty TicTacToe game!')
    # Ask player mark
    print('Would you like to be first player (X) or second player (O): ')
    determine_player_mark()

    if HUMAN_PLAYER == PLAYER2_MARK:
        ai_pro(COMPUTER_PLAYER)
    while not game_end(HUMAN_PLAYER, COMPUTER_PLAYER):
        if is_winner(BOARD, COMPUTER_PLAYER) : break
        show_board(BOARD)
        input_player_move()
        if is_winner(BOARD, HUMAN_PLAYER) : break
        ai_pro(COMPUTER_PLAYER)

    show_board(BOARD)

    if is_winner(BOARD, HUMAN_PLAYER):
        print('Congratulations you won!')
        wins_human += 1
    elif is_winner(BOARD, COMPUTER_PLAYER):
        print('Unfortunately you lost :c')
        wins_bot += 1
    else:
        print('Game resulted in a tie :O')
    games_played += 1

    if play_again():
        reset_board()
        play_game_manual()

    print('Thank you for playing dude!:)')
    print('You won ' + str(wins_human) + ' games while your opponent the best AI bot ever won '
          + str(wins_bot) + ' and there were ' + str(games_played - wins_human - wins_bot) + ' ties.')


# AI types are either 0 (PRO) or 1 (BEGINNER).
def play_ai_game(ai_type1, ai_type2, loops):
    print('The best AI\'s of the land will now face off!')
    ai_types = ['AI pro', 'AI beginner']
    ai1_mark = 'X'
    ai2_mark = 'O'
    ai1_wins = 0
    ai2_wins = 0

    for i in range(0, loops):
        while not game_end(ai1_mark, ai2_mark):
            ai(ai_type1, ai1_mark)
            if is_winner(BOARD, ai1_mark):
                ai1_wins += 1

            if game_end(ai1_mark, ai2_mark):
                break

            ai(ai_type2, ai2_mark)
            if is_winner(BOARD, ai2_mark):
                ai2_wins += 1
        reset_board()
    print("""Bot {0} won {1} times, Bot {2} won {3} times and there were {4} ties. ({5}%/{6}%/{7}%)""".format(
            ai_types[ai_type1], ai1_wins, ai_types[ai_type2], ai2_wins, loops - ai1_wins - ai2_wins,
            ai1_wins/loops*100, ai2_wins/loops*100, (loops-ai1_wins-ai2_wins)/loops*100))


play_ai_game(1, 1, 1000000)