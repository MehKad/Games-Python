import random
import tkinter as tk
from tkinter import messagebox

# Function to check the game status
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

# Function to handle button clicks
def make_move(row, col):
    global board, current_player, buttons

    if board[row][col] != " ":
        messagebox.showerror("Invalid Move", "Invalid move! Try again.")
        return

    board[row][col] = current_player
    button = buttons[row][col]
    button.config(text=current_player, state=tk.DISABLED)

    if check_winner(board, current_player):
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        reset_game()
    elif all(board[row][col] != " " for row in range(3) for col in range(3)):
        messagebox.showinfo("Game Over", "It's a tie!")
        reset_game()
    else:
        current_player = "O" if current_player == "X" else "X"
        player_label.config(text=f"Current Player: {current_player}")

# Function to reset the game
def reset_game():
    global board, current_player

    # Clear the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Reset buttons and enable them
    for row in range(3):
        for col in range(3):
            button = buttons[row][col]
            button.config(text=" ", state=tk.NORMAL)
    
    # Randomly choose starting player
    current_player = random.choice(["X", "O"])
    player_label.config(text=f"Current Player: {current_player}")

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Create a frame for the game board
board_frame = tk.Frame(window, bg="black")
board_frame.pack(pady=10)

# Create the game board buttons
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(
            board_frame,
            text=" ",
            font=("Arial", 20),
            width=6,
            height=3,
            command=lambda r=row, c=col: make_move(r, c)
        )
        button.grid(row=row, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)

# Create a frame for the player label and reset button
controls_frame = tk.Frame(window)
controls_frame.pack(pady=10)

# Create a label to display the current player
player_label = tk.Label(controls_frame, text="Current Player: X", font=("Arial", 14))
player_label.grid(row=0, column=0, padx=10)

# Create a reset button
reset_button = tk.Button(controls_frame, text="Reset", font=("Arial", 14), command=reset_game)
reset_button.grid(row=0, column=1, padx=10)

# Initialize the game
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = random.choice(["X", "O"])
player_label.config(text=f"Current Player: {current_player}")

# Start the main event loop
window.mainloop()
