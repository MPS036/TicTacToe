board = [' ' for x in range(10)]


def insert_letter(letter, pos):
    board[pos] = letter


def free_space(pos):
    return board[pos] == ' '


def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def is_winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) | (bo[4] == le and bo[5] == le and bo[6] == le) | (bo[1] == le and bo[2] == le and bo[3] == le) | (bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) | (bo[3] == le and bo[6] == le and bo[9] == le) | (bo[1] == le and bo[5] == le and bo[9] == le) | (bo[3] == le and bo[5] == le and bo[7] == le)


def player_move():
    run = True
    while run:
        move = input('Select a position where to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if (move > 0) and (move < 10):
                if free_space(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print('This space is already taken')
            else:
                print('Select a number within the range')
        except:
            print('Type a number')


def computer_move():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if is_winner(boardCopy, let):
                move = i
                return move
    openCorners = []
    for i in possibleMoves:
        for i in [1, 3, 7, 9]:
            openCorners.append(i)
    if len(openCorners) > 0:
        move = select_random(openCorners)
        return move
    if 5 in possibleMoves:
        move = 5
        return move
    openEdges = []
    for i in possibleMoves:
        for i in [2, 4, 6, 8]:
            openEdges.append(i)
    if len(openEdges) > 0:
        move = select_random(openEdges)
    return move


def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def full_board(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print_board(board)
    while not(full_board(board)):
        if not (is_winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print('Sorry to tell you, but you lost to PC')
            break
        if not (is_winner(board, 'X')):
            move = computer_move()
            if move == 0:
                print('Well, it is a Tie Game')
            else:
                insert_letter('O', move)
                print('Computer made a play in position', move)
                print_board(board)
        else:
            print('Yay, you won! Well played')
            break

    if full_board(board):
        print('Well, it is a Tie Game')


main()