import random
import tkinter as tk
from tkinter import messagebox
import ctypes

# Set the gamingpad icon as the favicon for Tkinter windows
gamingpad_icon_path = "gamepad.png"

# Load the icon using ctypes
gamingpad_icon = ctypes.windll.shell32.Shell_NotifyIconW
gamingpad_icon_id = 0x201

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
    elif mode == "robot" and current_player == player_symbols[0]:
        make_robot_move()
        if not check_winner(board, player_symbols[0]) and not all(
            board[row][col] != " " for row in range(3) for col in range(3)
        ):
            current_player = player_symbols[0]  # Switch the player's symbol only if the game is not over
    else:
        current_player = player_symbols[1] if current_player == player_symbols[0] else player_symbols[0]


def make_robot_move():
    global current_player  # Declare current_player as a global variable

    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

    if empty_cells:
        row, col = random.choice(empty_cells)
        player = player_symbols[1]  # Use the opposite symbol of the current player
        board[row][col] = player
        button = buttons[row][col]
        button.config(text=player, state=tk.DISABLED)

        if check_winner(board, player):
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_game()
        elif all(board[row][col] != " " for row in range(3) for col in range(3)):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()

    # Switch the current player before making the move
    current_player = player_symbols[0] if current_player == player_symbols[1] else player_symbols[1]


def reset_game():
    global board, current_player

    board = [[" " for _ in range(3)] for _ in range(3)]

    for row in range(3):
        for col in range(3):
            button = buttons[row][col]
            button.config(text=" ", state=tk.NORMAL)

    current_player = player_symbols[0]


def set_mode(selection):
    global mode, player_symbols
    mode = selection
    player_symbols = ("X", "O") if mode == "multiplayer" else ("X", "O")  # Assign symbols based on the mode
    reset_game()


def open_tic_tac_toe():
    global menu, buttons

    menu.withdraw()

    # Create the main window for Tic Tac Toe
    window = tk.Toplevel()
    window.title("Tic Tac Toe")
    window.geometry("400x600")
    window.resizable(False, False)

    # Set the gamingpad icon for the Tkinter menu window (tic tac toe menu)
    window.wm_iconbitmap(gamingpad_icon_path)

    def back_to_menu():
        window.destroy()
        menu.deiconify()

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

    # Create a frame for the mode selection
    mode_frame = tk.Frame(window)
    mode_frame.pack(pady=10)

    # Create the mode selection radio buttons
    mode = tk.StringVar(value="multiplayer")
    multiplayer_radio = tk.Radiobutton(
        mode_frame,
        text="Multiplayer",
        variable=mode,
        value="multiplayer",
        command=lambda: set_mode("multiplayer")
    )
    multiplayer_radio.grid(row=0, column=0, padx=5)
    robot_radio = tk.Radiobutton(
        mode_frame,
        text="Against Bot",
        variable=mode,
        value="robot",
        command=lambda: set_mode("robot")
    )
    robot_radio.grid(row=0, column=1, padx=5)

    # Create a reset button
    reset_button = tk.Button(
        window,
        text="Reset",
        font=("Arial", 14),
        command=reset_game
    )
    reset_button.pack(pady=10)

    # Create a back button
    back_button = tk.Button(
        window,
        text="Back to Menu",
        font=("Arial", 14),
        command=back_to_menu
    )
    back_button.pack(pady=10)

    # Initialize the game
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_symbols = ("X", "O")
    current_player = player_symbols[0]


def open_pong():
    global menu
    menu.withdraw()

    # Create the Pong window
    pong_window = tk.Toplevel()
    pong_window.title("Pong")
    pong_window.geometry("400x600")
    pong_window.resizable(False, False)

    # Set the gamingpad icon for the Tkinter menu window
    pong_window.wm_iconbitmap(gamingpad_icon_path)

    def back_to_menu():
        pong_window.destroy()
        menu.deiconify()

    # Create a label for Pong
    label = tk.Label(pong_window, text="Pong Game", font=("Arial", 20))
    label.pack(pady=20)

    # Create a back button
    back_button = tk.Button(pong_window, text="Back to Menu", font=("Arial", 14), command=back_to_menu)
    back_button.pack(pady=10)


# Create the main menu
menu = tk.Tk()
menu.title("Game Menu")
menu.geometry("400x600")
menu.resizable(False, False)

# Set the gamingpad icon for the Tkinter menu window
menu.iconbitmap(gamingpad_icon_path)

# Create a label for the menu
label = tk.Label(menu, text="Select a game:", font=("Arial", 20))
label.pack(pady=20)

# Create buttons for each game
tic_tac_toe_button = tk.Button(
    menu,
    text="Tic Tac Toe",
    font=("Arial", 14),
    width=25,
    height=2,
    command=open_tic_tac_toe
)
tic_tac_toe_button.pack(pady=10)

pong_button = tk.Button(
    menu,
    text="Pong",
    font=("Arial", 14),
    width=25,
    height=2,
    command=open_pong
)
pong_button.pack(pady=10)

# Start the main event loop for the menu
menu.mainloop()
