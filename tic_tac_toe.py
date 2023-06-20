import random
import tkinter as tk
from tkinter import messagebox


def print_board(board):
    for row in board:
        print(row)


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


def make_move(row, col):
    global board, current_player

    if board[row][col] != " ":
        messagebox.showerror("Invalid Move", "Invalid move! Try again.")
        return

    board[row][col] = current_player
    button = buttons[row][col]
    button.config(text=current_player, state=tk.DISABLED)

    if check_winner(board, current_player):
        print_board(board)
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        reset_game()
    elif all(board[row][col] != " " for row in range(3) for col in range(3)):
        print_board(board)
        messagebox.showinfo("Game Over", "It's a tie!")
        reset_game()
    else:
        current_player = "O" if current_player == "X" else "X"


def reset_game():
    global board, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = random.choice(["X", "O"])

    for row in range(3):
        for col in range(3):
            button = buttons[row][col]
            button.config(text=" ", state=tk.NORMAL)


# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Create the game board buttons
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text=" ", font=("Arial", 20), width=6, height=3,
                           command=lambda r=row, c=col: make_move(r, c))
        button.grid(row=row, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)

# Initialize the game
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = random.choice(["X", "O"])

# Start the main event loop
window.mainloop()
