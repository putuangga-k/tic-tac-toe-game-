import tkinter as tk
import tkinter.messagebox as messagebox
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def player_move(button, board):
    row, col = button.grid_info()["row"], button.grid_info()["column"]
    if board[row][col] == " ":
        button.config(text="X", state="disabled", bg="lightgray")
        board[row][col] = "X"
        if check_winner(board, "X"):
            messagebox.showinfo("Congratulations!", "You win!")
            reset_game(board)
        elif is_board_full(board):
            messagebox.showinfo("Tie!", "It's a tie!")
            reset_game(board)
        else:
            computer_move(board)
    else:
        messagebox.showwarning("Invalid Move", "This cell is already taken. Try again.")

def computer_move(board):
    empty_positions = get_empty_positions(board)
    if empty_positions:
        row, col = random.choice(empty_positions)
        for child in frame.winfo_children():
            if child.grid_info()["row"] == row and child.grid_info()["column"] == col:
                child.config(text="O", state="disabled", bg="lightgray")
        board[row][col] = "O"
        if check_winner(board, "O"):
            messagebox.showinfo("Computer Wins!", "Computer wins! Better luck next time.")
            reset_game(board)
        elif is_board_full(board):
            messagebox.showinfo("Tie!", "It's a tie!")
            reset_game(board)

def reset_game(board):
    for child in frame.winfo_children():
        child.config(text=" ", state="normal", bg="white")
    for i in range(3):
        for j in range(3):
            board[i][j] = " "

root = tk.Tk()
root.title("Single Player Tic Tac Toe")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

board = [[" "]*3 for _ in range(3)]

buttons = []
for i in range(3):
    for j in range(3):
        button = tk.Button(frame, text=" ", font=("Helvetica", 20), width=4, height=2,
                           command=lambda i=i, j=j: player_move(buttons[i*3 + j], board))
        button.grid(row=i, column=j, padx=5, pady=5)
        buttons.append(button)

root.mainloop()
