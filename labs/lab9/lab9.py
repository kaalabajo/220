"""
Kaala Bajo
lab9.py


"""


def build_board():
    the_list = [1,2,3,4,5,6,7,8,9]
    return the_list


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    return str(board[position-1]).isnumeric()


def fill_spot(board, position, character):
    safe_character = character.strip().lower
    board[position-1] = character

def game_is_won(board):
    """lol im sorry this is gross. i wanted to ask if i could simplify it but i couldnt get a hold of anyone
    to ask for help before i had to go"""
    if (board[0] == "x") and (board[1] == "x") and (board[2] == "x"):
        return True
    elif (board[0] == "o") and (board[1] == "o") and (board[2] == "o"):
        return True

    elif (board[3] == "x") and (board[4] == "x") and (board[5] == "x"):
        return True
    elif (board[3] == "o") and (board[4] == "o") and (board[5] == "o"):
        return True

    elif (board[6] == "x") and (board[7] == "x") and (board[8] == "x"):
        return True
    elif (board[6] == "o") and (board[7] == "o") and (board[8] == "o"):
        return True

    elif (board[0] == "x") and (board[3] == "x") and (board[6] == "x"):
        return True
    elif (board[0] == "o") and (board[3] == "o") and (board[6] == "o"):
        return True

    elif (board[1] == "x") and (board[4] == "x") and (board[7] == "x"):
        return True
    elif (board[1] == "o") and (board[4] == "o") and (board[7] == "o"):
        return True

    elif (board[2] == "x") and (board[5] == "x") and (board[8] == "x"):
        return True
    elif (board[2] == "o") and (board[5] == "o") and (board[8] == "o"):
        return True

    elif (board[0] == "x") and (board[4] == "x") and (board[8] == "x"):
        return True
    elif (board[0] == "o") and (board[4] == "o") and (board[8] == "o"):
        return True

    elif (board[2] == "x") and (board[4] == "x") and (board[6] == "x"):
        return True
    elif (board[2] == "o") and (board[4] == "o") and (board[6] == "o"):
        return True

    else:
        return False

def game_over(board):
    a_bool_acc = 0
    for i in board:
        if str(i).isnumeric() == False: #if a element in the list is not a number add 1
            a_bool_acc += 1

    if game_is_won(board) == True:
        return True
    elif a_bool_acc == 9:
        return True
    else:
        return False



def get_winner(board):
    """i was also gonna ask if there was a better way at this point but i
    gave up at some point"""
    if (board[0] == "x") and (board[1] == "x") and (board[2] == "x"):
        return "x"
    elif (board[0] == "o") and (board[1] == "o") and (board[2] == "o"):
        return "o"

    elif (board[3] == "x") and (board[4] == "x") and (board[5] == "x"):
        return "x"
    elif (board[3] == "o") and (board[4] == "o") and (board[5] == "o"):
        return "o"

    elif (board[6] == "x") and (board[7] == "x") and (board[8] == "x"):
        return 'x'
    elif (board[6] == "o") and (board[7] == "o") and (board[8] == "o"):
        return 'o'

    elif (board[0] == "x") and (board[3] == "x") and (board[6] == "x"):
        return 'x'
    elif (board[0] == "o") and (board[3] == "o") and (board[6] == "o"):
        return "o"

    elif (board[1] == "x") and (board[4] == "x") and (board[7] == "x"):
        return 'x'
    elif (board[1] == "o") and (board[4] == "o") and (board[7] == "o"):
        return "o"

    elif (board[2] == "x") and (board[5] == "x") and (board[8] == "x"):
        return 'x'
    elif (board[2] == "o") and (board[5] == "o") and (board[8] == "o"):
        return "o"

    elif (board[0] == "x") and (board[4] == "x") and (board[8] == "x"):
        return 'x'
    elif (board[0] == "o") and (board[4] == "o") and (board[8] == "o"):
        return 'o'

    elif (board[2] == "x") and (board[4] == "x") and (board[6] == "x"):
        return 'x'
    elif (board[2] == "o") and (board[4] == "o") and (board[6] == "o"):
        return 'o'

    else:
        return None


def play(board):
    restart = 0
    play_again = 'y'
    #eval(input("Play again? "))
    while play_again[0] == "y" or play_again[0] == "Y": #TEMPORARY for testing
        board = build_board()
        print_board(board)
        while not game_is_won(board):
            x_move = eval(input("X's, choose a position: "))
            if is_legal(board, x_move) == False:
                x_move = eval(input("Not valid. Pick an unselected position: "))
            fill_spot(board, x_move, "x")
            print_board(board)
            if game_over(board):
                break


            o_move = eval(input("O's, choose a position: "))
            if is_legal(board, o_move) == False:
                o_move = eval(input("Not valid. Pick an unselected position: "))
            fill_spot(board, o_move, "o")
            print_board(board)
            if game_over(board):
                break

        if game_over(board) == True and get_winner(board) != None:
            print("{}'s win!".format(get_winner(board)))
        else:
            print("Tie!")
        play_again = input("Play again? ")


def main():
    play(build_board())


if __name__ == '__main__':
    main()
