import random

HUMAN = "X"
AI = "O"

board = [' ' for _ in range(10)]

def insert_letter(letter: str, pos: int) -> None:
    board[pos] = letter

def free_space(pos: int) -> bool:
    return board[pos] == " "

def print_board(bo) -> None:
    print("   |   |")
    print(f" {bo[1]} | {bo[2]} | {bo[3]}")
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(f" {bo[4]} | {bo[5]} | {bo[6]}")
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(f" {bo[7]} | {bo[8]} | {bo[9]}")
    print("   |   |")

def is_winner(bo, le: str) -> bool:
    wins = [
        (7, 8, 9),
        (4, 5, 6),
        (1, 2, 3),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    ]
    return any(bo[a] == bo[b] == bo[c] == le for a, b, c in wins)
    
def available_moves(bo) -> list[int]:
    return [i for i in range(1, 10) if bo[i] == " "]

def player_move() -> None:
    while True:
        move_str = input(f"Select a position to place '{HUMAN}' (1-9): ").strip()
        try:
            move = int(move_str)
        except ValueError:
            print("Type a number.")
            continue

        if move not in range(1, 10):
            print("Select a number within the range 1-9.")
            continue

        if not free_space(move):
            print("This space is already taken.")
            continue

        insert_letter(HUMAN, move)
        return

def select_random(moves: list[int]) -> int:
    return random.choice(moves)

def computer_move() -> int:
    possible = available_moves(board)

    # 1) win if possible, 2) block human win
    for let in (AI, HUMAN):
        for i in possible:
            copy_board = board[:]
            copy_board[i] = let
            if is_winner(copy_board, let):
                return i

    # 3) corners
    corners = [i for i in (1, 3, 7, 9) if i in possible]
    if corners:
        return select_random(corners)

    # 4) center
    if 5 in possible:
        return 5

    # 5) edges
    edges = [i for i in (2, 4, 6, 8) if i in possible]
    if edges:
        return select_random(edges)

    return 0

def full_board(bo) -> bool:
    return " " not in bo[1:]

def main() -> None:
    print_board(board)

    while True:
        if is_winner(board, AI):
            print("Sorry to tell you, but you lost to PC.")
            break
        if is_winner(board, HUMAN):
            print("Yay, you won! Well played.")
            break
        if full_board(board):
            print("Well, it is a Tie Game.")
            break

        player_move()
        print_board(board)

        if is_winner(board, HUMAN) or full_board(board):
            continue

        move = computer_move()
        if move == 0:
            print("Well, it is a Tie Game.")
            break

        insert_letter(AI, move)
        print(f"Computer made a play in position {move}")
        print_board(board)

if __name__ == "__main__":
    main()
