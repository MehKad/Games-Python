import random


def print_board(board):
    print("---------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(cell, end="|")
        print("\n---------")


def check_winner(board, player):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)

    while True:
        print_board(board)

        print(f"Current player: {current_player}")

        if current_player == "X":
            row = int(input("Enter row number (0-2): "))
            col = int(input("Enter column number (0-2): "))
        else:
            row = random.randint(0, 2)
            col = random.randint(0, 2)

        if board[row][col] != " ":
            print("Invalid move! Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if all(board[row][col] != " " for row in range(3) for col in range(3)):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


play_game()
